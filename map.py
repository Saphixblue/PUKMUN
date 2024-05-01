# map.py
import pygame as pg
import game


class Map:
    def __init__(self, window_size, cell_size):
        self.window_size = window_size
        self.cell_size = cell_size
        self.cols = window_size[0] // cell_size[0]
        self.rows = window_size[1] // cell_size[1]
        
        # Création de la carte avec des cases vides par défaut
        self.map_data = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def draw_map(self, screen):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.map_data[i][j] == 3:
                    # Dessiner un mur (obstacle)

                    screen.blit(game.obstacle, [j * self.cell_size[0], i * self.cell_size[1]])
                    #obstacle_rect = pg.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                    '''pg.draw.rect(screen, (255, 255, 255), obstacle_rect)
                    '''

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



'''
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
'''




'''
import pygame as pg
import os

class Map:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.map = self.generate_map()
    
    def generate_map(self):
        """
        Generate the map layout with obstacles and other elements.
        """
        # Define map dimensions and cell size
        map_width = 23
        map_height = 20
        cell_size = 32  # Adjust this value as needed
        
        # Create an empty map
        map_layout = [[0] * map_width for _ in range(map_height)]
        
        # Add boundaries (obstacles) around the map
        for i in range(map_width):
            map_layout[0][i] = 3
            map_layout[map_height - 1][i] = 3
        for j in range(map_height):
            map_layout[j][0] = 3
            map_layout[j][map_width - 1] = 3
        
        # Add other elements to the map (e.g., points, bonuses, etc.)
        # You can add your logic here
        
        return map_layout

    def draw_map(self, screen):
        """
        Draw the map on the screen.
        """
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                # Draw obstacles and other elements based on cell values
                if cell == 3:
                    # Draw an obstacle
                    obstacle_rect = pg.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                    pg.draw.rect(screen, (0, 0, 255), obstacle_rect)  # Blue color for obstacles
                # Add conditions for drawing other elements
                
    def place_obstacle(self, x, y, obstacle_type):
        """
        Place an obstacle on the map at the specified position.
        """
        # Add logic to place different types of obstacles
        pass
'''
