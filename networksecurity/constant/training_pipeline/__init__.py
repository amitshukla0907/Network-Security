import os
import sys
import pandas as pd
import numpy as np

"""
    Data ingestion related constant start with DATA_INGESTION VAR NAME
"""

TARGET_COLUMN: str = "Result"
PIPELINE_NAME: str = "networksecurity"
ARTIFACT_DIR: str = "ArtifactS"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "AMITAI"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2