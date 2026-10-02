import pandas as pd
import numpy as np
import os
import random
from datetime import datetime, timedelta


def generate_messy_transaction_logs():
    print("Generating extensive unstructured system logs...")
    np.random.seed(11145)  # Secure seeding matching profile logic

    num_entries = 45000
    start_time = datetime(2026, 8, 1, 0, 0, 0)

    # Generate realistic timestamps
    timestamps = [
        start_time + timedelta(seconds=i * random.randint(1, 5))
        for i in range(num_entries)
    ]

    # Simulating messy unstructured log logs
    components = ["AUTH_SERVICE", "PAYMENT_GATEWAY", "USER_SESSION", "DATA_API"]
    actions = [
        "LOGIN_SUCCESS",
        "FETCH_BAL",
        "TRANSACTION_INIT",
        "DB_QUERY_EXEC",
        "LOGOUT",
    ]
    statuses = [
        "SUCCESS",
        "SUCCESS",
        "SUCCESS",
        "WARNING",
        "FAIL",
    ]  # Intentionally heavy successes

    print("Structuring log parameters...")
    data = {
        "Timestamp": [ts.strftime("%Y-%m-%d %H:%M:%S") for ts in timestamps],
        "Component": np.random.choice(components, size=num_entries),
        "Action": np.random.choice(actions, size=num_entries),
        "Response_Time_MS": np.random.exponential(scale=120, size=num_entries).round(2),
        "Status_Flag": np.random.choice(statuses, size=num_entries),
        "User_ID": [f"USR_{random.randint(1000, 9999)}" for _ in range(num_entries)],
    }

    df = pd.DataFrame(data)

    # Inject deliberate systemic performance drops (server spikes above 1500ms)
    df.loc[df.sample(frac=0.02).index, "Response_Time_MS"] = np.random.uniform(
        1500, 4500, size=int(num_entries * 0.02)
    ).round(2)
    df.loc[df["Response_Time_MS"] > 1500, "Status_Flag"] = "FAIL"

    # Save output to local raw environment
    os.makedirs("data/raw", exist_ok=True)
    raw_out = "data/raw/unstructured_system_logs.csv"
    df.to_csv(raw_out, index=False)
    print(f"Success! Generated {len(df)} messy log coordinates at: {raw_out}")


if __name__ == "__main__":
    generate_messy_transaction_logs()
