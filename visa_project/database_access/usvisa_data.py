from visa_project.configuration.mongo_db_connection import MongoDBClient
from visa_project.constants import DATABASE_NAME
from visa_project.exception import USvisaException

import pandas as pd
import numpy as np
import sys
from typing import Optional

class USvisaData:
    """
    This class helps to convert entire MongoDB records as Pandas DataFrame
    """
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise USvisaException(e, sys)
    
    def export_collection_as_dataframe(self, collection_name:str, database_name:Optional[str]=None) -> pd.DataFrame:
                                                                  # database_name can be either str OR None
        """_summary_

        exports:
            entire collectin as dataframe

        Returns:
            _type_: pd.DataFrame of collection
        """
        
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df =df.drop(columns = ['_id'], axis =1)
            df.replace({"na":np.nan}, inplace=True)
            return df
        except Exception as e:
            raise USvisaException(e, sys)



