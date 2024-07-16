import os
import sys
import numpy as np
from src.GemstonePricePrediction.logger import logging
from src.GemstonePricePrediction.exception import CustomException
from src.GemstonePricePrediction.utils import save_object, evaluate_model
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from dataclasses import dataclass  # Import dataclass from dataclasses module

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet()
            }
            
            model_report = evaluate_model(X_train, y_train, X_test, y_test, models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')

            save_object(file_path=self.model_trainer_config.trained_model_file_path, obj=best_model)
        
        except Exception as e:
            logging.info('Exception occurred at Model Training')
            raise CustomException(e, sys)

if __name__ == "__main__":
    # Example usage:
    # Replace with actual train_array and test_array
    train_array = np.random.rand(100, 5)  # Example data
    test_array = np.random.rand(50, 5)    # Example data
    
    trainer = ModelTrainer()
    trainer.initiate_model_training(train_array, test_array)
