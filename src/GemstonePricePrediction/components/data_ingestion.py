
import pandas as pd
import os
import sys
from pathlib import Path
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class DataIngestionConfig:
    raw_data_path: Path = Path("artifacts", "raw.csv")
    train_data_path: Path = Path("artifacts", "train.csv")
    test_data_path: Path = Path("artifacts", "test.csv")

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self):
        logger.info("Data ingestion started")
        try:
            data = pd.read_csv(Path(r'C:\Firstendtoendproject\notebooks\data\GemstonePricePrediction.csv'))
            logger.info("Reading a dataframe")

            self.config.raw_data_path.parent.mkdir(parents=True, exist_ok=True)
            data.to_csv(self.config.raw_data_path, index=False)
            logger.info("Saved the raw dataset in artifact folder")

            logger.info("Performing train test split")
            train_data, test_data = train_test_split(data, test_size=0.25, random_state=42)
            logger.info("Train test split completed")

            train_data.to_csv(self.config.train_data_path, index=False)
            test_data.to_csv(self.config.test_data_path, index=False)

            logger.info("Data ingestion part completed")
            return train_data, test_data

        except Exception as e:
            logger.error(f"Error during data ingestion: {str(e)}")
            raise

if __name__ == "__main__":
    config = DataIngestionConfig()
    obj = DataIngestion(config)
    obj.initiate_data_ingestion()
