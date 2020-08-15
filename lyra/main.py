#!/usr/bin/env python3
import sys
import os

import utils.download_playlists
import utils.prepare_dataset
import utils.manage_playlists

ROOT_DIR = os.path.dirname(os.path.abspath("../setup.py"))

def main():
    print("Downloading dataset")
    
    #utils.prepare_dataset.download()
    utils.prepare_dataset.split()
    
if __name__ == "__main__":
    main()