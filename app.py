from asyncio.windows_events import NULL
import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
import imgToText as proc
import cv2
import matplotlib as plt
from PIL import Image

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def wetImage():
    if request.method=="GET":
        return render_template("index.html",prediction_text='')
    file=request.files['file']
    if file.filename=='':
        return render_template("index.html",prediction_text='')
    print(file.filename)
    img = Image.open(file.stream)
    return render_template("index.html",prediction_text=proc.getText(img))
    


if __name__=="__main__":
    app.run(debug=True)