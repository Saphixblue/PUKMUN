# fantome_fantome.py
from abc import ABC
import random

from fantomes.fantome_interface import FantomeInterface
from sprite_handler import SpriteHandler


# Le fantôme fantôme se déplace lentement de case en case en ignorant les obstacles.
# Il emprunte le chemin le plus court vers PUKMUN
# Lorsqu'il est affaibli, il redevient tangible et fuit PUKMUN dans le labyrinthe.
# Si PUKMUN le mange, celui-ci obtient la faculté de passer à travers les obstacles pendant un moment
# Mort, il rejoint le pit et se reforme


class FantomeFantome(FantomeInterface, ABC):
    def __init__(self, DEPART, DIMENSION_MAP, CELL_SIZE):
        super().__init__(DEPART, DIMENSION_MAP, CELL_SIZE)

        sprite_handler = SpriteHandler(self.CELL_SIZE)

        self.vitesse_vivant = 1.25
        self.vitesse = self.vitesse_vivant


        # TODO: Importer tous les sprites
        self.fantome_fantome_DL_image = sprite_handler.fantome_fantome_DL_image()
        self.fantome_fantome_DR_image = sprite_handler.fantome_fantome_DR_image()
        self.fantome_fantome_L_image = sprite_handler.fantome_fantome_L_image()
        self.fantome_fantome_R_image = sprite_handler.fantome_fantome_R_image()
        self.fantome_fantome_UL_image = sprite_handler.fantome_fantome_UL_image()
        self.fantome_fantome_UR_image = sprite_handler.fantome_fantome_UR_image()

        self.fantome_fantome_weak_blue_L = sprite_handler.fantome_fantome_weak_blue_L_image()
        self.fantome_fantome_weak_blue_R = sprite_handler.fantome_fantome_weak_blue_R_image()

        self.fantome_fantome_weak_white_L = sprite_handler.fantome_fantome_weak_white_L_image()
        self.fantome_fantome_weak_white_R = sprite_handler.fantome_fantome_weak_white_R_image()

        self.fantome_fantome_mort_DL_image = sprite_handler.fantome_fantome_mort_DL_image()
        self.fantome_fantome_mort_DR_image = sprite_handler.fantome_fantome_mort_DR_image()
        self.fantome_fantome_mort_L_image = sprite_handler.fantome_fantome_mort_L_image()
        self.fantome_fantome_mort_R_image = sprite_handler.fantome_fantome_mort_R_image()
        self.fantome_fantome_mort_UL_image = sprite_handler.fantome_fantome_mort_UL_image()
        self.fantome_fantome_mort_UR_image = sprite_handler.fantome_fantome_mort_UR_image()

        self.controle = "LEFT"
        self.sprite = self.fantome_fantome_L_image
        # TODO: Update le sprite
        # self.sprite

        # TODO: Calibrer la collision box
        # self.collision_box
        # self.taille_collision_box

    # TODO: Override toutes les fonctions de l'interface

    def fantome_update_action(self, game_map):
        if self.fantome_check_case():
            if self.weak == 0:
                if self.dead == 0:
                    self.fantome_deplacement(game_map)
                else:
                    self.fantome_deplacement(game_map)
            elif self.weak == 1:
                self.fantome_deplacement_weak(game_map)

        self.fantome_update_coordonnees_pixels(game_map)
        self.fantome_update_case()

    def fantome_update_deplacement(self, game_map):
        if self.action == "LEFT":
            self.fantome_gauche(game_map)
        elif self.action == "RIGHT":
            self.fantome_droite(game_map)
        elif self.action == "DOWN":
            self.fantome_bas(game_map)
        elif self.action == "UP":
            self.fantome_haut(game_map)

    def fantome_deplacement(self, game_map):
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0] and self.coordonnees_cases[1] * self.CELL_SIZE == self.coordonnees_pixels[1]:
            if self.controle == "LEFT":
                self.action = "LEFT"
            elif self.controle == "RIGHT":
                self.action = "RIGHT"
            elif self.controle == "UP":
                self.action = "UP"
            elif self.controle == "DOWN":
                self.action = "DOWN"

    # TODO: Revoir si c'est vraiment nécessaire
    def fantome_deplacement_weak(self, game_map):
        if self.controle == "LEFT":
            if not self.fantome_check_collision_obstacle_left(game_map):
                self.action = "LEFT"
        elif self.controle == "RIGHT":
            if not self.fantome_check_collision_obstacle_right(game_map):
                self.action = "RIGHT"
        elif self.controle == "UP":
            if not self.fantome_check_collision_obstacle_up(game_map):
                self.action = "UP"
        elif self.controle == "DOWN":
            if not self.fantome_check_collision_obstacle_down(game_map):
                self.action = "DOWN"

        '''if self.action == "LEFT":
            if self.fantome_check_collision_obstacle_left(game_map):
                self.action = "STOP"
        elif self.action == "RIGHT":
            if self.fantome_check_collision_obstacle_right(game_map):
                self.action = "STOP"
        elif self.action == "UP":
            if self.fantome_check_collision_obstacle_up(game_map):
                self.action = "STOP"
        elif self.action == "DOWN":
            if self.fantome_check_collision_obstacle_down(game_map):
                self.action = "STOP"'''

    def fantome_deplacement_dead(self, game_map):
        if self.controle == "LEFT":
            if not self.fantome_check_collision_obstacle_left(game_map):
                self.action = "LEFT"
        elif self.controle == "RIGHT":
            if not self.fantome_check_collision_obstacle_right(game_map):
                self.action = "RIGHT"
        elif self.controle == "UP":
            if not self.fantome_check_collision_obstacle_up(game_map):
                self.action = "UP"
        elif self.controle == "DOWN":
            if not self.fantome_check_collision_obstacle_down(game_map):
                self.action = "DOWN"

    def fantome_check_case(self):
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0] and self.coordonnees_cases[1] * self.CELL_SIZE == self.coordonnees_pixels[1]:
            return True
        return False

    def fantome_check_collision_obstacle_left(self, game_map):
        next_x = self.coordonnees_cases[0] - 1 if self.coordonnees_cases[0] != 0 else game_map.DIMENSION_MAP[0] - 1
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0]:
            if game_map.map_data[next_x][self.coordonnees_cases[1]] == 3:
                return True
        return False

    def fantome_check_collision_obstacle_right(self, game_map):
        next_x = self.coordonnees_cases[0] + 1 if self.coordonnees_cases[0] != game_map.DIMENSION_MAP[0] - 1 else 0
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0]:
            if game_map.map_data[next_x][self.coordonnees_cases[1]] == 3:
                return True
        return False

    def fantome_check_collision_obstacle_up(self, game_map):
        next_y = self.coordonnees_cases[1] - 1 if self.coordonnees_cases[1] != 0 else game_map.DIMENSION_MAP[1] - 1
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0]:
            if game_map.map_data[self.coordonnees_cases[0]][next_y] == 3:
                return True
        return False

    def fantome_check_collision_obstacle_down(self, game_map):
        next_y = self.coordonnees_cases[1] + 1 if self.coordonnees_cases[1] != game_map.DIMENSION_MAP[1] - 1 else 0
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0]:
            if game_map.map_data[self.coordonnees_cases[0]][next_y] == 3 or \
                    (self.dead == 0 and game_map.map_data[self.coordonnees_cases[0]][next_y] == 5):
                return True
        return False

    def fantome_gauche(self, game_map):
        self.coordonnees_pixels = [self.coordonnees_pixels[0] - self.vitesse, self.coordonnees_pixels[1]]
        self.direction_sprite = "LEFT"
        self.orientation_sprite = "LEFT"
        self.fantome_update_case()

    def fantome_droite(self, game_map):
        self.coordonnees_pixels = [self.coordonnees_pixels[0] + self.vitesse, self.coordonnees_pixels[1]]
        self.direction_sprite = "RIGHT"
        self.orientation_sprite = "RIGHT"
        self.fantome_update_case()

    def fantome_haut(self, game_map):
        self.coordonnees_pixels = [self.coordonnees_pixels[0], self.coordonnees_pixels[1] - self.vitesse]
        self.direction_sprite = "UP"
        self.fantome_update_case()

    def fantome_bas(self, game_map):
        self.coordonnees_pixels = [self.coordonnees_pixels[0], self.coordonnees_pixels[1] + self.vitesse]
        self.direction_sprite = "DOWN"
        self.fantome_update_case()

    def fantome_update_case(self):
        if self.coordonnees_pixels[0] % self.CELL_SIZE == 0:
            self.coordonnees_cases[0] = int(self.coordonnees_pixels[0]) // self.CELL_SIZE
        if self.coordonnees_pixels[1] % self.CELL_SIZE == 0:
            self.coordonnees_cases[1] = int(self.coordonnees_pixels[1]) // self.CELL_SIZE

    def fantome_update_coordonnees_pixels(self, game_map):
        if self.coordonnees_pixels[0] < 0:
            self.coordonnees_pixels[0] = (game_map.DIMENSION_MAP[0] - 1) * self.CELL_SIZE + self.vitesse
        elif self.coordonnees_pixels[0] > (game_map.DIMENSION_MAP[0] - 1) * self.CELL_SIZE:
            self.coordonnees_pixels[0] = 0 - self.vitesse

        if self.coordonnees_pixels[1] < 0:
            self.coordonnees_pixels[1] = (game_map.DIMENSION_MAP[1] - 1) * self.CELL_SIZE + self.vitesse
        elif self.coordonnees_pixels[1] > (game_map.DIMENSION_MAP[1] - 1) * self.CELL_SIZE:
            self.coordonnees_pixels[1] = 0 - self.vitesse

    # TODO: Gestion sprites weak et dead
    # TODO: Update collision box ici
    def fantome_update_sprite(self, frame, compteur):
        if self.weak == 0:
            if self.dead == 0:
                if self.direction_sprite == "LEFT":
                    self.sprite = self.fantome_fantome_L_image
                elif self.direction_sprite == "RIGHT":
                    self.sprite = self.fantome_fantome_R_image
                elif self.direction_sprite == "UP":
                    if self.orientation_sprite == "LEFT":
                        self.sprite = self.fantome_fantome_UL_image
                    elif self.orientation_sprite == "RIGHT":
                        self.sprite = self.fantome_fantome_UR_image
                elif self.direction_sprite == "DOWN":
                    if self.orientation_sprite == "LEFT":
                        self.sprite = self.fantome_fantome_DL_image
                    elif self.orientation_sprite == "RIGHT":
                        self.sprite = self.fantome_fantome_DR_image
            elif self.dead == 1:
                if self.direction_sprite == "LEFT":
                    self.sprite = self.fantome_fantome_mort_L_image
                elif self.direction_sprite == "RIGHT":
                    self.sprite = self.fantome_fantome_mort_R_image
                elif self.direction_sprite == "UP":
                    if self.orientation_sprite == "LEFT":
                        self.sprite = self.fantome_fantome_mort_UL_image
                    elif self.orientation_sprite == "RIGHT":
                        self.sprite = self.fantome_fantome_mort_UR_image
                elif self.direction_sprite == "DOWN":
                    if self.orientation_sprite == "LEFT":
                        self.sprite = self.fantome_fantome_mort_DL_image
                    elif self.orientation_sprite == "RIGHT":
                        self.sprite = self.fantome_fantome_mort_DR_image
        elif self.weak == 1:
            if self.orientation_sprite == "LEFT":
                if compteur > 2:
                    # 2 dernières secondes du compteur = clignote
                    self.sprite = self.fantome_fantome_weak_blue_L
                else:
                    if 0 <= frame < 30:
                        self.sprite = self.fantome_fantome_weak_blue_L
                    else:
                        self.sprite = self.fantome_fantome_weak_white_L
            elif self.orientation_sprite == "RIGHT":
                if compteur > 2:
                    # 2 dernières secondes du compteur = clignote
                    self.sprite = self.fantome_fantome_weak_blue_R
                else:
                    if 0 <= frame < 30:
                        self.sprite = self.fantome_fantome_weak_blue_R
                    else:
                        self.sprite = self.fantome_fantome_weak_white_R

    def fantome_comportement(self, game_map, pukmun_coordonnees_cases):
        if self.weak == 0:
            if self.dead == 1:
                self.fantome_comportement_dead(game_map)
                self.vitesse = self.vitesse_mort
            else:
                self.vitesse = self.vitesse_vivant
                x_diff = self.coordonnees_cases[0] - pukmun_coordonnees_cases[0]
                y_diff = self.coordonnees_cases[1] - pukmun_coordonnees_cases[1]

                left = 0
                right = 0
                up = 0
                down = 0

                if x_diff > 0:
                    left = x_diff
                    right = self.DIMENSION_MAP[0] - x_diff
                elif x_diff < 0:
                    left = self.DIMENSION_MAP[0] + x_diff
                    right = -x_diff
                else:
                    left = self.DIMENSION_MAP[0] - 1
                    right = self.DIMENSION_MAP[0] - 1  # Si le fantôme atteint la coordonnée de PUKMUN, on le force à bouger selon l'autre axe

                if y_diff > 0:
                    up = y_diff
                    down = self.DIMENSION_MAP[1] - y_diff
                elif y_diff < 0:
                    up = self.DIMENSION_MAP[1] + y_diff
                    down = -y_diff
                else:
                    up = self.DIMENSION_MAP[1] - 1
                    down = self.DIMENSION_MAP[1] - 1

                if self.action == "LEFT":
                    right = 99
                if self.action == "RIGHT":
                    left = 99
                if self.action == "UP":
                    down = 99
                if self.action == "DOWN":
                    up = 99

                if min(left, right, up, down) == left:
                    self.controle = "LEFT"
                if min(left, right, up, down) == right:
                    self.controle = "RIGHT"
                if min(left, right, up, down) == up:
                    self.controle = "UP"
                if min(left, right, up, down) == down:
                    self.controle = "DOWN"

                rdm = random.random()

                if self.controle == "LEFT" or self.controle == "RIGHT":
                    if rdm < 0.05:
                        self.controle = "UP"
                    elif rdm < 0.10:
                        self.controle = "DOWN"
                elif self.controle == "UP" or self.controle == "DOWN":
                    if rdm < 0.05:
                        self.controle = "LEFT"
                    elif rdm < 0.10:
                        self.controle = "RIGHT"
        else:
            self.vitesse = self.vitesse_weak
            self.fantome_comportement_weak(game_map, pukmun_coordonnees_cases)

    def fantome_comportement_weak(self, game_map, pukmun_coordonnees_cases):
        x_diff = self.coordonnees_cases[0] - pukmun_coordonnees_cases[0]
        y_diff = self.coordonnees_cases[1] - pukmun_coordonnees_cases[1]

        left = 0
        right = 0
        up = 0
        down = 0

        if x_diff > 0:
            left = x_diff
            if self.coordonnees_cases[1] == 11:
                right = self.DIMENSION_MAP[0] - x_diff
            else:
                right = self.DIMENSION_MAP[0] + self.coordonnees_cases[0]
        elif x_diff < 0:
            if self.coordonnees_cases[1] == 11:
                left = self.DIMENSION_MAP[0] + x_diff
            else:
                left = self.DIMENSION_MAP[0] + self.coordonnees_cases[0]
            right = -x_diff
        else:
            left = self.DIMENSION_MAP[0] + self.coordonnees_cases[0]
            right = self.DIMENSION_MAP[0] + self.coordonnees_cases[0] # Si le fantôme atteint la coordonnée de PUKMUN, on le force à bouger selon l'autre axe

        if y_diff > 0:
            up = y_diff
            down = self.DIMENSION_MAP[1] + self.coordonnees_cases[1]
        elif y_diff < 0:
            up = self.DIMENSION_MAP[1] + self.coordonnees_cases[1]
            down = -y_diff
        else:
            up = self.DIMENSION_MAP[1] + self.coordonnees_cases[1]
            down = self.DIMENSION_MAP[1] + self.coordonnees_cases[1]

        # On encourage le fantôme à continuer sur sa lancée s'il n'y a pas d'intersection

        if self.action == "LEFT" and self.fantome_check_collision_obstacle_up(game_map) and self.fantome_check_collision_obstacle_down(game_map):
            left = 100
        elif self.action == "RIGHT" and self.fantome_check_collision_obstacle_up(game_map) and self.fantome_check_collision_obstacle_down(game_map):
            right = 100
        elif self.action == "UP" and self.fantome_check_collision_obstacle_left(game_map) and self.fantome_check_collision_obstacle_right(game_map):
            up = 100
        elif self.action == "DOWN" and self.fantome_check_collision_obstacle_left(game_map) and self.fantome_check_collision_obstacle_right(game_map):
            down = 100

        if self.fantome_check_collision_obstacle_left(game_map):
            left = -1
            if self.action == "LEFT":
                right = 0
        if self.fantome_check_collision_obstacle_right(game_map):
            right = -1
            if self.action == "RIGHT":
                left = 0
        if self.fantome_check_collision_obstacle_up(game_map):
            up = -1
            if self.action == "UP":
                down = 0
        if self.fantome_check_collision_obstacle_down(game_map):
            down = -1
            if self.action == "DOWN":
                up = 0

        if max(left, right, up, down) == left:
            self.controle = "LEFT"
        if max(left, right, up, down) == right:
            self.controle = "RIGHT"
        if max(left, right, up, down) == up:
            self.controle = "UP"
        if max(left, right, up, down) == down:
            self.controle = "DOWN"

    def fantome_comportement_dead(self, game_map):
        x_diff = self.coordonnees_cases[0] - 12
        y_diff = self.coordonnees_cases[1] - 10

        left = 98
        right = 98
        up = 98
        down = 98

        # Calcul des distances pour les mouvements horizontaux
        if x_diff > 0:
            left = x_diff
            if self.coordonnees_cases[1] == 11:
                right = self.DIMENSION_MAP[0] - x_diff
            '''else:
                right = self.DIMENSION_MAP[0] + self.coordonnees_cases[0]'''
        elif x_diff < 0:
            if self.coordonnees_cases[1] == 11:
                left = self.DIMENSION_MAP[0] + x_diff
            '''else:
                left = self.DIMENSION_MAP[0] + self.coordonnees_cases[0]'''
            right = -x_diff
        '''else:
            left = right = self.DIMENSION_MAP[0] + self.coordonnees_cases[0]'''  # Si sur la même colonne, éviter mouvement horizontal

        # Calcul des distances pour les mouvements verticaux
        if y_diff > 0:
            up = y_diff
            '''down = self.DIMENSION_MAP[1] + self.coordonnees_cases[1]'''
        elif y_diff < 0:
            '''up = self.DIMENSION_MAP[1] + self.coordonnees_cases[1]'''
            down = -y_diff
        '''else:
            up = down = self.DIMENSION_MAP[1] + self.coordonnees_cases[1]'''  # Si sur la même ligne, éviter mouvement vertical

        # Encourager la direction actuelle
        if self.action == "LEFT":
            left = 97
            right = 99
        elif self.action == "RIGHT":
            right = 97
            left = 99
        elif self.action == "UP":
            up = 97
            down = 99
        elif self.action == "DOWN":
            down = 97
            up = 99

        # self.fantome_update_action(game_map)

        # Vérifier les collisions avec les obstacles
        if self.fantome_check_collision_obstacle_left(game_map):
            left = 100
        if self.fantome_check_collision_obstacle_right(game_map):
            right = 100
        if self.fantome_check_collision_obstacle_up(game_map):
            up = 100
        if self.fantome_check_collision_obstacle_down(game_map):
            down = 100

        # Choisir la direction avec la plus petite distance
        min_distance = min(left, right, up, down)
        if min_distance == left:
            self.controle = "LEFT"
        elif min_distance == right:
            self.controle = "RIGHT"
        elif min_distance == up:
            self.controle = "UP"
        elif min_distance == down:
            self.controle = "DOWN"

    def fantome_check_collision_pukmun(self, game_map, pukmun_coordonnees_pixels):
        x_diff = self.coordonnees_pixels[0] - pukmun_coordonnees_pixels[0]
        y_diff = self.coordonnees_pixels[1] - pukmun_coordonnees_pixels[1]

        collision_horizontale = False
        collision_verticale = False

        if x_diff > 0:
            if self.orientation_sprite == "LEFT":
                if (self.coordonnees_pixels[0] + self.CELL_SIZE/20) <= (pukmun_coordonnees_pixels[0] + self.CELL_SIZE - self.CELL_SIZE/10) <= (self.coordonnees_pixels[0] + self.CELL_SIZE - self.CELL_SIZE/5):
                    collision_horizontale = True
            elif self.orientation_sprite == "RIGHT":
                if (self.coordonnees_pixels[0] + self.CELL_SIZE / 5) <= (pukmun_coordonnees_pixels[0] + self.CELL_SIZE - self.CELL_SIZE / 10) <= (self.coordonnees_pixels[0] + self.CELL_SIZE - self.CELL_SIZE / 20):
                    collision_horizontale = True
        elif x_diff < 0:
            if self.orientation_sprite == "LEFT":
                if (self.coordonnees_pixels[0] + self.CELL_SIZE / 20) <= (pukmun_coordonnees_pixels[0] + self.CELL_SIZE / 10) <= (self.coordonnees_pixels[0] + self.CELL_SIZE - self.CELL_SIZE / 5):
                    collision_horizontale = True
            elif self.orientation_sprite == "RIGHT":
                if (self.coordonnees_pixels[0] + self.CELL_SIZE / 5) <= (pukmun_coordonnees_pixels[0] + self.CELL_SIZE / 10) <= (self.coordonnees_pixels[0] + self.CELL_SIZE - self.CELL_SIZE / 20):
                    collision_horizontale = True
        else:
            collision_horizontale = True

        if y_diff > 0:
            if (self.coordonnees_pixels[1] + ((3*self.CELL_SIZE)/20)) <= (pukmun_coordonnees_pixels[1] + self.CELL_SIZE - self.CELL_SIZE / 10) <= (self.coordonnees_pixels[1] + self.CELL_SIZE - self.CELL_SIZE / 10):
                collision_verticale = True
        elif y_diff < 0:
            if (self.coordonnees_pixels[1] + ((3*self.CELL_SIZE)/20)) <= (pukmun_coordonnees_pixels[1] + self.CELL_SIZE / 10) <= (self.coordonnees_pixels[1] + self.CELL_SIZE - self.CELL_SIZE / 10):
                collision_verticale = True
        else:
            collision_verticale = True

        if collision_horizontale and collision_verticale:
            return True
        return False

