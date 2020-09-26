import numpy as np
import os
import tensorflow as tf

from tensorflow import keras
from tensorflow import function

@tf.function
def serve(model_file):
    model = tf.keras.models.load_model(model_file)
    return model

def determine_genre(model_file, working_directory, id):
    img_height = 180
    img_width = 180
    
    #model = tf.keras.models.load_model(model_file)
    model = serve(model_file)

    img = keras.preprocessing.image.load_img(id + ".png", target_size=(img_height, img_width))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    return np.argmax(score)