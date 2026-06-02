import cv2
from video_controller import VideoController

from config import CAMERA_INDEX, WINDOW_NAME
from face_tracker import FaceTracker

cap = cv2.VideoCapture(CAMERA_INDEX)

tracker = FaceTracker()
video = VideoController()

focused_frames = 0
distracted_frames = 0

DOG_TRIGGER = 2
DOG_STOP = 10

dog_active = False

while True:

    # ```
    success, frame = cap.read()

    if not success:
        break

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
        if (
            distracted_frames >= DOG_TRIGGER
            and not dog_active
        ):

            video.play_video()

            dog_active = True
        if (
            focused_frames >= DOG_STOP
            and dog_active
        ):

            video.stop_video()

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

        iris = tracker.get_eye_position(face_landmarks)

        cv2.putText(
            frame,
            f"X: {iris['x']:.2f}",
            (20, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            f"Y: {iris['y']:.2f}",
            (20, 190),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

    else:

        cv2.putText(
            frame,
            "NO FACE",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    cv2.imshow(WINDOW_NAME, frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    # ```

cap.release()
cv2.destroyAllWindows()
