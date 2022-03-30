from __future__ import division, print_function
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

import sys
import os
import glob
import re
import numpy as np

app = Flask(__name__)

MODEL_PATH = 'model.h5'

model = load_model(MODEL_PATH)

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size = (224, 224))
    
    x = image.img_to_array(img)

    x = x / 255
    x = np.expand_dims(x, axis = 0)

    preds = model.predict(x)
    preds = np.argmax(preds, axis = 1)

    if preds == 0:
        preds = "Chevrolet Spark"
    elif preds == 1:
        preds = "Genesis G70"
    elif preds == 2:
        preds = "Genesis G80"
    elif preds == 3:
        preds = "Genesis G90"
    elif preds == 4:
        preds = "Genesis GV70"
    elif preds == 5:
        preds = "Genesis GV80"
    elif preds == 6:
        preds = "Hyundai Avante"
    elif preds == 7:
        preds = "Hyundai Equus"
    elif preds == 8:
        preds = "Hyundai Grandeur"
    elif preds == 9:
        preds = "Hyundai Maxcruz"
    elif preds == 10:
        preds = "Hyundai Palisade"
    elif preds == 11:
        preds = "Hyundai SantaFE"
    elif preds == 12:
        preds = "Hyundai Venue"
    elif preds == 13:
        preds = "Kia K3"
    elif preds == 14:
        preds = "Kia K5"
    elif preds == 15:
        preds = "Kia K7"
    elif preds == 16:
        preds = "Kia K8"
    elif preds == 17:
        preds = "Kia Mohave"
    elif preds == 18:
        preds = "Kia Morning"
    else:
        preds = "Kia Sorento"
        
    return preds

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        preds = model_predict(file_path, model)
        result = preds

        return result
    return None

if __name__ == '__main__':
    app.run(host = '0.0.0.0')