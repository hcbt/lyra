#Main program file that does all the magic.
import sys
import os

import yt.download
import yt.resources
import model.compiled_model

youtube_url = "https://www.youtube.com"
youtube_video_url = youtube_url + "/watch?v="
youtube_playlist_url = youtube_url + "/playlist?list="

ROOT_DIR = os.path.dirname(os.path.abspath("../setup.py"))

def create_new_playlists(genres):
    pl = yt.resources.playlists()#Initiates class for ids and titles
    playlist_ids = pl.playlist_id()#List of playlist ids
    playlist_titles = pl.playlist_title()#List of playlist titles
    playlist_map = {} #Dictionary for appending genres to playlists
        
    print("List of playlists in your channel: ")
    for count, item in enumerate(playlist_titles):
        print(count, item)
    
    for genre in genres:
        playlist_map[genre] = pl.create_playlist(input("Please input playlist name for " + genre + ": "))
    
    return playlist_map

def select_playlists(genres):
    pl = yt.resources.playlists()#Initiates class for ids and titles
    playlist_ids = pl.playlist_id()#List of playlist ids
    playlist_titles = pl.playlist_title()#List of playlist titles
    playlist_map = {} #Dictionary for appending genres to playlists
    
    #Print a list of playlists and append selected playlists to genres
    print("List of playlists in your channel: ")
    for count, item in enumerate(playlist_titles):
        print(count, item)
        
    for genre in genres:
        playlist_map[genre] = playlist_ids[int(input("Please select playlist for " + genre + ": "))]
    
    return playlist_map

def move_to_playlist(genres, playlist_map, scores_map):
    ytp = yt.resources.playlistItems()

    for score in scores_map:
        ytp.add_to_playlist(playlist_map[genres[scores_map[score]]], score[:-4])
        print(score[:-4], playlist_map[genres[scores_map[score]]])

def main():
    #Main parameters
    model_file = "model/lyra.h5"
    playlist = "https://www.youtube.com/playlist?list=PLk9OF3AXEsI4Th-Xm-LPKP6HYbIxxpiQw"
    destination = ROOT_DIR + "/tmp"
    genres = ["house", "techno"]#To-do: get genres from model classes
    spectrograms = os.listdir(destination)

    #Needs a switch
    playlist_map = select_playlists(genres)
    #playlist_map = create_new_playlists(genres)

    scores_map = model.compiled_model.determine_genre(model_file, destination, spectrograms)#Maps tracks to genres

    move_to_playlist(genres, playlist_map, scores_map)#Adds tracks to genre playlists 

if __name__ == "__main__":
    main()