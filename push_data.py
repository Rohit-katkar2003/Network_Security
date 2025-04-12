import os 
import sys 
import json 
from dotenv import load_dotenv 

load_dotenv() 

MANGO_DB_URL = os.getenv('MANGO_DB_URL')


import certifi # help to make valid request to mangodb_url 
ca = certifi.where()  # ca = trusted certificate 

import pandas as pd 
import pymongo 
import numpy as np 
from networksecurity.exception.exception import NetworkSecurityException 
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try: 
            pass 
        except Exception as e: 
            raise NetworkSecurityException(e ,sys) 
    
    def csv_to_json_convertor(self , file_path): 
        try: 
            df = pd.read_csv(file_path)
            df.reset_index(drop=True , inplace=True)  
            records = list(json.loads(df.T.to_json()).values()) 

            return records
        except Exception as e: 
            raise NetworkSecurityException(e , sys) 
        
    def insert_data_mangodb(self ,records , database , collection): 
        try: 
            self.database = database 
            self.records = records 
            self.collection = collection 

            self.mango_client = pymongo.MongoClient(MANGO_DB_URL) 
            self.database = self.mango_client[self.database] 
            self.collection = self.database[self.collection] 
            self.collection.insert_many(self.records) 
            return (len(self.records)) 
        
        except Exception as e: 
            raise NetworkSecurityException(e , sys) 
        

if __name__ == '__main__': 
    FILE_PATH = 'network_data\phisingData.csv'
    DATABASE = 'ROHITAI' 
    Collection = 'NetworkData' 
    networkobj = NetworkDataExtract() 
    records = networkobj.csv_to_json_convertor(FILE_PATH) 
    n_of_records = networkobj.insert_data_mangodb(records=records , database=DATABASE , collection=Collection)  
    print('Total records : ',n_of_records)