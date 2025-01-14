#import sys
#sys.path.append('/Users/admin/src/tello-gesture-control')

import cv2
#cap = cv2.VideoCapture('http://10.142.47.47:81/cam.mjpeg')
#cap = cv2.VideoCapture('http://10.142.47.47:81')
#cap = cv2.VideoCapture('rtsp://cv2:vitsi4$u@10.142.47.31')
#cap = cv2.VideoCapture('rtsp://cv2:vitsi4$u@10.142.47.31/Streaming/channels/2/')
cap = cv2.VideoCapture('http://10.142.47.13:81')

while True:
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue

    print(frame.shape)
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == 27:
        exit(0)