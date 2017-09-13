import cv2
import copy
from collections import deque

lista_1 = deque()
numero = 0
com_furo = 0

def floodfill(pixel,valor):
    global lista_1, im_2
    troca = im_2[pixel[0],pixel[1]]

    lista_1.append(pixel)
    im_2[pixel[0],pixel[1]] = valor
    while not len(lista_1) == 0:
        elemento = lista_1.pop()
        for x in range(-1, 2):
            for y in range(-1, 2):
                try:
                    if im_2[elemento[0] + x, elemento[1] + y] == troca and not [elemento[0] + x, elemento[1] + y] in lista_1:
                        lista_1.append([elemento[0] + x, elemento[1] + y])
                        im_2[elemento[0] + x, elemento[1] + y] = valor

                except:
                    pass


image = cv2.imread("bolhas.png",0)
cv2.namedWindow("image")
cv2.imshow("image", image)
height, width = image.shape
im_2 = copy.copy(image)
cv2.waitKey(0)


for x in range(width):
    if im_2[0,x] == 255:
        floodfill([0,x],0)
    if im_2[height-1, x] == 255:
        floodfill([height-1,x],0)

for y in range(width):
    if im_2[y,0] == 255:
        floodfill([y,0],0)
    if im_2[y, width-1] == 255:
        floodfill([y, width-1],0)

numero += 20
for x in range(height):
    for y in range(width):
        if im_2[x,y] == 255:
            floodfill([x,y],numero)
            numero += 1

print(numero-20)

cv2.imshow("image", im_2)
cv2.waitKey(0)

floodfill([0,0],255)

for x in range(height):
    for y in range(width):
        if im_2[x,y] == 0:
            floodfill([x,y],255)
            if im_2[x,y-1] != 255:
                com_furo += 1
                floodfill([x,y-1],255)

print(com_furo)

cv2.waitKey(0)
cv2.destroyAllWindows()
