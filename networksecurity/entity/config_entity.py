from datetime import datetime
import os

from networksecurity.constant import training_pipeline


print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)


class TrainingPipelineConfig:

    def __init__(self, timestamp=datetime.now()):

        timestamp = timestamp.strftime("%m%d%Y__%H%M%S")

        self.pipeline_name = training_pipeline.PIPELINE_NAME

        self.artifact_name = training_pipeline.ARTIFACT_DIR

        self.artifact_dir = os.path.join(
            self.artifact_name,
            timestamp
        )

        self.timestamp: str = timestamp


class DataIngestionConfig:

    def __init__(
        self,
        training_pipeline_config: TrainingPipelineConfig
    ):

        # MongoDB database
        self.database_name = (
            training_pipeline.DATA_INGESTION_DATABASE_NAME
        )

        # MongoDB collection
        self.collection_name = (
            training_pipeline.DATA_INGESTION_COLLECTION_NAME
        )

        # Data ingestion directory
        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME
        )

        # Feature store directory
        self.feature_store_dir = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR
        )

        # Ingested directory
        self.ingested_dir = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR
        )

        # Feature store file
        self.feature_store_file_path = os.path.join(
            self.feature_store_dir,
            training_pipeline.FILE_NAME
        )

        # Training file
        self.training_file_path = os.path.join(
            self.ingested_dir,
            training_pipeline.TRAIN_FILE_NAME
        )

        # Testing file
        self.testing_file_path = os.path.join(
            self.ingested_dir,
            training_pipeline.TEST_FILE_NAME
        )

        # Train-test split ratio
        self.train_test_split_ratio = (
            training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        )