import cv2
import mediapipe as mp

class FaceTracker:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh

        # ```
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def get_landmarks(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.face_mesh.process(rgb)

    def get_eye_position(self, landmarks):
        left_iris = landmarks[468]

        return {
            "x": left_iris.x * 100,
            "y": left_iris.y * 100
        }

    def get_direction(self, landmarks):

        # ```
        iris = self.get_eye_position(landmarks)

        x = iris["x"]
        y = iris["y"]

        if y > 58:
            return "DOWN"

        elif y < 35:
            return "CENTER"

        elif x < 50:
            return "LEFT"

        elif x > 62:
            return "RIGHT"

        else:
            return "CENTER"
        # ```
