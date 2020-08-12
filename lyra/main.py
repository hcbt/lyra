#!/usr/bin/env python3
import sys
import os

import utils.download_playlists

def main():
    # Read command line arguments
    playlist = sys.argv[1]
    destination = sys.argv[2]
    
    #download a given playlist
    utils.download_playlists(playlist, destination)

if __name__ == "__main__":
    main()