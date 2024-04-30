# map.py

class Map:
    def __init__(self, DIMENSION_MAP, CELL_SIZE):

        self.DIMENSION_MAP = DIMENSION_MAP
        self.CELL_SIZE = CELL_SIZE
        self.WINDOW_SIZE = (self.DIMENSION_MAP[0]*self.CELL_SIZE, self.DIMENSION_MAP[1]*self.CELL_SIZE)

        # Création de la carte avec des cases vides par défaut
        self.map_data = [[0 for _ in range(self.DIMENSION_MAP[0])] for _ in range(self.DIMENSION_MAP[1])]

    def draw_rectangle_obstacle(self, x, y, longueur, largeur):
        for i in range(longueur):
            for j in range(largeur):
                if 0 <= x + i < self.DIMENSION_MAP[0] and 0 <= y + j < self.DIMENSION_MAP[1]:
                    self.map_data[x + i][y + j] = 3

    def draw_angle_obstacle(self, x, y, longueur, position_angle, longueur_angle, direction_angle):
        for i in range(longueur):
            if 0 <= x + i < self.DIMENSION_MAP[0] and 0 <= y < self.DIMENSION_MAP[1]:
                self.map_data[x + i][y] = 3
        for j in range(longueur_angle):
            if direction_angle == "haut":
                direction = -j
            else:
                direction = j
            if 0 <= x + position_angle - 1 < self.DIMENSION_MAP[0] and 0 <= y + direction + 1 < self.DIMENSION_MAP[1]:
                self.map_data[x + position_angle - 1][y + direction + 1] = 3
