'''import os
path ="notebook/research.ipynb"

dir,file=os.path.split(path)
os.makedirs(dir,exist_ok=True)

with open(path,"w")as f:
    pass'''

# test.py

from src.GemstonePricePrediction.pipelines.prediction_pipeline import CustomData

custdataobj = CustomData(0.33, "Premium", "G", "IF", 60.8, 58, 4.42, 4.46, 2.7)
data = custdataobj.get_data_as_dataframe()

print(data)
