import pytesseract
import cv2

def getText(image):
  return(pytesseract.image_to_string(image))

# image = cv2.imread("j.png")
# getText(image)