
import cv2
import numpy as np

#img = cv2.imread("deneme2.png")
cap = cv2.VideoCapture('Untitled.m4v')
while True :
    _, frame = cap.read()
    cv2.circle(frame, (767, 1294), 20, (0, 0, 255), -1)
    cv2.circle(frame, (761, 987), 20, (0, 0, 255), -1)
    cv2.circle(frame, (1350, 1207), 20, (0, 0, 255), -1)
    cv2.circle(frame, (340, 1027), 20, (0, 0, 255), -1)


    pts_src = np.array([[0, 0, 0], [74, 0, 0], [0, 40, 0], [-65, 40, 0]])
    pts_dst = np.array([[767, 1294,], [1350, 1207], [761, 987], [340, 1027]])
    h, status = cv2.findHomography(pts_src, pts_dst, cv2.RANSAC, 5.0)

    point3D = h * 




    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

