from cnnClassifer import logger
from cnnClassifer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

#logger.info("Welcome to my custome log")

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e