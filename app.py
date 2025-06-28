import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('energy_model.pkl')

st.title("Smart Home Energy Usage Predictor")

hour = st.slider("Select Hour of Day", 0, 23, 12)
day = st.selectbox("Select Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
day_number = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(day)

prediction = model.predict([[hour, day_number]])[0]

st.write(f"### 🔌 Predicted Energy Usage: {prediction:.2f} kW")
