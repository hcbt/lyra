#Main program file that does all the magic.
import numpy as np
import sys
import os

import yt.download
import yt.manage_playlists
import model.compiled_model

ROOT_DIR = os.path.dirname(os.path.abspath("../setup.py"))

def create_new_playlists():
    pass
    #Create output playlists for given genres
    #for genre in genres:
    #    playlists.append(yt.manage_playlists.create_playlist(genre))
    #    print(genre, playlists[len(playlists)-1])#Prints playlist id for every genre

def select_playlists():
    pass

def main():
    #Main parameters
    model_file = "model/lyra.h5"
    playlist = "https://www.youtube.com/playlist?list=PLk9OF3AXEsI4Th-Xm-LPKP6HYbIxxpiQw"
    destination = ROOT_DIR + "/tmp"
    genres = ["house", "techno"]#To-do: get genres from model classes
    playlists = []
    
    #Download input playlist
    #print("Downloading the playlist")
    #utils.download_playlists.download(playlist, destination)
    #spectrograms = os.listdir(destination)
    
    #for spectrogram in spectrograms:
    #    spectrogram_path = destination + "/" + spectrogram
    #    score = model.compiled_model.determine_genre(model_file, spectrogram_path)
    #    print(score)
     
    #model.compiled_model.determine_genre(model_file, destination, spectrograms)
    
    playlist_id = "PLS9qGVIfZRpzbz76tJhZai1gTrm_WSo9t"
    video_id = "ML8JomV445E"
    
    print(yt.resources.playlistItems.add_to_playlist(playlist_id, video_id))
    
if __name__ == "__main__":
    main()