import backend

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

lyra = FastAPI()

@lyra.get("/")
async def root():
    return {"message": "Hello world"}

@lyra.get("/playlist/{playlist_id}")
async def playlist(playlist_id):
    return {"items": backend.playlist_items(playlist_id)}

@lyra.get("/video/{video_id}")
async def video(video_id):
    return {"genre": backend.find_genre(video_id)}