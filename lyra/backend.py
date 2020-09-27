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
        playlist[video_id] = genres[find_genre_youtube(video_id, working_directory)]

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
    #model_file = os.path.abspath(os.path.join(ROOT_DIR, "model/lyra.h5"))
    #print("current dir model: " + os.getcwd())
    
    print(pathlib.Path(__file__).parent.absolute())
    #print("current dir pre download: " + os.getcwd())
    
    yt.download.download(video_id, working_directory)
    print("current dir pre analysis: " + os.getcwd())
    analysis.feature_extraction.build_spectrogram(video_id, working_directory)
    print("current dir pre model: " + os.getcwd())
    id_genre = model.compiled_model.determine_genre(ROOT_DIR, working_directory, video_id)

    return id_genre