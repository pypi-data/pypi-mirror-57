import logging
import os
import pandas as pd
import time

from auger_ml.FSClient import FSClient
from auger_ml.data_source.data_source_api_pandas import DataSourceAPIPandas
from auger_ml.data_splitters.XYNumpyDataPrep import XYNumpyDataPrep
from auger_ml.Utils import remove_dups_from_list, get_uid, get_uid4


class ModelExporter(object):
    def __init__(self, options):
        self.options = options

    def load_model(self, model_path):
        from auger_ml.preprocessors.space import ppspace_is_timeseries_model

        model = FSClient().loadObjectFromFile(os.path.join(model_path, "model.pkl.gz"))

        options = FSClient().readJSONFile(os.path.join(model_path, "options.json"))
        timeseries_model = options.get('timeSeriesFeatures') and ppspace_is_timeseries_model(options.get('algorithm_name'))

        return model, timeseries_model

    def preprocess_target(self, model_path, data_path=None, records=None, features=None):

        ds = DataSourceAPIPandas.create_dataframe(data_path, records, features)

        return self.preprocess_target_ds(model_path, ds)

    def preprocess_target_ds(self, model_path, ds):
        import numpy as np

        options = FSClient().readJSONFile(os.path.join(model_path, "options.json"))
        target_categoricals = FSClient().readJSONFile(os.path.join(model_path, "target_categoricals.json"))        
        y_true =  None

        if not options.get('targetFeature') or not options.get('targetFeature') in ds.columns:
            return y_true, target_categoricals

        if options.get('timeSeriesFeatures'):
            y_true = np.ravel(ds.df[options.get('targetFeature')].astype(np.float64, copy=False), order='C')
        else:
            if target_categoricals and options.get('targetFeature') in target_categoricals:
                ds.convertToCategorical(options.get('targetFeature'), is_target=True, 
                    categories=target_categoricals.get(options.get('targetFeature')).get('categories'))

            y_true = np.ravel(ds.df[options.get('targetFeature')], order='C')

        return y_true, target_categoricals

    def preprocess_data(self, model_path, data_path=None, records=None, features=None, predict_value_num=None):
        from auger_ml.AugerMLPreprocessors import AugerMLPreprocessors
        from auger_ml.preprocessors.space import ppspace_is_timeseries_model, pspace_get_fold_group_names

        options = FSClient().readJSONFile(os.path.join(model_path, "options.json"))

        options['featureColumns'] = options.get('originalFeatureColumns')
        data_features = options['featureColumns'][:]
        if options.get('timeSeriesFeatures'):
            data_features.extend(options.get('timeSeriesFeatures'))
            data_features.append(options.get('targetFeature'))

        data_features = remove_dups_from_list(data_features)

        if features is None:
            features = data_features

        ds = DataSourceAPIPandas.create_dataframe(data_path, records, features)

        if set(data_features).issubset(set(ds.columns)):
            if options.get('targetFeature') in ds.columns and not options.get('targetFeature') in data_features:
                data_features.append(options.get('targetFeature'))

            ds.df = ds.df[data_features]
        else:
            raise Exception("Prediction data missing columns:%s"%(set(data_features)-set(ds.columns)))

        transforms = FSClient().readJSONFile(os.path.join(model_path, "transformations.json"))
        ds.transform(transforms, cache_to_file=False)

        target_categoricals = FSClient().readJSONFile(os.path.join(model_path, "target_categoricals.json"))

        X_test, Y_test = None, None
        if options.get('timeSeriesFeatures'):

            if predict_value_num is not None:
                if predict_value_num == len(ds.df):
                    return None, None, None

                ds.df = ds.df.iloc[:(predict_value_num + 1)]  # truncate dataset

            pp = AugerMLPreprocessors(options)
            pp.transform_predicted_data(ds, model_path, target_categoricals)

            X_test, Y_test = XYNumpyDataPrep(options).split_predict_timeseries(ds.df)

        else:
            X_test = {}
            if options.get('ensemble', False):
                fold_groups = pspace_get_fold_group_names(options.get('timeSeriesFeatures'))
                for fold_group in fold_groups:
                    options['fold_group'] = fold_group

                    ds2 = DataSourceAPIPandas(options)
                    ds2.df = ds.df.copy()

                    pp = AugerMLPreprocessors(options)
                    pp.transform_predicted_data(ds2, model_path, target_categoricals)
                    X_test[fold_group], Y_test = XYNumpyDataPrep(options).split_predict(ds2.df)
            else:
                pp = AugerMLPreprocessors(options)
                pp.transform_predicted_data(ds, model_path, target_categoricals)
                X_test, Y_test = XYNumpyDataPrep(options).split_predict(ds.df)

        return X_test, Y_test, target_categoricals
                
    def predict_by_model(self, model_path, path_to_predict=None, records=None, 
        features=None, threshold=None, predict_value_num=None, json_result=False):
        from auger_ml.preprocessors.space import ppspace_is_timeseries_model

        model, timeseries_model = self.load_model(model_path)
        X_test, Y_test, target_categoricals = self.preprocess_data(model_path, 
            data_path=path_to_predict, records=records, features=features, predict_value_num=predict_value_num)

        if X_test is None:
            return None

        options = FSClient().readJSONFile(os.path.join(model_path, "options.json"))

        ds = DataSourceAPIPandas({'data_path': path_to_predict})
        if options.get('timeSeriesFeatures'):
            if ppspace_is_timeseries_model(options.get('algorithm_name')):
                results = model.predict((X_test, Y_test, False))[-1:]
            else:
                results = model.predict(X_test.iloc[-1:])

            ds.df = pd.DataFrame({
                options['targetFeature']: results,
                options['timeSeriesFeatures'][0]: X_test.index[-1:]
            })
        else:
            results = None
            results_proba = None
            proba_classes = None
            try:
                if threshold:
                    if hasattr(model, 'predict_proba') and callable(getattr(model, 'predict_proba')):
                        try:
                            results_proba = model.predict_proba(X_test)
                        except AttributeError as e:
                            logging.info("predict_proba is property, try _predict_proba")
                            results_proba = model._predict_proba(X_test)

                    elif hasattr(model, 'decision_function'):
                        results_proba = model.decision_function(X_test)

                    if results_proba is not None:
                        results = []
                        proba_classes = model.classes_
                        for item in results_proba:
                            found = False
                            for idx, prob in enumerate(item):
                                if prob > threshold:
                                    results.append(proba_classes[idx])
                                    found = True
                                    #break

                            if not found:
                                results.append(proba_classes[0])
            except:
                logging.exception("predict_proba failed.")

            if results is None: 
                results = model.predict(X_test)

            try:
                results = list(results)
            except Exception as e:
                #print("INFO: Prediction result with type: %s convert to list failed: %s"%(type(results), str(e)))
                results = [results]

            if options['targetFeature'] in target_categoricals:
                results = DataSourceAPIPandas.revertCategories(results,
                                              target_categoricals[options['targetFeature']]['categories'])
                if proba_classes is not None:
                    proba_classes = DataSourceAPIPandas.revertCategories(proba_classes,
                                              target_categoricals[options['targetFeature']]['categories'])
            if path_to_predict:
                ds.load(use_cache=False)
            else:
                ds.load_records(records, features=features, use_cache=False)

            try:
                results = list(results)
            except Exception as e:
                #print("INFO: Prediction result with type: %s convert to list failed: %s"%(type(results), str(e)))
                results = [results]

            ds.df[options['targetFeature']] = results
            if results_proba is not None:
                for idx, name in enumerate(proba_classes):
                    ds.df['proba_'+str(name)] = list(results_proba[:,idx])

                #ds.df = self._format_proba_predictions(ds.df)

        prediction_ids = []
        for i in range(0,ds.count()):
            prediction_ids.append(get_uid4())

        ds.df.insert(loc=0, column='prediction_id', value=prediction_ids)
        
        if options.get('support_review_model', False):
            uid_prediction = self.options.get('prediction_id', get_uid())
            ds.saveToBinFile(os.path.join(model_path, "predictions", uid_prediction+"_results.pkl.gz"))

        if path_to_predict and not json_result:
            parent_path = FSClient().getParentFolder(path_to_predict)
            file_name = os.path.basename(path_to_predict)
            predict_path = os.path.join( parent_path, "predictions",
                os.path.splitext(file_name)[0] + "_%s_%s_predicted.csv"%(get_uid(), options.get('uid')))
            ds.saveToCsvFile(predict_path, compression=None)
            print(predict_path)
            return predict_path
        else:
            if json_result:
                return ds.df.to_json(orient='split', index=False)

            return ds.df

    def _format_proba_predictions(self, predictions):
        predictions_no_proba = predictions[predictions.columns.drop(
            list(predictions.filter(regex='proba_'))
        )]
        predictions_proba = predictions.filter(regex='proba_').reset_index()
        predictions = predictions_no_proba.reset_index().iloc[:, list((0, -1))]

        if not predictions_proba.empty:
            predictions = pd.merge(predictions, predictions_proba, on='index')

        predictions.drop(['index'], inplace=True, axis=1)

        return predictions

    def predict_by_model_ts_recursive(self, model_path, path_to_predict=None, records=None, features=None,
                                      start_prediction_num=None):
        options = FSClient().readJSONFile(os.path.join(model_path, "options.json"))
        targetFeature = options['targetFeature']

        i = start_prediction_num
        result = []
        while True:
            res = self.predict_by_model(model_path, path_to_predict, records, features, predict_value_num=i)
            if res is None:
                break

            if path_to_predict is not None:
                ds = DataSourceAPIPandas({'data_path': res})
                ds.load(features = [targetFeature], use_cache = False)
                res = ds.df
                #res = pd.read_csv(res, encoding='utf-8', escapechar='\\', usecols=[targetFeature])

            #assert len(res) == 1
            result.append(res[targetFeature][0])
            i += 1

        return result

    def score_by_model(self, model_path, predict_path=None, test_path=None, 
            records=None, features=None, test_records=None, test_features=None,
            start_prediction_num=20):
        from auger_ml.Utils import calculate_scores

        res = {}
        options = FSClient().readJSONFile(os.path.join(model_path, "options.json"))
        y_pred = None

        if options.get('timeSeriesFeatures'):
            y_pred = self.predict_by_model_ts_recursive(model_path, 
                path_to_predict=predict_path, records=records, features=features, start_prediction_num=start_prediction_num)
        else:
            predictions = self.predict_by_model(model_path, path_to_predict=predict_path,
                records=records, features=features)
            if predict_path:
                y_pred, target_categoricals = self.preprocess_target(model_path, data_path=predictions)
            else:
                y_pred, target_categoricals = self.preprocess_target(model_path, records=predictions, features=[options.get('targetFeature')])

            #TODO: support proba scores and threshold

        if test_path is None and test_records is None:
            test_path = predict_path

        y_true, target_categoricals = self.preprocess_target(model_path, data_path=test_path,
            records=test_records, features=test_features)

        if test_path == predict_path:
            y_true = y_true[:len(y_pred)]

        res['all_scores'] = calculate_scores(options, y_test=y_true, y_pred=y_pred)
            
        return res

    def score_actuals(self, model_path, actuals_path = None, actual_records=None):
        from auger_ml.Utils import calculate_scores

        options = FSClient().readJSONFile(os.path.join(model_path, "options.json"))
        features = ['prediction_id', options.get('targetFeature')]

        ds_actuals = DataSourceAPIPandas.create_dataframe(actuals_path, actual_records, features)
        ds_actuals.df.rename(columns = {options.get('targetFeature'): 'auger_actual'}, inplace = True)
        actuals_count = ds_actuals.count()

        all_files = FSClient().listFolder(os.path.join(model_path, "predictions/*_results.pkl.gz"), 
            wild=True, removeFolderName=True, meta_info=True)
        all_files.sort(
            key=lambda f: f['last_modified'],
            reverse=True
        )                    
        for file in all_files:
            df_prediction_results = DataSourceAPIPandas({})
            df_prediction_results.loadFromBinFile(os.path.join(model_path, "predictions", file['path']))

            ds_actuals.df = ds_actuals.df.merge(df_prediction_results.df, how='left', on='prediction_id', copy=False)
            match_count = ds_actuals.df.count()[options.get('targetFeature')]
            if actuals_count == match_count:
                break

        ds_actuals.dropna(columns=[options.get('targetFeature')])
        ds_true = DataSourceAPIPandas({})
        ds_true.df = ds_actuals.df[['auger_actual']].rename(columns={'auger_actual':options.get('targetFeature')})

        y_pred, _ = self.preprocess_target_ds(model_path, ds_actuals)
        y_true, _ = self.preprocess_target_ds(model_path, ds_true)

        score = calculate_scores(options, y_test=y_true, y_pred=y_pred)

        ds_actuals.drop(options.get('targetFeature'))
        ds_actuals.df = ds_actuals.df.rename(columns={'auger_actual':options.get('targetFeature')})

        uid_actuals = self.options.get('actuals_id', get_uid())
        ds_actuals.saveToBinFile(os.path.join(model_path, "predictions", uid_actuals+"_actuals.pkl.gz"))            

        return score

    def build_review_data(self, model_path, data_path=None):
        options = FSClient().readJSONFile(os.path.join(model_path, "options.json"))
        if not data_path:
            data_path = options['data_path']

        review_data_path = os.path.splitext(data_path)[0] + "_review_%s.pkl.gz"%(get_uid())
            
        ds_train = DataSourceAPIPandas.create_dataframe(data_path)

        all_files = FSClient().listFolder(os.path.join(model_path, "predictions/*_actuals.pkl.gz"), 
            wild=True, removeFolderName=True, meta_info=True)
        all_files.sort(
            key=lambda f: f['last_modified'],
            reverse=True
        )                    
        for file in all_files:
            ds_actuals = DataSourceAPIPandas({})
            ds_actuals.loadFromBinFile(os.path.join(model_path, "predictions", file['path']))
            ds_actuals.drop(['prediction_id'])

            ds_train.df = pd.concat([ds_train.df, ds_actuals.df], ignore_index=True)
            ds_train.drop_duplicates()

        ds_train.saveToBinFile(review_data_path)

        return review_data_path    