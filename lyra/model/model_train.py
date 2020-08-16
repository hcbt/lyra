import pandas as pd
import numpy as np
from numpy import argmax
import matplotlib.pyplot as plt
import random
import warnings
import os
from PIL import Image
import pathlib
import csv

# sklearn Preprocessing
from sklearn.model_selection import train_test_split

#Keras
import keras
from keras import layers
from keras.layers import Activation, Dense, Dropout, Conv2D, Flatten, MaxPooling2D, GlobalMaxPooling2D, GlobalAveragePooling1D, AveragePooling2D, Input, Add
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.optimizers import SGD

train_datagen = ImageDataGenerator(
    rescale = 1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True
)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory(
    "data_split/train",
    target_size = (64, 64),
    batch_size = 1,
    class_mode = "categorical",
    shuffle = False
)

test_set = test_datagen.flow_from_directory(
    "data_split/val",
    target_size = (64, 64),
    batch_size = 1,
    class_mode = "categorical",
    shuffle = False
)

model = Sequential()
input_shape=(64, 64, 3)

#1st hidden layer
model.add(Conv2D(32, (3, 3), strides=(2, 2), input_shape=input_shape))
model.add(AveragePooling2D((2, 2), strides=(2,2)))
model.add(Activation('relu'))

#2nd hidden layer
model.add(Conv2D(64, (3, 3), padding="same"))
model.add(AveragePooling2D((2, 2), strides=(2,2)))
model.add(Activation('relu'))

#3rd hidden layer
model.add(Conv2D(64, (3, 3), padding="same"))
model.add(AveragePooling2D((2, 2), strides=(2,2)))
model.add(Activation('relu'))

#Flatten
model.add(Flatten())
model.add(Dropout(rate=0.5))

#Add fully connected layer.
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(rate=0.5))

#Output layer
model.add(Dense(2))
model.add(Activation('softmax'))
model.summary()

epochs = 200
batch_size = 8
learning_rate = 0.01
decay_rate = learning_rate / epochs
momentum = 0.9
sgd = SGD(lr=learning_rate, momentum=momentum, decay=decay_rate, nesterov=False)
model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=['accuracy'])

model.fit_generator(
        training_set,
        steps_per_epoch=100,
        epochs=50,
        validation_data=test_set,
        validation_steps=50)