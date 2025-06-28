import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from datetime import datetime

# Load model and data
model = joblib.load("energy_model.pkl")
df = pd.read_csv("power_data.csv", parse_dates=["Datetime"], index_col="Datetime")

# Title
st.title("Smart Home Energy Usage Predictor")

# User input
hour = st.slider("Select Hour of Day", 0, 23, 13)
day = st.selectbox("Select Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
day_number = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(day)

# Prediction
prediction = model.predict([[hour, day_number]])[0]
st.markdown(f"🔌 **Predicted Energy Usage: {prediction:.2f} kW**")

# --- 1. Anomaly Warning ---
threshold = 2.5  # You can adjust this
if prediction > threshold:
    st.warning("⚠️ High usage alert! Consider delaying non-essential appliance use.")
else:
    st.success("✅ Usage is within normal range.")

# --- 2. Cost Estimation ---
cost_per_kwh = 6.0  # ₹/kWh — adjust to your local rate
estimated_cost = prediction * cost_per_kwh
st.write(f"💰 **Estimated Cost**: ₹{estimated_cost:.2f}")

# --- 3. Best Hour Suggestion ---
best_hour = df.groupby("hour")["Global_active_power"].mean().idxmin()
st.info(f"🕒 **Best Hour to Use Appliances**: {best_hour}:00 (Lowest average usage)")

# --- 4. Today's Usage Trend ---
today_data = df[df.index.date == pd.Timestamp.now().date()]
if not today_data.empty:
    st.subheader("📈 Today's Energy Usage Trend")
    fig, ax = plt.subplots()
    ax.plot(today_data.index.hour, today_data["Global_active_power"], marker='o')
    ax.set_xlabel("Hour")
    ax.set_ylabel("Power (kW)")
    ax.set_title("Energy Usage Throughout Today")
    st.pyplot(fig)
else:
    st.info("No data available for today's usage yet.")

# --- 5. Appliance Suggestion (Optional Bonus) ---
appliance = st.selectbox("Appliance You Plan to Use", ["None", "Washing Machine", "Heater", "AC"])
if appliance != "None":
    low_usage_hours = df.groupby('hour')["Global_active_power"].mean().nsmallest(3).index.tolist()
    if hour in low_usage_hours:
        st.success(f"✅ It's a good time to use the {appliance}.")
    else:
        st.warning(f"⚠️ Consider using the {appliance} during off-peak hours (e.g., {low_usage_hours[0]}:00).")
