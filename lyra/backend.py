import tempfile
import sys
import os

import yt.download
import yt.resources
#import model.compiled_model

ytp = yt.resources.playlistItems()

def playlist_items(playlist_id):
    items = ytp.video_id(playlist_id)
    return items

def find_genre(video_id):
    ROOT_DIR = os.path.dirname(os.path.abspath("../setup.py"))
    model_file = "model/lyra.h5"
    destination = ROOT_DIR + "/tmp"
    genres = ["house", "techno"]#To-do: get genres from model classes

    pass