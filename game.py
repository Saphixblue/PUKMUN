# game.py

import pygame
import sys
import os
from Map import Map
from levels.level_1 import Level1
from pukmun import Pukmun
from sprite_handler import SpriteHandler


class Game:
    def __init__(self):

        pygame.init()

        self.DIMENSION_MAP = (25, 22) # (colonnes, lignes)
        self.CELL_SIZE = 30
        self.WINDOW_SIZE = (self.DIMENSION_MAP[0] * self.CELL_SIZE, self.DIMENSION_MAP[1] * self.CELL_SIZE)

        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)

        pygame.display.set_caption("PUKMUN")

        self.level_1 = Level1(self.DIMENSION_MAP, self.CELL_SIZE)
        # self.level_2
        # self.level_3
        # self.level_4
        # self.level_5

        self.game_map = self.level_1.level_1_map
        self.pukmun = self.level_1.pukmun
        self.level_1.draw_level_on_map()

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.clock.tick(self.fps)

        self.frame = 0
        self.check_frame = 0

        self.level = 1

        self.score = 0

    # Fonction pour quitter le jeu
    def quit_game(self):
        pygame.quit()
        sys.exit()

    # Boucle principale du jeu
    def game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.pukmun.controle = "LEFT"
                    elif event.key == pygame.K_d:
                        self.pukmun.controle = "RIGHT"
                    elif event.key == pygame.K_z:
                        self.pukmun.controle = "UP"
                    elif event.key == pygame.K_s:
                        self.pukmun.controle = "DOWN"

            # Effacer l'écran
            self.screen.fill((0, 0, 0))

            # Dessiner la carte
            self.game_map.draw_map(self.screen)

            if pygame.time.get_ticks() // (1000 // self.fps) % self.fps != self.frame:
                self.pukmun.pukmun_update_case(self.game_map)
                self.pukmun.pukmun_update_action(self.game_map)
                self.pukmun.pukmun_update_deplacement(self.game_map)
                # self.pukmun.pukmun_update_deplacement_sprite(self.game_map)
                self.pukmun.pukmun_update_sprite(pygame.time.get_ticks() // (1000 // self.fps) % self.fps)

                '''
                print(pygame.time.get_ticks() // (1000 // self.fps) % self.fps)
                print(self.pukmun.coordonnees_pixels)
                print(self.pukmun.coordonnees_cases)
                '''
                print(self.score)



                if self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] == 0:
                    self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] = 2
                    self.score += 10

                # Update de la valeur de la frame
                self.frame = pygame.time.get_ticks() // (1000 // self.fps) % self.fps

            # Dessiner Pac-Man
            self.screen.blit(self.pukmun.sprite, (self.pukmun.coordonnees_pixels[0], self.pukmun.coordonnees_pixels[1]))


            # Mettre à jour l'affichage
            pygame.display.flip()

            # Limiter le nombre d'images par seconde
            # pygame.time.Clock().tick(60)

'''
if __name__ == "__main__":
    game()
'''