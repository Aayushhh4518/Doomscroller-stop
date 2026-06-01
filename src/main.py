from video_controller import VideoController
import time

video = VideoController()

print("Opening dog video...")

video.play_video()

time.sleep(5)

print("Test complete")