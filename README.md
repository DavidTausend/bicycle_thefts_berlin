# Bicycle Thefts in Berlin - Predictive Analytics Project

<img src="/static/images/readme/diebstahlfall.webp" alt="Bicycle theft">

<h3 align="center"><a href="https://bicycle-thefts-berlin-ceae7bd5d222.herokuapp.com/">➡️ View the live project here ⬅️</a></h3>

<br/>

<div align="center">

</div>

## Introduction

This project involves the analysis of bicycle theft incidents in Berlin using machine learning, data visualization, and exploratory analysis techniques. The goal is to generate actionable insights and data-driven recommendations to help reduce theft incidents and support law enforcement strategies.

<br>

## Table of Contents

- [Bicycle Thefts in Berlin - Predictive Analytics Project](#bicycle-thefts-in-berlin---predictive-analytics-project)
  * [Introduction](#introduction)
  * [Table of Contents](#table-of-contents)
  * [Dataset Content](#dataset-content)
  * [Business Requirements](#business-requirements)
  * [Hypothesis and How to Validate](#hypothesis-and-how-to-validate)
    + [Hypothesis 1:](#hypothesis-1-)
    + [Hypothesis 2:](#hypothesis-2-)
    + [Hypothesis 3:](#hypothesis-3-)
  * [Mapping Business Requirements to Data Visualization and ML Tasks](#mapping-business-requirements-to-data-visualization-and-ml-tasks)
  * [ML Business Case](#ml-business-case)
    + [Classification Model](#classification-model)
  * [Epics and User Stories](#epics-and-user-stories)
    + [Epic 1: Data Collection and Preparation](#epic-1--data-collection-and-preparation)
    + [Epic 2: Data Visualization and Analysis](#epic-2--data-visualization-and-analysis)
    + [Epic 3: Model Training and Validation](#epic-3--model-training-and-validation)
    + [Epic 4: Dashboard Development](#epic-4--dashboard-development)
    + [Epic 5: Deployment and Release](#epic-5--deployment-and-release)
  * [Dashboard Design](#dashboard-design)
    + [Page 1: Project Summary](#page-1--project-summary)
    + [Page 2: Project Hypotheses](#page-2--project-hypotheses)
    + [Page 3: Feature Correlation Study](#page-3--feature-correlation-study)
    + [Page 4: Theft Risk Prediction](#page-4--theft-risk-prediction)
    + [Page 5: Model Performance](#page-5--model-performance)
  * [Technologies Used](#technologies-used)
    + [Languages](#languages)
    + [Python Packages](#python-packages)
    + [Other Tools](#other-tools)
  * [Testing](#testing)
    + [Manual Testing](#manual-testing)
      - [Test Scenarios](#test-scenarios)
    + [PEP 8 Validation](#pep-8-validation)
  * [Deployment & Local Development](#deployment---local-development)
    + [Deployment](#deployment)
    + [Local Development](#local-development)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
      - [Committing and Pushing Changes](#committing-and-pushing-changes)
  * [Acknowledgements](#acknowledgements)

[Generate TOC](https://ecotrust-canada.github.io/markdown-toc/)

---

## Dataset Content

The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/arnewo/bicycle-thefts-in-berlin). and it contains information on bicycle theft incidents in Berlin. Each record represents a reported theft and includes details such as the type of bicycle, location, and time of theft.

| Attribute         | Description                        | Example Value       |
|-------------------|------------------------------------|---------------------|
| IncidentID        | Unique identifier for each theft   | 123456              |
| DateTime          | Date and time of the theft         | 2023-04-15 14:30    |
| Location          | Location of theft                  | Berlin-Mitte        |
| BicycleType       | Type of stolen bicycle             | Mountain Bike       |
| TheftMethod       | How the theft occurred             | Cut lock            |
| PoliceReport      | Whether the incident was reported  | Yes/No              |

---

## Business Requirements

1. **Insight into Theft Patterns:** Identify the most common theft patterns based on location, time, and type of bicycle.
2. **Predictive Model:** Develop a machine learning model to predict high-risk areas and times for bicycle theft.

---

## Hypothesis and How to Validate

### Hypothesis 1:
- **Statement:** Bicycle thefts are more common in central districts and during specific timeframes.
- **Validation:** Analyze theft incidents by district and time of day to determine high-risk patterns.

### Hypothesis 2:
- **Statement:** Certain types of bicycles, such as e-bikes, are more frequently targeted.
- **Validation:** Perform a frequency analysis of thefts by bicycle type.

### Hypothesis 3:
- **Statement:** Theft incidents are less likely to occur in well-lit and monitored areas.
- **Validation:** Cross-reference theft locations with lighting and surveillance data (if available).

---

## Mapping Business Requirements to Data Visualization and ML Tasks

- **Requirement 1:** Use data visualizations (location, time series plots) to explore and present theft trends.
- **Requirement 2:** Develop a classification model to predict theft risk based on features such as location and time.

| Business Requirement                   | Mapped Tasks                                                         |
|-----------------------------------------|----------------------------------------------------------------------|
| Insight into Theft Patterns             | Perform exploratory data analysis and create visualizations.          |
| Predictive Model                        | Build and train a machine learning classification model.             |
| High-risk times and locations analysis  | Generate time series and location for theft incidents.       |
| Feature correlation analysis            | Calculate feature correlations and display results on the dashboard.  |

---

---

## ML Business Case

### Classification Model

We aim to develop a machine learning model that can predict the likelihood of bicycle theft incidents based on location, time, and bicycle attributes. The target variable is theft risk, categorized as either "High Risk" or "Low Risk."

- **Model Type:** Classification Model
- **Features:** Bicycle type, time of theft, location, theft method, and other contextual factors
- **Target Variable:** Theft risk level (High/Low)
- **Success Metrics:** 
  - Minimum accuracy of 80% on both training and test datasets
  - Precision and recall metrics to assess prediction quality
- **Model Failure Criteria:** 
  - Model accuracy below 75%
  - Precision or recall metrics significantly below the target range
- **Model Output:** A risk prediction and probability score indicating theft likelihood

The dataset used to train this model is publicly available on [Kaggle](https://www.kaggle.com/datasets/arnewo/bicycle-thefts-in-berlin).

---

## Epics and User Stories

The project is divided into several **Epics**, each containing multiple **User Stories** to facilitate agile development.

### Epic 1: Data Collection and Preparation
- **User Story:** As a data analyst, I want to import and explore the dataset so that I can understand its structure and quality.
- **User Story:** As a data analyst, I want to clean and prepare the data to ensure it is ready for analysis and model training.

### Epic 2: Data Visualization and Analysis
- **User Story:** As a data scientist, I want to create visualizations to analyze theft patterns, including trends over time and high-risk locations.
- **User Story:** As a data analyst, I want to perform a correlation study to identify which features are most predictive of theft risk.

### Epic 3: Model Training and Validation
- **User Story:** As a data scientist, I want to train a machine learning model to predict theft risk based on historical data.
- **User Story:** As a data engineer, I want to optimize the model using hyperparameter tuning to achieve the best performance.
- **User Story:** As a data scientist, I want to evaluate the model's performance to ensure it meets the success criteria.

### Epic 4: Dashboard Development
- **User Story:** As a non-technical user, I want to view a project summary that outlines the goals, dataset, and key insights.
- **User Story:** As a user, I want to input parameters into the model to receive a theft risk prediction for specific scenarios.
- **User Story:** As a user, I want to view performance metrics to understand the model's accuracy and reliability.

### Epic 5: Deployment and Release
- **User Story:** As a user, I want to access the application on a live web platform to explore project insights and predictions.
- **User Story:** As a developer, I want clear deployment instructions to replicate the project on other servers.

---

## Dashboard Design

The dashboard is designed to provide both technical and non-technical users with access to data-driven insights and prediction tools. The following pages are included:

### Page 1: Project Summary
- Overview of the project, dataset, and business requirements
- Introduction to the problem of bicycle thefts in Berlin

### Page 2: Project Hypotheses
- Presentation of hypotheses and validation results based on data analysis

### Page 3: Feature Correlation Study
- Visualizations and insights into feature correlations
- Correlation matrix of theft-related features

### Page 4: Theft Risk Prediction
- Form-based input for predicting theft risk based on location, time, and bicycle type
- Display of risk prediction results

### Page 5: Model Performance
- Summary of model performance metrics such as accuracy, precision, and recall
- Visualizations of prediction accuracy and confusion matrix

---

## Technologies Used

### Languages
- [Python](https://www.python.org/)

### Python Packages
- [Pandas](https://pandas.pydata.org/docs/) - Data manipulation and analysis
- [Numpy](https://numpy.org/) - Numerical computations
- [Matplotlib](https://matplotlib.org/) - Data visualization
- [Streamlit](https://streamlit.io/) - Interactive data dashboards
- [Scikit-learn](https://scikit-learn.org/) - Machine learning library
- [Geopandas](https://geopandas.org/) - Spatial data analysis

### Other Tools
- [Git](https://git-scm.com/) - Version control
- [GitHub](https://github.com/) - Repository management
- [Gitpod]: (https://www.gitpod.io/) - Cloud-based IDE 
- [Heroku](https://www.heroku.com/) - Application deployment

---

## Testing

### Manual Testing
The application was manually tested to verify that each feature functions as intended. This includes:
- Navigating between dashboard pages
- Interacting with form elements and submitting data
- Viewing prediction results and visualizations

### User Story Testing

---

#### As a non-technical user, I can view a project summary that describes the project, dataset, and business requirements to understand the project at a glance.

| Feature               | Action                       | Expected Result                                     | Actual Result         |
|-----------------------|------------------------------|----------------------------------------------------|-----------------------|
| Project Summary Page  | Viewing summary page          | Page is displayed, can move between sections        | Functions as intended |

---

#### As a non-technical user, I can view the project hypotheses and validations to determine what the project was trying to achieve and whether it was successful.

| Feature                | Action                         | Expected Result                                  | Actual Result         |
|------------------------|---------------------------------|-------------------------------------------------|-----------------------|
| Project Hypotheses Page| Navigate to page                | Clicking on navbar link in sidebar navigates to correct page | Functions as intended |

---

#### As a non-technical user, I can enter unseen data into the model and receive a prediction (Business Requirement 2).

| Feature             | Action                         | Expected Result                                  | Actual Result         |
|---------------------|---------------------------------|-------------------------------------------------|-----------------------|
| Prediction Page     | Navigate to page                | Clicking on navbar link in sidebar navigates to correct page | Functions as intended |
| Enter Live Data     | Interact with widgets           | All widgets are interactive, respond to user input | Functions as intended |
| Live Prediction     | Click on 'Predict' button       | Clicking on button displays message on page with prediction and % chance | Functions as intended |

---

#### As a technical user, I can view the correlation analysis to see how the outcomes were reached (Business Requirement 1).

| Feature               | Action                         | Expected Result                                  | Actual Result         |
|-----------------------|---------------------------------|-------------------------------------------------|-----------------------|
| Correlation Study Page| Navigate to page                | Clicking on navbar link in sidebar navigates to correct page | Functions as intended |
| Correlation Data      | View correlation data           | Correlation data is displayed on dashboard       | Functions as intended |
| Location Visualization | Tick localtion checkbox           | Risk is displayed               | Functions as intended |
| Feature Correlation   | Select feature from dropdown box| Relevant feature plot is displayed               | Functions as intended |

---

#### As a technical user, I can view all the data to understand the model performance and see statistics related to the model (Business Requirement 2).

| Feature             | Action                         | Expected Result                                  | Actual Result         |
|---------------------|---------------------------------|-------------------------------------------------|-----------------------|
| Model Performance Page | Navigate to page             | Clicking on navbar link in sidebar navigates to correct page | Functions as intended |
| Success Metrics      | View page                      | Success metrics outlined in business case are displayed | Functions as intended |
| ML Pipelines         | View page                      | Both ML pipelines are displayed                  | Functions as intended |
| Feature Importance   | View page                      | Most important features are plotted and displayed | Functions as intended |
| Model Performance    | View page                      | Confusion matrix for train and test sets is displayed | Functions as intended |

---

### PEP 8 Validation
- All Python code was validated for PEP 8 compliance.
- Minor warnings related to long strings in docstrings and Streamlit content were ignored as they do not affect readability.

---

## Deployment & Local Development

### Deployment

### Local Development

The site is deployed using Heroku.

To deploy the site using Heroku - [Heroku](https://bicycle-thefts-berlin-ceae7bd5d222.herokuapp.com/)

1. Fork or clone this repository.
2. Create a new Heroku app.
3. Choose a region.
4. Set the buildbacks to Python and NodeJS in that order.
5. In Heroku's settings, add a config var of PORT and set the value to 8000.
6. Link the Heroku app to the Github respository.
7. Click on Deploy.

The site has now been deployed. Please note that this process may take a few minutes before the site goes live.

#### How to Fork

To fork the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project: [DavidTausend/bicycle_thefts_berlin](https://github.com/DavidTausend/bicycle_thefts_berlin)
3. Click the "Fork" button in the top right corner.

#### How to Clone

To clone the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project: [DavidTausend/bicycle_thefts_berlin](https://github.com/DavidTausend/bicycle_thefts_berlin)
3. Click on the "Code" button, select whether you would like to clone with HTTPS, SSH, or GitHub CLI, and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type `git clone` into the terminal and then paste the link you copied in step 3. Press enter.

#### Committing and Pushing Changes

After making changes to your local copy, you can commit and push them to GitHub:

1. Open the terminal in the directory of your cloned repository.
2. Use `git status` to see the changes you've made.
3. Use `git add .` to stage all changes for commit, or `git add <filename>` to stage specific files.
4. Use `git commit -m "Your commit message here"` to commit your changes with a descriptive message.
5. Use `git push origin main` to push your changes to the main branch on GitHub.

---

## Acknowledgements

- Thanks to the Berlin open data initiative for providing the dataset.
- Special thanks to my mentor for their guidance throughout the project.


[Back to top](#table-of-contents)