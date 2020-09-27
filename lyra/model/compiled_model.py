import tensorflow as tf
import numpy as np
import pathlib
import os

from tensorflow import keras
from tensorflow import function

def determine_genre(ROOT_DIR, working_directory, id):
    model_file = os.path.abspath(os.path.join(ROOT_DIR, "model/lyra.h5"))
    
    model = tf.keras.models.load_model(model_file)

    img_height = 180
    img_width = 180

    img = keras.preprocessing.image.load_img(id + ".png", target_size=(img_height, img_width))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    return np.argmax(score)