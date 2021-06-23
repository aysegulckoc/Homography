'''
import numpy as np
from cv2 import cv2

img_raw = cv2.imread('/Users/aysegulkoc/Pictures/or.png')
roi = cv2.selectROI(img_raw)
print(roi)

roi_crop = img_raw[int(roi[1]):int(roi[1]+roi[3]),
                   int(roi[0]):int(roi[0]+roi[2])]

cv2.imshow("ROI", roi_crop)
# cv2.imwrite("crop.png",roi_crop )

cv2.waitKey(0)

'''
from cv2 import cv2

cap = cv2.VideoCapture('/Users/aysegulkoc/Movies/3_01.mp4')

while True:
    ret, frame = cap.read()
    roi = cv2.selectROI(frame)
    print(roi)
    roi_crop = frame[int(roi[1]):int(roi[1]+roi[3]),
                     int(roi[0]):int(roi[0]+roi[2])]
    (h, w, z) = frame.shape
    print(h)
    print(w)
    print(z)

    cv2.imshow("ROI", roi_crop)
    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
cv2.destroyAllWindows()
