import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True) # Its making a directory with the file Path

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(X_train,y_train,X_test,y_test,models,param):
    """ This function will evaluate the performance of the model.
    """
    try:

        report = {} # empty dictionary

        ## Iterating over each of the model mentioned in model_trainer.py file

        for i in range(len(list(models))):

            model = list(models.values())[i] # getting models one by one from mode_trainer.py file
            para = param[list(models.keys())[i]] # All parameters we have here from mode_trainer.py file

            ## GridSearchCV
            gs = GridSearchCV(model,para,cv= 3)#n_jobs=n_jobs,verbose=verbose,refit = refit)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            # model.fit(X_train,y_train) # training  model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train,y_train_pred)

            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e,sys)


