import pandas as pd
import numpy as np
from logger import logger

def generate_log_data(num_records=10000):
    logger.info(f"Generating {num_records} log records...")

    log_data = {
        "timestamp": pd.date_range(start="2025-03-01", periods=num_records, freq="T"),
        "ip_address": [f"192.168.1.{i % 255}" for i in range(num_records)],
        "status_code": np.random.choice([200, 404, 500, 301, 403, 503], num_records, p=[0.7, 0.1, 0.05, 0.05, 0.05, 0.05]),
        "url": [f"/page_{i % 10}.html" for i in range(num_records)]
    }

    df = pd.DataFrame(log_data)
    df["hour"] = df["timestamp"].dt.hour
    logger.info("Log data generation complete.")

    return df
