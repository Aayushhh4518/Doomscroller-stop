import cv2

from config import CAMERA_INDEX, WINDOW_NAME
from face_tracker import FaceTracker

cap = cv2.VideoCapture(CAMERA_INDEX)

tracker = FaceTracker()

while True:
    success, frame = cap.read()

    if not success:
        break

    results = tracker.get_landmarks(frame)

    if results.multi_face_landmarks:

        cv2.putText(
            frame,
            "FACE MESH ACTIVE",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        for face_landmarks in results.multi_face_landmarks:

            for landmark in face_landmarks.landmark:

                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])

                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

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

cap.release()
cv2.destroyAllWindows()