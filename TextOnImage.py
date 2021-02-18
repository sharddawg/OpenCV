import cv2
import numpy as np

# np.zeros gives us a matrix full of zeros.
# (500, 500, 3) is the size.
# np.uint8 gives us values ranging from 0 to 256.
img = np.zeros((500, 500, 3), np.uint8)
print(img.shape)
# We know img is a matrix.
# 166:332 and 166:332 is to take a limit on the matrix. Only those pixels will be coloured.
# 0, 0, 255 is the colour. Its blue, green, red.
img[166:332, 166:332] = 0, 0, 255
# cv2.line makes a line on the image.
# (0,0) is the starting point.
# (500,500) is the ending point. Its width and then height.
cv2.line(img, (0, 0), (500, 500), (255, 255, 0), 2)
cv2.line(img, (0, 500), (500, 0), (255, 255, 0), 2)
cv2.line(img, (0, 250), (500, 250), (200, 255, 0), 2)
cv2.rectangle(img, (166, 166), (332, 332), (200, 255, 0), 2)
cv2.circle(img, (250, 250), 83, (200, 255, 0), 2)
# cv2.putText puts text in the desired location.
# cv2.FONT is used to define the font.
# 1 is the scale factor.
cv2.putText(img, "SHAPES", (188, 380), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)
cv2.imshow("random image", img)
cv2.waitKey(0)
