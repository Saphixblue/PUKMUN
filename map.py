# map.py
from sprite_handler import SpriteHandler


class Map:
    def __init__(self, DIMENSION_MAP, CELL_SIZE):

        self.DIMENSION_MAP = DIMENSION_MAP
        self.CELL_SIZE = CELL_SIZE
        self.WINDOW_SIZE = (self.DIMENSION_MAP[0] * self.CELL_SIZE, self.DIMENSION_MAP[1] * self.CELL_SIZE)

        # Création de la carte avec des cases vides par défaut
        self.map_data = [[0 for _ in range(self.DIMENSION_MAP[1])] for _ in range(self.DIMENSION_MAP[0])]

        sprite_handler = SpriteHandler(self.CELL_SIZE)

        self.petit_graille_image = sprite_handler.petit_graille_image()
        self.gros_graille_image = sprite_handler.gros_graille_image()
        self.tile_vide_image = sprite_handler.tile_vide_image()
        self.tile_image = sprite_handler.tile_image()
        self.trou_image = sprite_handler.trou_image()
        self.porte_image = sprite_handler.porte_image()

    def draw_rectangle_obstacle(self, x, y, longueur, largeur):
        for i in range(longueur):
            for j in range(largeur):
                if 0 <= x + i < self.DIMENSION_MAP[0] and 0 <= y + j < self.DIMENSION_MAP[1]:
                    self.map_data[x + i][y + j] = 3

    def draw_angle_obstacle(self, x, y, longueur, position_angle=0, longueur_angle=0, direction_angle="haut"):
        for i in range(longueur):
            if 0 <= x + i < self.DIMENSION_MAP[0] and 0 <= y < self.DIMENSION_MAP[1]:
                self.map_data[x + i][y] = 3
        for j in range(longueur_angle):
            if direction_angle == "haut":
                direction = -(j + 1)
            else:
                direction = j + 1
            if 0 <= x + position_angle - 1 < self.DIMENSION_MAP[0] and 0 <= y + direction + 1 < self.DIMENSION_MAP[1]:
                self.map_data[x + position_angle - 1][y + direction] = 3

    def draw_hole(self, x, y, longueur=1, largeur=1):
        for i in range(longueur):
            for j in range(largeur):
                if 0 <= x + i < self.DIMENSION_MAP[0] and 0 <= y + j < self.DIMENSION_MAP[1]:
                    self.map_data[x + i][y + j] = 4

    def draw_map(self, screen):
        for i in range(self.DIMENSION_MAP[0]):
            for j in range(self.DIMENSION_MAP[1]):
                if self.map_data[i][j] == 0:
                    screen.blit(self.petit_graille_image, [i * self.CELL_SIZE, j * self.CELL_SIZE])
                elif self.map_data[i][j] == 1:
                    screen.blit(self.gros_graille_image, [i * self.CELL_SIZE, j * self.CELL_SIZE])
                elif self.map_data[i][j] == 2:
                    screen.blit(self.tile_vide_image, [i * self.CELL_SIZE, j * self.CELL_SIZE])
                elif self.map_data[i][j] == 3:
                    screen.blit(self.tile_image, [i * self.CELL_SIZE, j * self.CELL_SIZE])
                elif self.map_data[i][j] == 4:
                    screen.blit(self.trou_image, [i * self.CELL_SIZE, j * self.CELL_SIZE])
                elif self.map_data[i][j] == 5:
                    screen.blit(self.porte_image, [i * self.CELL_SIZE, j * self.CELL_SIZE])
