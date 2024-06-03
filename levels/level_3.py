# level_3
from levels.level_interface import LevelInterface
from pukmun import Pukmun
from fantomes.fantome_interface import FantomeInterface
from fantomes.fantome_fantome import FantomeFantome


class Level3(LevelInterface):
    def __init__(self, DIMENSION_MAP, CELL_SIZE):
        super().__init__(DIMENSION_MAP, CELL_SIZE)
        self.pukmun = Pukmun([12, 12], CELL_SIZE)
        self.fantomes = [FantomeFantome([self.fantomes_depart[0][0], self.fantomes_depart[0][1]], DIMENSION_MAP, CELL_SIZE), FantomeFantome([self.fantomes_depart[1][0], self.fantomes_depart[1][1]], DIMENSION_MAP, CELL_SIZE), FantomeFantome([self.fantomes_depart[2][0], self.fantomes_depart[2][1]], DIMENSION_MAP, CELL_SIZE), FantomeFantome([self.fantomes_depart[3][0], self.fantomes_depart[3][1]], DIMENSION_MAP, CELL_SIZE)]
        self.fantomes[2].compteur_sortie = 4
        self.fantomes[3].compteur_sortie = 7

        self.fantomes[2].controle = None
        self.fantomes[2].action = None

        self.fantomes[3].controle = None
        self.fantomes[3].action = None

        # Initialiser un tableau de Fantomes, les ajouter avec leurs coordonnées de départ

    def draw_level_on_map(self):
        self.level_map.draw_angle_obstacle(7, 1, 4)
        self.level_map.draw_angle_obstacle(14, 1, 4)

        self.level_map.draw_rectangle_obstacle(2, 2, 2, 2)
        self.level_map.draw_rectangle_obstacle(21, 2, 2, 2)

        self.level_map.draw_angle_obstacle(5, 3, 3, 1, 2)
        self.level_map.draw_angle_obstacle(9, 3, 2, 1, 3, "bas")
        self.level_map.draw_angle_obstacle(14, 3, 2, 2, 3, "bas")
        self.level_map.draw_angle_obstacle(17, 3, 3, 3, 2)

        self.level_map.draw_rectangle_obstacle(2, 5, 3, 3)
        self.level_map.draw_angle_obstacle(6, 5, 2, 1, 2, "bas")
        self.level_map.draw_angle_obstacle(11, 5, 3, 2, 3)
        self.level_map.draw_angle_obstacle(17, 5, 2, 2, 2, "bas")
        self.level_map.draw_rectangle_obstacle(20, 5, 3, 3)

        self.level_map.draw_angle_obstacle(8, 7, 4, 1, 4, "bas")
        self.level_map.draw_angle_obstacle(13, 7, 4, 4, 4, "bas")

        # self.level_map.draw_rectangle_obstacle(6, 9, 1, 5)
        # self.level_map.draw_rectangle_obstacle(18, 9, 1, 5)
        self.level_map.draw_angle_obstacle(6, 9, 1)
        self.level_map.draw_angle_obstacle(18, 9, 1)

        # self.level_map.draw_angle_obstacle(0, 11, 6)
        # self.level_map.draw_angle_obstacle(19, 11, 6)
        self.level_map.draw_angle_obstacle(7, 11, 1)
        self.level_map.draw_angle_obstacle(17, 11, 1)

        self.level_map.draw_rectangle_obstacle(10, 12, 1, 2)
        self.level_map.draw_rectangle_obstacle(14, 12, 1, 2)

        self.level_map.draw_angle_obstacle(6, 13, 1)
        self.level_map.draw_rectangle_obstacle(8, 13, 1, 3)
        self.level_map.draw_rectangle_obstacle(16, 13, 1, 3)
        self.level_map.draw_angle_obstacle(18, 13, 1)

        self.level_map.draw_rectangle_obstacle(1, 14, 2, 3)
        self.level_map.draw_rectangle_obstacle(22, 14, 2, 3)

        self.level_map.draw_angle_obstacle(4, 15, 2)
        self.level_map.draw_angle_obstacle(10, 15, 5, 3, 2)
        self.level_map.draw_angle_obstacle(19, 15, 2)

        self.level_map.draw_angle_obstacle(6, 17, 2, 2, 2)
        self.level_map.draw_angle_obstacle(9, 17, 7, 4, 1)
        self.level_map.draw_angle_obstacle(17, 17, 2, 1, 2)

        self.level_map.draw_rectangle_obstacle(1, 18, 2, 3)
        self.level_map.draw_rectangle_obstacle(12, 18, 1, 2)
        self.level_map.draw_rectangle_obstacle(22, 18, 2, 3)

        self.level_map.draw_angle_obstacle(4, 19, 2, 1, 2)
        self.level_map.draw_angle_obstacle(7, 19, 2, 2, 1, "bas")
        self.level_map.draw_rectangle_obstacle(10, 19, 1, 2)
        # self.level_map.draw_angle_obstacle(7, 19, 3, 3, 1)
        self.level_map.draw_rectangle_obstacle(14, 19, 1, 2)
        self.level_map.draw_angle_obstacle(16, 19, 2, 1, 1, "bas")
        self.level_map.draw_angle_obstacle(19, 19, 2, 2, 2)

        # Gros grailles
        self.level_map.map_data[1][17] = 1
        self.level_map.map_data[23][17] = 1
        self.level_map.map_data[9][8] = 1
        self.level_map.map_data[15][8] = 1
