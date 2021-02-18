import cv2

img = cv2.imread("Images/justiceleague.jpeg")
# img.shape gives us the shape of the image.
print(img.size)
# resize helps us resize the image.
# (640, 480) is the new size of the image.
# 480 is the height. 640 is the width.
img_resized = cv2.resize(img, (1000, 1000))
cv2.imshow("resized image", img_resized)
cv2.imshow("image", img)
cv2.waitKey(0)
