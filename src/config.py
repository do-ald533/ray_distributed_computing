import os
from dotenv import load_dotenv

load_dotenv()

RAY_ADDRESS = os.getenv("RAY_ADDRESS", "ray://ray-head:10001")

LOG_FILE = os.getenv("LOG_FILE", "logs.log")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

DATA_CHUNK_SIZE = int(os.getenv("DATA_CHUNK_SIZE", 10))

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "log_analysis")
MONGO_RAW_COLLECTION = os.getenv("MONGO_RAW_COLLECTION", "raw_logs")
MONGO_PROCESSED_COLLECTION = os.getenv("MONGO_PROCESSED_COLLECTION", "processed_logs")
MONGO_ANOMALY_COLLECTION = os.getenv("MONGO_ANOMALY_COLLECTION", "anomalies")
