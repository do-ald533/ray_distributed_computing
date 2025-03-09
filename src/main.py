import ray
import numpy as np
import pandas as pd
from collections import defaultdict
from cluster import connect_to_ray 
from data_generator import generate_log_data
from anomaly_detector import detect_anomalies
from log_processor import process_chunk
from db import save_raw_logs, save_processed_logs, save_anomalies
from logger import logger
from config import DATA_CHUNK_SIZE

def main():
    
    try:
        logger.info("Connecting to Ray cluster...")
        connect_to_ray()

        logger.info("Generating log data...")
        df = generate_log_data()
        save_raw_logs(df)

        logger.info("Detecting anomalies...")
        df = detect_anomalies(df)

        num_chunks = min(DATA_CHUNK_SIZE, len(df)) 
        data_chunks = np.array_split(df, num_chunks)

        logger.info(f"Distributing log processing across {num_chunks} chunks...")

        chunk_refs = [ray.put(chunk) for chunk in data_chunks]
        results = ray.get([process_chunk.remote(chunk_ref) for chunk_ref in chunk_refs])

        logger.info("Log processing complete.")

        final_status_counts = defaultdict(int)
        final_url_counts = defaultdict(int)
        final_hourly_counts = defaultdict(int)
        final_anomaly_counts = defaultdict(int)

        for status_counts, url_counts, hourly_counts, anomaly_counts in results:
            for key, value in status_counts.items():
                final_status_counts[key] += value
            for key, value in url_counts.items():
                final_url_counts[key] += value
            for key, value in hourly_counts.items():
                final_hourly_counts[key] += value
            for key, value in anomaly_counts.items():
                final_anomaly_counts[key] += value

        logger.info("Aggregating processed data...")

        processed_data = pd.DataFrame.from_dict(final_status_counts, orient="index", columns=["status_code_count"])
        processed_data["url_count"] = processed_data.index.map(lambda x: final_url_counts.get(x, 0))
        processed_data["hourly_requests"] = processed_data.index.map(lambda x: final_hourly_counts.get(x, 0))
        processed_data["anomaly_count"] = processed_data.index.map(lambda x: final_anomaly_counts.get(x, 0))

        logger.info("Saving processed logs and anomalies...")
        save_processed_logs(processed_data)
        save_anomalies(df)

        logger.info("Pipeline execution completed successfully.")

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
