import cv2
import numpy as np

img = cv2.imread("Images/sample2.jpeg")
# width and height seem to affect the ratio of the final image.
print(img.shape)
width, height = 700, 1000
# points1 is a 2D 4x2 matrix.
# all the points here are the 4 end points of the particular thing we need to get a birds eye view for.
points1 = np.float32([[323, 236], [797, 246], [42, 852], [689, 997]])
# points2 is also a 2D 4x2 matrix.
# here we have to correspond to the points in points1.
# for example, [364,12] is the top left point, and it will become the new origin for the cropped image.
# width and height are the literal width and height of the particular object you want a bev for.
# to enlarge or reduce the size of the original image just keep the ratio of width and height same.
points2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# ratta for now
matrix = cv2.getPerspectiveTransform(points1, points2)
img_wp = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("page", img)
cv2.imshow("warped page", img_wp)
cv2.waitKey(0)
