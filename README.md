# 🔋 Smart Home Energy Usage Predictor

A lightweight, interactive Streamlit web app that predicts household electricity consumption by hour and day of the week. This project helps optimize energy usage by providing intelligent insights such as:

- ⚡ Hourly energy prediction
- 💸 Cost estimation
- ⚠️ High usage alerts
- 🕒 Recommended best time to use appliances
- 📈 Today's usage trend visualization
- ✅ Appliance usage suggestions

---

## 🚀 Features

| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| 🔌 **Energy Prediction**       | Predicts power usage (in kW) based on selected hour and weekday             |
| 💰 **Cost Estimation**         | Calculates estimated electricity cost based on local per kWh pricing        |
| ⚠️ **Anomaly Detection**       | Warns user if predicted usage crosses a defined threshold                   |
| 🕒 **Best Hour Suggestion**    | Shows the hour with lowest average usage across dataset                     |
| 📈 **Today's Usage Chart**     | Line plot of hourly usage for the current day                               |
| 💡 **Appliance Scheduler**     | Suggests whether to use an appliance at the selected time                   |

---

## 📂 Project Structure

smart-home-energy-app/
├── app.py # Streamlit web app
├── energy_model.pkl # Trained Random Forest model
├── power_data.csv # Hourly energy data used for analysis
├── requirements.txt # Dependencies for deployment


