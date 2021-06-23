
from cv2 import cv2
# img = cv2.imread("deneme2.png")
cap = cv2.VideoCapture('/Users/aysegulkoc/Movies/2_01.mp4')
while True:
    _, frame = cap.read()
    (h, w, z) = frame.shape

    cv2.circle(frame, (200, 550), 20, (0, 0, 255), -1)
    # cv2.circle(frame, (767, 1294), 20, (0, 255, 0), -1)
    cv2.circle(frame, (1150, 780), 20, (255, 0, 255), -1)
    # cv2.circle(frame, (340, 1027), 20, (0, 0, 255), -1)
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

print()

print(h)
print(w)
print(z)
