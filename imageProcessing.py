import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import tensorflow as tf



def prepare(filepath):
    IMG_SIZE = 100  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)  # read in the image, convert to grayscale
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize image to match model's expected sizing
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)  # return the image with shaping that TF wants.

def predictImage(im):
    Categories = ["Non psorasis", "Psorasis"]
    new_model = tf.keras.models.load_model("Valid.model")

    prediction = new_model.predict([prepare('D:/College Files/project/dataset/Skin_disease_list/Non psorasis/DLE-005.jpg')])

    print(Categories[int(prediction[0][0])])


