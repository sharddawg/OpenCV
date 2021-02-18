import cv2
import numpy as np
# from matplotlib import pyplot as plt

img = cv2.imread("Images/puppy.jpg")
img_resize = cv2.resize(img, (400, 300))
# Subtracting 255 from all values in the image matrix inverts them
img_negative1 = (255 - img_resize)
# or
img_negative2 = cv2.bitwise_not(img_resize)
joined = np.hstack((img_resize, img_negative1, img_negative2))
cv2.imshow('joined', joined)
cv2.waitKey(0)


