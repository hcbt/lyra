import numpy as np
import tempfile
import logging
import pathlib
import sys
import os

import db.db
import yt.download
import yt.resources
import analysis.feature_extraction
import model.process
import model.load

def process_playlist_youtube(playlist_id):
    ROOT_DIR = pathlib.Path(__file__).parent.absolute()
    model_file = model.load.load_model(ROOT_DIR)

    playlist = {}

    video_ids = playlist_items_youtube(playlist_id)

    working_directory = tempfile.mkdtemp()

    #Find genre for every track in the playlist
    for video_id in video_ids:
        try:
            playlist[video_id] = find_genre_youtube(model_file, video_id, working_directory)
        except:
            pass

    return playlist

def process_track_youtube(model_file, video_id):
    working_directory = tempfile.mkdtemp()

    try:
        return find_genre_youtube(model_file, video_id, working_directory)
    except:
        pass

#Returns ids of items in a playlist
def playlist_items_youtube(playlist_id):
    ytp = yt.resources.playlistItems()

    items = ytp.video_id(playlist_id)
    return items

#Gets genres for a list of ids
def find_genre_youtube(model_file, video_id, working_directory):
    ROOT_DIR = pathlib.Path(__file__).parent.absolute()
    genres = ["house", "techno"]

    #Check by id if track already exists in db, if not - do analysis
    if db.db.find_entry(video_id) is None:
        yt.download.download(video_id, working_directory)
        analysis.feature_extraction.build_spectrogram(video_id, working_directory)
        genre = model.process.determine_genre(model_file, ROOT_DIR, working_directory, video_id)
        db.db.add_entry(video_id, genres[genre])#Adds entry to db for new track
        id_genre = genres[genre]
    else:
        id_genre = db.db.find_entry(video_id)["genre"]

    return id_genre