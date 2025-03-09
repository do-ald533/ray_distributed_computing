import pymongo
from config import MONGO_URI, MONGO_DB, MONGO_RAW_COLLECTION, MONGO_PROCESSED_COLLECTION, MONGO_ANOMALY_COLLECTION
from logger import logger

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]

def save_raw_logs(data):
    try:
        db[MONGO_RAW_COLLECTION].insert_many(data.to_dict("records"))
        logger.info(f"Inserted {len(data)} raw log records into MongoDB.")
    except Exception as e:
        logger.error(f"Failed to insert raw logs: {e}")

def save_processed_logs(data):
    try:
        db[MONGO_PROCESSED_COLLECTION].insert_many(data.to_dict("records"))
        logger.info(f"Inserted {len(data)} processed log records into MongoDB.")
    except Exception as e:
        logger.error(f"Failed to insert processed logs: {e}")

def save_anomalies(data):
    try:
        anomalies = data[data["is_anomaly"] == "Anomaly"]
        db[MONGO_ANOMALY_COLLECTION].insert_many(anomalies.to_dict("records"))
        logger.info(f"Inserted {len(anomalies)} anomaly records into MongoDB.")
    except Exception as e:
        logger.error(f"Failed to insert anomalies: {e}")
