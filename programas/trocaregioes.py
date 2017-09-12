import cv2
import numpy as np

image = cv2.imread("nina.jpg",0)
cv2.imshow("image",image)
height, width = image.shape
cv2.waitKey(0)


[a,b] = np.split(image,[int(height/2)], 0)
image = np.concatenate((b,a))
[a,b] = np.split(image,[int(width/2)], 1)
image = np.concatenate((b,a),1)
cv2.imshow("image",image)
cv2.waitKey(0)

cv2.destroyAllWindows()
