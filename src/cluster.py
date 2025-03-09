import ray
from config import RAY_ADDRESS
from logger import logger

def connect_to_ray():
    try:
        ray.init(address=RAY_ADDRESS, ignore_reinit_error=True)
        logger.info(f"Connected to Ray cluster at {RAY_ADDRESS}")
    except Exception as e:
        logger.error(f"Failed to connect to Ray cluster: {e}")
