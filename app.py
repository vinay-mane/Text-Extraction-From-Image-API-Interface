from asyncio.windows_events import NULL
import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
# import imgToText as proc
import cv2
import matplotlib as plt
from PIL import Image
import pytesseract

app = Flask(__name__)

def getText(image):
  return(pytesseract.image_to_string(image))

@app.route('/',methods=['POST'])
def wetImage():
    # if request.method=='GET':
    #     return render_template('index.html',prediction_text='')
    file=request.files['file']
    if file.filename=='':
        return render_template('index.html',prediction_text='')
    print(file.filename)
    img = Image.open(file.stream)
    return render_template('index.html',prediction_text=getText(img))
    # return render_template("index.html",prediction_text="aabc")
    


if __name__=="__main__":
    app.run(debug=True)