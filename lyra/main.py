#!/usr/bin/env python3
import numpy as np
import sys
import os

import yt.download
import yt.manage_playlists
import model.compiled_model

ROOT_DIR = os.path.dirname(os.path.abspath("../setup.py"))

def main():
    #Main parameters
    model_file = "model/lyra.h5"
    playlist = "https://www.youtube.com/playlist?list=PLk9OF3AXEsI4Th-Xm-LPKP6HYbIxxpiQw"
    destination = ROOT_DIR + "/tmp"
    genres = ["house", "techno"]
    playlists = []
    
    #Download input playlist
    #print("Downloading the playlist")
    #utils.download_playlists.download(playlist, destination)
    spectrograms = os.listdir(destination)
    
    #Create output playlists for given genres
    #for genre in genres:
    #    print(genre, yt.manage_playlists.create_playlist(genre))
    #    playlists.append(yt.manage_playlists.create_playlist(genre))
    
    #for spectrogram in spectrograms:
    #    spectrogram_path = destination + "/" + spectrogram
    #    score = model.compiled_model.determine_genre(model_file, spectrogram_path)
    #    print(score)
     
    model.compiled_model.determine_genre(model_file, destination, spectrograms)
        
    #for track in destination:
    #    print(track, model.compiled_model.determine_genre(model_file, track))
    
    #playlist_name = "haus"
    
    #playlist_id = yt.manage_playlists.create_playlist(playlist_name)
    #print(playlist_id)
    
    #print("Sorting tracks in the playlist")
    #for files in destination:
    
    #load_model(model_file)
    
    #genre = model.compiled_model.determine_genre(model_file, track_path)

    #print(genre)
    
if __name__ == "__main__":
    main()