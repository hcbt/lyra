# lyra

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

* cd lyra/lyra
* uvicorn api:lyra --reload