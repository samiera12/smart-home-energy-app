import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load data
df = pd.read_csv('power_data.txt', sep=';', nrows=100000, na_values='?', low_memory=False)
df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], dayfirst=True)
df = df.set_index('Datetime')[['Global_active_power']].dropna()
df = df.resample('1H').mean().dropna()

df['hour'] = df.index.hour
df['dayofweek'] = df.index.dayofweek

# Train model
X = df[['hour', 'dayofweek']]
y = df['Global_active_power']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=50, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'energy_model.pkl')
print("✅ Model saved as energy_model.pkl")
# Save processed data for dashboard use
df.to_csv("power_data.csv")
