import pandas as pd

class DataExt:

    def __init__(self,file_path:str):
        self.file_path = file_path

    def fetch_text(self,separator:str):
        # Write your custom logic
        df = pd.read_csv(self.file_path, sep=separator)
        print(df.head())

    def fetch_json(self):
        # Write your custom logic
        df = pd.read_json(self.file_path)
        print(df.head())

    def fetch_parquet(self):
        # Write your custom logic
        df = pd.read_parquet(self.file_path)   
        print(df.head()) 

obj_text = DataExt("Ch-1_OOP/Files/orders.tsv")
obj_text.fetch_text(separator="\t")

obj_json = DataExt("Ch-1_OOP/Files/orders.json")
obj_json.fetch_json()

obj_parquet = DataExt("Ch-1_OOP/Files/orders.parquet")
obj_parquet.fetch_parquet()

