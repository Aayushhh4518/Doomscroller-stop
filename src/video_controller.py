import os
from config import VIDEO_PATH


class VideoController:
    def __init__(self):
        self.is_playing = False

    def play_video(self):
        if not self.is_playing:
            os.startfile(VIDEO_PATH)
            self.is_playing = True

    def stop_video(self):
        self.is_playing = False