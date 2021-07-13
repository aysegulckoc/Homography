from cv2 import cv2
import numpy as np

im = cv2.imread("example2.png")
# 2D image points
image_points = np.array([(767, 1294), (1350, 1207), (761, 987), (310, 1015)],
                        dtype="double")

# 3D model points 
model_points = np.array([(0.0, 0.0, 0.0), (74.0, 0.0, 0.0), (0.0, 40.0, 0.0),
                        (-65.0, 40.0, 0.0), ])

h, status = cv2.findHomography(image_points, model_points, cv2.RANSAC, 5.0)
print(f"Homografi Matrix : {h}")

#Calculation homograpy matrix for camera calibration
result = np.matmul(h,  np.array([953, 1337, 1]).reshape(3, 1))

result = result / result[2]

print(f"Result Matrix : {result}")

cv2.imshow("Output", im)
cv2.waitKey(0)
