import cv2

# Read image
img = cv2.imread("Images/puppy.jpg")
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# GaussianBlur is used to add blur to an image.
# (9,9) is an argument used to define how strong the blur is. It can only be odd numbers.
img_blur = cv2.GaussianBlur(img_grey, (9, 9), 0)
cv2.imshow("blur image", img_blur)
cv2.imshow("grey image", img_grey)
cv2.waitKey(0)
