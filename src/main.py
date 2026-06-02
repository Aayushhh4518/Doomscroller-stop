from video_controller import VideoController
import time

video = VideoController()

print("Opening dog video...")

video.play_video()
# pyrefly: ignore [missing-import]
import cv2
from config import CAMERA_INDEX, WINDOW_NAME

cap = cv2.VideoCapture(CAMERA_INDEX)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow(WINDOW_NAME, frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
time.sleep(5)

print("Test complete")