import streamlit as st
import pandas as pd

def page_theft_prediction_body():
    st.title("Theft Prediction")

    # Description of the page
    st.write("This page allows users to input features to predict bicycle theft risk in Berlin.")

    # Example form for user input
    st.subheader("Enter Details for Prediction")
    
    # Example form inputs (replace with your actual feature names and options)
    bike_type = st.selectbox("Bicycle Type", ["Mountain Bike", "Road Bike", "Electric Bike"])
    theft_time = st.slider("Time of Day (Hour)", min_value=0, max_value=23, value=12)
    neighborhood = st.text_input("Neighborhood")
    
    # Mock prediction button
    if st.button("Predict"):
        # Mock prediction result (replace this with your actual prediction code)
        prediction = "High Risk" if theft_time > 18 else "Low Risk"
        st.subheader("Prediction Result")
        st.write(f"The predicted risk of theft is: **{prediction}**")

    # Optional: Display sample data
    st.subheader("Sample Data Preview")
    try:
        data = pd.read_csv("outputs/datasets/cleaned/TestSetCleaned.csv")
        st.dataframe(data.head(5))
    except Exception as e:
        st.error(f"Error loading sample data: {e}")
