# sprite_handler

import pygame
import os


class SpriteHandler:
    def __init__(self, CELL_SIZE):
        self.current_path = os.path.dirname(__file__)
        self.image_path = os.path.join(self.current_path, 'images')

        self.CELL_SIZE = CELL_SIZE

    def load_image(self, image_name):
        image_path = os.path.join(self.image_path, image_name)
        image = pygame.image.load(image_path).convert_alpha()
        return pygame.transform.smoothscale(image, (self.CELL_SIZE, self.CELL_SIZE))

    def petit_graille_image(self):
        petit_graille_image = self.load_image('Truc_a_graille.png')
        return petit_graille_image

    def gros_graille_image(self):
        gros_graille_image = self.load_image('Gros_graille.png')
        return gros_graille_image

    def tile_vide_image(self):
        tile_vide_image = self.load_image('Tile_vide.png')
        return tile_vide_image

    def tile_image(self):
        tile_image = self.load_image('Tile_2.png')
        return tile_image

    def trou_image(self):
        trou_image = self.load_image('Trou_2.png')
        return trou_image

    # TODO Créer l'image et remplacer
    def porte_image(self):
        porte_image = self.load_image('Tile_vide.png')
        return porte_image

    # TODO: Si on a le temps, créer des sprites pour PUKMUN ivre et fantôme

    def pukmun_mange_0_DL_image(self):
        pukmun_mange_0_DL_image = self.load_image('Pukmun_mange_0_DL.png')
        return pukmun_mange_0_DL_image

    def pukmun_mange_0_DR_image(self):
        pukmun_mange_0_DR_image = self.load_image('Pukmun_mange_0_DR.png')
        return pukmun_mange_0_DR_image

    def pukmun_mange_0_L_image(self):
        pukmun_mange_0_L_image = self.load_image('Pukmun_mange_0_L.png')
        return pukmun_mange_0_L_image

    def pukmun_mange_0_R_image(self):
        pukmun_mange_0_R_image = self.load_image('Pukmun_mange_0_R.png')
        return pukmun_mange_0_R_image

    def pukmun_mange_0_UL_image(self):
        pukmun_mange_0_UL_image = self.load_image('Pukmun_mange_0_UL.png')
        return pukmun_mange_0_UL_image

    def pukmun_mange_0_UR_image(self):
        pukmun_mange_0_UR_image = self.load_image('Pukmun_mange_0_UR.png')
        return pukmun_mange_0_UR_image

    def pukmun_mange_1_DL_image(self):
        pukmun_mange_1_DL_image = self.load_image('Pukmun_mange_1_DL.png')
        return pukmun_mange_1_DL_image

    def pukmun_mange_1_DR_image(self):
        pukmun_mange_1_DR_image = self.load_image('Pukmun_mange_1_DR.png')
        return pukmun_mange_1_DR_image

    def pukmun_mange_1_L_image(self):
        pukmun_mange_1_L_image = self.load_image('Pukmun_mange_1_L.png')
        return pukmun_mange_1_L_image

    def pukmun_mange_1_R_image(self):
        pukmun_mange_1_R_image = self.load_image('Pukmun_mange_1_R.png')
        return pukmun_mange_1_R_image

    def pukmun_mange_1_UL_image(self):
        pukmun_mange_1_UL_image = self.load_image('Pukmun_mange_1_UL.png')
        return pukmun_mange_1_UL_image

    def pukmun_mange_1_UR_image(self):
        pukmun_mange_1_UR_image = self.load_image('Pukmun_mange_1_UR.png')
        return pukmun_mange_1_UR_image

    def pukmun_mange_2_DL_image(self):
        pukmun_mange_2_DL_image = self.load_image('Pukmun_mange_2_DL.png')
        return pukmun_mange_2_DL_image

    def pukmun_mange_2_DR_image(self):
        pukmun_mange_2_DR_image = self.load_image('Pukmun_mange_2_DR.png')
        return pukmun_mange_2_DR_image

    def pukmun_mange_2_L_image(self):
        pukmun_mange_2_L_image = self.load_image('Pukmun_mange_2_L.png')
        return pukmun_mange_2_L_image

    def pukmun_mange_2_R_image(self):
        pukmun_mange_2_R_image = self.load_image('Pukmun_mange_2_R.png')
        return pukmun_mange_2_R_image

    def pukmun_mange_2_UL_image(self):
        pukmun_mange_2_UL_image = self.load_image('Pukmun_mange_2_UL.png')
        return pukmun_mange_2_UL_image

    def pukmun_mange_2_UR_image(self):
        pukmun_mange_2_UR_image = self.load_image('Pukmun_mange_2_UR.png')
        return pukmun_mange_2_UR_image

    def pukmun_mort_1_image(self):
        pukmun_mort_1_image = self.load_image('Pukmun_mort_1.png')
        return pukmun_mort_1_image

    def pukmun_mort_2_image(self):
        pukmun_mort_2_image = self.load_image('Pukmun_mort_2.png')
        return pukmun_mort_2_image

    def pukmun_mort_3_image(self):
        pukmun_mort_3_image = self.load_image('Pukmun_mort_3.png')
        return pukmun_mort_3_image

    def pukmun_mort_4_image(self):
        pukmun_mort_4_image = self.load_image('Pukmun_mort_4.png')
        return pukmun_mort_4_image

    def pukmun_mort_5_image(self):
        pukmun_mort_5_image = self.load_image('Pukmun_mort_5.png')
        return pukmun_mort_5_image

    def pukmun_mort_6_image(self):
        pukmun_mort_6_image = self.load_image('Pukmun_mort_6.png')
        return pukmun_mort_6_image

    def pukmun_mort_7_image(self):
        pukmun_mort_7_image = self.load_image('Pukmun_mort_7.png')
        return pukmun_mort_7_image

    def pukmun_mort_8_image(self):
        pukmun_mort_8_image = self.load_image('Pukmun_mort_8.png')
        return pukmun_mort_8_image

    def pukmun_mort_9_image(self):
        pukmun_mort_9_image = self.load_image('Pukmun_mort_9.png')
        return pukmun_mort_9_image

    def pukmun_mort_10_image(self):
        pukmun_mort_10_image = self.load_image('Pukmun_mort_10.png')
        return pukmun_mort_10_image

    def pukmun_mort_11_image(self):
        pukmun_mort_11_image = self.load_image('Pukmun_mort_11.png')
        return pukmun_mort_11_image

    def pukmun_mort_12_image(self):
        pukmun_mort_12_image = self.load_image('Pukmun_mort_12.png')
        return pukmun_mort_12_image

    # TODO Créer image
    '''
    def image_vide(self):
        image_vide = self.load_image('image_vide.png')
        return image_vide
    '''

    def shield_D_image(self):
        shield_D_image = self.load_image('Shield_D.png')
        return shield_D_image

    def shield_L_image(self):
        shield_L_image = self.load_image('Shield_L.png')
        return shield_L_image

    def shield_R_image(self):
        shield_R_image = self.load_image('Shield_R.png')
        return shield_R_image

    def shield_U_image(self):
        shield_U_image = self.load_image('Shield_U.png')
        return shield_U_image

    def powered_shield_D_image(self):
        powered_shield_D_image = self.load_image('Powered_Shield_D.png')
        return powered_shield_D_image

    def powered_shield_L_image(self):
        powered_shield_L_image = self.load_image('Powered_Shield_L.png')
        return powered_shield_L_image

    def powered_shield_R_image(self):
        powered_shield_R_image = self.load_image('Powered_Shield_R.png')
        return powered_shield_R_image

    def powered_shield_U_image(self):
        powered_shield_U_image = self.load_image('Powered_Shield_U.png')
        return powered_shield_U_image

    def fantome_fantome_DL_image(self):
        fantome_fantome_DL_image = self.load_image('Fantome_fantome_DL.png')
        return fantome_fantome_DL_image

    def fantome_fantome_DR_image(self):
        fantome_fantome_DR_image = self.load_image('Fantome_fantome_DR.png')
        return fantome_fantome_DR_image

    def fantome_fantome_L_image(self):
        fantome_fantome_L_image = self.load_image('Fantome_fantome_L.png')
        return fantome_fantome_L_image

    def fantome_fantome_R_image(self):
        fantome_fantome_R_image = self.load_image('Fantome_fantome_R.png')
        return fantome_fantome_R_image

    def fantome_fantome_UL_image(self):
        fantome_fantome_UL_image = self.load_image('Fantome_fantome_UL.png')
        return fantome_fantome_UL_image

    def fantome_fantome_UR_image(self):
        fantome_fantome_UR_image = self.load_image('Fantome_fantome_UR.png')
        return fantome_fantome_UR_image

    def fantome_fantome_weak_blue_L_image(self):
        fantome_fantome_weak_blue_L_image = self.load_image('Fantome_fantome_weak_blue_L.png')
        return fantome_fantome_weak_blue_L_image

    def fantome_fantome_weak_blue_R_image(self):
        fantome_fantome_weak_blue_R_image = self.load_image('Fantome_fantome_weak_blue_R.png')
        return fantome_fantome_weak_blue_R_image

    def fantome_fantome_weak_white_L_image(self):
        fantome_fantome_weak_white_L_image = self.load_image('Fantome_fantome_weak_white_L.png')
        return fantome_fantome_weak_white_L_image

    def fantome_fantome_weak_white_R_image(self):
        fantome_fantome_weak_white_R_image = self.load_image('Fantome_fantome_weak_white_R.png')
        return fantome_fantome_weak_white_R_image

    def fantome_fantome_mort_DL_image(self):
        fantome_fantome_mort_DL_image = self.load_image('Fantome_fantome_mort_DL.png')
        return fantome_fantome_mort_DL_image

    def fantome_fantome_mort_DR_image(self):
        fantome_fantome_mort_DR_image = self.load_image('Fantome_fantome_mort_DR.png')
        return fantome_fantome_mort_DR_image

    def fantome_fantome_mort_L_image(self):
        fantome_fantome_mort_L_image = self.load_image('Fantome_fantome_mort_L.png')
        return fantome_fantome_mort_L_image

    def fantome_fantome_mort_R_image(self):
        fantome_fantome_mort_R_image = self.load_image('Fantome_fantome_mort_R.png')
        return fantome_fantome_mort_R_image

    def fantome_fantome_mort_UL_image(self):
        fantome_fantome_mort_UL_image = self.load_image('Fantome_fantome_mort_UL.png')
        return fantome_fantome_mort_UL_image

    def fantome_fantome_mort_UR_image(self):
        fantome_fantome_mort_UR_image = self.load_image('Fantome_fantome_mort_UR.png')
        return fantome_fantome_mort_UR_image

    def fantome_ivre_DL_image(self):
        fantome_ivre_DL_image = self.load_image('Fantome_ivre_DL.png')
        return fantome_ivre_DL_image

    def fantome_ivre_DR_image(self):
        fantome_ivre_DR_image = self.load_image('Fantome_ivre_DR.png')
        return fantome_ivre_DR_image

    def fantome_ivre_L_image(self):
        fantome_ivre_L_image = self.load_image('Fantome_ivre_L.png')
        return fantome_ivre_L_image

    def fantome_ivre_R_image(self):
        fantome_ivre_R_image = self.load_image('Fantome_ivre_R.png')
        return fantome_ivre_R_image

    def fantome_ivre_UL_image(self):
        fantome_ivre_UL_image = self.load_image('Fantome_ivre_UL.png')
        return fantome_ivre_UL_image

    def fantome_ivre_UR_image(self):
        fantome_ivre_UR_image = self.load_image('Fantome_ivre_UR.png')
        return fantome_ivre_UR_image

    def fantome_ivre_nrv_DL_image(self):
        fantome_ivre_nrv_DL_image = self.load_image('Fantome_ivre_nrv_DL.png')
        return fantome_ivre_nrv_DL_image

    def fantome_ivre_nrv_DR_image(self):
        fantome_ivre_nrv_DR_image = self.load_image('Fantome_ivre_nrv_DR.png')
        return fantome_ivre_nrv_DR_image

    def fantome_ivre_nrv_L_image(self):
        fantome_ivre_nrv_L_image = self.load_image('Fantome_ivre_nrv_L.png')
        return fantome_ivre_nrv_L_image

    def fantome_ivre_nrv_R_image(self):
        fantome_ivre_nrv_R_image = self.load_image('Fantome_ivre_nrv_R.png')
        return fantome_ivre_nrv_R_image

    def fantome_ivre_nrv_UL_image(self):
        fantome_ivre_nrv_UL_image = self.load_image('Fantome_ivre_nrv_UL.png')
        return fantome_ivre_nrv_UL_image

    def fantome_ivre_nrv_UR_image(self):
        fantome_ivre_nrv_UR_image = self.load_image('Fantome_ivre_nrv_UR.png')
        return fantome_ivre_nrv_UR_image

    def fantome_ivre_weak_blue_L_image(self):
        fantome_ivre_weak_blue_L_image = self.load_image('Fantome_ivre_weak_blue_L.png')
        return fantome_ivre_weak_blue_L_image

    def fantome_ivre_weak_blue_R_image(self):
        fantome_ivre_weak_blue_R_image = self.load_image('Fantome_ivre_weak_blue_R.png')
        return fantome_ivre_weak_blue_R_image

    def fantome_ivre_weak_white_L_image(self):
        fantome_ivre_weak_white_L_image = self.load_image('Fantome_ivre_weak_white_L.png')
        return fantome_ivre_weak_white_L_image

    def fantome_ivre_weak_white_R_image(self):
        fantome_ivre_weak_white_R_image = self.load_image('Fantome_ivre_weak_white_R.png')
        return fantome_ivre_weak_white_R_image

    def fantome_ivre_mort_DL_image(self):
        fantome_ivre_mort_DL_image = self.load_image('Fantome_ivre_mort_DL.png')
        return fantome_ivre_mort_DL_image

    def fantome_ivre_mort_DR_image(self):
        fantome_ivre_mort_DR_image = self.load_image('Fantome_ivre_mort_DR.png')
        return fantome_ivre_mort_DR_image

    def fantome_ivre_mort_L_image(self):
        fantome_ivre_mort_L_image = self.load_image('Fantome_ivre_mort_L.png')
        return fantome_ivre_mort_L_image

    def fantome_ivre_mort_R_image(self):
        fantome_ivre_mort_R_image = self.load_image('Fantome_ivre_mort_R.png')
        return fantome_ivre_mort_R_image

    def fantome_ivre_mort_UL_image(self):
        fantome_ivre_mort_UL_image = self.load_image('Fantome_ivre_mort_UL.png')
        return fantome_ivre_mort_UL_image

    def fantome_ivre_mort_UR_image(self):
        fantome_ivre_mort_UR_image = self.load_image('Fantome_ivre_mort_UR.png')
        return fantome_ivre_mort_UR_image

    def fantome_mafieux_DL_image(self):
        fantome_mafieux_DL_image = self.load_image('Fantome_mafieux_DL.png')
        return fantome_mafieux_DL_image

    def fantome_mafieux_DR_image(self):
        fantome_mafieux_DR_image = self.load_image('Fantome_mafieux_DR.png')
        return fantome_mafieux_DR_image

    def fantome_mafieux_L_image(self):
        fantome_mafieux_L_image = self.load_image('Fantome_mafieux_L.png')
        return fantome_mafieux_L_image

    def fantome_mafieux_R_image(self):
        fantome_mafieux_R_image = self.load_image('Fantome_mafieux_R.png')
        return fantome_mafieux_R_image

    def fantome_mafieux_UL_image(self):
        fantome_mafieux_UL_image = self.load_image('Fantome_mafieux_UL.png')
        return fantome_mafieux_UL_image

    def fantome_mafieux_UR_image(self):
        fantome_mafieux_UR_image = self.load_image('Fantome_mafieux_UR.png')
        return fantome_mafieux_UR_image

    def fantome_mafieux_dodge_L_image(self):
        fantome_mafieux_dodge_L_image = self.load_image('Fantome_mafieux_dodge_L.png')
        return fantome_mafieux_dodge_L_image

    def fantome_mafieux_dodge_R_image(self):
        fantome_mafieux_dodge_R_image = self.load_image('Fantome_mafieux_dodge_R.png')
        return fantome_mafieux_dodge_R_image

    def fantome_mafieux_mort_DL_image(self):
        fantome_mafieux_mort_DL_image = self.load_image('Fantome_mafieux_mort_DL.png')
        return fantome_mafieux_mort_DL_image

    def fantome_mafieux_mort_DR_image(self):
        fantome_mafieux_mort_DR_image = self.load_image('Fantome_mafieux_mort_DR.png')
        return fantome_mafieux_mort_DR_image

    def fantome_mafieux_mort_L_image(self):
        fantome_mafieux_mort_L_image = self.load_image('Fantome_mafieux_mort_L.png')
        return fantome_mafieux_mort_L_image

    def fantome_mafieux_mort_R_image(self):
        fantome_mafieux_mort_R_image = self.load_image('Fantome_mafieux_mort_R.png')
        return fantome_mafieux_mort_R_image

    def fantome_mafieux_mort_UL_image(self):
        fantome_mafieux_mort_UL_image = self.load_image('Fantome_mafieux_mort_UL.png')
        return fantome_mafieux_mort_UL_image

    def fantome_mafieux_mort_UR_image(self):
        fantome_mafieux_mort_UR_image = self.load_image('Fantome_mafieux_mort_UR.png')
        return fantome_mafieux_mort_UR_image

    def bullet_DL_image(self):
        bullet_DL_image = self.load_image('Bullet_DL.png')
        return bullet_DL_image

    def bullet_DR_image(self):
        bullet_DR_image = self.load_image('Bullet_DR.png')
        return bullet_DR_image

    def bullet_L_image(self):
        bullet_L_image = self.load_image('Bullet_L.png')
        return bullet_L_image

    def bullet_R_image(self):
        bullet_R_image = self.load_image('Bullet_R.png')
        return bullet_R_image

    def bullet_UL_image(self):
        bullet_UL_image = self.load_image('Bullet_UL.png')
        return bullet_UL_image

    def bullet_UR_image(self):
        bullet_UR_image = self.load_image('Bullet_UR.png')
        return bullet_UR_image

    def golden_bullet_DL_image(self):
        golden_bullet_DL_image = self.load_image('Golden_Bullet_DL.png')
        return golden_bullet_DL_image

    def golden_bullet_DR_image(self):
        golden_bullet_DR_image = self.load_image('Golden_Bullet_DR.png')
        return golden_bullet_DR_image

    def golden_bullet_L_image(self):
        golden_bullet_L_image = self.load_image('Golden_Bullet_L.png')
        return golden_bullet_L_image

    def golden_bullet_R_image(self):
        golden_bullet_R_image = self.load_image('Golden_Bullet_R.png')
        return golden_bullet_R_image

    def golden_bullet_UL_image(self):
        golden_bullet_UL_image = self.load_image('Golden_Bullet_UL.png')
        return golden_bullet_UL_image

    def golden_bullet_UR_image(self):
        golden_bullet_UR_image = self.load_image('Golden_Bullet_UR.png')
        return golden_bullet_UR_image

    def puntos_200_image(self):
        puntos_200_image = self.load_image('200_puntos.png')
        return puntos_200_image

    def puntos_400_image(self):
        puntos_400_image = self.load_image('400_puntos.png')
        return puntos_400_image

    def puntos_800_image(self):
        puntos_800_image = self.load_image('800_puntos.png')
        return puntos_800_image

    def puntos_1600_image(self):
        puntos_1600_image = self.load_image('1600_puntos.png')
        return puntos_1600_image
