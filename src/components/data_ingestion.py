import pandas as pd
import numpy as np
from src.logger import logging
from dataclasses import dataclass

@dataclass
class DataIngestion:
    file_path:str = "data/data.csv"

    def ingest(self):
        logging.info("Ingesting data...")
        try:
            data = pd.read_csv(self.file_path, sep=';')
            logging.info("Data ingestion successful.")
            return data
        except Exception as e:
            logging.error(f"Error in Data Ingestion: {e}")
            return None
        
ex = DataIngestion()
data = ex.ingest()
