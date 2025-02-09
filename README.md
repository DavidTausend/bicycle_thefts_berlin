# Bicycle Thefts in Berlin - Predictive Analytics Project

<img src="/static/images/readme/diebstahlfall.webp" alt="">

This project involves the analysis of bicycle theft incidents in Berlin using machine learning, data visualization, and exploratory analysis techniques. The goal is to generate actionable insights and data-driven recommendations to help reduce theft incidents and support law enforcement strategies.

## Table of Contents

[Generate TOC](https://ecotrust-canada.github.io/markdown-toc/)

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

## Business Requirements

1. **Insight into Theft Patterns:** Identify the most common theft patterns based on location, time, and type of bicycle.
2. **Predictive Model:** Develop a machine learning model to predict high-risk areas and times for bicycle theft.

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

## Mapping Business Requirements to Data Visualization and ML Tasks

- **Requirement 1:** Use data visualizations (heatmaps, time series plots) to explore and present theft trends.
- **Requirement 2:** Develop a classification model to predict theft risk based on features such as location and time.


