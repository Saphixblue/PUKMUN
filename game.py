import pygame
import sys
from levels.level_1 import Level1
from levels.level_2 import Level2
from levels.level_3 import Level3
from levels.level_4 import Level4
from levels.level_5 import Level5
from sound_handler import SoundHandler


class Game:
    def __init__(self, son, langue):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()

        self.DIMENSION_MAP = (25, 22)  # (colonnes, lignes)
        self.CELL_SIZE = 30
        self.WINDOW_SIZE = (self.DIMENSION_MAP[0] * self.CELL_SIZE, self.DIMENSION_MAP[1] * self.CELL_SIZE + self.CELL_SIZE)

        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)

        pygame.display.set_caption("PUKMUN")

        # Niveau actuel
        self.level = None

        self.game_map = None
        self.pukmun = None

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.running = True

        self.frame = 0

        self.level_number = 3

        self.score = 0
        # Score à incrémenter en même temps que score de base, on lui retire 10000 chaque fois qu'il le dépasse
        self.score_extra_life = 0

        # Permet de compter les secondes
        self.compteur = 0

        # Détermine si l'on est au début d'un niveau (1) ou non (0)
        self.level_start = 1

        # Détermine si le niveau est sous l'effet d'un gros graille (1) ou non (0)
        self.gros_graille = 0

        # Détermine le nombre de grailles dans un niveau
        self.nombre_de_grailles = None

        # Nombre de grailles mangés par PUKMUN
        self.grailles_manges = 0

        # Nombre de vies restantes de PUKMUN
        self.lives = 3

        self.sound_handler = SoundHandler()

        self.intro_sound = self.sound_handler.intro_sound()
        self.graille_1_sound = self.sound_handler.graille_1_sound()
        self.graille_2_sound = self.sound_handler.graille_2_sound()
        self.fantome_deplacement_sound = self.sound_handler.fantome_deplacement_sound()
        self.gros_graille_sound = self.sound_handler.gros_graille_sound()
        self.graille_fantome_sound = self.sound_handler.graille_fantome_sound()
        self.fantome_mort_sound = self.sound_handler.fantome_mort_sound()
        self.extra_life_sound = self.sound_handler.extra_life_sound()
        self.pukmun_mort_sound = self.sound_handler.pukmun_mort_sound()

        self.graille = 1

        self.perte_vie = 0
        self.fin_de_jeu = 0

        self.initial = 1

        self.langue = langue
        self.son = son

        # Set volumes
        self.graille_1_sound.set_volume(self.son)
        self.graille_2_sound.set_volume(self.son)

    def level_init(self):
        if self.level_number == 1:
            self.level = Level1(self.DIMENSION_MAP, self.CELL_SIZE)
        elif self.level_number == 2:
            self.level = Level2(self.DIMENSION_MAP, self.CELL_SIZE)
        elif self.level_number == 3:
            self.level = Level3(self.DIMENSION_MAP, self.CELL_SIZE)
        elif self.level_number == 4:
            self.level = Level4(self.DIMENSION_MAP, self.CELL_SIZE)
        elif self.level_number == 5:
            self.level = Level5(self.DIMENSION_MAP, self.CELL_SIZE)

        if self.initial:
            self.game_map = self.level.level_map
        self.pukmun = self.level.pukmun
        self.level.draw_level_on_map()

        self.clock.tick(self.fps)

        self.frame = 0

        # Détermine le nombre de grailles dans un niveau
        self.nombre_de_grailles = 0
        for i in range(self.DIMENSION_MAP[0]):
            for j in range(self.DIMENSION_MAP[1]):
                if self.game_map.map_data[i][j] == 0 or self.game_map.map_data[i][j] == 1:
                    self.nombre_de_grailles += 1

        # Nombre de grailles mangés par PUKMUN
        self.grailles_manges = 0

        self.start_level()

    # Fonction pour quitter le jeu
    def quit_game(self):
        pygame.quit()
        sys.exit()

    def handle_events(self):
        self.pukmun.shield_direction = "NONE"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.pukmun.controle = "LEFT"
                    self.pukmun.pukmun_update_controle_ivre()
                elif event.key == pygame.K_d:
                    self.pukmun.controle = "RIGHT"
                    self.pukmun.pukmun_update_controle_ivre()
                elif event.key == pygame.K_z:
                    self.pukmun.controle = "UP"
                    self.pukmun.pukmun_update_controle_ivre()
                elif event.key == pygame.K_s:
                    self.pukmun.controle = "DOWN"
                    self.pukmun.pukmun_update_controle_ivre()

            # Peut-être gérer différemment ici, mais ça fonctionne pas mal

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.pukmun.shield_controle = "LEFT"
            elif keys[pygame.K_RIGHT]:
                self.pukmun.shield_controle = "RIGHT"
            elif keys[pygame.K_UP]:
                self.pukmun.shield_controle = "UP"
            elif keys[pygame.K_DOWN]:
                self.pukmun.shield_controle = "DOWN"
            else:
                self.pukmun.shield_controle = "NONE"

        self.pukmun.pukmun_update_controle_shield()

    def update_game(self):
        if self.level_start == 1:
            self.level_init()
            self.initial = 0

        # Update du score et des cases
        if self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] == 0:
            self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] = 2
            self.score += 10
            self.score_extra_life += 10
            self.grailles_manges += 1
            if self.graille == 1:
                self.graille_1_sound.play()
                self.graille = 2
            elif self.graille == 2:
                self.graille_2_sound.play()
                self.graille = 1
        if self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] == 1:
            self.game_map.map_data[self.pukmun.coordonnees_cases[0]][self.pukmun.coordonnees_cases[1]] = 2
            self.score += 50
            self.score_extra_life += 50
            self.grailles_manges += 1
            self.gros_graille_sound.play()
            # TODO: Parcourir le tableau de fantômes, mettre weak à 1 et compteur à 8 (8 secondes d'effet pour le gros graille)
            # self.pukmun.powered = 1

        if self.score_extra_life // 10000 == 1:
            self.score_extra_life -= 10000
            self.extra_life_sound.play()
            self.gagner_une_vie()

        deplacement_fantome = False

        for fantome in self.level.fantomes:
            if fantome.dead == 0 and fantome.weak == 0:
                deplacement_fantome = True
            if fantome.fantome_check_collision_pukmun(self.game_map, self.pukmun.coordonnees_pixels):
                self.gestion_collision_pukmun_fantome(fantome)

        if deplacement_fantome and not self.sound_handler.get_fantome_deplacement_channel().get_busy():
            self.sound_handler.get_fantome_deplacement_channel().play(self.fantome_deplacement_sound)

        # Update de la valeur de la frame
        self.frame = pygame.time.get_ticks() // (1000 // self.fps) % self.fps

    # TODO: Ajouter début de niveau
    # Boucle principale du jeu
    def game(self):
        self.running = True
        while self.running:
            self.update_game()

            self.handle_events()

            # Limiter le nombre d'images par seconde
            self.clock.tick(60)

            # Effacer l'écran
            self.screen.fill((0, 0, 0))

            # Dessiner la carte
            self.game_map.draw_map(self.screen)

            self.pukmun.pukmun_update_case()
            self.pukmun.pukmun_update_action(self.game_map)
            self.pukmun.pukmun_update_deplacement()
            self.pukmun.pukmun_update_sprite(pygame.time.get_ticks() // (1000 // self.fps) % self.fps)
            self.pukmun.pukmun_update_controle_shield()
            self.pukmun.pukmun_update_sprite_shield()

            for fantome in self.level.fantomes:
                if fantome.compteur_sortie != 0 and fantome.compteur_frame_sortie == self.frame:
                    fantome.compteur_sortie -= 1
                if fantome.compteur_sortie == 0:
                    fantome.fantome_comportement(self.game_map, self.pukmun.coordonnees_cases)
                fantome.fantome_update_case()
                fantome.fantome_update_action(self.game_map)
                fantome.fantome_update_deplacement(self.game_map)

                fantome.fantome_check_collision_pukmun(self.game_map, self.pukmun.coordonnees_pixels)

                fantome.fantome_update_sprite()

            # Dessiner Pac-Man
            self.screen.blit(self.pukmun.sprite, (self.pukmun.coordonnees_pixels[0], self.pukmun.coordonnees_pixels[1]))
            if self.pukmun.shield_sprite is not None:
                self.screen.blit(self.pukmun.shield_sprite, (self.pukmun.coordonnees_pixels[0], self.pukmun.coordonnees_pixels[1]))

            # Dessiner les fantômes
            for fantome in self.level.fantomes:
                self.screen.blit(fantome.sprite,(fantome.coordonnees_pixels[0], fantome.coordonnees_pixels[1]))

            # Mettre à jour l'affichage
            pygame.display.flip()

            if self.grailles_manges == self.nombre_de_grailles:
                self.level_complete()
                self.level_start = 1
                self.initial = 1

    # TODO: Afficher GAME OVER (quelques secondes), si high score --> updateLeaderBoard(), remise du score à zéro puis renvoi du joueur à l'écran titre
    def game_over(self):
        print("Game over")
        # Afficher "Game Over" à l'écran 3 secondes
        # Définition de la taille maximale du texte
        max_text_size = self.CELL_SIZE

        # Création de la police avec la taille maximale
        font = pygame.font.Font(None, max_text_size)

        # Rendu du texte "GAME OVER"
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))

        # Calcul de la position du texte pour le centrer
        text_rect = game_over_text.get_rect(center=(self.DIMENSION_MAP[0] * self.CELL_SIZE // 2, 10.5 * self.CELL_SIZE))

        # Affichage du texte sur l'écran
        self.screen.blit(game_over_text, text_rect)

        # Mise à jour de l'affichage
        pygame.display.flip()

        # Attente de 2 secondes
        pygame.time.delay(2000)

        # Mise à jour de l'affichage
        pygame.display.flip()

        # Attente de 3 secondes
        pygame.time.delay(3000)

        # Revenir au menu
        self.running = False
        self.return_to_menu()

    # TODO: Faire disparaître toutes les entités, faire disparaître tous les sons du jeu, jouer l'animation + son de mort de PUKMUN et lui retirer une vie.
    # Si plus de vies --> game_over
    def perdre_une_vie(self):
        # Limiter le nombre d'images par seconde
        self.clock.tick(60)

        # Figer le jeu pendant une demi-seconde
        self.pukmun.sprite = self.pukmun.pukmun_mort_1_image
        pygame.mixer.stop()
        pygame.time.delay(500)

        # Effacer l'écran et redessiner la carte sans les fantômes
        self.screen.fill((0, 0, 0))
        self.game_map.draw_map(self.screen)

        # Jouer le son de mort de Pukmun
        self.pukmun_mort_sound.play()

        # Afficher l'animation de mort de Pukmun
        for frame in range(60):  # 60 frames pour l'animation de mort
            self.pukmun.pukmun_mort(frame)
            self.screen.fill((0, 0, 0))
            self.game_map.draw_map(self.screen)
            self.screen.blit(self.pukmun.sprite, (self.pukmun.coordonnees_pixels[0], self.pukmun.coordonnees_pixels[1]))
            pygame.display.flip()
            pygame.time.delay(16)  # Ajuster le délai pour une animation fluide

        # Réduire le nombre de vies de Pukmun
        self.lives -= 1

        pygame.time.delay(500)

        # Vérifier si le jeu est terminé
        if self.lives <= 0:
            self.game_over()
        else:
            # Redémarrer le niveau
            self.level_start = 1
            self.level_init()
        print("Perdre une vie")

    def gagner_une_vie(self):
        if self.lives < 5:
            self.lives += 1

    # TODO: Si possible, afficher 3, 2, 1, Go! pendant la musique sous le pit des fantômes
    # TODO: Tous les éléments sont placés; tout est immobile pendant que la musique de début se joue
    def start_level(self):
        # Dessiner la carte
        self.screen.fill((0, 0, 0))
        self.game_map.draw_map(self.screen)

        # Placer Pukmun
        self.screen.blit(self.pukmun.sprite, (self.pukmun.coordonnees_pixels[0], self.pukmun.coordonnees_pixels[1]))

        # TODO: Placer les fantômes
        for fantome in self.level.fantomes:
            self.screen.blit(fantome.sprite, (fantome.coordonnees_pixels[0], fantome.coordonnees_pixels[1]))

        pygame.display.flip()

        self.intro_sound.play()
        pygame.time.delay(4000)  # Attendre 4 secondes

        self.level_start = 0

    # TODO: Décommenter quand level_start() est fait, et quand tous les niveaux sont implémentés
    def level_complete(self):
        self.level_number += 1
        if self.level_number == 6:
            self.level_number = 1

    # TODO: Décommenter quand level_start() est fait, et quand tous les niveaux sont implémentés
    def previous_level(self):
        self.level_number -= 1
        if self.level_number == 0:
            self.level_number = 5

    # Gestion de la collision entre PUKMUN et les fantômes en fonction de leur état
    # TODO: Si PUKMUN n'est pas sous gros graille :
    # Si fantôme ivre ou fantôme fantôme --> Perd une vie
    # Sinon :
    # Si fantôme ivre ou fantôme fantôme --> Le mange, obtient les points et les affiche, fantôme devient mort
    # Fantôme mafieux --> Dodge
    def gestion_collision_pukmun_fantome(self, fantome):
        # Si PUKMUN pas sous gros graille
        self.perdre_une_vie()

    # Gestion de la collision entre PUKMUN et la balle en fonction de leur état
    # TODO: Si bouclier non déployé dans la bonne direction --> Perd une vie
    # Si déployé dans la bonne direction :
    # Si powered --> golden passe à 1 et balle renvoyée
    # Sinon --> Balle renvoyée
    def gestion_collision_pukmun_balle(self, fantome_mafieux):
        print("Gestion collision pukmun_balle")

    # Gestion de la collision entre la balle et le fantôme mafieux qui l'a tirée en fonction de leur état
    # TODO: Si golden --> fantome dead à 1
    # Sinon : Dodge
    def gestion_collision_balle_fantome(self, fantome_mafieux):
        print("Gestion collision pukmun_balle_fantome")

    def return_to_menu(self):
        # Fermeture du jeu
        pygame.quit()

        # Code pour revenir au menu
        import subprocess
        subprocess.run(["python", "menu.py"])

        sys.exit()



'''
if __name__ == "__main__":
    game()
'''
