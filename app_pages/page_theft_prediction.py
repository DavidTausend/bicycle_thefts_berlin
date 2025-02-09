import streamlit as st
import pandas as pd
import geopandas as gpd
import traceback

# Function to load neighborhoods from the GeoJSON file
def load_neighborhoods():
    try:
        lor_gdf = gpd.read_file("inputs/datasets/raw/lor_planungsraeume_2021.geojson")
        # Ensure 'PLR_ID' is treated as a string and padded with zeros
        lor_gdf['PLR_ID'] = lor_gdf['PLR_ID'].astype(str).str.zfill(8)

        # Remove 'geometry' column for display in Streamlit
        st.write("Sample data from GeoJSON:", lor_gdf.drop(columns=['geometry']).head())

        return lor_gdf[['PLR_NAME', 'PLR_ID']].sort_values(by='PLR_NAME').dropna()
    except Exception as e:
        st.error(f"Error loading neighborhoods: {e}")
        return pd.DataFrame()

# Function to load the theft data from CSV
def load_theft_data():
    try:
        theft_data = pd.read_csv("inputs/datasets/raw/Fahrraddiebstahl.csv", encoding='latin1')
        # Ensure 'LOR' is treated as a string and padded with zeros
        theft_data['LOR'] = theft_data['LOR'].astype(str).str.zfill(8)
        st.write("Sample theft data preview:", theft_data.head(5))
        return theft_data
    except Exception as e:
        st.error(f"Error loading theft data: {e}")
        st.write(traceback.format_exc())
        return pd.DataFrame()

# Function to predict theft risk
def predict_theft_risk(theft_time, bike_type, neighborhood_id, theft_data):
    st.write("Debug - Input Parameters:", theft_time, bike_type, neighborhood_id)

    # Filter the data based on input parameters
    filtered_data = theft_data[
        (theft_data['LOR'] == neighborhood_id) &
        (theft_data['ART_DES_FAHRRADS'].str.lower() == bike_type.lower())
    ]

    # Debug: Display full filtering details
    st.write("Filtered data preview:", filtered_data)
    st.write("Filtered data size:", filtered_data.shape[0])

    if filtered_data.empty:
        st.warning("Filtered data is empty. No matches found for this combination.")
        return "Low Risk"

    # Determine the most common theft hour
    common_theft_hour = filtered_data['TATZEIT_ANFANG_STUNDE'].value_counts().idxmax()
    st.write("Common theft hour:", common_theft_hour)

    # Check if input time is within high-risk hours
    if theft_time >= common_theft_hour - 1 and theft_time <= common_theft_hour + 1:
        return "High Risk"

    return "Low Risk"

# Streamlit page content
def page_theft_prediction_body():
    st.title("Bicycle Theft Prediction")

    # Load theft data
    theft_data = load_theft_data()
    if theft_data.empty:
        st.error("Theft data not available. Cannot make predictions.")
        return

    # Display column names for debugging
    st.write("Theft data columns:", theft_data.columns.tolist())

    # Load neighborhood options
    neighborhood_data = load_neighborhoods()
    if neighborhood_data.empty:
        st.error("No neighborhoods available. Check data loading.")
        return

    # Input form
    st.subheader("Enter Details for Prediction")
    bike_type = st.selectbox("Bicycle Type", theft_data['ART_DES_FAHRRADS'].dropna().unique())
    theft_time = st.slider("Time of Day (Hour)", min_value=0, max_value=23, value=12)
    neighborhood_name = st.selectbox("Neighborhood", neighborhood_data['PLR_NAME'])

    # Get neighborhood ID for matching
    neighborhood_row = neighborhood_data.loc[neighborhood_data['PLR_NAME'] == neighborhood_name]
    if neighborhood_row.empty:
        st.error(f"Neighborhood '{neighborhood_name}' not found. Please check your data.")
        return

    neighborhood_id = neighborhood_row['PLR_ID'].values[0]

    # Prediction button
    if st.button("Predict"):
        prediction = predict_theft_risk(theft_time, bike_type, neighborhood_id, theft_data)
        st.subheader("Prediction Result")
        st.write(f"The predicted risk of theft is: **{prediction}**")

    # Display sample data
    st.subheader("Sample Data Preview")
    st.dataframe(theft_data.head(5))
