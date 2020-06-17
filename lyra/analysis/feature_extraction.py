#!/usr/bin/env python3
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import scipy.io.wavfile

#load audio as waveform y, set sampling rate to sr
def load_file(id):
    sr, y = scipy.io.wavfile.read(id + ".wav")
    return y, sr

#audio to spectrogram
def build_spectrogram(id):
    #os.chdir(destination)
    y, sr = load_file(id)

    plt.figure(figsize=(10, 10))
    ax = plt.axes()
    ax.set_axis_off()
    plt.specgram(y[:, 0], NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap=plt.get_cmap("inferno"), sides="default", mode="default", scale="dB")
    plt.savefig(id + ".png", bbox_inches='tight', transparent=True, pad_inches=0.0)