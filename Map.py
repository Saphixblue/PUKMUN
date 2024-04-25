# map.py
import pygame as pg

class Map:
    def __init__(self, window_size, cell_size):
        self.window_size = window_size
        self.cell_size = cell_size
        self.rows = window_size[1] // cell_size
        self.cols = window_size[0] // cell_size

        # Création de la carte avec des cases vides par défaut
        self.map_data = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def draw_map(self, screen):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.map_data[i][j] == 3:
                    # Dessiner un mur (obstacle)
                    obstacle_rect = pg.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                    pg.draw.rect(screen, (255, 255, 255), obstacle_rect)

    def draw_rectangle_obstacle(self, x, y, longueur, largeur):
        for i in range(longueur):
            for j in range(largeur):
                if 0 <= x + i < self.rows and 0 <= y + j < self.cols:
                    self.map_data[x + i][y + j] = 3

    def draw_angle_obstacle(self, x, y, longueur, position_angle, longueur_angle, direction_angle):
        for i in range(longueur):
            if 0 <= x + i < self.rows and 0 <= y < self.cols:
                self.map_data[x + i][y] = 3
        for j in range(longueur_angle):
            if direction_angle == "haut":
                direction = -j
            else:
                direction = j
            if 0 <= x + position_angle - 1 < self.rows and 0 <= y + direction + 1 < self.cols:
                self.map_data[x + position_angle - 1][y + direction + 1] = 3