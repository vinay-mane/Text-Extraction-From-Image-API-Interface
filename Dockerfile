FROM python:3.7 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install tesseract-ocr
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app