# Bicycle Thefts in Berlin - Predictive Analytics Project

user stories ideas:

# Bicycle Thefts in Berlin - Project

## Overview
This project aims to analyze and predict bicycle theft patterns in Berlin using machine learning. The goal is to develop a Streamlit-based web application that visualizes key insights and provides predictive analytics based on various factors like time, location, and bike type.

---

### Prerequisites
- Python 3.8+
- Streamlit
- Pandas, NumPy, Scikit-learn, Plotly, etc.

## User Stories

### Backlog
1. **Data Source Identification**
   - **As a** data analyst,
   - **I want to** identify and validate reliable data sources for bicycle thefts in Berlin,
   - **so that** I can ensure the accuracy and completeness of the dataset for analysis.

2. **Stakeholder Interviews**
   - **As a** project manager,
   - **I want to** conduct interviews with key stakeholders (e.g., city officials, police officers),
   - **so that** I can gather detailed requirements and expectations for the project.

3. **Define Success Metrics**
   - **As a** data scientist,
   - **I want to** define clear success metrics for the predictive models,
   - **so that** I can effectively evaluate their performance.

### To Do
1. **Data Collection**
   - **As a** data engineer,
   - **I want to** collect and consolidate data from various sources (e.g., police reports, open data portals),
   - **so that** I have a comprehensive dataset for analysis.

2. **Data Cleaning and Preprocessing**
   - **As a** data scientist,
   - **I want to** clean and preprocess the collected data,
   - **so that** it is suitable for exploratory analysis and modeling.

3. **Exploratory Data Analysis (EDA)**
   - **As a** data analyst,
   - **I want to** perform EDA on the dataset,
   - **so that** I can uncover patterns, trends, and insights related to bicycle thefts.

### In Progress
1. **Feature Engineering**
   - **As a** data scientist,
   - **I want to** create new features from the existing data (e.g., time of day, weather conditions),
   - **so that** I can improve the performance of the predictive models.

2. **Model Selection and Training**
   - **As a** machine learning engineer,
   - **I want to** select and train various machine learning models (e.g., Random Forest, XGBoost),
   - **so that** I can determine the best-performing model for predicting bike theft risk.

### Testing
1. **Model Evaluation**
   - **As a** data scientist,
   - **I want to** evaluate the trained models using defined success metrics (e.g., accuracy, precision, recall),
   - **so that** I can select the most effective model for deployment.

2. **Dashboard Functionality Testing**
   - **As a** QA tester,
   - **I want to** test the Streamlit dashboard for functionality and usability,
   - **so that** I can ensure it meets user requirements and provides accurate predictions.

### Done
1. **Initial Data Load and Inspection**
   - **As a** data analyst,
   - **I want to** load the dataset and inspect its structure,
   - **so that** I can understand the available data and plan further analysis.

2. **Basic Visualizations**
   - **As a** data analyst,
   - **I want to** create basic visualizations (e.g., theft counts by neighborhood, time trends),
   - **so that** stakeholders can quickly grasp the key insights from the data.

3. **Deploy Streamlit App**
   - **As a** developer,
   - **I want to** deploy the Streamlit application to a platform like Heroku,
   - **so that** users can access the dashboard online.

---

## Additional User Stories for Enhanced Functionality

### Interactive Features
1. **User Input for Predictions**
   - **As a** bicycle owner,
   - **I want to** input specific details (e.g., location, time, bike type) into the dashboard,
   - **so that** I can receive a personalized theft risk prediction.

2. **Interactive Maps**
   - **As a** city official,
   - **I want to** interact with maps displaying theft hotspots,
   - **so that** I can visually identify and analyze high-risk areas.

### Advanced Analytics
1. **Time Series Forecasting**
   - **As a** data scientist,
   - **I want to** implement time series forecasting,
   - **so that** I can predict future trends in bicycle thefts.

2. **Correlation Analysis**
   - **As a** data analyst,
   - **I want to** perform correlation analysis between different features,
   - **so that** I can identify which factors are most strongly associated with bike thefts.

### User Experience Enhancements
1. **Responsive Design**
   - **As a** user,
   - **I want to** access the dashboard on various devices (e.g., mobile, tablet, desktop),
   - **so that** I can view insights conveniently from anywhere.

