FROM python:3.7 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    python3 \
    #python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove
# RUN apt-get install tesseract-ocr
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app