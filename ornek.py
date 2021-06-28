
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
