import cv2
import numpy as np


# This function is used as an argument in the createTrackbar function.
# Just rote for now.
def empty(x):
    pass


# Storing image name in a variable.
image_name = 'Images/puppy.jpg'
# namedWindow creates a a new window of the name you want.
cv2.namedWindow("trackbar")
# resizeWindow resizes the window we want. The name of the window has to be the same in the argument.
cv2.resizeWindow("trackbar", 400, 300)
# Here we create the slider trackbars and give them names.
# 179 is the maximum value on the trackbar. All minimum values are 0.
# empty is just a empty function defined at the start of the code. It's just ratta for now.
# here we created 6 sliders.
# hue minimum, hue maximum, saturation minimum, saturation maximum, value minimum, value maximum.
# max value for hue is 179. Max value for saturation and value is 255.
# Again just rote for now.
# Here, 0, 168, 79, 255, 141, 255 are values we obtained after manipulating the trackbar values of h_min, h_max etc.
# We manipulated the values till the particular colour we wanted was white in our mask image.
cv2.createTrackbar("hue min", "trackbar", 0, 179, empty)
cv2.createTrackbar("hue max", "trackbar", 168, 179, empty)
cv2.createTrackbar("sat min", "trackbar", 79, 255, empty)
cv2.createTrackbar("sat max", "trackbar", 255, 255, empty)
cv2.createTrackbar("value min", "trackbar", 141, 255, empty)
cv2.createTrackbar("value max", "trackbar", 255, 255, empty)

# We use a while loop to see the values of hue, sat, and val change in real time.
# Also to see the changes to the images in real time.
while True:
    img = cv2.imread(image_name)
    img_resize = cv2.resize(img, (400, 300))
    # To detect a colour, we need to convert it to HSV colour space.
    img_HSV = cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV)
    # getTrackbarPos gives us whatever value we slide to in the trackbar for hue min etc.
    # They will be stored in all these variables.
    # Again the names of the trackbars and the window have to be the same.
    h_min = cv2.getTrackbarPos("hue min", "trackbar")
    h_max = cv2.getTrackbarPos("hue max", "trackbar")
    s_min = cv2.getTrackbarPos("sat min", "trackbar")
    s_max = cv2.getTrackbarPos("sat max", "trackbar")
    v_min = cv2.getTrackbarPos("value min", "trackbar")
    v_max = cv2.getTrackbarPos("value max", "trackbar")
    # This print statement will give us real time updates on how the values of h_min, max etc change.
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    # we take the values we got from the getTrackbarPos method and store them in an array created using numpy.
    # lower stores all the min values and upper stores all the max values.
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img_HSV, lower, upper)
    img_result = cv2.bitwise_and(img_resize, img_resize, mask=mask)
    cv2.imshow("puppy", img_resize)
    cv2.imshow("hsv", img_HSV)
    cv2.imshow("mask", mask)
    cv2.imshow("result", img_result)
    cv2.waitKey(1)
