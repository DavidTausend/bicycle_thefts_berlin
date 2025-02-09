import streamlit as st


def page_project_hypotheses_body() -> None:
    """
    Render the Project Hypotheses page.

    This page outlines the project hypotheses, presents key findings,
    and evaluates their validity based on the analysis of bicycle theft
    data in Berlin.
    """
    st.write("### Project Hypotheses")

    # Sidebar navigation for hypotheses
    st.write(
        """
        * [Hypothesis 1](#hypothesis-1)
        * [Hypothesis 2](#hypothesis-2)
        * [Hypothesis 3](#hypothesis-3)
        """
    )

    # Hypothesis 1
    st.write("#### Hypothesis 1")
    st.info(
        "We suspect that most bicycle thefts in Berlin occur during "
        "nighttime hours."
    )

    st.write("##### Findings:")
    st.success(
        """
        - Theft records indicate a higher incidence of theft during
          daytime hours.
        - Neighborhoods with higher population density saw more thefts.
        - Lighting conditions and CCTV presence seem to have minimal impact.
        """
    )

    # Hypothesis 2
    st.write("#### Hypothesis 2")
    st.info(
        "We hypothesize that specific types of bicycles (e.g., e-bikes, "
        "mountain bikes) are more frequently targeted by thieves."
    )

    st.write("##### Findings:")
    st.success(
        """
        - This hypothesis was partially correct.
        - E-bikes were targeted more frequently, but city bikes and road
          bikes also showed high theft rates.
        - Common bike types were targeted due to ease of resale.
        """
    )

    # Hypothesis 3
    st.write("#### Hypothesis 3")
    st.info(
        "We believe that theft rates are highest in districts with fewer "
        "security measures."
    )

    st.write("##### Findings:")
    st.success(
        """
        - Theft rates were higher in districts with high tourist traffic
          and minimal local awareness.
        - Areas with poorly secured bike racks experienced more thefts.
        - Community initiatives and patrols showed a decrease in theft
          incidents.
        """
    )
