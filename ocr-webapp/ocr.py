import easyocr
import cv2

reader = easyocr.Reader(['en'])

def extract_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = reader.readtext(gray, detail=0)
    return "\n".join(result)
