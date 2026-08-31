from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    TrainingPipelineConfig,
    DataTransformationConfig
)

import sys


if __name__ == "__main__":

    try:
        # 1. Create Training Pipeline Config
        training_pipeline_config = TrainingPipelineConfig()

        # 2. Create Data Ingestion Config
        data_ingestion_config = DataIngestionConfig(
            training_pipeline_config
        )

        # 3. Create Data Ingestion Object
        data_ingestion = DataIngestion(
            data_ingestion_config
        )

        logging.info("Initiating data ingestion")

        # 4. Start Data Ingestion
        data_ingestion_artifact = (
            data_ingestion.initiate_data_ingestion()
        )

        logging.info("Data ingestion completed")

        print(data_ingestion_artifact)

        # 5. Create Data Validation Config
        data_validation_config = DataValidationConfig(
            training_pipeline_config
        )

        # 6. Create Data Validation Object
        data_validation = DataValidation(
            data_validation_config=data_validation_config,
            data_ingestion_artifact=data_ingestion_artifact
        )

        logging.info("Initiating data validation")

        # 7. Start Data Validation
        data_validation_artifact = (
            data_validation.initiate_data_validation()
        )

        logging.info("Data validation completed")

        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(training_pipeline_config)
        logging.info("data transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data transformation ended")
    except Exception as e:
        raise NetworkSecurityException(e, sys)