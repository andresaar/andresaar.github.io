import cv2
import numpy as np
from copy import copy

video_r = cv2.VideoCapture("traffic.mp4")
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
video_w = cv2.VideoWriter("traffic_tilt.avi",fourcc , video_r.get(cv2.CAP_PROP_FPS), (int(video_r.get(cv2.CAP_PROP_FRAME_WIDTH)),int(video_r.get(cv2.CAP_PROP_FRAME_HEIGHT))),True)

l1 = 400
l2 = 600
d = 20
m = 0


def alpha(x, l1, l2, d):
    return (0.5 * (np.tanh((x-l1)/(d+0.0001)) - np.tanh((x-l2)/(d+0.0001))))

def tilt_filter():
    global height, width, l1, l2, d
    array = np.ones([height,width])
    for y in range(height):
        array[y,:] *= alpha(y, l1, l2, d)
    return np.array(array,dtype=np.float32)

def applyTilt(image, image_2):
    global height, width, l1, l2, d, result
    filtro = tilt_filter()

    filtro_negativo = np.ones([height, width], dtype=np.float32) - filtro
    for i in range(depth):
        result[:,:,i] = cv2.multiply(filtro,image[:,:,i])
        result[:,:,i] += cv2.multiply(filtro_negativo,image_2[:,:,i])

while True:
    ret, frame = video_r.read()
    if not ret:
        break
    ret, frame = video_r.read()
    if not ret:
        break
    ret, frame = video_r.read()
    if not ret:
        break
    if not ret:
        break
    ret, frame = video_r.read()
    if not ret:
        break



    height, width, depth = frame.shape
    result = np.zeros([height,width,depth])

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype("float32")
    (h, s, v) = cv2.split(frame)
    s = s * 1.5
    s = np.clip(s, 0, 255)
    frame = cv2.merge([h, s, v])
    frame = cv2.cvtColor(frame.astype("uint8"), cv2.COLOR_HSV2BGR)
    frame = np.array(frame, dtype=np.float32)

    media = np.ones([3, 3], dtype=np.float32)
    mask = cv2.scaleAdd(media, 1 / 9.0, np.zeros([3, 3], dtype=np.float32))
    frame_blur = copy(frame)
    for i in range(10):
        frame_blur = cv2.filter2D(frame_blur, -1, mask, anchor=(1, 1))

    applyTilt(frame, frame_blur)

    result = np.array(result,dtype=np.uint8)
    # cv2.waitKey(2)

    # cv2.imshow("hola", result)

    video_w.write(result)

video_r.release()
video_w.release()
cv2.destroyAllWindows()



