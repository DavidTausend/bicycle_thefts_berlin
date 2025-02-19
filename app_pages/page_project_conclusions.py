import streamlit as st


def page_project_conclusions_body() -> None:
    """
    Render the Project Conclusions page.

    This page summarizes the findings of the bicycle theft analysis,
    provides business insights, and offers actionable recommendations.
    """
    st.write("### Project Conclusions")

    # Sidebar navigation links for the sections
    st.write(
        """
        * [Summary of Findings](#summary-of-findings)
        * [Business Insights](#business-insights)
        * [Recommendations](#recommendations)
        """
    )

    # Summary of Findings
    st.write("#### Summary of Findings")
    st.info(
        """
        The analysis of bicycle thefts in Berlin has led to the following
        key findings:

        - Certain types of bicycles (e.g., 'Mountainbike' and 'Rennrad')
          are more frequently targeted by theft.
        - Bicycle thefts occur more frequently in specific time periods
          (e.g., late evening hours and weekends).
        - Theft incidents are concentrated in particular neighborhoods
          or areas with high foot and bike traffic.
        - The predictive model demonstrated strong performance on key
          metrics, with an F1 score indicating balanced precision and
          recall.
        """
    )

    # Business Insights
    st.write("#### Business Insights")
    st.success(
        """
        - Law enforcement and city planners can focus resources on theft
          hotspots identified by the analysis.
        - Awareness campaigns could target specific time periods to
          encourage residents to secure their bicycles.
        - Data-driven insurance models can offer tailored premiums based
          on theft risk in different areas.
        """
    )

    # Recommendations
    st.write("#### Recommendations")
    st.warning(
        """
        - Implement additional preventive measures in high-risk
          neighborhoods, such as surveillance cameras and secure
          parking areas.
        - Provide bike owners with guidelines on securing their bikes,
          including locking techniques and high-risk locations to avoid.
        - Collect more detailed data on theft patterns to further
          enhance predictive accuracy and improve early detection
          strategies.
        """
    )
