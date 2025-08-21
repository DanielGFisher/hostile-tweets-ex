from pymongo import MongoClient
import pandas as pd
import os

class MongoFetcher:
    """
    Connect to MongoDB Atlas and fetch all documents
    Connection details are hardcoded (No time to implement flexibility)
    """
    def __init__(self):
        self.uri = os.getenv("MONGO_URI")
        self.db_name = "IranMalDB"
        self.col_name = "tweets"
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]
        self.col = self.db[self.col_name]

    def fetch_all(self) -> pd.DataFrame:
        """
        Fetch all tweets and return a Pandas dataframe
        """
        documents = list(self.col.find({}))
        rows = []
        for doc in documents:
            rows.append({
                "id": str(doc.get("_id")),
                "original_text":  str(doc.get("Text"))
            })
        return pd.DataFrame(rows)
