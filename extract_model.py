import os
import pickle
import numpy as np

import tensorflow as tf
from tensorflow import keras

from PIL import Image
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.models import Model

class extracting_model:
    def __init__(self):
        vgg16_model = VGG16(weights="imagenet")
        self.model = Model(inputs=vgg16_model.inputs, outputs=vgg16_model.get_layer("fc1").output)

    def image_preprocess(self,img):
        img = img.resize((224, 224))
        img = img.convert("RGB")
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        return x

    def extract_vector(self,image_path):
        print("Extracting : ", image_path)
        img = Image.open(image_path)
        img_tensor = self.image_preprocess(img)

        # Trich dac trung
        vector = self.model.predict(img_tensor)[0]
        # Chuan hoa vector = chia chia L2 norm (tu google search)
        vector = vector / np.linalg.norm(vector)
        return vector

    def extracting_dataset(self, dataset):
        data_folder = dataset

        # Khoi tao model

        vectors = []
        paths = []

        for image_path in os.listdir(data_folder):
            # Noi full path
            image_path_full = os.path.join(data_folder, image_path)
            # Trich dac trung
            image_vector = self.extract_vector(image_path_full)
            # Add dac trung va full path vao list
            vectors.append(image_vector)
            paths.append(image_path_full)

        # save vao file
        vector_file = "vectors.pkl"
        path_file = "paths.pkl"

        pickle.dump(vectors, open(vector_file, "wb"))
        pickle.dump(paths, open(path_file, "wb"))

if __name__ == "__main__":
    model = extracting_model()
    model.extracting_dataset("cat")
    print("Done")