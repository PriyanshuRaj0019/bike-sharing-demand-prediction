# 🚲 Bike Sharing Demand Prediction

A Predictive Analytics project that forecasts bike rental demand using historical weather and seasonal data. The project applies multiple machine learning models, evaluates their performance, and provides an interactive Streamlit application for demand prediction.

## Project Objective

Build a predictive model to forecast bike rental demand using historical data and machine learning techniques.

## Key Features

* Data Cleaning and Preprocessing
* Feature Engineering from Datetime Data
* Exploratory Data Analysis
* Multiple Regression Models
* Model Performance Evaluation
* Prediction Visualization
* Interactive Streamlit Interface

## Dataset Features

* Season
* Holiday
* Working Day
* Weather Condition
* Temperature
* Feels-Like Temperature
* Humidity
* Wind Speed
* Year
* Month
* Day
* Hour
* Day of Week

### Target Variable

* Count (Total Bike Rentals)

## Machine Learning Models Used

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

## Evaluation Metrics

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

## Repository Structure

```text
.
├── bike_demand_prediction.ipynb
├── app.py
├── requirements.txt
├── correlation_heatmap.png
├── feature_importance.png
├── model_comparison.png
└── prediction_plot.png
```

## Visualizations Included

### Correlation Heatmap

Shows relationships between features and bike rental demand.

### Model Comparison

Compares the performance of multiple regression models.

### Feature Importance

Identifies the most influential factors affecting bike demand.

### Actual vs Predicted

Visualizes prediction accuracy of the selected model.

## Streamlit Application

The project includes an interactive Streamlit dashboard where users can:

* Enter weather and seasonal conditions
* Generate bike demand predictions
* Interact with the trained machine learning model

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run app.py
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Streamlit

## Learning Outcomes

* Predictive Modeling
* Regression Analysis
* Data Preprocessing
* Feature Engineering
* Model Evaluation
* Trend Analysis
* Data Visualization
* Dashboard Development

## Author

Priyanshu Raj
