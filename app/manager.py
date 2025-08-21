from app.fetcher import MongoFetcher
from app.processor import TextProcessor

class DataManager:
    def __init__(self):
        self.fetcher = MongoFetcher()
        self.df = None

    def load_and_process(self):
        """
        Manage load and process (clean) of data
        """
        raw_df = self.fetcher.fetch_all()
        processor = TextProcessor(raw_df)
        self.df = processor.process()
        return self.df