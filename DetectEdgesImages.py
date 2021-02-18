import cv2

# Read image
img = cv2.imread("Images/sample3.jpg")
img = cv2.resize(img, (700, 930))
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# GaussianBlur is used to add blur to an image.
# (9,9) is an argument used to define how strong the blur is. It can only be odd numbers.
img_blur = cv2.GaussianBlur(img_grey, (99, 99), 0)
# Canny is used to detect edges in the image.
# The numbered arguments are threshold values for how defined edges should be.
# Higher the threshold values, lower the edge detection.
img_canny = cv2.Canny(img, 70, 140)
cv2.imshow("canny image", img_canny)
cv2.imshow("blur image", img_blur)
cv2.imshow("grey image", img_grey)
cv2.waitKey(0)
