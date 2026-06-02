import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

VIDEO_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "dog.mp4"
)

AUDIO_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "dog_sound.mp3"
)

CAMERA_INDEX = 0

WINDOW_NAME = "DoomScroller Stop"