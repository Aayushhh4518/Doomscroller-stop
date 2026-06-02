import pygame


class AudioController:

    def __init__(self, audio_path):
        pygame.mixer.init()
        self.audio_path = audio_path

    def play(self):

        if not pygame.mixer.music.get_busy():

            pygame.mixer.music.load(self.audio_path)
            pygame.mixer.music.play(-1)

    def stop(self):

        pygame.mixer.music.stop()