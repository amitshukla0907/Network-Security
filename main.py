from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    TrainingPipelineConfig
)

import sys


if __name__ == "__main__":

    try:

        # Create Training Pipeline Config object
        trainingpipelineconfig = TrainingPipelineConfig()

        # Create Data Ingestion Config object
        dataingestionconfig = DataIngestionConfig(
            trainingpipelineconfig
        )

        # Create Data Ingestion object
        data_ingestion = DataIngestion(
            dataingestionconfig
        )

        logging.info("Initiate the data ingestion")

        # Start data ingestion
        dataingestionartifact = (
            data_ingestion.initiate_data_ingestion()
        )

        print(dataingestionartifact)

    except Exception as e:

        raise NetworkSecurityException(e, sys)