import cv2
import numpy as np
from copy import copy

def printMask(mask):
    heigh, width = mask.shape
    for y in range(heigh):
        for x in range(width):
            print(str(mask[y,x]) + "   ")
        print('\n')

def menu():
    print("\nPressione a tecla para ativar o filtro:"
          "\na - calcular modulo"
          "\nm - media"
          "\ng - gauss"
          "\nv - vertical"
          "\nh - horizontal"
          "\nl - laplaciano"
          "\nx - laplaciano do gaussiano"
          "\nesc - sair\n")

media = np.ones([3,3],dtype=np.float32)
gauss = np.array([[1,2,1],
                 [2,4,2],
                 [1,2,1]],dtype=np.float32)
horizontal = np.array([[-1,0,1],
                 [-2,0,2],
                 [-1,0,1]],dtype=np.float32)
vertical = np.array([[-1,-2,-1],
                 [0,0,0],
                 [1,2,1]],dtype=np.float32)
laplacian = np.array([[0,-1,0],
                 [-1,4,-1],
                 [0,-1,0]],dtype=np.float32)

mask = copy(media)
image = cv2.imread("nina.jpg",0)
height, width = image.shape
mask1 = cv2.scaleAdd(mask,1/9.0,np.zeros([3,3],dtype=np.float32))
mask, mask1 = mask1, mask
absolute = True

menu()
case = -1
while True:
    nova = copy(image)
    cv2.flip(nova,1,nova)
    cv2.imshow("original", nova)
    nova32 = np.array(nova,dtype=np.float32)
    frameFiltered = cv2.filter2D(nova32,-1,mask,anchor=(1,1))
    if absolute:
        frameFiltered = abs(frameFiltered)
    result = np.array(frameFiltered,dtype=np.uint8)
    if case == ord('x'):
        result = lap_gauss
    cv2.imshow("filtroespacial",result)
    case = cv2.waitKey(10)
    if case == ord('a'):
        menu()
        absolute = not absolute
    elif case == ord('m'):
        menu()
        mask = copy(media)
        mask1 = cv2.scaleAdd(mask,1/9.0,np.zeros([3,3],dtype=np.float32))
        mask = mask1
        printMask(mask)
    elif case == ord('g'):
        menu()
        mask = copy(gauss)
        mask1 = cv2.scaleAdd(mask, 1/16.0, np.zeros([3, 3],dtype=np.float32))
        mask = mask1
        printMask(mask)
    elif case == ord('h'):
        menu()
        mask = copy(horizontal)
        printMask(mask)
    elif case == ord('v'):
        menu()
        mask = copy(vertical)
        printMask(mask)
    elif case == ord('l'):
        menu()
        mask = copy(laplacian)
        printMask(mask)
    elif case == ord('x'):
        menu()
        mask = copy(gauss)
        mask = cv2.scaleAdd(mask, 1 / 16.0, np.zeros([3, 3], dtype=np.float32))
        nova32 = np.array(nova, dtype=np.float32)
        nova32 = cv2.filter2D(nova32, -1, mask, anchor=(1, 1))
        mask = copy(laplacian)
        lap_gauss = cv2.filter2D(nova32, -1, mask, anchor=(1, 1))
        lap_gauss = np.array(lap_gauss,dtype=np.uint8)

    elif case == 27:
        break
    else:
        pass

cv2.destroyAllWindows()
