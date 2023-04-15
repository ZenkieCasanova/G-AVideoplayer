import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import confirmation

def classify1():
    new_model = load_model('C:/Users/Mark Renzkie/PycharmProjects/pythonProject5/AGEKAGGLENOW2.h5')
    import os

    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

    def loadImage(filepath):
        test_img = image.load_img(filepath, target_size=(128, 128))
        test_img = image.img_to_array(test_img)
        test_img = np.expand_dims(test_img, axis=0)
        test_img /= 255
        return test_img

    picture = 'C:/Users/Mark Renzkie/PycharmProjects/pythonProject5/face.jpg'
    age_pred, gender_pred = new_model.predict(loadImage(picture))
    img = image.load_img(picture)
    max = -1
    count = 0

    for i in age_pred[0]:
        if i > max:
            max = i
            temp = count
        count += 1

    if temp == 0:
        confirmation.age = '1-15'
    if temp == 1:
        confirmation.age  = '16-58'
    if temp == 2:
        confirmation.age  = '59-70+'

    if gender_pred[0][0] > gender_pred[0][1]:
        confirmation.gender = 'Male'
    else:
        confirmation.gender = 'Female'

if __name__ == '__main__':
    classify1()

