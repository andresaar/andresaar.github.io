import cv2
import numpy as np
from random import *
from copy import copy

step = 5
jitter = 3
raio = 2
kernel = np.ones([3,3],dtype=np.uint8)

image_or = cv2.imread("nina.jpg")
image = cv2.cvtColor(image_or,cv2.COLOR_BGR2GRAY)

height, width, depth = image_or.shape
xrange, yrange = np.arange(0, int(height / step)), np.arange(0, int(width / step))

for i in range(len(xrange)):
    xrange[i] = int(xrange[i] * step + step / 2)
for j in range(len(yrange)):
    yrange[j] = int(yrange[j] * step + step / 2)

points = copy(image_or)
points = cv2.blur(points,(5,5))
points = cv2.blur(points,(5,5))
points = cv2.blur(points,(5,5))

vector = np.arange(10,200,10)
shuffle(vector)

for i in vector:
    np.random.shuffle(xrange)

    canny = cv2.Canny(image,i,3*i)
    canny = cv2.dilate(canny,kernel,iterations=1)

    for j in xrange:
        np.random.shuffle(yrange)
        for k in yrange:
            if canny[j,k] == 255:
                x = j + randrange(-jitter, jitter)
                y = k + randrange(-jitter, jitter)
                pixel = image_or[j, k].tolist()
                bola = int(raio + (i)/190*randrange(2,5))
                cv2.circle(points, (y, x), bola, pixel, -1, cv2.LINE_AA)

cv2.imshow("pontilhado", np.hstack((image_or,points)))
cv2.imwrite("cannypoints.jpg", points)
cv2.waitKey(0)
cv2.destroyAllWindows()