# level_interface
from abc import ABC, abstractmethod
from map import Map

# Pour des niveaux de 25*22 cases
class LevelInterface(ABC):
    def __init__(self, DIMENSION_MAP, CELL_SIZE):
        self.level_map = Map(DIMENSION_MAP, CELL_SIZE)
        self.pukmun = None
        self.fantomes = None

        # TODO: Renseigner les coordonnées de départ des fantômes dans leur ordre de sortie
        # self.depart_fantome_1
        # self.depart_fantome_2
        # self.depart_fantome_3
        # self.depart_fantome_4

        # Dessin du pit des fantômes
        self.level_map.draw_angle_obstacle(9, 9, 3, 1, 2, "bas")
        self.level_map.draw_angle_obstacle(10, 11, 6, 6, 2, "haut")
        self.level_map.draw_rectangle_obstacle(13, 9, 2, 1)

        # Vidange du pit des fantômes
        for i in range(5):
            self.level_map.map_data[10 + i][10] = 2

        # Porte du pit des fantômes
        self.level_map.map_data[12][9] = 5

        # Dessin des murs
        self.level_map.draw_rectangle_obstacle(0, 0, 25, 1)
        self.level_map.draw_rectangle_obstacle(0, 21, 25, 1)
        self.level_map.draw_rectangle_obstacle(24, 1, 1, 10)
        self.level_map.draw_rectangle_obstacle(0, 1, 1, 10)
        self.level_map.draw_rectangle_obstacle(0, 12, 1, 9)
        self.level_map.draw_rectangle_obstacle(24, 12, 1, 9)
        self.level_map.draw_rectangle_obstacle(1, 9, 5, 2)
        self.level_map.draw_rectangle_obstacle(1, 12, 5, 2)
        self.level_map.draw_rectangle_obstacle(19, 9, 5, 2)
        self.level_map.draw_rectangle_obstacle(19, 12, 5, 2)

    @abstractmethod
    def draw_level_on_map(self):
        pass