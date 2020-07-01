import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
import numpy as np
import matplotlib.pyplot as plt

train_dir = "../data_split/train"
validation_dir = "../data_split/val"

train_house_dir = os.path.join(train_dir, "house")
train_techno_dir = os.path.join(train_dir, "techno")

validation_house_dir = os.path.join(validation_dir, "house")
validation_techno_dir = os.path.join(validation_dir, "techno")

num_house_tr = len(os.listdir(train_house_dir))
num_techno_tr = len(os.listdir(train_techno_dir))

num_house_val = len(os.listdir(validation_house_dir))
num_techno_val = len(os.listdir(validation_techno_dir))

total_train = num_house_tr + num_techno_tr
total_val = num_house_val + num_techno_val

print('total training house images:', num_house_tr)
print('total training techno images:', num_techno_tr)

print('total validation house images:', num_house_val)
print('total validation techno images:', num_techno_val)
print("--")
print("Total training images:", total_train)
print("Total validation images:", total_val)

batch_size = 32
epochs = 15
IMG_HEIGHT = 775
IMG_WIDTH = 770

train_image_generator = ImageDataGenerator(rescale = 1./255,
                                           rotation_range = 45,
                                           width_shift_range = .15,
                                           height_shift_range= .15,
                                           horizontal_flip = True,
                                           zoom_range = 0.5) # Generator for our training data

validation_image_generator = ImageDataGenerator(rescale = 1./255) # Generator for our validation data

train_data_gen = train_image_generator.flow_from_directory(batch_size = batch_size,
                                                           directory = train_dir,
                                                           shuffle = False,
                                                           target_size = (IMG_HEIGHT, IMG_WIDTH),
                                                           class_mode = "binary")

val_data_gen = validation_image_generator.flow_from_directory(batch_size = batch_size,
                                                              directory = validation_dir,
                                                              target_size = (IMG_HEIGHT, IMG_WIDTH),
                                                              class_mode = "binary")

model = Sequential([
    Conv2D(16, 3, padding='same', activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH ,3)),
    MaxPooling2D(),
    #Dropout(0.2),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    #Dropout(0.2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(1)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.summary()

model.fit(train_data_gen,
          steps_per_epoch=total_train // batch_size,
          epochs=epochs,
          validation_data=val_data_gen,
          validation_steps=total_val // batch_size
)

model.evaluate(train_data_gen)