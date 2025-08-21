from fetcher import MongoFetcher
from manager import DataManager
from processor import TextProcessor

## Test MongoFetcher & TextProcessor
# mf = MongoFetcher()
# df = mf.fetch_all()
# processor = TextProcessor(df)
# processed_df = processor.process()
# print(processed_df)

## Test DataManager
dm = DataManager()
dm.load_and_process()

print(dm.df.to_json())