2. **Accessibility Features**
   - **As a** user with disabilities,
   - **I want to** use the dashboard with screen readers and keyboard navigation,
   - **so that** I can access the information without barriers.

---

## Project Structure
- **Backlog:** User Stories 1, 2, 3
- **To Do:** User Stories 4, 5, 6
- **In Progress:** User Stories 7, 8
- **Testing:** User Stories 9, 10
- **Done:** User Stories 11, 12, 13
- **Additional Enhancements:** User Stories 14-19 can be placed in Backlog or To Do based on priority.


## Dashboard Design (Streamlit App User Interface)

The dashboard is designed to cater to two main user types:
- **Non-Technical Users:** Business stakeholders such as project managers and city officials.
- **Technical Users:** Data practitioners interested in model performance and detailed analytics.

### **Page 1: Quick Project Summary**
- **Project Overview:** Brief description of the project goals and objectives.
- **Project Terms & Jargon:** Definitions of key terms used in the project.
- **Describe Project Dataset:** Overview of the dataset, including sources and key attributes.
- **State Business Requirements:** Clear listing of the business needs the project addresses.

### **Page 2: Bicycle Theft Patterns Study**
- **State Business Requirement 1:** Identify and visualize theft patterns.
- **Checkbox:** Data inspection (display number of rows and columns, first ten rows of data).
- **Display Correlated Variables:** Show variables most correlated with bike thefts and draw conclusions.
- **Checkbox:** Individual plots for each correlated variable.
- **Checkbox:** Parallel plot to visualize relationships between thefts and correlated variables.

### **Page 3: Theft Risk Predictor**
- **State Business Requirement 2:** Predict the likelihood of bike theft.
- **Widgets Inputs:** Allow users to input variables such as location, time, bike type.
- **Run Predictive Analysis Button:** 
  - **Outputs:**
    - Theft risk prediction based on input variables.
    - Probability of theft occurring.
    - Suggestions for reducing theft risk.
    
### **Page 4: Project Hypotheses and Validation**
- **State Each Hypothesis:** List project hypotheses related to bike theft.
- **Validation Process:**
  - **Hypothesis 1:** High-risk areas have a higher frequency of bike thefts.
    - **Validation:** Correlation study confirms higher theft rates in specific neighborhoods.
  - **Hypothesis 2:** Certain times of day have higher theft incidents.
    - **Validation:** Time-based analysis supports increased thefts during evening hours.
  - **Hypothesis 3:** Specific bike types are targeted more frequently.
    - **Validation:** Data shows higher theft rates for certain bike categories.
- **Conclusions:** Summarize findings and their implications for stakeholders.

### **Page 5: Model Performance - Predict Theft Risk**
- **ML Pipeline Steps:** Overview of the machine learning pipeline used.
- **Feature Importance:** Visualization showing which features contribute most to theft predictions.
- **Pipeline Performance:** Metrics such as accuracy, precision, recall, and ROC-AUC scores.

### **Page 6: Model Performance - Predictive Insights**
- **Model Considerations:** Discussion on model selection and parameter tuning.
- **Performance Metrics:** Detailed metrics and evaluation of the model's performance.
- **Visualizations:** Confusion matrix, ROC curves, and other relevant plots.

### **Page 7: Cluster Analysis**
- **Cluster Identification:** Use clustering algorithms to identify patterns in theft data.
- **Silhouette Plot:** Assess the quality of the clusters.
- **Cluster Distribution:** Show distribution of theft incidents across different clusters.
- **Relative Percentage of Thefts in Each Cluster:** Visual representation of theft distribution.
- **Cluster Profile:** Detailed profile of each cluster, highlighting key characteristics.

---

## Dashboard Principles

### Clear Use Case and Course of Action
- **Use Case:** Each page addresses specific business requirements, providing actionable insights.
- **Course of Action:** Users can navigate through the dashboard to perform data inspections, run predictions, and understand model performances to make informed decisions.

### Tailored to User Types
- **Non-Technical Users:** Focus on visualizations, summaries, and actionable insights.
- **Technical Users:** Provide detailed analytics, model performance metrics, and advanced visualizations.

---

pandas doc
https://pandas.pydata.org/docs/

pip install -r requirements.txt