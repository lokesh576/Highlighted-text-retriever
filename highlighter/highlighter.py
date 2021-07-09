from . import utils
import cv2
import pytesseract as tess 
from django.conf import settings
import os


def highlighter_func(path):
    img = cv2.imread(path)
    imgResult = utils.detectColor(img)
    #print(tess.image_to_string(img2))
    cv2.imwrite(os.path.join(settings.MEDIA_ROOT, "mask_and_original.jpg"), imgResult)
    final_count = utils.getContours(imgResult, img)
    li = []
    for i in range(1,final_count+1):
        imname = str(i)+'.jpg'
        text = tess.image_to_string(cv2.imread(os.path.join(settings.MEDIA_ROOT, imname)))
        li.append(text[:len(text)-2])
    return li