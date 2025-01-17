import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifacts', "raw_data.csv")
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    validation_data_path: str = os.path.join('artifacts', "validation.csv")

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()
        
    def ingest_data(self):
        logging.info("Starting data ingestion process...")
        try:
            # Read the customer dataset
            df = pd.read_csv('artifacts/data.csv', sep=';')
            logging.info(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")

            df.drop_duplicates(inplace=True)
            df['Income'] = df['Income'].fillna(df['Income'].median())
            df=df[df['Income']<120000]
            df.dropna(inplace=True)

            # Save raw data
            os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)
            df.to_csv(self.config.raw_data_path, index=False)
            logging.info(f"Raw data saved at {self.config.raw_data_path}.")

            # Split the dataset into train, validation, and test sets
            train_set, temp_set = train_test_split(df, train_size=0.7, random_state=42)
            valid_set, test_set = train_test_split(temp_set, test_size=0.5, random_state=42)

            # Save the datasets
            train_set.to_csv(self.config.train_data_path, index=False)
            valid_set.to_csv(self.config.validation_data_path, index=False)
            test_set.to_csv(self.config.test_data_path, index=False)

            logging.info(f"Train data saved at {self.config.train_data_path}.")
            logging.info(f"Validation data saved at {self.config.validation_data_path}.")
            logging.info(f"Test data saved at {self.config.test_data_path}.")
            
            logging.info("Data ingestion completed successfully.")
            return (
                self.config.train_data_path,
                self.config.validation_data_path,
                self.config.test_data_path,
            )
        
        except Exception as e:
            logging.error("Error during data ingestion.")
            raise CustomException(e, sys)



