import cv2

# Read image
# img = cv2.imread('Images/puppy.jpg', 0) will also convert image to greyscale.
img = cv2.imread("Images/puppy.jpg")
# Changing colourspace using cvtColor.
# cv2.COLOR_BGR2GREY is an argument used to change to greyscale. Many others are available.
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grey image", img_grey)
cv2.waitKey(0)
