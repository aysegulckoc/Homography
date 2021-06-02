from cv2 import cv2
import numpy as np

im = cv2.imread("deneme2.png")
# 2D image points. If you change the image, you need to change vector
image_points = np.array([(767, 1294), (1350, 1207), (761, 987), (310, 1015)],
                        dtype="double")

# 3D model points.
model_points = np.array([(0.0, 0.0, 0.0), (74.0, 0.0, 0.0), (0.0, 40.0, 0.0),
                        (-65.0, 40.0, 0.0), ])
h, status = cv2.findHomography(image_points, model_points, cv2.RANSAC, 5.0)
print(f"Homografi Matrix : {h}")

sonuc = np.matmul(h,  np.array([953, 1337, 1]).reshape(3, 1))
# sonuc1 = np.matmul(h,  np.array([314,1330,1]).reshape(3,1) )


sonuc = sonuc / sonuc[2]
# sonuc1 = sonuc1 / sonuc1[2]


print(f"sonuc Matrix : {sonuc}")
# print(f"sonuc1 Matrix : {sonuc1}")

cv2.imshow("Output", im)
cv2.waitKey(0)
