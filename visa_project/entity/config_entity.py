'''
The entity folder in a project follows a common software engineering pattern, 
particularly from domain-driven design (DDD), where "entities" represent core domain 
objects with identity and behavior. In the context of your MLOps pipeline, 
it serves as a centralized place for defining the data structures 
(often as Python dataclasses) that encapsulate key concepts like configurations 
and artifacts.
'''
'''
onfig_entity manipulates constants to create path.
'''
import os
from visa_project.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP:str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    pipeline_name:str = PIPELINE_NAME
    artifact_dir:str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
    timestamp:str = TIMESTAMP

training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir:str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIRECTORY_NAME)
    feature_store_file_path:str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path:str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path:str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio:float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = DATA_INGESTION_COLLECTION_NAME 