import os

import youtube_dl

youtube_url = "https://www.youtube.com"
youtube_video_url = youtube_url + "/watch?v="
youtube_playlist_url = youtube_url + "/playlist?list="

class Logger(object):
    def debug(self, message):
        #print(message)
        pass

    def warning(self, message):
        print(message)

    def error(self, message):
        print(message)

def download_progress_hook(client):
    #if client["status"] == "finished":
    #    print("Done downloading")
    pass

def download(id, working_directory):
    os.chdir(working_directory)

    # audio only, we dont need video obviously
    ytdl_options = {
        "ignoreerrors": True,
        "format": "bestaudio",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
        }],
        "logger": Logger(), 
        "progress_hooks": [download_progress_hook], 
        "outtmpl": "%(id)s.%(ext)s",
    }

    with youtube_dl.YoutubeDL(ytdl_options) as ytdl:
        video = ytdl.extract_info(id, download=False)
        #title = video["title"]
        #artist = video["artist"]
        #track = video["track"]
        
        #print("Title: " + str(title) + " Artist: " + str(artist) + " Track: " + str(track))
        
        ytdl.download([id])
        
def get_metadata(id):
    ytdl_options = {
        "logger": Logger()
    }

    with youtube_dl.YoutubeDL(ytdl_options) as ytdl:
        video = ytdl.extract_info(id, download=False)
        
        artist = video["artist"]
        track = video["track"]
        
        return artist, track