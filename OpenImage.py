import cv2

# cv2.imread reads an image
img = cv2.imread("Images/puppy.jpg")
cv2.imshow("image", img)
# If argument in waitKey is 0, that means infinite delay.
# If it's 1, means 1ms and so on
cv2.waitKey(0)
