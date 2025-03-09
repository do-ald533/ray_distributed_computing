import os
from dotenv import load_dotenv

load_dotenv()

RAY_ADDRESS = os.getenv("RAY_ADDRESS", "ray://ray-head:10001")

LOG_FILE = os.getenv("LOG_FILE", "logs.log")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

DATA_CHUNK_SIZE = int(os.getenv("DATA_CHUNK_SIZE", 10))
