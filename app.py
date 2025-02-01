import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, f1_score, classification_report

# Define paths for test data, models, and feature columns
test_data_path = 'outputs/datasets/featured/TestSet_Featured.csv'
logistic_model_path = '/workspace/bicycle_thefts_berlin/jupyter_notebooks/Logistic Regression_model.pkl'
random_forest_model_path = '/workspace/bicycle_thefts_berlin/jupyter_notebooks/Random Forest_model.pkl'
model_columns_path = '/workspace/bicycle_thefts_berlin/jupyter_notebooks/model_columns.pkl'

# 1. Data Loading Test
def test_data_loading():
    try:
        test_data = pd.read_csv(test_data_path)
        st.write("Data loaded successfully")
        st.write(test_data.head())
        return test_data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# 2. Model Loading Test
def test_model_loading():
    try:
        logistic_model = joblib.load(logistic_model_path)
        random_forest_model = joblib.load(random_forest_model_path)
        st.write("Models loaded successfully")
        return logistic_model, random_forest_model
    except FileNotFoundError as e:
        st.error(f"Error loading models: {e}")
        return None, None

# 3. Align features with model's expected columns
def align_features_and_target(X_test, y_test):
    try:
        # Convert date columns to numeric timestamps
        date_columns = ['ANGELEGT_AM', 'TATZEIT_ENDE_DATUM']
        for col in date_columns:
            if col in X_test.columns:
                X_test[col] = pd.to_datetime(X_test[col], errors='coerce').astype('int64') // 10**9

        # Convert all non-numeric columns to numeric
        X_test = X_test.apply(pd.to_numeric, errors='coerce').fillna(0)

        # Align features with expected columns
        expected_columns = joblib.load(model_columns_path)
        X_test_aligned = X_test.reindex(columns=expected_columns, fill_value=0)

        # Remove missing values in the target column
        y_test_cleaned = pd.to_numeric(y_test, errors='coerce').dropna().astype(int)

        # Ensure alignment between features and target
        X_test_aligned = X_test_aligned.loc[y_test_cleaned.index]

        # Debug output
        st.write(f"Aligned X_test shape: {X_test_aligned.shape}")
        st.write(f"Cleaned y_test shape: {y_test_cleaned.shape}")

        # Final consistency check
        if X_test_aligned.shape[0] != y_test_cleaned.shape[0]:
            st.error("Mismatch between number of samples in X_test and y_test after alignment.")
            return None, None

        return X_test_aligned, y_test_cleaned
    except Exception as e:
        st.error(f"Error aligning features and target: {e}")
        return None, None

# 4. Interactive Elements Test
def test_interactive_elements():
    st.write("Testing interactive elements")
    selected_model = st.selectbox("Choose a model to evaluate", ["Logistic Regression", "Random Forest"])
    if selected_model:
        st.write(f"Selected model: {selected_model}")
    return selected_model

# 5. Model Prediction and Metrics Display
def test_model_prediction(model, X_test, y_test):
    try:
        # Perform prediction
        y_pred = model.predict(X_test)

        # Metrics Calculation
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='weighted')

        st.write(f"Accuracy: {accuracy:.4f}")
        st.write(f"F1 Score: {f1:.4f}")
        st.write("Classification Report:")
        st.text(classification_report(y_test, y_pred))
    except Exception as e:
        st.error(f"Error during prediction: {e}")

# 6. Main Dashboard Testing Logic
def main():
    st.title("Dashboard Functionality Testing")

    # Step 1: Load Data
    test_data = test_data_loading()
    if test_data is None:
        return

    # Display column data types for debugging
    st.write("Test Data Types:", test_data.dtypes)

    # Separate features and target
    TARGET_COLUMN = 'VERSUCH'
    X_test = test_data.drop(columns=[TARGET_COLUMN])
    y_test = test_data[TARGET_COLUMN]

    # Step 2: Align Test Data Features and Target
    X_test, y_test = align_features_and_target(X_test, y_test)
    if X_test is None or y_test is None:
        return

    # Step 3: Load Models
    logistic_model, random_forest_model = test_model_loading()
    if not logistic_model or not random_forest_model:
        return

    # Step 4: Test Interactive Elements
    selected_model_name = test_interactive_elements()

    # Step 5: Perform Prediction Based on Selected Model
    if selected_model_name == "Logistic Regression":
        test_model_prediction(logistic_model, X_test, y_test)
    elif selected_model_name == "Random Forest":
        test_model_prediction(random_forest_model, X_test, y_test)

if __name__ == "__main__":
    main()
