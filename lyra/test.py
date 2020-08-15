#!/usr/bin/env python3
import sys
import os

import utils.download_playlists
import utils.prepare_dataset
import utils.manage_playlists

ROOT_DIR = os.path.dirname(os.path.abspath("../setup.py"))

def main(): 
    utils.prepare_dataset.download()    
    
    #print("Testing playlists")
    #print(utils.manage_playlists.list_playlists())
    
    #playlist_name = "topkeks"
    #print(utils.manage_playlists.create_playlist(playlist_name))
    
if __name__ == "__main__":
    main()