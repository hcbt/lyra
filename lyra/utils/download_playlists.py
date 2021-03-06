#Downloads all tracks from specified playlist and generates spectrograms for those tracks
import multiprocessing
import itertools
import time
import sys
import os

import youtube.youtube_resources
import youtube.youtube_download
import analysis.feature_extraction

youtube_url = "https://www.youtube.com"
youtube_video_url = youtube_url + "/watch?v="
youtube_playlist_url = youtube_url + "/playlist?list="

ROOT_DIR = os.path.dirname(os.path.abspath("../setup.py"))

def download(playlist, destination):
    # Gets playlist id from the full link
    playlist_id = playlist.split("list=")[1]
    playlist_items = utils.youtube_resources.playlistItems()
    video_ids = playlist_items.video_id(playlist_id)
    video_titles = playlist_items.video_title(playlist_id)

    # Download all videos from playlist, build spectrograms, remove leftover files
    try:
        os.chdir(destination)
        
        #Set the multiprocessing pool        
        pool1 = multiprocessing.Pool(multiprocessing.cpu_count()//2)
        pool2 = multiprocessing.Pool(multiprocessing.cpu_count()//2)
        
        pool1.map_async(utils.youtube_download.download, video_ids)
        pool1.close()
        time.sleep(30)
        pool2.map_async(analysis.feature_extraction.build_spectrogram, video_ids)
        pool1.join()
        pool2.close()
        pool2.join()
        
        for id in video_ids:
            os.remove(id + ".wav")
        
    except:
        print(os.getcwd())#To show current path in case of path error
        print("Error")