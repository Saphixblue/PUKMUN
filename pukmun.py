# pukmun.py
from sprite_handler import SpriteHandler


class Pukmun:
    def __init__(self, DEPART, CELL_SIZE):
        self.DEPART = DEPART
        self.CELL_SIZE = CELL_SIZE

        self.coordonnees_cases = DEPART
        self.coordonnees_pixels = [DEPART[0] * self.CELL_SIZE, DEPART[1] * self.CELL_SIZE]

        self.vitesse = 2.5  # En pixels/frame

        self.controle = "LEFT"
        self.action = "LEFT"

        self.orientation_sprite = "LEFT"  # facing
        self.direction_sprite = "LEFT"  # deplacement

        self.powered = 0
        self.fantome = 0
        self.ivre = 0

        self.shield_controle = "NONE"
        self.shield_direction = "NONE"

        sprite_handler = SpriteHandler(self.CELL_SIZE)

        self.pukmun_mange_0_DL_image = sprite_handler.pukmun_mange_0_DL_image()
        self.pukmun_mange_0_DR_image = sprite_handler.pukmun_mange_0_DR_image()
        self.pukmun_mange_0_L_image = sprite_handler.pukmun_mange_0_L_image()
        self.pukmun_mange_0_R_image = sprite_handler.pukmun_mange_0_R_image()
        self.pukmun_mange_0_UL_image = sprite_handler.pukmun_mange_0_UL_image()
        self.pukmun_mange_0_UR_image = sprite_handler.pukmun_mange_0_UR_image()

        self.pukmun_mange_0_ivre_DL_image = sprite_handler.pukmun_mange_0_ivre_DL_image()
        self.pukmun_mange_0_ivre_DR_image = sprite_handler.pukmun_mange_0_ivre_DR_image()
        self.pukmun_mange_0_ivre_L_image = sprite_handler.pukmun_mange_0_ivre_L_image()
        self.pukmun_mange_0_ivre_R_image = sprite_handler.pukmun_mange_0_ivre_R_image()
        self.pukmun_mange_0_ivre_UL_image = sprite_handler.pukmun_mange_0_ivre_UL_image()
        self.pukmun_mange_0_ivre_UR_image = sprite_handler.pukmun_mange_0_ivre_UR_image()

        self.pukmun_mange_0_fantome_DL_image = sprite_handler.pukmun_mange_0_fantome_DL_image()
        self.pukmun_mange_0_fantome_DR_image = sprite_handler.pukmun_mange_0_fantome_DR_image()
        self.pukmun_mange_0_fantome_L_image = sprite_handler.pukmun_mange_0_fantome_L_image()
        self.pukmun_mange_0_fantome_R_image = sprite_handler.pukmun_mange_0_fantome_R_image()
        self.pukmun_mange_0_fantome_UL_image = sprite_handler.pukmun_mange_0_fantome_UL_image()
        self.pukmun_mange_0_fantome_UR_image = sprite_handler.pukmun_mange_0_fantome_UR_image()

        self.pukmun_mange_0_fantome_ivre_DL_image = sprite_handler.pukmun_mange_0_fantome_ivre_DL_image()
        self.pukmun_mange_0_fantome_ivre_DR_image = sprite_handler.pukmun_mange_0_fantome_ivre_DR_image()
        self.pukmun_mange_0_fantome_ivre_L_image = sprite_handler.pukmun_mange_0_fantome_ivre_L_image()
        self.pukmun_mange_0_fantome_ivre_R_image = sprite_handler.pukmun_mange_0_fantome_ivre_R_image()
        self.pukmun_mange_0_fantome_ivre_UL_image = sprite_handler.pukmun_mange_0_fantome_ivre_UL_image()
        self.pukmun_mange_0_fantome_ivre_UR_image = sprite_handler.pukmun_mange_0_fantome_ivre_UR_image()

        self.pukmun_mange_1_DL_image = sprite_handler.pukmun_mange_1_DL_image()
        self.pukmun_mange_1_DR_image = sprite_handler.pukmun_mange_1_DR_image()
        self.pukmun_mange_1_L_image = sprite_handler.pukmun_mange_1_L_image()
        self.pukmun_mange_1_R_image = sprite_handler.pukmun_mange_1_R_image()
        self.pukmun_mange_1_UL_image = sprite_handler.pukmun_mange_1_UL_image()
        self.pukmun_mange_1_UR_image = sprite_handler.pukmun_mange_1_UR_image()

        self.pukmun_mange_1_ivre_DL_image = sprite_handler.pukmun_mange_1_ivre_DL_image()
        self.pukmun_mange_1_ivre_DR_image = sprite_handler.pukmun_mange_1_ivre_DR_image()
        self.pukmun_mange_1_ivre_L_image = sprite_handler.pukmun_mange_1_ivre_L_image()
        self.pukmun_mange_1_ivre_R_image = sprite_handler.pukmun_mange_1_ivre_R_image()
        self.pukmun_mange_1_ivre_UL_image = sprite_handler.pukmun_mange_1_ivre_UL_image()
        self.pukmun_mange_1_ivre_UR_image = sprite_handler.pukmun_mange_1_ivre_UR_image()

        self.pukmun_mange_1_fantome_DL_image = sprite_handler.pukmun_mange_1_fantome_DL_image()
        self.pukmun_mange_1_fantome_DR_image = sprite_handler.pukmun_mange_1_fantome_DR_image()
        self.pukmun_mange_1_fantome_L_image = sprite_handler.pukmun_mange_1_fantome_L_image()
        self.pukmun_mange_1_fantome_R_image = sprite_handler.pukmun_mange_1_fantome_R_image()
        self.pukmun_mange_1_fantome_UL_image = sprite_handler.pukmun_mange_1_fantome_UL_image()
        self.pukmun_mange_1_fantome_UR_image = sprite_handler.pukmun_mange_1_fantome_UR_image()

        self.pukmun_mange_1_fantome_ivre_DL_image = sprite_handler.pukmun_mange_1_fantome_ivre_DL_image()
        self.pukmun_mange_1_fantome_ivre_DR_image = sprite_handler.pukmun_mange_1_fantome_ivre_DR_image()
        self.pukmun_mange_1_fantome_ivre_L_image = sprite_handler.pukmun_mange_1_fantome_ivre_L_image()
        self.pukmun_mange_1_fantome_ivre_R_image = sprite_handler.pukmun_mange_1_fantome_ivre_R_image()
        self.pukmun_mange_1_fantome_ivre_UL_image = sprite_handler.pukmun_mange_1_fantome_ivre_UL_image()
        self.pukmun_mange_1_fantome_ivre_UR_image = sprite_handler.pukmun_mange_1_fantome_ivre_UR_image()

        self.pukmun_mange_2_DL_image = sprite_handler.pukmun_mange_2_DL_image()
        self.pukmun_mange_2_DR_image = sprite_handler.pukmun_mange_2_DR_image()
        self.pukmun_mange_2_L_image = sprite_handler.pukmun_mange_2_L_image()
        self.pukmun_mange_2_R_image = sprite_handler.pukmun_mange_2_R_image()
        self.pukmun_mange_2_UL_image = sprite_handler.pukmun_mange_2_UL_image()
        self.pukmun_mange_2_UR_image = sprite_handler.pukmun_mange_2_UR_image()

        self.pukmun_mange_2_ivre_DL_image = sprite_handler.pukmun_mange_2_ivre_DL_image()
        self.pukmun_mange_2_ivre_DR_image = sprite_handler.pukmun_mange_2_ivre_DR_image()
        self.pukmun_mange_2_ivre_L_image = sprite_handler.pukmun_mange_2_ivre_L_image()
        self.pukmun_mange_2_ivre_R_image = sprite_handler.pukmun_mange_2_ivre_R_image()
        self.pukmun_mange_2_ivre_UL_image = sprite_handler.pukmun_mange_2_ivre_UL_image()
        self.pukmun_mange_2_ivre_UR_image = sprite_handler.pukmun_mange_2_ivre_UR_image()

        self.pukmun_mange_2_fantome_DL_image = sprite_handler.pukmun_mange_2_fantome_DL_image()
        self.pukmun_mange_2_fantome_DR_image = sprite_handler.pukmun_mange_2_fantome_DR_image()
        self.pukmun_mange_2_fantome_L_image = sprite_handler.pukmun_mange_2_fantome_L_image()
        self.pukmun_mange_2_fantome_R_image = sprite_handler.pukmun_mange_2_fantome_R_image()
        self.pukmun_mange_2_fantome_UL_image = sprite_handler.pukmun_mange_2_fantome_UL_image()
        self.pukmun_mange_2_fantome_UR_image = sprite_handler.pukmun_mange_2_fantome_UR_image()

        self.pukmun_mange_2_fantome_ivre_DL_image = sprite_handler.pukmun_mange_2_fantome_ivre_DL_image()
        self.pukmun_mange_2_fantome_ivre_DR_image = sprite_handler.pukmun_mange_2_fantome_ivre_DR_image()
        self.pukmun_mange_2_fantome_ivre_L_image = sprite_handler.pukmun_mange_2_fantome_ivre_L_image()
        self.pukmun_mange_2_fantome_ivre_R_image = sprite_handler.pukmun_mange_2_fantome_ivre_R_image()
        self.pukmun_mange_2_fantome_ivre_UL_image = sprite_handler.pukmun_mange_2_fantome_ivre_UL_image()
        self.pukmun_mange_2_fantome_ivre_UR_image = sprite_handler.pukmun_mange_2_fantome_ivre_UR_image()

        self.pukmun_mort_1_image = sprite_handler.pukmun_mort_1_image()
        self.pukmun_mort_2_image = sprite_handler.pukmun_mort_2_image()
        self.pukmun_mort_3_image = sprite_handler.pukmun_mort_3_image()
        self.pukmun_mort_4_image = sprite_handler.pukmun_mort_4_image()
        self.pukmun_mort_5_image = sprite_handler.pukmun_mort_5_image()
        self.pukmun_mort_6_image = sprite_handler.pukmun_mort_6_image()
        self.pukmun_mort_7_image = sprite_handler.pukmun_mort_7_image()
        self.pukmun_mort_8_image = sprite_handler.pukmun_mort_8_image()
        self.pukmun_mort_9_image = sprite_handler.pukmun_mort_9_image()
        self.pukmun_mort_10_image = sprite_handler.pukmun_mort_10_image()
        self.pukmun_mort_11_image = sprite_handler.pukmun_mort_11_image()
        self.pukmun_mort_12_image = sprite_handler.pukmun_mort_12_image()

        self.image_vide = sprite_handler.image_vide()

        self.shield_L_image = sprite_handler.shield_L_image()
        self.shield_R_image = sprite_handler.shield_R_image()
        self.shield_U_image = sprite_handler.shield_U_image()
        self.shield_D_image = sprite_handler.shield_D_image()
        self.powered_shield_L_image = sprite_handler.powered_shield_L_image()
        self.powered_shield_R_image = sprite_handler.powered_shield_R_image()
        self.powered_shield_U_image = sprite_handler.powered_shield_U_image()
        self.powered_shield_D_image = sprite_handler.powered_shield_D_image()

        self.sprite = self.pukmun_mange_1_L_image

        self.shield_sprite = None

        # TODO: Calibrer la collision box
        self.coordonnees_collision_box = [self.coordonnees_pixels[0]+2, self.coordonnees_pixels[1]+2]
        self.taille_collision_box = [(16*CELL_SIZE)/30, (16*CELL_SIZE)/30]  # [Longueur, largeur]

    def pukmun_update_action(self, game_map):
        if self.pukmun_check_case():
            if self.fantome == 0:
                self.pukmun_deplacement(game_map)
            elif self.fantome == 1:
                self.pukmun_deplacement_fantome()

        self.pukmun_update_coordonnees_pixels(game_map)
        self.pukmun_update_case()

    def pukmun_update_deplacement(self):
        if self.action == "LEFT":
            self.pukmun_gauche()
        elif self.action == "RIGHT":
            self.pukmun_droite()
        elif self.action == "DOWN":
            self.pukmun_bas()
        elif self.action == "UP":
            self.pukmun_haut()
        # print([self.coordonnees_cases[0] * self.CELL_SIZE, self.coordonnees_cases[1] * self.CELL_SIZE] != self.coordonnees_pixels)

    def pukmun_update_controle_ivre(self):
        if self.ivre == 1:
            if self.controle == "LEFT":
                self.controle = "RIGHT"
            elif self.controle == "RIGHT":
                self.controle = "LEFT"
            elif self.controle == "UP":
                self.controle = "DOWN"
            elif self.controle == "DOWN":
                self.controle = "UP"

    def pukmun_deplacement(self, game_map):
        if self.controle == "LEFT":
            if not self.pukmun_check_collision_obstacle_left(game_map):
                self.action = "LEFT"
        elif self.controle == "RIGHT":
            if not self.pukmun_check_collision_obstacle_right(game_map):
                self.action = "RIGHT"
        elif self.controle == "UP":
            if not self.pukmun_check_collision_obstacle_up(game_map):
                self.action = "UP"
        elif self.controle == "DOWN":
            if not self.pukmun_check_collision_obstacle_down(game_map):
                self.action = "DOWN"

        if self.action == "LEFT":
            if self.pukmun_check_collision_obstacle_left(game_map):
                self.action = "STOP"
        elif self.action == "RIGHT":
            if self.pukmun_check_collision_obstacle_right(game_map):
                self.action = "STOP"
        elif self.action == "UP":
            if self.pukmun_check_collision_obstacle_up(game_map):
                self.action = "STOP"
        elif self.action == "DOWN":
            if self.pukmun_check_collision_obstacle_down(game_map):
                self.action = "STOP"

    def pukmun_deplacement_fantome(self):
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0] and self.coordonnees_cases[1] * self.CELL_SIZE == self.coordonnees_pixels[1]:
            if self.controle == "LEFT":
                self.action = "LEFT"
            elif self.controle == "RIGHT":
                self.action = "RIGHT"
            elif self.controle == "UP":
                self.action = "UP"
            elif self.controle == "DOWN":
                self.action = "DOWN"

    def pukmun_check_case(self):
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0] and self.coordonnees_cases[1] * self.CELL_SIZE == self.coordonnees_pixels[1]:
            return True
        return False

    def pukmun_check_collision_obstacle_left(self, game_map):
        next_x = self.coordonnees_cases[0] - 1 if self.coordonnees_cases[0] != 0 else game_map.DIMENSION_MAP[0] - 1
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0]:
            if game_map.map_data[next_x][self.coordonnees_cases[1]] == 3:
                return True
        return False

    def pukmun_check_collision_obstacle_right(self, game_map):
        next_x = self.coordonnees_cases[0] + 1 if self.coordonnees_cases[0] != game_map.DIMENSION_MAP[0] - 1 else 0
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0]:
            if game_map.map_data[next_x][self.coordonnees_cases[1]] == 3:
                return True
        return False

    def pukmun_check_collision_obstacle_up(self, game_map):
        next_y = self.coordonnees_cases[1] - 1 if self.coordonnees_cases[1] != 0 else game_map.DIMENSION_MAP[1] - 1
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0]:
            if game_map.map_data[self.coordonnees_cases[0]][next_y] == 3:
                return True
        return False

    def pukmun_check_collision_obstacle_down(self, game_map):
        next_y = self.coordonnees_cases[1] + 1 if self.coordonnees_cases[1] != game_map.DIMENSION_MAP[1] - 1 else 0
        if self.coordonnees_cases[0] * self.CELL_SIZE == self.coordonnees_pixels[0]:
            if game_map.map_data[self.coordonnees_cases[0]][next_y] == 3 or game_map.map_data[self.coordonnees_cases[0]][next_y] == 5:
                return True
        return False

    def pukmun_gauche(self):
        self.coordonnees_pixels = [self.coordonnees_pixels[0] - self.vitesse, self.coordonnees_pixels[1]]
        self.direction_sprite = "LEFT"
        self.orientation_sprite = "LEFT"
        self.pukmun_update_case()

    def pukmun_droite(self):
        self.coordonnees_pixels = [self.coordonnees_pixels[0] + self.vitesse, self.coordonnees_pixels[1]]
        self.direction_sprite = "RIGHT"
        self.orientation_sprite = "RIGHT"
        self.pukmun_update_case()

    def pukmun_bas(self):
        self.coordonnees_pixels = [self.coordonnees_pixels[0], self.coordonnees_pixels[1] + self.vitesse]
        self.direction_sprite = "DOWN"
        self.pukmun_update_case()

    def pukmun_haut(self):
        self.coordonnees_pixels = [self.coordonnees_pixels[0], self.coordonnees_pixels[1] - self.vitesse]
        self.direction_sprite = "UP"
        self.pukmun_update_case()

    def pukmun_update_case(self):
        if self.coordonnees_pixels[0] % self.CELL_SIZE == 0:
            self.coordonnees_cases[0] = int(self.coordonnees_pixels[0]) // self.CELL_SIZE
        if self.coordonnees_pixels[1] % self.CELL_SIZE == 0:
            self.coordonnees_cases[1] = int(self.coordonnees_pixels[1]) // self.CELL_SIZE

    def pukmun_update_coordonnees_pixels(self, game_map):
        if self.coordonnees_pixels[0] < 0:
            self.coordonnees_pixels[0] = (game_map.DIMENSION_MAP[0] - 1) * self.CELL_SIZE + self.vitesse
        elif self.coordonnees_pixels[0] > (game_map.DIMENSION_MAP[0] - 1) * self.CELL_SIZE:
            self.coordonnees_pixels[0] = 0 - self.vitesse

        if self.coordonnees_pixels[1] < 0:
            self.coordonnees_pixels[1] = (game_map.DIMENSION_MAP[1] - 1) * self.CELL_SIZE + self.vitesse
        elif self.coordonnees_pixels[1] > (game_map.DIMENSION_MAP[1] - 1) * self.CELL_SIZE:
            self.coordonnees_pixels[1] = 0 - self.vitesse

    def pukmun_update_sprite(self, frame):
        frame = frame % 20

        if self.ivre == 0 and self.fantome == 0:
            if self.direction_sprite == "LEFT":
                if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                    self.sprite = self.pukmun_mange_1_L_image
                elif 4 <= frame < 8:
                    self.sprite = self.pukmun_mange_2_L_image
                elif 12 <= frame < 20:
                    self.sprite = self.pukmun_mange_0_L_image
            elif self.direction_sprite == "RIGHT":
                if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                    self.sprite = self.pukmun_mange_1_R_image
                elif 4 <= frame < 8:
                    self.sprite = self.pukmun_mange_2_R_image
                elif 12 <= frame < 20:
                    self.sprite = self.pukmun_mange_0_R_image
            elif self.direction_sprite == "UP":
                if self.orientation_sprite == "LEFT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_UL_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_UL_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_UL_image
                elif self.orientation_sprite == "RIGHT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_UR_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_UR_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_UR_image
            elif self.direction_sprite == "DOWN":
                if self.orientation_sprite == "LEFT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_DL_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_DL_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_DL_image
                elif self.orientation_sprite == "RIGHT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_DR_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_DR_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_DR_image

        elif self.ivre == 1 and self.fantome == 0:
            if self.direction_sprite == "LEFT":
                if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                    self.sprite = self.pukmun_mange_1_ivre_L_image
                elif 4 <= frame < 8:
                    self.sprite = self.pukmun_mange_2_ivre_L_image
                elif 12 <= frame < 20:
                    self.sprite = self.pukmun_mange_0_ivre_L_image
            elif self.direction_sprite == "RIGHT":
                if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                    self.sprite = self.pukmun_mange_1_ivre_R_image
                elif 4 <= frame < 8:
                    self.sprite = self.pukmun_mange_2_ivre_R_image
                elif 12 <= frame < 20:
                    self.sprite = self.pukmun_mange_0_ivre_R_image
            elif self.direction_sprite == "UP":
                if self.orientation_sprite == "LEFT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_ivre_UL_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_ivre_UL_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_ivre_UL_image
                elif self.orientation_sprite == "RIGHT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_ivre_UR_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_ivre_UR_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_ivre_UR_image
            elif self.direction_sprite == "DOWN":
                if self.orientation_sprite == "LEFT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_ivre_DL_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_ivre_DL_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_ivre_DL_image
                elif self.orientation_sprite == "RIGHT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_ivre_DR_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_ivre_DR_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_ivre_DR_image
        elif self.ivre == 0 and self.fantome == 1:
            if self.direction_sprite == "LEFT":
                if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                    self.sprite = self.pukmun_mange_1_fantome_L_image
                elif 4 <= frame < 8:
                    self.sprite = self.pukmun_mange_2_fantome_L_image
                elif 12 <= frame < 20:
                    self.sprite = self.pukmun_mange_0_fantome_L_image
            elif self.direction_sprite == "RIGHT":
                if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                    self.sprite = self.pukmun_mange_1_fantome_R_image
                elif 4 <= frame < 8:
                    self.sprite = self.pukmun_mange_2_fantome_R_image
                elif 12 <= frame < 20:
                    self.sprite = self.pukmun_mange_0_fantome_R_image
            elif self.direction_sprite == "UP":
                if self.orientation_sprite == "LEFT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_fantome_UL_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_fantome_UL_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_fantome_UL_image
                elif self.orientation_sprite == "RIGHT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_fantome_UR_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_fantome_UR_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_fantome_UR_image
            elif self.direction_sprite == "DOWN":
                if self.orientation_sprite == "LEFT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_fantome_DL_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_fantome_DL_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_fantome_DL_image
                elif self.orientation_sprite == "RIGHT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_fantome_DR_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_fantome_DR_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_fantome_DR_image

        elif self.ivre == 1 and self.fantome == 1:
            if self.direction_sprite == "LEFT":
                if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                    self.sprite = self.pukmun_mange_1_fantome_ivre_L_image
                elif 4 <= frame < 8:
                    self.sprite = self.pukmun_mange_2_fantome_ivre_L_image
                elif 12 <= frame < 20:
                    self.sprite = self.pukmun_mange_0_fantome_ivre_L_image
            elif self.direction_sprite == "RIGHT":
                if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                    self.sprite = self.pukmun_mange_1_fantome_ivre_R_image
                elif 4 <= frame < 8:
                    self.sprite = self.pukmun_mange_2_fantome_ivre_R_image
                elif 12 <= frame < 20:
                    self.sprite = self.pukmun_mange_0_fantome_ivre_R_image
            elif self.direction_sprite == "UP":
                if self.orientation_sprite == "LEFT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_fantome_ivre_UL_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_fantome_ivre_UL_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_fantome_ivre_UL_image
                elif self.orientation_sprite == "RIGHT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_fantome_ivre_UR_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_fantome_ivre_UR_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_fantome_ivre_UR_image
            elif self.direction_sprite == "DOWN":
                if self.orientation_sprite == "LEFT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_fantome_ivre_DL_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_fantome_ivre_DL_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_fantome_ivre_DL_image
                elif self.orientation_sprite == "RIGHT":
                    if 0 <= frame < 4 or 8 <= frame < 12 or self.action == "STOP":
                        self.sprite = self.pukmun_mange_1_fantome_ivre_DR_image
                    elif 4 <= frame < 8:
                        self.sprite = self.pukmun_mange_2_fantome_ivre_DR_image
                    elif 12 <= frame < 20:
                        self.sprite = self.pukmun_mange_0_fantome_ivre_DR_image

    def pukmun_update_controle_shield(self):
        if self.ivre == 1:
            if self.shield_controle == "LEFT":
                self.shield_controle = "RIGHT"
            elif self.shield_controle == "RIGHT":
                self.shield_controle = "LEFT"
            elif self.shield_controle == "UP":
                self.shield_controle = "DOWN"
            elif self.shield_controle == "DOWN":
                self.shield_controle = "UP"

        self.shield_direction = self.shield_controle

    # TODO: Afficher sprite du shield sur les coordonnees_pixels de PUKMUN si shield_direction != "NONE"
    def pukmun_update_shield(self):
        print("Update_shield")
        # if self.shield_sprite is not None:

    def pukmun_update_sprite_shield(self):
        if self.powered == 0:
            if self.shield_direction == "LEFT":
                self.shield_sprite = self.shield_L_image
            elif self.shield_direction == "RIGHT":
                self.shield_sprite = self.shield_R_image
            elif self.shield_direction == "UP":
                self.shield_sprite = self.shield_U_image
            elif self.shield_direction == "DOWN":
                self.shield_sprite = self.shield_D_image
            else:
                self.shield_sprite = None
        elif self.powered == 1:
            if self.shield_direction == "LEFT":
                self.shield_sprite = self.powered_shield_L_image
            elif self.shield_direction == "RIGHT":
                self.shield_sprite = self.powered_shield_R_image
            elif self.shield_direction == "UP":
                self.shield_sprite = self.powered_shield_U_image
            elif self.shield_direction == "DOWN":
                self.shield_sprite = self.powered_shield_D_image
            else:
                self.shield_sprite = None

    # TODO: Animation de mort de PUKMUN en durée son mort/12 frames (si plus d'1 seconde, basculer cette fonction dans Game)
    def pukmun_mort(self):
        print("Mort PUKMUN")