import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self) -> None:
        pass

    def predict(self,features):
        """ This function will be doing prediction"""
        try:
            model_path=os.path.join("artifacts","model.pkl") # taking model.pkl for prediction
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl') # preprocessor.pkl is doing scaler,tranformation etc
            print("Before Loading")
            print(os.getcwd())
            model=load_object(file_path = model_path) # load object will load the pickle file, load_obj is in utils.py file
            preprocessor=load_object(file_path = preprocessor_path) # loading preprocessor pickle file
            print("After Loading")
            data_scaled=preprocessor.transform(features) # scaling data once recieved
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    """ This class will be helpful in mapping input provided by frontEnd to the backend"""

    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education:str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score


    def get_data_as_data_frame(self):

        """This will return our input data in the form of dataframe. As we have train our model in df """

        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)