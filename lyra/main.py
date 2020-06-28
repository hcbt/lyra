#!/usr/bin/env python3

import multiprocessing
import itertools
import time
import sys
import os

import youtube_resources
import youtube_download

import analysis.feature_extraction

youtube_url = "https://www.youtube.com"
youtube_video_url = youtube_url + "/watch?v="
youtube_playlist_url = youtube_url + "/playlist?list="

def main():
    # Read command line arguments
    playlist = sys.argv[1]
    destination = sys.argv[2]

    # Gets playlist id from the full link
    playlist_id = playlist.split("list=")[1]
    playlist_items = youtube_resources.playlistItems()
    video_ids = playlist_items.video_id(playlist_id)

    
    # Download all videos from playlist, build spectrograms, remove leftover files
    try:
        os.chdir(destination)
        
        #Set the multiprocessing pool        
        pool1 = multiprocessing.Pool(multiprocessing.cpu_count()//2)
        pool2 = multiprocessing.Pool(multiprocessing.cpu_count()//2)
        
        pool1.map_async(youtube_download.download, video_ids)
        pool1.close()
        time.sleep(20)
        pool2.map_async(analysis.feature_extraction.build_spectrogram, video_ids)
        pool1.join()
        pool2.close()
        pool2.join()
        
        for id in video_ids:
            os.remove(id + ".wav")
        
    except:
        print("Error")

if __name__ == "__main__":
    main()
