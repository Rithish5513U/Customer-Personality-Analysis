import os
import sys
import pandas as pd
from sklearn.cluster import KMeans
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

class Trainer:
    def __init__(self):
        pass
    
    def trainer(self, file_path):
        """
        Function to train the model and save it
        Args:
            file_path (str) : Read the cleaned data
            
        Returns:
            None
        """
        logging.info("Model training started...")
        try:
            kmeans = KMeans(n_clusters=3, random_state=1)
            df = pd.read_csv(file_path)
            kmeans.fit(df)
            save_object('artifacts/model.pkl', kmeans)
            logging.info("Model saved successfully")
            
        except Exception as e:
            raise CustomException(e, sys)
        
obj = Trainer()
obj.trainer('artifacts/cleaned_data.csv')
        

        

