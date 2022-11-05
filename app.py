from flask import Flask,request,app,render_template
import imgToText as proc
from PIL import Image


app = Flask(__name__)

# def getText(image):
#   return(pytesseract.image_to_string(image))

@app.route('/',methods=['POST','GET'])
def wetImage():
    if request.method=='GET':
        return render_template("index.html",prediction_text='')
    file=request.files['file']
    if file.filename=='':
        return render_template("index.html",prediction_text='')
    print(file.filename)
    img = Image.open(file.stream)
    return render_template("index.html",prediction_text=proc.getText(img))
    # return render_template("index.html",prediction_text="aabc")
    


if __name__=="__main__":
    app.run(debug=True)