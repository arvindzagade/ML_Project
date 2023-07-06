import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

 ## for every component we need to create a config file where we will pass input

@dataclass
class ModelTrainerConfig:
    """ Will take the input required for the training
    """
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    """ This class will be responsible for training the model
    """

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    
    def initiate_model_trainer(self,train_array,test_array):
        """ Model training will be initiated throught this function
        """
        try:
            logging.info("Splitting training and test input data")

            # taking data from data_transformation.py and then dividing train data into train_test split
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1], ## take all the data expect the last column
                train_array[:,-1], # only last column for y_train
                test_array[:,:-1], # all except for target column for test purpose
                test_array[:,-1] # only target column for test purpose
                
            )

            ## creating a dictionary of models

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
            
            ## Evaluate model function is written in utils.py 
            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models)

            # To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            # To get best model name from dict
            best_model_name = list(model_report.keys())[ list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            # if we are getting model with less than 60% good accuracy we will not consider that one
            if best_model_score < 0.6:
                raise CustomException("No best model found")

            logging.info(f"Best Found Model on both training and testing dataset")

            # we saving the model path below
            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj= best_model
            )

            ## checking our prediction on test data
            predicted=best_model.predict(X_test)

            r2_square = r2_score(y_test,predicted)
            return r2_square

        except Exception as e:
            raise CustomException (e,sys)

            



