import ray
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cluster import connect_to_ray
from data_generator import generate_log_data
from anomaly_detector import detect_anomalies
from log_processor import process_chunk
from logger import logger
from config import DATA_CHUNK_SIZE

def main():
    connect_to_ray()

    df = generate_log_data()
    df = detect_anomalies(df)

    num_chunks = DATA_CHUNK_SIZE
    data_chunks = np.array_split(df, num_chunks)

    logger.info(f"Distributing log processing across {num_chunks} chunks...")

    results = ray.get([process_chunk.remote(chunk) for chunk in data_chunks])

    logger.info("Log processing complete.")

if __name__ == "__main__":
    main()
