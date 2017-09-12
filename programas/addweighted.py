import cv2
import numpy as np
from copy import copy

alfa_slider = 0
alfa_slider_max = 100

top_slider = 0
top_slider_max = 100

def on_trackbar_blend(alfaslider):
    global image1, imageTop, alfa_slider
    alfa_slider = alfaslider
    alfa = float(alfa_slider/alfa_slider_max)
    blended = cv2.addWeighted(image1, alfa, imageTop, 1-alfa,0.0)
    cv2.imshow("addweighted", blended)

def on_trackbar_line(topslider):
    global image1, top_slider, imageTop, image2, alfa_slider
    top_slider = topslider
    imageTop = copy(image1)
    limit = int(top_slider*255 / 100)
    if limit > 0:
        tmp = image2[0:limit,0:256]
        imageTop[0:limit,0:256] = tmp
    on_trackbar_blend(alfa_slider)

image1 = cv2.imread("blend1.jpg")
image2 = cv2.imread("blend2.jpg")
imageTop = copy(image2)
cv2.namedWindow("addweighted",1)
trackbarName = "Alpha x " + str(alfa_slider_max)
cv2.createTrackbar(trackbarName,"addweighted",alfa_slider,alfa_slider_max,on_trackbar_blend)
trackbarName = "Scanline x " + str(top_slider_max)
cv2.createTrackbar(trackbarName,"addweighted",top_slider,top_slider_max,on_trackbar_line)

cv2.waitKey(0)

cv2.destroyAllWindows()