import cv2

img = cv2.imread("Images/puppy.jpg")
# img.shape gives us the shape of the image.
print(img.size)
# resize helps us resize the image.
# (640, 480) is the new size of the image.
# 480 is the height. 640 is the width.
img_resized = cv2.resize(img, (640, 480))
print(img_resized.size)
# Image is just a matrix made up of 1D arrays.
# First height 0:200 then width 700:1000
img_cropped = img[0:720, 700:1000]
cv2.imshow("cropped image", img_cropped)
cv2.imshow("resized image", img_resized)
cv2.imshow("image", img)
cv2.waitKey(0)
