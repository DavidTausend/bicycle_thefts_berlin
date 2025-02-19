import streamlit as st
import pandas as pd


def page_feat_correlation_body() -> None:
    """
    Render the Feature Correlation Study page.

    This page includes an overview of the business requirement, dataset
    preview, Pearson correlation matrix calculation, and visualization.
    """
    # Load the dataset
    data = pd.read_csv("outputs/datasets/cleaned/TestSetCleaned.csv")

    # Page Header
    st.write("# Feature Correlation Study")

    # Business Requirement
    st.write("## Business Requirement")
    st.write(
        """
        We need to perform a correlation study to determine which features
        correlate most closely with bicycle theft occurrences. This will
        help identify key attributes that impact theft risk and can be
        used to improve prediction models.
        """
    )

    # Inspect the Dataset
    st.write("## Inspect the Dataset")
    st.write("Here is a preview of the dataset:")
    st.dataframe(data.head())

    # Calculate Pearson Correlation
    st.write("## Pearson Correlation Matrix")

    # Select only numeric columns for correlation
    numeric_data = data.select_dtypes(include=["number"])

    # Check if numeric data is available
    if numeric_data.empty:
        st.error(
            "No numeric columns found in the dataset to calculate correlation."
        )
        return

    # Calculate correlation matrix
    correlation_matrix = numeric_data.corr(method="pearson")

    # Display the correlation matrix as table
    st.write("### Correlation Matrix")
    st.dataframe(correlation_matrix)

    # Conclusions
    st.write("## Conclusions")
    st.write(
        """
        The Pearson correlation matrix provides insights into relationships
        between various numerical attributes in the dataset. This information
        can guide feature selection for model development.
        """
    )
