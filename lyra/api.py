import backend

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

lyra = FastAPI()

@lyra.get("/")
async def root():
    return {"message": "Hello world"}

@lyra.get("/youtube/auth")
async def google_auth():
    pass

@lyra.get("/spotify/auth")
async def spotify_auth():
    pass

@lyra.get("/youtube/playlist/{playlist_id}")
async def youtube_playlist(playlist_id):
    return {"items": backend.process_playlist_youtube(playlist_id)}

@lyra.get("/youtube/video/{video_id}")
async def youtube_video(video_id):
    return {"items": [{video_id: {"genre": backend.process_track_youtube(video_id) }}]}