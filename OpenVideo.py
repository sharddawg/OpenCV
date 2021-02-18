import cv2

vid = cv2.VideoCapture("Videos/final shii 2.2.mp4")
while True:
    # success is a boolean. frame stores every frame from the video vid.
    success, frame = vid.read()
    # "video" is the name of the window that will pop up
    cv2.imshow("video", frame)
    # this shit is just ratta for now
    if cv2.waitKey(1) and 0xFF == ord("q"):
        break
