# sound_handler

import pygame
import os


class SoundHandler:
    def __init__(self):
        self.current_path = os.path.dirname(__file__)
        self.sound_path = os.path.join(self.current_path, 'sons')

    def load_son(self, sound_name):
        sound_path = os.path.join(self.image_path, sound_name)

        # TODO: Trouver comment load un son
        # son =

    # TODO: Reprendre la logique de SpriteHandler et faire une fonction par son