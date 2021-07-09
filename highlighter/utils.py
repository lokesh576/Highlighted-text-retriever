import cv2
import numpy as np
from PIL import Image as im
from django.conf import settings
import os

def detectColor(img):
    hsv = [0, 179, 125, 255, 0, 255]
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV",imgHSV)

    lower = np.array([hsv[0], hsv[2], hsv[4]])
    upper = np.array([hsv[1], hsv[3], hsv[5]])
    mask = cv2.inRange(imgHSV, lower, upper)

    data = im.fromarray(mask)
    data.save(os.path.join(settings.MEDIA_ROOT, "masked_image.jpg"))

    mask = cv2.imread(os.path.join(settings.MEDIA_ROOT, "masked_image.jpg"))
    #cv2.imshow("mask", mask)

    imgResult = cv2.bitwise_and(img, mask)
    return imgResult

def getContours(imgResult, img):
    imgGray = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)

    contours, hierarchy = cv2.findContours(imgGray, cv2.RETR_EXTERNAL, 
                                           cv2.CHAIN_APPROX_SIMPLE)
    final_contors = []
    high_count = 0
    for cnt in contours:
        if cv2.contourArea(cnt)>600:
            high_count+=1
            final_contors.append(cnt)
            x,y,w,h = cv2.boundingRect(cnt)
            roi = img[y:y+h, x:x+w]
            imname = str(high_count)+'.jpg'
            cv2.imwrite(os.path.join(settings.MEDIA_ROOT, imname), roi)
            #cv2.imshow(os.path.join(settings.MEDIA_ROOT, imname),roi)
            cv2.waitKey(0)
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            img = cv2.drawContours(img, [box], 0, (0,255,0), 3)
    return high_count
