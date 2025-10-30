import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
    SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
    
    CORS_ORIGINS = ["*"]
    
    MAX_RECOMMENDATIONS = 20
    MIN_RECOMMENDATIONS = 1
    
    SUPPORTED_EMOTIONS = [
        "sadness", "joy", "anger", "fear", "love", "surprise"
    ]

config = Config()