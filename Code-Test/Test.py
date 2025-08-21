from app.fetcher import MongoFetcher
from app.manager import DataManager
from app.processor import TextProcessor
from app.main import get_tweets

# # Test MongoFetcher & TextProcessor
# mf = MongoFetcher()
# df = mf.fetch_all()
# processor = TextProcessor(df)
# processed_df = processor.process()
# print(processed_df)
#
# # Test DataManager
# dm = DataManager()
# dm.load_and_process()
# #
# print(dm.df.to_dict(orient='records')[1])
#
tweets = get_tweets()

print(tweets)