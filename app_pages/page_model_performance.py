import streamlit as st
import pandas as pd
import os

def page_model_performance_body():
    st.title("Model Performance")

    predictions_path = '/workspace/bicycle_thefts_berlin/jupyter_notebooks/outputs/models/predictions.csv'

    # Check if the file exists
    if not os.path.exists(predictions_path):
        st.error("Predictions file not found. Please ensure 'predictions.csv' exists in the 'outputs/models/' directory.")
        return

    # Load the predictions
    try:
        predictions_df = pd.read_csv(predictions_path)
    except Exception as e:
        st.error(f"Error reading predictions file: {e}")
        return

    # Ensure required columns are present
    if not {'Actual', 'Predicted'}.issubset(predictions_df.columns):
        st.error("The predictions file must contain 'Actual' and 'Predicted' columns.")
        return

    # Display basic performance metrics
    st.write("### Model Performance Metrics")
    
    # Example performance calculation (replace with actual metrics)
    accuracy = (predictions_df['Actual'] == predictions_df['Predicted']).mean()
    st.metric("Accuracy", f"{accuracy:.2%}")

    # Display a sample of the predictions
    st.write("### Sample Predictions")
    st.dataframe(predictions_df.head())
