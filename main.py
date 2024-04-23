# main .py

import pygame
import sys
from menu import menu # pour pouvoir lancer la fonction menu de menu.py

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre principale
WINDOW_SIZE = (800, 600)
BLACK = (0, 0, 0)

# Créer la fenêtre principale
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pac-Man")

# Fonction pour quitter le jeu
def quit_game():
    pygame.quit()
    sys.exit()

# Fonction principale
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        # Lancer le menu principal
        menu()

        pygame.display.flip()

# Vérifie si ce script est exécuté directement par Python en tant que programme principal.
# Si c'est le cas, lance la fonction principale main(), définie plus haut.
if __name__ == "__main__":
    main()