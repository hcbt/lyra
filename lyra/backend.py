import numpy as np
import tempfile
import logging
import pathlib
import sys
import os

import yt.download
import yt.resources
import analysis.feature_extraction
import model.compiled_model

ytp = yt.resources.playlistItems()

def process_playlist_youtube(playlist_id):
    playlist = {}

    genres = ["house", "techno"]

    video_ids = playlist_items_youtube(playlist_id)

    working_directory = tempfile.mkdtemp()

    for video_id in video_ids:
        try: 
            playlist[video_id] = genres[find_genre_youtube(video_id, working_directory)]
        except:
            pass

    return playlist

def process_track_youtube(video_id):
    genres = ["house", "techno"]

    working_directory = tempfile.mkdtemp()

    return str(genres[find_genre_youtube(video_id, working_directory)])

#Returns ids of items in a playlist
def playlist_items_youtube(playlist_id):
    items = ytp.video_id(playlist_id)
    return items

#Gets genres for a list of ids
def find_genre_youtube(video_id, working_directory):
    ROOT_DIR = pathlib.Path(__file__).parent.absolute()
    
    #print(pathlib.Path(__file__).parent.absolute())
    
    yt.download.download(video_id, working_directory)
    analysis.feature_extraction.build_spectrogram(video_id, working_directory)
    id_genre = model.compiled_model.determine_genre(ROOT_DIR, working_directory, video_id)

    return id_genre