import pandas as pd
import numpy as np
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from dataclasses import dataclass


@dataclass
class DataCleaning:
    data = DataIngestion().ingest()
    def clean(self):
        logging.info("Data Cleaning started...")
        try:
            df = self.data
            df['Camp'] = df['AcceptedCmp1']+df['AcceptedCmp2']+df['AcceptedCmp3']+df['AcceptedCmp4']+df['AcceptedCmp5']+df['Response']
            df['Purchases'] = df['NumDealsPurchases']+df['NumCatalogPurchases']+df['NumWebPurchases']+df['NumStorePurchases']
            df['Marital_Status']=df['Marital_Status'].replace({
                'Divorced':'Alone',
                'Single':'Alone',
                'Married':'In couple'
                ,'Together':'In couple',
                'Absurd':'Alone',
                'Widow':'Alone',
                'YOLO':'Alone'
            })
            df['Education']=df['Education'].replace({
                'Basic':'Undergraduate',
                '2n Cycle':'Undergraduate'
                ,'Graduation':'Postgraduate'
                ,'Master':'Postgraduate',
                'PhD':'Postgraduate'
            })
            df['Children']=df['Kidhome']+df['Teenhome']
            df=df.rename(columns={
                'MntWines': "Wines",
                'MntFruits':'Fruits',
                'MntMeatProducts':'Meat',
                'MntFishProducts':'Fish',
                'MntSweetProducts':
                'Sweets','MntGoldProds':'Gold'
            })
            df.drop(columns=['AcceptedCmp1','AcceptedCmp2','AcceptedCmp3','AcceptedCmp4','AcceptedCmp5','Response','NumStorePurchases',
                'NumWebPurchases','NumCatalogPurchases','NumDealsPurchases','NumWebVisitsMonth','Year_Birth','Recency','Complain','Kidhome',
                'Teenhome'
            ], inplace = True)
            logging.info("Data Cleaning Done")
            return df
        except:
            return None
