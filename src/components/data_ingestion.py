import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass # we can directly define our class variable
class DataIngestionConfig():
    """ Any input required will give through this class
    """
    # below are the inputs that we are providing to our data ingestion component
    ## all the output will be stored in artifact folder
    train_data_path : str = os.path.join('artifacts','train.csv') # path we are providing to our data ingestion component
    test_data_path : str = os.path.join('artifacts','test.csv')
    raw_data_path : str = os.path.join('artifacts','raw_data.csv')

class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig() ## input of above class will be stored in ingestion_config

    def initiate_data_ingestion(self):
        """ we can read our data from database
        """
        logging.info("Entered the data ingestion method or component")
        try:
            ## Currently reading data from csv file
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) # if folder is there its ok
            # saving raw data to artifact folder
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set, test_set =  train_test_split(df,test_size=0.2,random_state=42)
            # saving train data to train/ artifact folder
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            # saving raw data to test / artifact folder
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e :
            raise CustomException(e,sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()