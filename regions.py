import cv2

refPt = []

def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))

image = cv2.imread("nina.jpg",0)
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
cv2.imshow("image", image)

while True:
    key = cv2.waitKey(10) & 0xFF
    if len(refPt)==2:
        for y in range(refPt[0][0], refPt[1][0]):
            for x in range(refPt[0][1], refPt[1][1]):
                image[x][y] = 255 - image[x][y]
        cv2.imshow("image", image)
        image = cv2.imread("nina.jpg", 0)
        key = cv2.waitKey()
        cv2.imshow("image", image)
        refPt = []
        if key == ord("z") or key == -1:
            break
        cv2.imshow("image", image)


cv2.destroyAllWindows()




