import cv2
import numpy as np
from copy import copy

l1 = 0
l2 = 0
d = 0
y = 0
delta = 0

image = cv2.imread("natal.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype("float32")
(h,s,v) = cv2.split(image)
s = s*1.5
s = np.clip(s,0,255)
image = cv2.merge([h,s,v])
image = cv2.cvtColor(image.astype("uint8"), cv2.COLOR_HSV2BGR)
image = np.array(image,dtype=np.float32)


height, width, depth = image.shape

media = np.ones([3,3],dtype=np.float32)
mask = cv2.scaleAdd(media,1/9.0,np.zeros([3,3],dtype=np.float32))
image_2 = copy(image)
for i in range(10):
    image_2 = cv2.filter2D(image_2,-1,mask,anchor=(1,1))

result = np.zeros([height, width, depth])

def sety(l):
    global l1, l2, y, delta
    y = l
    l1 = y - int(delta/2)
    l2 =  y + int(delta/2)
    applyTilt()

def setdelta(l):
    global l1, l2, y, delta
    delta = l
    l1 = y - int(delta/2)
    l2 =  y + int(delta/2)
    applyTilt()

def setd(dv):
    global d
    d = dv
    applyTilt()

def alpha(x, l1, l2, d):
    return (0.5 * (np.tanh((x-l1)/(d+0.0001)) - np.tanh((x-l2)/(d+0.0001))))

def tilt_filter():
    global height, width, l1, l2, d
    array = np.ones([height,width])
    for y in range(height):
        array[y,:] *= alpha(y, l1, l2, d)
    return np.array(array,dtype=np.float32)

def applyTilt():
    global height, width, l1, l2, d, result
    filtro = tilt_filter()

    filtro_negativo = np.ones([height, width], dtype=np.float32) - filtro
    for i in range(depth):
        result[:,:,i] = cv2.multiply(filtro,image[:,:,i])
        result[:,:,i] += cv2.multiply(filtro_negativo,image_2[:,:,i])

    cv2.imshow("tilt",np.array(result,dtype=np.uint8))

cv2.imshow("tilt",np.array(image,dtype=np.uint8))
trackbarName = "Y " + str(height)
cv2.createTrackbar(trackbarName,"tilt",l1,height,sety)
trackbarName = "DELTA " + str(height)
cv2.createTrackbar(trackbarName,"tilt",l2,height,setdelta)
trackbarName = "D " + str(100)
cv2.createTrackbar(trackbarName,"tilt",d,100,setd)

cv2.waitKey(0)
cv2.imwrite("tilt.jpg",result)
cv2.destroyAllWindows()


