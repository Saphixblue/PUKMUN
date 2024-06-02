# fantome_ivre.py
from fantomes.fantome_interface import FantomeInterface
from sprite_handler import SpriteHandler


# Le fantôme ivre se déplace aléatoirement dans le labyrinthe. (Comment exactement ? Peut-il revenir sur ses pas ? Si oui, quand ?)

# Lorsqu'il voit PUKMUN, il lui fonce dessus à pleine vitesse.
# S'il ne tue pas PUKMUN, il continue sa charge jusqu'à rencontrer un obstacle.
# Il la reprend s'il voit PUKMUN, sinon il reprendra ses déplacements aléatoires

# Lorsqu'il est affaibli, il ne change pas son comportement.
# Le manger donnera le statut "ivre" à PUKMUN (géré dans game), ce qui inverse ses contrôles (géré dans pukmun)

# Pour l'éliminer, passer dessus lorsqu'il est affaibli

# Mort, il rejoint le pit et se reforme


class FantomeIvre(FantomeInterface):
    def __init__(self, DEPART, DIMENSION_MAP, CELL_SIZE):
        super().__init__(DEPART, DIMENSION_MAP, CELL_SIZE)

        sprite_handler = SpriteHandler(self.CELL_SIZE)

        self.fantome_ivre_DL_image = sprite_handler.fantome_ivre_DL_image()
        self.fantome_ivre_DR_image = sprite_handler.fantome_ivre_DR_image()
        self.fantome_ivre_L_image = sprite_handler.fantome_ivre_L_image()
        self.fantome_ivre_R_image = sprite_handler.fantome_ivre_R_image()
        self.fantome_ivre_UL_image = sprite_handler.fantome_ivre_UL_image()
        self.fantome_ivre_UR_image = sprite_handler.fantome_ivre_UR_image()

        self.fantome_ivre_nrv_DL_image = sprite_handler.fantome_ivre_nrv_DL_image()
        self.fantome_ivre_nrv_DR_image = sprite_handler.fantome_ivre_nrv_DR_image()
        self.fantome_ivre_nrv_L_image = sprite_handler.fantome_ivre_nrv_L_image()
        self.fantome_ivre_nrv_R_image = sprite_handler.fantome_ivre_nrv_R_image()
        self.fantome_ivre_nrv_UL_image = sprite_handler.fantome_ivre_nrv_UL_image()
        self.fantome_ivre_nrv_UR_image = sprite_handler.fantome_ivre_nrv_UR_image()

        self.fantome_ivre_weak_blue_L_image = sprite_handler.fantome_ivre_weak_blue_L_image()
        self.fantome_ivre_weak_blue_R_image = sprite_handler.fantome_ivre_weak_blue_R_image()
        self.fantome_ivre_weak_white_L_image = sprite_handler.fantome_ivre_weak_white_L_image()
        self.fantome_ivre_weak_white_R_image = sprite_handler.fantome_ivre_weak_white_R_image()

        self.fantome_ivre_mort_DL_image = sprite_handler.fantome_ivre_mort_DL_image()
        self.fantome_ivre_mort_DR_image = sprite_handler.fantome_ivre_mort_DR_image()
        self.fantome_ivre_mort_L_image = sprite_handler.fantome_ivre_mort_L_image()
        self.fantome_ivre_mort_R_image = sprite_handler.fantome_ivre_mort_R_image()
        self.fantome_ivre_mort_UL_image = sprite_handler.fantome_ivre_mort_UL_image()
        self.fantome_ivre_mort_UR_image = sprite_handler.fantome_ivre_mort_UR_image()

        self.sprite = self.fantome_ivre_DL_image

        # TODO: Calibrer la collision box
        # self.collision_box

        self.rage = 0
        self.vitesse_rage = 2 * self.vitesse

    # TODO: Override toutes les méthodes de l'interface

    def fantome_update_action(self, game_map):
        print("Fantôme Update Action")

    def fantome_update_deplacement(self, game_map):
        print("Fantôme Update Déplacement")

    def fantome_deplacement(self, game_map):
        print("Fantôme Déplacement")

    def fantome_check_case(self):
        print("Fantôme Check Case")

    def fantome_check_collision_obstacle_left(self, game_map):
        print("Fantôme Check Collision Obstacle Left")

    def fantome_check_collision_obstacle_right(self, game_map):
        print("Fantôme Check Collision Obstacle Right")

    def fantome_check_collision_obstacle_up(self, game_map):
        print("Fantôme Check Collision Obstacle Up")

    def fantome_check_collision_obstacle_down(self, game_map):
        print("Fantôme Check Collision Obstacle Down")

    def fantome_gauche(self, game_map):
        print("Fantôme Gauche")

    def fantome_droite(self, game_map):
        print("Fantôme Droite")

    def fantome_haut(self, game_map):
        print("Fantôme Haut")

    def fantome_bas(self, game_map):
        print("Fantôme Bas")

    def fantome_update_case(self):
        print("Fantôme Update Case")

    def fantome_update_coordonnees_pixels(self, game_map):
        print("Fantôme Update Coordonnées Pixels")

    def fantome_update_sprite(self):
        print("Fantôme Update Sprite")

    def fantome_comportement(self, game_map):
        print("Fantôme Comportement")

    def fantome_comportement_weak(self, game_map):
        print("Fantôme Comportement Weak")

    def fantome_comportement_dead(self, game_map):
        print("Fantôme Comportement Dead")

    # TODO
    # Détaille le comportement du fantôme quand il est enragé
    def comportement_rage(self, game_map):
        if self.action == "LEFT":
            if not self.fantome_check_collision_obstacle_left(game_map):
                self.controle = "LEFT"
            else:
                self.rage = 0
        if self.action == "RIGHT":
            if not self.fantome_check_collision_obstacle_right(game_map):
                self.controle = "RIGHT"
            else:
                self.rage = 0
        if self.action == "UP":
            if not self.fantome_check_collision_obstacle_up(game_map):
                self.controle = "UP"
            else:
                self.rage = 0
        if self.action == "DOWN":
            if not self.fantome_check_collision_obstacle_down(game_map):
                self.controle = "DOWN"
            else:
                self.rage = 0

    # TODO (Doit sûrement être basculée dans game)
    # Renvoie True si PUKMUN est sur la même ligne ou colonne sans obstacle entre eux
    def voit_pukmun(self, game_map):
        print("Voit PUKMUN")
