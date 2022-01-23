import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import tensorflow as tf
from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense, Dropout, Activition, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D



Datadir="D:/College Files/project/dataset/Skin_disease_list"
Categories=["Non psorasis","Psorasis"]
#Categories=["Cat","Dog"]

# for category in Categories:
#     path=os.path.join(Datadir, category)
#     for img in os.listdir(path):
#         img_array=cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
#         plt.imshow(img_array, cmap="gray")
#         plt.show()
#         break
#     break

    #print(img_array)

IMG_SIZE = 100
    #
    # new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    # plt.imshow(new_array, cmap='gray')
    # plt.show()

training_data = []


def create_training_data():
    IMG_SIZE = 100
    for category in Categories:
        path = os.path.join(Datadir, category)
        class_num = Categories.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass


create_training_data()

print(len(training_data))


random.shuffle(training_data)

for sample in training_data:
    print(sample[1])


X=[]
y=[]

for features, label in training_data:
    X.append(features)
    y.append(label)
IMG_SIZE = 100
X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
y = np.array(y)


f=1
while f==1:
    X=X/255.0
    #tensorflow.python.keras
    model = Sequential()
    model.add(Conv2D(64,(3,3), input_shape = X.shape[1:]))
    model.add(tf.keras.layers.Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))


    model.add(Conv2D(64,(3,3)))
    model.add(tf.keras.layers.Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))


    model.add(Flatten())
    model.add(Dense(64))
    model.add(tf.keras.layers.Activation("relu"))

    model.add(Dense(1))
    model.add(tf.keras.layers.Activation('sigmoid'))

    model.compile(loss="binary_crossentropy",optimizer="adam",metrics=['accuracy'])

    model.fit(X,y,batch_size=32, epochs=10, validation_split=0.1)
    val_loss,val_acc=model.evaluate(X,y)
    acc=float(val_acc)
    if acc>0.89:
        model.save('Valid.model')
        f=0