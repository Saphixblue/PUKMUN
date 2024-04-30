#sprite_handler

import pygame
import os


class SpriteHandler:
    def __init__(self, CELL_SIZE):
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, 'images')

        self.CELL_SIZE = CELL_SIZE

    def load_image(self, image_name):
        image_path = os.path.join(self.image_path, image_name)
        image = pygame.image.load(image_path).convert()
        return pygame.transform.scale(image, (self.CELL_SIZE, self.CELL_SIZE))

    def tile_image(self):
        tile_image = self.load_image('Tile_1.png')
        return tile_image
