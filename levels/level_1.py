# level_1
from Map import Map
from pukmun import Pukmun


class Level1:
    def __init__(self, DIMENSION_MAP, CELL_SIZE):
        self.level_1_map = Map(DIMENSION_MAP, CELL_SIZE)
        self.pukmun = Pukmun([0, 10], CELL_SIZE)
        # self.enemies =
        # Initialiser un tableau de Fantomes

    def draw_level_on_map(self):
        # Mettre en place un obstacle sur la carte
        self.level_1_map.draw_rectangle_obstacle(5, 10, 5,
                                              1)  # Dessine un rectangle à la case (10;10) longueur 5, largeur 1
        self.level_1_map.draw_angle_obstacle(2, 2, 3, 2, 1,
                                          "bas")  # dessin angle en (2,2); longueur 3; position angle 2, longueurangle 1; position "bas"
        self.level_1_map.draw_angle_obstacle(10, 20, 3, 2, 3,
                                          "haut")  # dessin angle en (2,2); longueur 3; position angle 2, longueurangle 1; position "bas"
        self.level_1_map.draw_rectangle_obstacle(0, 0, 2, 1)
        self.level_1_map.draw_rectangle_obstacle(12, 9, 1, 9)
        self.level_1_map.draw_rectangle_obstacle(14, 9, 1, 8)
        self.level_1_map.draw_rectangle_obstacle(1, 9, 1, 8)
        # self.game_map.draw_rectangle_obstacle(12, 9, 1, 9)
        # game_map.draw_rectangle_obstacle(0, 0, 30,30)  # Dessine un rectangle à la case (10;10) longueur 5, largeur 1
