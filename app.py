import streamlit as st
import pandas as pd
import os
from src.utils import load_object
from src.pipeline.prediction_pipeline import PreditctPipeline, InputData
from src.exception import CustomException
import sys

def main():
    st.title("Customer Cluster Prediction")

    with st.form("Customer Input Form", clear_on_submit=True):
        st.subheader("Enter Customer Details")
        
        education = st.selectbox(
            "Education Level", ["Basic", "2n Cycle", "Graduation", "Master", "PhD"]
        )

        marital = st.selectbox(
            "Marital Status",
            ["Single", "Married", "Divorced", "Together", "Widow", "Absurd", "YOLO"],
        )

        income = st.number_input("Yearly Income (e.g., 30000)", min_value=0.0, step=500.0)
        wines = st.number_input("Wines Purchased (e.g., 5)", min_value=0, step=1)
        fruits = st.number_input("Fruits Purchased (e.g., 3)", min_value=0, step=1)
        meat = st.number_input("Meat Purchased (e.g., 10)", min_value=0, step=1)
        fish = st.number_input("Fish Purchased (e.g., 2)", min_value=0, step=1)
        sweet = st.number_input("Sweets Purchased (e.g., 4)", min_value=0, step=1)
        gold = st.number_input("Gold Purchased (e.g., 1)", min_value=0, step=1)
        camp = st.number_input("Campaign Accepted (e.g., 1)", min_value=0, step=1)
        purchases = st.number_input("Total Purchases (e.g., 15)", min_value=0, step=1)
        children = st.number_input("Number of Children (e.g., 2)", min_value=0, step=1)
        submitted = st.form_submit_button("Predict Cluster")

        if submitted:
            try:
                preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
                preprocessor = load_object(preprocessor_path)

                input_data = InputData(
                    education=education,
                    marital=marital,
                    income=income,
                    wines=wines,
                    fruits=fruits,
                    meat=meat,
                    fish=fish,
                    sweet=sweet,
                    gold=gold,
                    camp=camp,
                    purchases=purchases,
                    children=children,
                )

                input_df = input_data.get_data_as_dataFrame()

                processed_data = preprocessor.transform(input_df)

                pipeline = PreditctPipeline()
                prediction = pipeline.predict(processed_data)

                if prediction[0] == 0:
                    st.success("The customer belongs to Premium cluster (Top Rated consumer)")
                elif prediction[0] == 1:
                    st.success("The customer belongs to Pro cluster (Good consumer)")
                else:
                    st.success("The customer belongs to Beginner cluster (Less consumed)")

            except CustomException as e:
                st.error(f"An error occurred: {str(e)}")
            except Exception as e:
                st.error(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
