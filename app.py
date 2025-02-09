import streamlit as st
from app_pages.multipage import MultiPage

# Importing pages
from app_pages.page_project_summary import page_project_summary_body
from app_pages.page_project_hypotheses import page_project_hypotheses_body
from app_pages.page_feat_correlation import page_feat_correlation_body
from app_pages.page_theft_prediction import page_theft_prediction_body
from app_pages.page_model_performance import page_model_performance_body
from app_pages.page_project_conclusions import page_project_conclusions_body


def main() -> None:
    """
    Main function to define and run the Streamlit app.

    The app uses a multipage structure, each page focusing on different
    aspects of the bicycle theft analysis project.
    """
    # Create an instance of MultiPage app
    app = MultiPage(app_name="Bicycle Theft Predictor")

    # Add pages to the app
    app.app_page("Project Summary", page_project_summary_body)
    app.app_page("Project Hypotheses", page_project_hypotheses_body)
    app.app_page("Feature Correlation Study", page_feat_correlation_body)
    app.app_page("Bicycle Theft Prediction", page_theft_prediction_body)
    app.app_page("Model Performance", page_model_performance_body)
    app.app_page("Project Conclusions", page_project_conclusions_body)

    # Run the app
    app.run()


if __name__ == "__main__":
    main()
