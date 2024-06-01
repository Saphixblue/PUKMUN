# level_interface
from abc import ABC, abstractmethod


class FantomeInterface(ABC):
    def __init__(self, DEPART, DIMENSION_MAP, CELL_SIZE):
        self.DEPART = DEPART
        self.DIMENSION_MAP = DIMENSION_MAP
        self.CELL_SIZE = CELL_SIZE
        self.coordonnees_cases = DEPART
        self.coordonnees_pixels = [DEPART[0] * self.CELL_SIZE, DEPART[1] * self.CELL_SIZE]
        self.vitesse = 2.5

        self.controle = "NONE"
        self.action = "NONE"

        self.orientation_sprite = "NONE"
        self.direction_sprite = "NONE"

        self.weak = 0
        self.dead = 0

        self.sprite = None

        self.collision_box = None
        self.taille_collision_box = None

        self.compteur_sortie = 0
        self.compteur_frame_sortie = 59

        self.compteur_weak_mort = 0
        self.compteur_frame_weak_mort = 59

    # Appelle fantome_deplacement() si sur une case, puis update coordonnees et case
    @abstractmethod
    def fantome_update_action(self, game_map):
        pass

    # Appelle les fonctions de déplacement en fonction de la valeur de action
    @abstractmethod
    def fantome_update_deplacement(self, game_map):
        pass

    # Update action en fonction du controle ( ATTENTION sûrement pas nécessaire si géré dans comportement)
    @abstractmethod
    def fantome_deplacement(self, game_map):
        pass

    def fantome_deplacement_weak(self, game_map):
        pass

    # Renvoie True si sur une case
    @abstractmethod
    def fantome_check_case(self):
        pass

    # Renvoie True si obstacle sur case gauche
    @abstractmethod
    def fantome_check_collision_obstacle_left(self, game_map):
        pass

    # Renvoie True si obstacle sur case droite
    @abstractmethod
    def fantome_check_collision_obstacle_right(self, game_map):
        pass

    # Renvoie True si obstacle sur case haut
    @abstractmethod
    def fantome_check_collision_obstacle_up(self, game_map):
        pass

    # Renvoie True si obstacle sur case bas
    @abstractmethod
    def fantome_check_collision_obstacle_down(self, game_map):
        pass

    # Fait aller le fantôme vers la gauche, update direction et orientation sprite en fonction, et update case
    @abstractmethod
    def fantome_gauche(self, game_map):
        pass

    # Fait aller le fantôme vers la droite, update direction et orientation sprite en fonction, et update case
    @abstractmethod
    def fantome_droite(self, game_map):
        pass

    # Fait aller le fantôme vers le haut, update direction et orientation sprite en fonction, et update case
    @abstractmethod
    def fantome_haut(self, game_map):
        pass

    # Fait aller le fantôme vers le bas, update direction et orientation sprite en fonction, et update case
    @abstractmethod
    def fantome_bas(self, game_map):
        pass

    # Si le fantôme est sur une case, update coordonnees_cases
    @abstractmethod
    def fantome_update_case(self):
        pass

    # Permet au fantôme de naviger d'un bord à l'autre de l'écran en sortant de la map
    @abstractmethod
    def fantome_update_coordonnees_pixels(self, game_map):
        pass

    # Update le sprite du fantôme en fonction de son état, son orientation et sa direction
    @abstractmethod
    def fantome_update_sprite(self):
        pass

    # Détaille le comportement général du fantôme (appelle les autres fonctions comportement en fonction de l'état du fantôme)
    @abstractmethod
    def fantome_comportement(self, game_map, pukmun_coordonnees_cases):
        pass

    # Détaille le comportement du fantôme lorsqu'il est affaibli
    @abstractmethod
    def fantome_comportement_weak(self, game_map):
        pass

    # Détaille le comportement du fantôme lorsqu'il est mort
    @abstractmethod
    def fantome_comportement_dead(self, game_map):
        pass

    @abstractmethod
    def fantome_check_collision_pukmun(self, game_map, pukmun_coordonnees_pixels):
        pass

