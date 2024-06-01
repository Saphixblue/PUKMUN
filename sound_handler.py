# sound_handler

import pygame
import os


class SoundHandler:
    def __init__(self):
        self.current_path = os.path.dirname(__file__)
        self.sound_path = os.path.join(self.current_path, 'sons')

        # Création d'un canal spécifique pour le son de déplacement du fantôme
        self.fantome_deplacement_channel = pygame.mixer.Channel(1)
        self.fantome_weak_channel = pygame.mixer.Channel(2)

    def load_son(self, sound_name):
        sound_path = os.path.join(self.sound_path, sound_name)
        son = pygame.mixer.Sound(sound_path)
        return son

    # TODO: Reprendre la logique de SpriteHandler et faire une fonction par son
    def intro_sound(self):
        intro_sound = self.load_son('intro.mp3')
        return intro_sound

    def graille_1_sound(self):
        graille_1_sound = self.load_son('graille_1.wav')
        return graille_1_sound

    def graille_2_sound(self):
        graille_2_sound = self.load_son('graille_2.wav')
        return graille_2_sound

    def fantome_deplacement_sound(self):
        fantome_deplacement_sound = self.load_son('fantome_deplacement.wav')
        return fantome_deplacement_sound

    def gros_graille_sound(self):
        gros_graille_sound = self.load_son('gros_graille.wav')
        return gros_graille_sound

    def graille_fantome_sound(self):
        graille_fantome_sound = self.load_son('graille_fantome.mp3')
        return graille_fantome_sound

    def fantome_mort_sound(self):
        fantome_mort_sound = self.load_son('fantome_mort.wav')
        return fantome_mort_sound

    def extra_life_sound(self):
        extra_life_sound = self.load_son('extra_life.mp3')
        return extra_life_sound

    def pukmun_mort_sound(self):
        pukmun_mort_sound = self.load_son('pukmun_mort.mp3')
        return pukmun_mort_sound

    # Méthode pour renvoyer le canal spécifique pour le son de déplacement des fantômes
    def get_fantome_deplacement_channel(self):
        return self.fantome_deplacement_channel

    # Méthode pour renvoyer le canal spécifique pour le son de déplacement des fantômes
    def get_fantome_weak_channel(self):
        return self.fantome_weak_channel

    # TODO: Trouver des sons pour la dodge du mafieux, le tir du mafieux, le reflect de la balle et le fantôme ivre qui s'énerve