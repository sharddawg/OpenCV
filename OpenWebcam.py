import cv2
# Here VideoCapture(0) means opening the default webcam on the computer. 0 is the id for default webcam
vid = cv2.VideoCapture(0)
# set(3, 640) means 3 is the id for setting the length of the window and 640 means the 640 pixels lengthwise
vid.set(3, 640)
# set(4, 480) means 4 is the id for setting the height of the window and 480 means the 480 pixels heightwise
vid.set(4, 480)
# set(10, 100) means 10 is the id to control brightness and 100 is the value of the brightness
vid.set(10, 100)
while True:
    # success is a boolean. frame stores every frame from the video vid.
    success, frame = vid.read()
    # "webcam" is the name of the window that will pop up
    cv2.imshow("webcam", frame)
    # this shit is just ratta for now
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
