from src.GemstonePricePrediction.components.data_ingestion import DataIngestion


import os
import sys
from src.GemstonePricePrediction.logger import logging
from src.GemstonePricePrediction.exception import customexception
import pandas as pd

obj=DataIngestion()

obj.initiate_data_ingestion()