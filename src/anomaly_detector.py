from sklearn.ensemble import IsolationForest
from logger import logger

def detect_anomalies(df):
    logger.info("Training Isolation Forest for anomaly detection...")

    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    df["anomaly"] = model.fit_predict(df[["hour", "status_code"]])
    df["is_anomaly"] = df["anomaly"].apply(lambda x: "Anomaly" if x == -1 else "Normal")

    num_anomalies = df[df["is_anomaly"] == "Anomaly"].shape[0]
    logger.info(f"Anomaly detection complete. Found {num_anomalies} anomalies.")

    return df

