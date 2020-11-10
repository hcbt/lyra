import tensorflow as tf
import numpy as np
import pathlib
import os

from tensorflow import keras
from tensorflow import function

def load_model(ROOT_DIR):
    model_file = os.path.abspath(os.path.join(ROOT_DIR, "model/lyra.h5"))

    model = tf.keras.models.load_model(model_file)

    return model