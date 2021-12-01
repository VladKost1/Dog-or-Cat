import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np


SIZE = 224
def resize_image(img):
  img = tf.cast(img, tf.float32)
  img = tf.image.resize(img, (SIZE, SIZE))
  img = img / 255.0
  return img

def recognize_animal(path):
    model = load_model('model.h5')
    img = load_img(path[1:])
    img_array = img_to_array(img)
    img_resized = resize_image(img_array)
    img_expended = np.expand_dims(img_resized, axis=0)
    prediction = model.predict(img_expended)[0][0]
    pred_label = 'КІТ' if prediction < 0.5 else 'ПЕС'
    return pred_label
