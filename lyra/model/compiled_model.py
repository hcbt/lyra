import numpy as np
import os
import tensorflow as tf
tf.get_logger().setLevel('INFO')

from tensorflow import keras

ROOT_DIR = os.path.dirname(os.path.abspath("../setup.py"))

def load_model(model_file):
    model = tf.keras.models.load_model(model_file)
    return model

def determine_genre(model_file, spectrogram):    
    class_names = ["house", "techno"]
    
    batch_size = 32
    img_height = 180
    img_width = 180
    
    model = load_model(model_file)

    img = keras.preprocessing.image.load_img(spectrogram, target_size=(img_height, img_width))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    
    genre = "This track most likely belongs to {} with a {:.2f} percent confidence.".format (class_names [np.argmax (score) ], 100 * np.max (score) ) 
    
    #print("This image most likely belongs to {} with a {:.2f} percent confidence.".format (class_names [np.argmax (score) ], 100 * np.max (score) ) )
    #print(class_names[np.argmax(score)])
    #return class_names[np.argmax(score)]
    
    return genre