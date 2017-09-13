import cv2
from copy import copy
import numpy as np
from matplotlib import pyplot as plt

nbins = 256

image = cv2.imread("nina.jpg",0)
cv2.imshow("nina",image)
cv2.waitKey(0)

hist = cv2.calcHist([image],[0],None,[nbins],[0,256])

hist_acum = []
hist_acum.append(int(hist[0]))
for i in hist[1:]:
    hist_acum.append(hist_acum[len(hist_acum)-1]+int(i))

im_2 = copy(image)

height, width = image.shape

print(height,width)

for y in range(height):
    for x in range(width):
        index = image[y,x]
        im_2[y,x] = np.round(hist_acum[index]*255/(height*width))

hist2 = cv2.calcHist([im_2],[0],None,[nbins],[0,256])


cv2.imshow("nina_eq",im_2)
plt.plot(hist,'.k')
plt.plot(hist2,'.r')
plt.xlim([0,nbins])
plt.show()
cv2.waitKey(0)


cv2.destroyAllWindows()