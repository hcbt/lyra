# lyra

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github//hcbt/lyra/blob/master/lyra.ipynb)

## Problem

If you're electronic music fan like me at some point you probably struggled with managing your playlists, especially if you're into many styles of electronic music. 

## Solution

Create a machine learning model to figure out to what style a track belongs and use a simple youtube client to add those tracks to genre playlists.

## Requirements

* Python 3.8 or later
* Tensorflow 2.3.0 or later
* A compatible gpu if you want to build a model yourself
* Youtube account with api access and some unused api calls

## Setup

* pip3 install -r requirements.txt

## Usage

python main.py "youtube-playlist-that-you-want-to-sort-into-genres" "destination-you-want-to-download-your-playlist-to"

To build a model yourself you can use the given google colab link.

## To-do

- [ ] Add expanded dataset with more samples and broader spectrum of genres
- [ ] Optimize code
- [ ] Add more sources than youtube - spotify and other streaming services (would need to change the model since current model uses CNN and hence needs to download actual audio file to convert it to image(spectrogram))
- [ ] A basic user interface
- [ ] Selectable output playlists
- [ ] Better error handling (currently there's basically none)