import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PreditctPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts","model.pkl")

            model = load_object(file_path = model_path)

            preds = model.predict(features)
            return preds
        except Exception as e:
            raise CustomException(e, sys)
        
class InputData:
    def __init__(self,
        education: str,
        marital: str,
        income: float,
        wines: int,
        fruits: int,
        meat: int,
        fish: int,
        sweet: int,
        gold: int,
        camp: int,
        purchases: int,
        children: int,
        ):

        self.education = education
        self.marital = marital
        self.income = income
        self.children = children
        self.wines = wines
        self.fruits = fruits
        self.fish = fish
        self.meat = meat
        self.sweet = sweet
        self.gold = gold
        self.purchases = purchases
        self.camp = camp

    def get_data_as_dataFrame(self):
        try:
            input_dict = {
                "Education": [self.education],
                "Marital_Status": [self.marital],
                "Income": [self.income],
                "Wines": [self.wines],
                "Fruits": [self.fruits],
                "Meat": [self.meat],
                "Fish": [self.fish],
                "Sweets": [self.sweet],
                "Gold": [self.gold],
                "camp": [self.camp],
                "Purchases": [self.purchases],
                "Children": [self.children],
            }

            convert_dict = {
                'Year_Birth': int,
                'Education': str,
                'Marital_Status': str,
                'Income': float,
                'Wines': int,
                'Fruits': int,
                'Meat': int,
                'Fish': int,
                'Sweets': int,
                'Gold': int,
                'camp': int,
                'Purchases': int,
                'Children': int,
            }

            df = pd.DataFrame(input_dict)

            df = df.astype(convert_dict)
            df['Education']=df['Education'].replace({'Basic':0,'2n Cycle':0,'Graduation':1,'Master':1,'PhD':1})
            df['Marital_Status']=df['Marital_Status'].replace({'Divorced':0,'Single':0,'Married':1,'Together':1,'Absurd':0,'Widow':0,'YOLO':0})
            df['Expenses']=df['Wines']+df['Fruits']+df['Fish']+df['Gold']+df['Meat']+df['Sweets']
            
            return df

        except Exception as e:
            raise CustomException(e, sys)