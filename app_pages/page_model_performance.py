import streamlit as st
import pandas as pd
import os
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)
import seaborn as sns
import matplotlib.pyplot as plt


def page_model_performance_body() -> None:
    """
    Render the Model Performance page.

    This page displays performance metrics and a sample of predictions
    generated by the machine learning model.
    """
    st.title("Model Performance")

    # Define the path to the predictions file
    predictions_path = (
        "jupyter_notebooks/outputs/models/"
        "predictions.csv"
    )

    # Check if the file exists
    if not os.path.exists(predictions_path):
        st.error(
            "Predictions file not found. Ensure 'predictions.csv' exists in "
            "the '/workspace/bicycle_thefts_berlin/jupyter_notebooks/outputs/"
            "models/' directory."
        )
        return

    # Load the predictions
    try:
        predictions_df = pd.read_csv(predictions_path)
    except Exception as e:
        st.error(f"Error reading predictions file: {e}")
        return

    # Ensure required columns are present
    required_columns = {"Actual", "Predicted"}
    if not required_columns.issubset(predictions_df.columns):
        st.error(
            "The predictions file must contain 'Actual' and 'Predicted' "
            "columns."
        )
        return

    # Display basic performance metrics
    st.write("### Model Performance Metrics")

    # Extract actual and predicted values
    y_true = predictions_df["Actual"]
    y_pred = predictions_df["Predicted"]

    # Calculate performance metrics
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(
        y_true, y_pred, average="weighted", zero_division=0
    )
    recall = recall_score(
        y_true, y_pred, average="weighted", zero_division=0
    )
    f1 = f1_score(
        y_true, y_pred, average="weighted", zero_division=0
    )

    # Display metrics
    st.metric("Accuracy", f"{accuracy:.2%}")
    st.metric("Precision", f"{precision:.2%}")
    st.metric("Recall", f"{recall:.2%}")
    st.metric("F1-Score", f"{f1:.2%}")

    # Confusion Matrix
    st.write("### Confusion Matrix")
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues",
        xticklabels=True, yticklabels=True
    )
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    st.pyplot(plt)

    # Display a sample of the predictions
    st.write("### Sample Predictions")
    st.dataframe(predictions_df.head())


# Call the function to run the page when needed
if __name__ == "__main__":
    page_model_performance_body()
