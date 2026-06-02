import cv2

from config import CAMERA_INDEX, WINDOW_NAME
from face_tracker import FaceTracker

cap = cv2.VideoCapture(CAMERA_INDEX)

tracker = FaceTracker()

while True:
    success, frame = cap.read()

    if not success:
        break

    results = tracker.detect_face(frame)
    print(results.detections)

    if results.detections:
        cv2.putText(
            frame,
            "FACE DETECTED",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )
    else:
        cv2.putText(
            frame,
            "NO FACE",
            (20, 40),
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