import tempfile
import sys
import os
import numpy as np

import yt.download
import yt.resources
import analysis.feature_extraction
import model.compiled_model

ytp = yt.resources.playlistItems()

#Gets genres for a list of ids
def find_genre_youtube(video_id, working_directory):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    model_file = os.path.join(ROOT_DIR, "model/lyra.h5")

    yt.download.download(video_id, working_directory)
    analysis.feature_extraction.build_spectrogram(video_id, working_directory)
    id_genre = model.compiled_model.determine_genre(model_file, working_directory, video_id)

    return id_genre

def main():
    genres = ["house", "techno"]#To-do: get genres from model classes
    working_directory = tempfile.mkdtemp()
    print("Current working dir: " + working_directory)

    video_id = "b94FUZf9CPM"

    #print(find_genre_youtube(video_id, working_directory))
    print(genres[find_genre_youtube(video_id, working_directory)])

if __name__ == "__main__":
    main()