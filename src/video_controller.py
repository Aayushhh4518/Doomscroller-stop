import os
from config import VIDEO_PATH

class VideoController:
    def __init__(self):
        pass

    def play_video(self):
        try:
            os.startfile(VIDEO_PATH)
        except Exception as e:
            print(f"Video Error: {e}")
