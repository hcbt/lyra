import tensorflow as tf
import numpy as np
import pathlib
import os

from tensorflow import keras
from tensorflow import function

def determine_genre(model, ROOT_DIR, working_directory, id):
    img = keras.preprocessing.image.load_img(id + ".png", target_size=(180, 180))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    os.chdir(ROOT_DIR)

    return np.argmax(score)