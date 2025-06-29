import pandas as pd
import numpy as np
from datetime import datetime
import time
import os

file = "power_data.csv"

# Create new entry for current hour
def simulate_hourly_entry():
    now = datetime.now().replace(minute=0, second=0, microsecond=0)
    hour = now.hour
    weekday = now.weekday()

    # Simulate power usage (kW): base + randomness
    power = round(np.random.uniform(0.5, 2.5) + 0.2 * np.sin(hour), 2)

    new_row = pd.DataFrame({
        "Datetime": [now],
        "hour": [hour],
        "day": [weekday],
        "Global_active_power": [power]
    })

    if os.path.exists(file):
        df = pd.read_csv(file, parse_dates=["Datetime"])
        df = pd.concat([df, new_row]).drop_duplicates("Datetime")
    else:
        df = new_row

    df.sort_values("Datetime", inplace=True)
    df.to_csv(file, index=False)
    print(f"✅ Added entry for {now} — {power} kW")

# Run once per hour
simulate_hourly_entry()
while True:
    simulate_hourly_entry()
    time.sleep(3600)  # wait 1 hour
