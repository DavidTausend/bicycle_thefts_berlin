import streamlit as st
import pandas as pd
import geopandas as gpd

# Function to load neighborhoods from the GeoJSON file
def load_neighborhoods():
    try:
        gdf = gpd.read_file("inputs/datasets/raw/lor_planungsraeume_2021.geojson")
        st.write("Columns in GeoDataFrame:", gdf.columns.tolist()) 
        return gdf['PLR_NAME'].sort_values().unique()  #
    except Exception as e:
        st.error(f"Error loading neighborhoods: {e}")
        return []

# Page content for theft prediction
def page_theft_prediction_body():
    st.title("Bicycle Theft Prediction")

    # Description of the page
    st.write("This page allows users to input features to predict bicycle theft risk in Berlin.")

    # Load neighborhoods
    neighborhoods = load_neighborhoods()

    # Validate if neighborhoods were loaded correctly
    if neighborhoods.size > 0:
        st.write("Available neighborhoods:", neighborhoods)  # Display loaded neighborhoods for user reference
    else:
        st.error("No neighborhoods available. Check data loading.")

    # Input form for prediction
    st.subheader("Enter Details for Prediction")
    
    bike_type = st.selectbox("Bicycle Type", ["Mountain Bike", "Road Bike", "Electric Bike"])
    theft_time = st.slider("Time of Day (Hour)", min_value=0, max_value=23, value=12)
    neighborhood = st.selectbox("Neighborhood", neighborhoods if neighborhoods.size > 0 else ["No data available"])

    # Mock prediction button
    if st.button("Predict"):
        if neighborhood == "No data available":
            st.error("Neighborhood data is missing. Cannot make prediction.")
        else:
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
