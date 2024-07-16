import sys
from pathlib import Path
from src.GemstonePricePrediction.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.GemstonePricePrediction.components.data_transformation import DataTransformation
from src.GemstonePricePrediction.components.model_trainer import ModelTrainer
from src.GemstonePricePrediction.exception import CustomException

def main():
    try:
        # Data Ingestion
        data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_path = Path(r'C:\Firstendtoendproject\notebooks\data\GemstonePricePrediction.csv')  # Update with your data path
        train_data, test_data = data_ingestion.initiate_data_ingestion(data_path)
        
        # Data Transformation
        data_transformation = DataTransformation()
        train_arr, test_arr = data_transformation.initialize_data_transformation(data_ingestion_config.train_data_path, data_ingestion_config.test_data_path)

        # Model Training
        model_trainer = ModelTrainer()
        model_trainer.initiate_model_training(train_arr, test_arr)

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    main()
