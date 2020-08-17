#!/usr/bin/env python3
import sys
import os

import utils.download_playlists
import model.compiled_model

ROOT_DIR = os.path.dirname(os.path.abspath("../setup.py"))

def main():
    #model = sys.argv[1]
    #playlist = sys.argv[2]
    #destination = sys.argv[3]
    
    model_file = "model/lyra.h5"
    playlist = "https://www.youtube.com/playlist?list=PLk9OF3AXEsI4Th-Xm-LPKP6HYbIxxpiQw"
    destination = ROOT_DIR + "/tmp"
    track_path = ROOT_DIR + "/test_data/V7kGgupwSaA.png"
    
    print("Downloading the playlist")
    utils.download_playlists.download(playlist, destination)
    
    #load_model(model_file)
    
    #genre = model.compiled_model.determine_genre(model_file, track_path)

    #print(genre)
    
if __name__ == "__main__":
    main()