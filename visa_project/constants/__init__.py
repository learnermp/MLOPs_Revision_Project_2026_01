import os
from datetime import datetime

'''
MongoDB connection related constants
'''

DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "visa_data"
MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME:str = "usvisa"
ARTIFACT_DIR:str = "artifact"
FILE_NAME:str = "usvisa.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
MODEL_FILE_NAME = "model.pkl"

'''
Data ingestion related constants
'''

DATA_INGESTION_COLLECTION_NAME:str = "visa_data"
DATA_INGESTION_DIRECTORY_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
'''
Feature store is a common MLOps concept: a central place to keep feature vectors 
that models consume.
'''
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2

