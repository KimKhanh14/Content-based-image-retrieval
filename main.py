import os
import math
import pickle
import numpy as np

import tensorflow as tf
from tensorflow import keras

from PIL import Image
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.models import Model

from extract_model import extracting_model

# Dinh nghia anh can tim kiem
search_image = "cat.jpg"
# Khoi tao model
model = extracting_model()

# Trich dac trung anh search
search_vector = model.extract_vector(search_image)
# Load 4700 vector tu vectors.pkl ra bien
vectors = pickle.load(open("vectors.pkl","rb"))
paths = pickle.load(open("paths.pkl","rb"))

# Tinh khoang cach tu search_vector den tat ca cac vector
distance = np.linalg.norm(vectors - search_vector, axis=1)

# Sap xep va lay ra K vector co khoang cach ngan nhat
K = 16
ids = np.argsort(distance)[:K]

# Tao oputput
nearest_image = [(paths[id], distance[id]) for id in ids]

# Ve len man hinh cac anh gan nhat do
import matplotlib.pyplot as plt

axes = []
grid_size = int(math.sqrt(K))
fig = plt.figure(figsize=(10,5))


for id in range(K):
    draw_image = nearest_image[id]
    axes.append(fig.add_subplot(grid_size, grid_size, id+1))

    axes[-1].set_title(draw_image[1])
    plt.imshow(Image.open(draw_image[0]))

fig.tight_layout()
plt.show()