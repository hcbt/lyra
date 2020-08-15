#!/usr/bin/env python3
import sys
import os

import split_folders

import utils.download_playlists

ROOT_DIR = os.path.dirname(os.path.abspath("../setup.py"))

def download():
    #Initialize dataset
    print("Downloading dataset")
    
    os.mkdir(ROOT_DIR + "/data/genres/house")
    os.mkdir(ROOT_DIR + "/data/genres/techno")
    
    utils.download_playlists.download("https://www.youtube.com/playlist?list=PLS9qGVIfZRpzFAyUAz0oh0X7XsDO6i1C0", ROOT_DIR + "/data/genres/house")# House playlist              
    utils.download_playlists.download("https://www.youtube.com/playlist?list=PLS9qGVIfZRpz5UMjAWwCdhHaJNT6V2Jna", ROOT_DIR + "/data/genres/techno")# Techno playlist
    
def split():
    split_folders.ratio(ROOT_DIR + "/data/", output = ROOT_DIR + "/data_split", seed = 1337, ratio = (.8, .2))