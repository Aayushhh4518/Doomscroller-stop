import os
from config import VIDEO_PATH


class VideoController:

    def play_video(self):
        try:
            os.startfile(VIDEO_PATH)
        except Exception as e:
            print(e)

    def stop_video(self):
        os.system("taskkill /f /im wmplayer.exe >nul 2>&1")
        os.system("taskkill /f /im Video.UI.exe >nul 2>&1")