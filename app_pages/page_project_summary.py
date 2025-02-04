import streamlit as st
import pandas as pd

# Load the dataset to display a preview
DATASET_DF = pd.read_csv("outputs/datasets/cleaned/TestSetCleaned.csv").head(5)

def page_project_summary_body():
    st.title("Bicycle Theft Predictor")

    # Sidebar navigation links
    st.write("### Navigation")
    st.write(
        """
        - [Project Summary](#project-summary)
        - [Project Dataset](#project-dataset)
        - [Feature Terminology](#feature-terminology)
        - [Business Requirements](#business-requirements)
        """
    )

    # Project Summary Section
    st.write("### Project Summary")
    st.write(
        """
        Bicycle thefts are a significant issue in Berlin, impacting residents and businesses. Understanding theft trends and risk factors is crucial for prevention strategies.

        This project aims to develop data-driven insights from bicycle theft reports in Berlin, leveraging machine learning and data visualization techniques to predict theft occurrences and patterns.
        """
    )

    # Project Dataset Section
    st.info("### Project Dataset\n")
    st.write(
        """
        **Dataset:** The dataset was sourced from Berlin's open data portal.

        **Attributes:** The dataset contains various attributes, such as timestamps, bicycle types, and theft locations.

        **Observations:** The dataset contains several thousand records spanning multiple years.
        """
    )

    # Display a preview of the dataset
    st.write("### Dataset Preview")
    st.dataframe(DATASET_DF)
