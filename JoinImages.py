import cv2
import numpy as np

img = cv2.imread("Images/puppy.jpg")
img = cv2.resize(img, (640, 480))
# np.hstack stands for horizontal stack.
# img is just a matrix.
# hstack horizontally stacks matrices.
# if the images to be stacked have different colour channels, it won't happen.
horizontal_joined_img = np.hstack((img, img))
# np.vstack stands for vertical stack.
# img is just a matrix.
# vstack vertically stacks matrices.
# if the images to be stacked have different colour channels, it won't happen.
vertical_joined_img = np.vstack((img, img))
cv2.imshow("horizontal", horizontal_joined_img)
cv2.imshow("vertical", vertical_joined_img)
cv2.waitKey(0)
