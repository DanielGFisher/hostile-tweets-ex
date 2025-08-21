from fastapi import FastAPI
from app.manager import DataManager

app = FastAPI()
dm = DataManager()

@app.get("/tweets")
def get_tweets():
    """
    Get all tweets with processed data -
    rarest_word, sentiment, weapons_detected
    """
    df = dm.load_and_process()
    return df.to_dict(orient='records')
