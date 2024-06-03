# level_2
from levels.level_interface import LevelInterface
from pukmun import Pukmun
from fantomes.fantome_interface import FantomeInterface
from fantomes.fantome_fantome import FantomeFantome


class Level2(LevelInterface):
    def __init__(self, DIMENSION_MAP, CELL_SIZE):
        super().__init__(DIMENSION_MAP, CELL_SIZE)
        self.pukmun = Pukmun([12, 12], CELL_SIZE)
        # self.fantomes =
        # Initialiser un tableau de Fantomes, les ajouter avec leurs coordonnées de départ
        self.fantomes = [
            FantomeFantome([self.fantomes_depart[0][0], self.fantomes_depart[0][1]], DIMENSION_MAP, CELL_SIZE),
            FantomeFantome([self.fantomes_depart[1][0], self.fantomes_depart[1][1]], DIMENSION_MAP, CELL_SIZE),
            FantomeFantome([self.fantomes_depart[2][0], self.fantomes_depart[2][1]], DIMENSION_MAP, CELL_SIZE),
            FantomeFantome([self.fantomes_depart[3][0], self.fantomes_depart[3][1]], DIMENSION_MAP, CELL_SIZE)]

        self.fantomes[2].compteur_sortie = 4
        self.fantomes[3].compteur_sortie = 7

        self.fantomes[2].controle = None
        self.fantomes[2].action = None

        self.fantomes[3].controle = None
        self.fantomes[3].action = None

    def draw_level_on_map(self):
        self.level_map.draw_angle_obstacle(2, 2, 7, 1, 1, "bas")
        self.level_map.draw_rectangle_obstacle(10, 2, 5, 2)
        self.level_map.draw_angle_obstacle(16, 2, 7, 7, 1, "bas")

        self.level_map.draw_angle_obstacle(4, 4, 5, 1, 1, "bas")
        self.level_map.draw_angle_obstacle(16, 4, 5, 5, 1, "bas")

        self.level_map.draw_angle_obstacle(6, 5, 3, 3, 2, "bas")
        self.level_map.draw_angle_obstacle(10, 5, 5)
        self.level_map.draw_angle_obstacle(16, 5, 3, 1, 2, "bas")

        self.level_map.draw_angle_obstacle(2, 7, 5, 1, 2)
        self.level_map.draw_angle_obstacle(10, 7, 5)
        self.level_map.draw_angle_obstacle(18, 7, 5, 5, 2)

        self.level_map.draw_rectangle_obstacle(7, 9, 1, 5)
        self.level_map.draw_rectangle_obstacle(17, 9, 1, 5)

        self.level_map.draw_angle_obstacle(9, 13, 7)

        self.level_map.draw_angle_obstacle(2, 15, 3, 1, 1, "bas")
        self.level_map.draw_angle_obstacle(6, 15, 6, 3, 4, "bas")
        self.level_map.draw_angle_obstacle(13, 15, 6, 4, 4, "bas")
        self.level_map.draw_angle_obstacle(20, 15, 3, 3, 1, "bas")

        self.level_map.draw_angle_obstacle(4, 17, 3, 3, 2, "bas")
        self.level_map.draw_angle_obstacle(12, 17, 1)
        self.level_map.draw_angle_obstacle(18, 17, 3, 1, 2, "bas")

        self.level_map.draw_angle_obstacle(2, 19, 3, 1, 1)
        self.level_map.draw_angle_obstacle(10, 19, 2, 1, 2)
        self.level_map.draw_angle_obstacle(13, 19, 2, 2, 2)
        self.level_map.draw_angle_obstacle(20, 19, 3, 3, 1)

        # Gros grailles
        self.level_map.map_data[5][5] = 1
        self.level_map.map_data[19][5] = 1
        self.level_map.map_data[7][16] = 1
        self.level_map.map_data[17][16] = 1