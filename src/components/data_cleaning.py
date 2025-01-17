import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from sklearn.preprocessing import LabelEncoder, StandardScaler
from src.logger import logging

class DataCleaning:
    def __init__(self):
        pass

    def clean_data(self, file_path: str):
        """
        Perform data cleaning on the provided dataset.

        Args:
            file_path (str): Path to the raw data file.

        Returns:
            pd.DataFrame: Cleaned DataFrame.
        """
        logging.info("Starting data cleaning process...")
        try:
            df = pd.read_csv(file_path)
            logging.info(f"Dataset loaded with shape: {df.shape}")

            columns_to_drop = ['ID','Z_CostContact','Z_Revenue','Dt_Customer']  # Example of unwanted columns
            df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

            df['camp'] = df['AcceptedCmp1']+df['AcceptedCmp2']+df['AcceptedCmp3']+df['AcceptedCmp4']+df['AcceptedCmp5']+df['Response']
            df.drop(columns=['AcceptedCmp1','AcceptedCmp2','AcceptedCmp3','AcceptedCmp4','AcceptedCmp5','Response'], inplace = True)

            df['Purchases'] = df['NumDealsPurchases']+df['NumCatalogPurchases']+df['NumWebPurchases']+df['NumStorePurchases']
            df.drop(columns=['NumStorePurchases','NumWebPurchases','NumCatalogPurchases','NumDealsPurchases','NumWebVisitsMonth','Year_Birth','Recency','Complain'], inplace=True)

            df['Marital_Status']=df['Marital_Status'].replace({'Divorced':'Alone','Single':'Alone','Married':'In couple','Together':'In couple','Absurd':'Alone','Widow':'Alone','YOLO':'Alone'})
            df['Education']=df['Education'].replace({'Basic':'Undergraduate','2n Cycle':'Undergraduate','Graduation':'Postgraduate','Master':'Postgraduate','PhD':'Postgraduate'})
            df['Children']=df['Kidhome']+df['Teenhome']
            df=df.rename(columns={'MntWines': "Wines",'MntFruits':'Fruits','MntMeatProducts':'Meat','MntFishProducts':'Fish','MntSweetProducts':'Sweets','MntGoldProds':'Gold'})
            df.drop(columns=['Kidhome','Teenhome'], inplace=True)
            df['Expenses']=df['Wines']+df['Fruits']+df['Fish']+df['Gold']+df['Meat']+df['Sweets']
            
            le = LabelEncoder()
            df['Education']=le.fit_transform(df['Education'])
            df['Marital_Status']=le.fit_transform(df['Marital_Status'])
            scaler = StandardScaler()
            df = scaler.fit_transform(df)
            df = pd.DataFrame(df)

            cleaned_data_path = os.path.join('artifacts', 'cleaned_data.csv')
            df.to_csv(cleaned_data_path, index=False)
            logging.info(f"Cleaned data saved at {cleaned_data_path}.")

            return df

        except Exception as e:
            logging.error("Error occurred during data cleaning.")
            raise CustomException(e, sys)
