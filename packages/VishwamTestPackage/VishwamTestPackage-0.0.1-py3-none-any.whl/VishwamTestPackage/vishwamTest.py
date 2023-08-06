import cv2
from imutils.video import VideoStream

def openVideoStream(camera_url):
    cap = VideoStream(src=camera_url).start()
    frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    while True:
        cv2.imshow('Stream',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# if __name__ == '__main__':
#     openVideoStream(0)