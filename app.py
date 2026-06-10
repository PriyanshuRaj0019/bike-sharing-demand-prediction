import streamlit as st
import joblib
import pandas as pd

model = joblib.load(
    "models/best_bike_demand_model.pkl"
)

st.title("Bike Sharing Demand Prediction")

season = st.selectbox(
    "Season",
    [1,2,3,4]
)

holiday = st.selectbox(
    "Holiday",
    [0,1]
)

workingday = st.selectbox(
    "Working Day",
    [0,1]
)

weather = st.selectbox(
    "Weather",
    [1,2,3,4]
)

temp = st.slider(
    "Temperature",
    0.0,
    45.0,
    25.0
)

atemp = st.slider(
    "Feels Like Temp",
    0.0,
    50.0,
    25.0
)

humidity = st.slider(
    "Humidity",
    0,
    100,
    60
)

windspeed = st.slider(
    "Wind Speed",
    0.0,
    70.0,
    15.0
)

year = st.number_input(
    "Year",
    2011,
    2025,
    2012
)

month = st.slider(
    "Month",
    1,
    12,
    6
)

day = st.slider(
    "Day",
    1,
    31,
    15
)

hour = st.slider(
    "Hour",
    0,
    23,
    8
)

dayofweek = st.slider(
    "Day Of Week",
    0,
    6,
    1
)

if st.button("Predict Demand"):

    input_data = pd.DataFrame([[
        season,
        holiday,
        workingday,
        weather,
        temp,
        atemp,
        humidity,
        windspeed,
        year,
        month,
        day,
        hour,
        dayofweek
    ]],
    columns=[
        "season",
        "holiday",
        "workingday",
        "weather",
        "temp",
        "atemp",
        "humidity",
        "windspeed",
        "year",
        "month",
        "day",
        "hour",
        "dayofweek"
    ])

    prediction = model.predict(
        input_data
    )[0]

    st.success(
        f"Predicted Bike Rentals: {int(prediction)}"
    )