import pygame
import sys
from pygame.locals import *


''''
# Initialisation de Pygame
pygame.init()


# Paramètres de la fenêtre
WINDOW_SIZE = (600, 600)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Créer la fenêtre
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pac-Man")

# Charger l'image de Pac-Man
Pacman = pygame.image.load('pacman.png').convert()
Pacman = pygame.transform.scale(Pacman, (40, 40))  # Redimensionner à la taille souhaitée
'''


def jeu(WINDOW_SIZE):
    # Position de départ de Pac-Man
    pacman_position = [300, 300]
    pacman_speed = 5

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Gestion du déplacement de Pac-Man
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pacman_position[0] -= pacman_speed
        if keys[pygame.K_RIGHT]:
            pacman_position[0] += pacman_speed
        if keys[pygame.K_UP]:
            pacman_position[1] -= pacman_speed
        if keys[pygame.K_DOWN]:
            pacman_position[1] += pacman_speed

        # Limitation de Pac-Man dans la fenêtre
        pacman_position[0] = max(0, min(pacman_position[0], WINDOW_SIZE[0] - Pacman.get_width()))
        pacman_position[1] = max(0, min(pacman_position[1], WINDOW_SIZE[1] - Pacman.get_height()))

        # Affichage de Pac-Man et de la carte
        screen.fill(BLACK)
        screen.blit(Pacman, pacman_position)
        pygame.display.flip()

        # Limiter le taux de rafraîchissement de l'écran
        pygame.time.Clock().tick(60)

