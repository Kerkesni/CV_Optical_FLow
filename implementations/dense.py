import numpy as np
import cv2 as cv
cap = cv.VideoCapture(cv.samples.findFile("../video/people_walking.mp4"))
ret, frame1 = cap.read()
prvs = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)

while(1):
    ret, frame2 = cap.read()
    mask = np.zeros_like(frame2)
    next = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)
    flow = cv.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    for x in range(0, next.shape[1], 15):
        for y in range(0, next.shape[0], 15):
            flowatxy = (flow[y][x][0]*10, flow[y][x][1]*10)
            mask = cv.line(mask, (x, y),(int(round(x+flowatxy[0])),int(round(y+flowatxy[1]))), (255, 0, 255), 2)

    img = cv.add(frame2, mask)
    cv.imshow('frame', img)

    # exiting & saving
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv.imwrite('opticalfb.png',img)
    prvs = next