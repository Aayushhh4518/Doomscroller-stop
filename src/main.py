import cv2
import numpy as np

from audio_controller import AudioController
from config import AUDIO_PATH, CAMERA_INDEX, WINDOW_NAME, VIDEO_PATH
from face_tracker import FaceTracker
from video_panel import VideoPanel

cap = cv2.VideoCapture(CAMERA_INDEX)

tracker = FaceTracker()
dog_video = VideoPanel(VIDEO_PATH)
audio = AudioController(AUDIO_PATH)

focused_frames = 0
distracted_frames = 0

DOG_TRIGGER = 2
DOG_STOP = 10

dog_active = False

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.resize(frame, (640, 480))

    results = tracker.get_landmarks(frame)

    if results.multi_face_landmarks:

        face_landmarks = results.multi_face_landmarks[0].landmark

        eye_direction = tracker.get_direction(face_landmarks)

        head_direction = tracker.get_head_direction(
            face_landmarks,
            frame.shape[1],
            frame.shape[0]
        )

        focused = (
            eye_direction == "CENTER"
            and head_direction == "CENTER"
        )

        if focused:

            focused_frames += 1
            distracted_frames = 0

        else:

            distracted_frames += 1
            focused_frames = 0

        if distracted_frames >= DOG_TRIGGER:
            if not dog_active:
                audio.play()
            dog_active=True    

        if focused_frames >= DOG_STOP:
            if dog_active:
                audio.stop()
            dog_active = False

        status = "FOCUSED" if focused else "DISTRACTED"

        color = (0, 255, 0) if focused else (0, 0, 255)

        cv2.putText(
            frame,
            status,
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2
        )

        cv2.putText(
            frame,
            f"HEAD: {head_direction}",
            (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 0),
            2
        )

    else:

        dog_active = True

        cv2.putText(
            frame,
            "NO FACE",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    if dog_active:

        dog_frame = dog_video.get_frame()

    else:

        dog_frame = np.zeros((480, 640, 3), dtype=np.uint8)

        cv2.putText(
            dog_frame,
            "FOCUSED",
            (180, 240),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (0, 255, 0),
            3
        )

    combined = np.hstack((dog_frame, frame))

    cv2.imshow(WINDOW_NAME, combined)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()