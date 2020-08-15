import pathlib
import sys
import os

import split_folders

import utils.download_playlists

ROOT_DIR = os.path.dirname(os.path.abspath("../setup.py"))

#Download the dataset
def download():
    os.chdir(ROOT_DIR)
    
    genres = "house techno".split()
    
    for genre in genres:
        pathlib.Path(f"data/genres/{genre}").mkdir(parents=True, exist_ok=True)
    
    print("downloading house dataset")
    utils.download_playlists.download("https://www.youtube.com/playlist?list=PLS9qGVIfZRpzFAyUAz0oh0X7XsDO6i1C0", "data/genres/house")# House playlist              
    print("downloading techno dataset")
    utils.download_playlists.download("https://www.youtube.com/playlist?list=PLS9qGVIfZRpz5UMjAWwCdhHaJNT6V2Jna", "data/genres/techno")# Techno playlist
    
def split():
    split_folders.ratio(ROOT_DIR + "/data/genres/", output = ROOT_DIR + "/data_split/", seed = 1337, ratio = (.8, .2))
    
def data_augmentation():
    pass