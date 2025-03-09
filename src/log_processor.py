import ray
from logger import logger

@ray.remote
def process_chunk(chunk):
    logger.info(f"Processing chunk with {len(chunk)} records...")

    try:
        status_counts = chunk["status_code"].value_counts().to_dict()
        url_counts = chunk["url"].value_counts().to_dict()
        hourly_counts = chunk["hour"].value_counts().to_dict()
        anomaly_counts = chunk["is_anomaly"].value_counts().to_dict()

        logger.info("Chunk processing complete.")
        return status_counts, url_counts, hourly_counts, anomaly_counts

    except Exception as e:
        logger.error(f"Error processing chunk: {e}")
        return {}, {}, {}, {}
