import streamlit as st
import pandas as pd
import geopandas as gpd
import traceback


def load_neighborhoods() -> pd.DataFrame:
    """
    Load and process the GeoJSON file containing neighborhood data.

    Returns:
        pd.DataFrame: Processed neighborhood data with 'PLR_NAME' and 'PLR_ID'.
    """
    try:
        lor_gdf = gpd.read_file(
            "inputs/datasets/raw/lor_planungsraeume_2021.geojson"
        )

        # Ensure 'PLR_ID' is treated as a string and padded with zeros
        lor_gdf['PLR_ID'] = (
            lor_gdf['PLR_ID'].astype(str).str.zfill(8)
        )

        # Remove 'geometry' column for display in Streamlit
        st.write(
            "Sample data from GeoJSON:",
            lor_gdf.drop(columns=['geometry']).head(),
        )

        return (
            lor_gdf[['PLR_NAME', 'PLR_ID']]
            .sort_values(by='PLR_NAME')
            .dropna()
        )
    except Exception as e:
        st.error(f"Error loading neighborhoods: {e}")
        return pd.DataFrame()


def load_theft_data() -> pd.DataFrame:
    """
    Load and process the CSV file containing bicycle theft data.

    Returns:
        pd.DataFrame: Processed theft data.
    """
    try:
        theft_data = pd.read_csv(
            "inputs/datasets/raw/Fahrraddiebstahl.csv",
            encoding='latin1',
        )

        # Ensure 'LOR' is treated as a string and padded with zeros
        theft_data['LOR'] = (
            theft_data['LOR'].astype(str).str.zfill(8)
        )

        st.write("Sample theft data preview:", theft_data.head(5))
        return theft_data
    except Exception as e:
        st.error(f"Error loading theft data: {e}")
        st.write(traceback.format_exc())
        return pd.DataFrame()


def predict_theft_risk(
    theft_time: int,
    bike_type: str,
    neighborhood_id: str,
    theft_data: pd.DataFrame,
) -> str:
    """
    Predict the risk of bicycle theft based on the provided parameters.

    Args:
        theft_time (int): The hour of the day when the theft is being assessed.
        bike_type (str): The type of bicycle.
        neighborhood_id (str): The ID of the neighborhood.
        theft_data (pd.DataFrame): The dataset containing theft records.

    Returns:
        str: The predicted risk of theft ('High Risk' or 'Low Risk').
    """
    st.write(
        "Input Parameters:",
        theft_time, bike_type, neighborhood_id,
    )

    # Filter the data based on input parameters
    filtered_data = theft_data[
        (theft_data['LOR'] == neighborhood_id)
        & (theft_data['ART_DES_FAHRRADS'].str.lower() == bike_type.lower())
    ]

    # Display full filtering details
    st.write("Filtered data preview:", filtered_data)
    st.write("Filtered data size:", filtered_data.shape[0])

    if filtered_data.empty:
        st.warning("Filtered data is empty. No matches found for this.")
        return "Low Risk"

    # Determine the most common theft hour
    common_theft_hour = (
        filtered_data['TATZEIT_ANFANG_STUNDE']
        .value_counts()
        .idxmax()
    )
    st.write("Common theft hour:", common_theft_hour)

    # Check if input time is within high-risk hours
    if common_theft_hour - 1 <= theft_time <= common_theft_hour + 1:
        return "High Risk"

    return "Low Risk"


def page_theft_prediction_body() -> None:
    """
    Render the Theft Prediction page.

    This page allows users to input parameters for theft risk prediction
    and view the results.
    """
    st.title("Bicycle Theft Prediction")

    # Load theft data
    theft_data = load_theft_data()
    if theft_data.empty:
        st.error("Theft data not available. Cannot make predictions.")
        return

    # Display column names
    st.write("Theft data columns:", theft_data.columns.tolist())

    # Load neighborhood options
    neighborhood_data = load_neighborhoods()
    if neighborhood_data.empty:
        st.error("No neighborhoods available. Check data loading.")
        return

    # Input form
    st.subheader("Enter Details for Prediction")
    bike_type = st.selectbox(
        "Bicycle Type",
        theft_data['ART_DES_FAHRRADS'].dropna().unique(),
    )
    theft_time = st.slider(
        "Time of Day (Hour)",
        min_value=0, max_value=23, value=12,
    )
    neighborhood_name = st.selectbox(
        "Neighborhood",
        neighborhood_data['PLR_NAME'],
    )

    # Get neighborhood ID for matching
    neighborhood_row = neighborhood_data.loc[
        neighborhood_data['PLR_NAME'] == neighborhood_name
    ]
    if neighborhood_row.empty:
        st.error(
            f"Neighborhood '{neighborhood_name}' not found. "
            "Please check your data."
        )
        return

    neighborhood_id = neighborhood_row['PLR_ID'].values[0]

    # Prediction button
    if st.button("Predict"):
        prediction = predict_theft_risk(
            theft_time, bike_type, neighborhood_id, theft_data
        )
        st.subheader("Prediction Result")
        st.write(f"The predicted risk of theft is: **{prediction}**")

    # Display sample data
    st.subheader("Sample Data Preview")
    st.dataframe(theft_data.head(5))
