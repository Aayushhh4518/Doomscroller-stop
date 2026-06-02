import cv2


class VideoPanel:

    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(video_path)

    def get_frame(self):

        success, frame = self.cap.read()

        if not success:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

            success, frame = self.cap.read()

        frame = cv2.resize(frame, (640, 480))

        return frame