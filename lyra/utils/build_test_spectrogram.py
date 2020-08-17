#!/usr/bin/env python3
import sys
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.io.wavfile

ROOT_DIR = os.path.dirname(os.path.abspath("../setup.py"))

# Load audio into numpy array, 
# waveform y, sampling rate sr
def load_file(id):
    sr, y = scipy.io.wavfile.read(id)
    return y, sr

# Audio to spectrogram
def build_spectrogram(id):
    y, sr = load_file(id)

    plt.figure(figsize=(10, 10))
    ax = plt.axes()
    ax.set_axis_off()
    plt.specgram(y[:, 0], NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap=plt.get_cmap("inferno"), sides="default", mode="default", scale="dB")
    plt.savefig(id + ".png", bbox_inches='tight', transparent=True, pad_inches=0.0)

def main(): 
    track = sys.argv[1]
    
    build_spectrogram(track)
    
if __name__ == "__main__":
    main()