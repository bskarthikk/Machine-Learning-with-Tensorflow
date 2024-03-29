# -*- coding: utf-8 -*-
"""image_classifier

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/138xpkffPPDgVYp9MpaJfO54gvDI7mEuz
"""

!pip3 install tensorflow==2.0.0-beta1

"""Working on the fashion mnist dataset"""

from __future__ import absolute_import, unicode_literals, division, print_function
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']

"""Check out the training data


1. The dimensions of training images
2. Sanity of training set is verified with the length of training labels
3. Variations in the labels are between 0 and 9
"""

train_images.shape

len(train_labels)

train_labels

"""Check out the testing data
1. The dimensions of testing images
2. Sanity of test set is verified with the length of testing labels
3. Variations in the labels are between 0 and 9
"""

test_images.shape

len(test_images)

test_labels

"""Checking out images"""

plt.figure()
plt.imshow(train_images[1])
plt.colorbar()
plt.grid(False)
plt.show()

"""Normalize the images corresponding to the range of pixels"""

train_images = train_images / 255.0
test_images = test_images / 255.0

"""Build the model"""

model = keras.Sequential([
                          keras.layers.Flatten(input_shape=(28, 28)),
                          keras.layers.Dense(128, activation = 'relu'),
                          keras.layers.Dense(10, activation = 'softmax')       
])

"""Compile the model using:
1. Loss Function
2. Optimizer
3. Metrics
"""

model.compile(optimizer='adam',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])

"""Train the model"""

model.fit(train_images, train_labels, epochs=11)

"""Test the model"""

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('\n Test accuracy:', test_acc)

"""Let's predict"""

predictions = model.predict(test_images)

np.argmax(predictions[7])

test_labels[7]