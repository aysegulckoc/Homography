
from cv2 import cv2
# img = cv2.imread("deneme2.png")
cap = cv2.VideoCapture('/Users/aysegulkoc/Movies/3_01.mp4')
while True:
    _, frame = cap.read()
    (h, w, z) = frame.shape

    cv2.circle(frame, (639, 600), 20, (0, 0, 255), -1)
    cv2.circle(frame, (1111, 800), 20, (0, 255, 0), -1)
    # cv2.circle(frame, (1350, 1207), 20, (0, 0, 255), -1)
    # cv2.circle(frame, (340, 1027), 20, (0, 0, 255), -1)
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

print(h)
print(w)
print(z)
