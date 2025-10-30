from pydantic import BaseModel, validator
from typing import List, Optional
import re

class EmotionRequest(BaseModel):
    text: str

    @validator("text")
    def must_be_descriptive(cls, v):
        cleaned = v.strip()
        error_msg = "Hmm... that looks like a random string. Try writing a short sentence about how you feel."

        # Hanya angka
        if not cleaned or cleaned.isnumeric():
            raise ValueError(error_msg)

        # Huruf kapital dan angka tanpa huruf kecil
        if (
            re.fullmatch(r"[A-Z0-9]+", cleaned) and
            not re.search(r"[AIUEO]", cleaned) 
        ):
            raise ValueError(error_msg)

        # Input huruf kecil tapi tidak mengandung vokal 
        if (
            re.fullmatch(r"[a-z0-9]+", cleaned) and  
            not re.search(r"[aeiou]", cleaned) 
        ):
            raise ValueError(error_msg)

        return cleaned
    
class EmotionScore(BaseModel):
    label: str
    score: float

class EmotionResponse(BaseModel):
    emotion: str
    predictions: List[EmotionScore]  

class Track(BaseModel):
    title: str
    artist: str
    url: str
    album_art: Optional[str] = None

class RecommendationResponse(BaseModel):
    tracks: List[Track]
    message: Optional[str] = None

class AnalyzeAndRecommendResponse(BaseModel):
    emotion: str
    tracks: List[Track]
    message: Optional[str] = None
