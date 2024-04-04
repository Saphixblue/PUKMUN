#importation de tous les modules de Pygame existants
import pygame
#sert à rendre publiques certaines constantes et fonctions de Pygame
from pygame.locals import *
import sys


# Dimensions de la fenêtre
largeur_fenetre = 400
hauteur_fenetre = 460

# Couleurs
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
BLANC = (255, 255, 255)

# Initialize pygame
pygame.init()

# Création de la fenêtre avec ses dimensions
screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
# On nomme l'onglet crée
pygame.display.set_caption('Pukmun')

# Chargement des images
Pacman = pygame.image.load('pacman.png').convert()
background = pygame.image.load('background.png').convert()


screen.blit(background, (0, 0))

'''

# Carte de jeu (exemple)
carte = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.#.##########.#.####.#",
    "#.####.#.##########.#.####.#",
    "#......#....##....#.....#..#",
    "######.#####.##.#####.######",
    "######.#####.##.#####.######",
    "######.##..........##.######",
    "######.##.###  ###.##.######",
    "      .   .##  ##.   .      ",
    "######.##.########.##.######",
    "######.##.########.##.######",
    "######.##.########.##.######",
    "######.##..........##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#..##..................##..#",
    "###.##.#.##########.#.##.###",
    "###.##.#.##########.#.##.###",
    "#......#....##....#.....#..#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################",
]

# Fonction pour dessiner la carte
def dessiner_carte():
    for y, ligne in enumerate(carte):
        for x, case in enumerate(ligne):
            if case == "#":  # Mur
                pygame.draw.rect(screen, BLEU, (x * 16, y * 16, 16, 16))
'''

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0

objects = []
#Créer x objets
for x in range(10):                 
    o = GameObject(Pacman, x*40, x)
    objects.append(o)
Jeu = True
while Jeu:
    for event in pygame.event.get():
        # Quit le pg si joueur appuye btn fermeture fenêtre ou appuye sur un btn
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    #boucles pour effacer et dessiner tous les objets
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    # maj des modifs à l'écran et redémmarage de la boucle
    pygame.display.update()
    #ralentit un peu le pg pour pouvoir avoir le temps de voir nos modifs à l'écran
    pygame.time.delay(100)



'''
# Fonction pour dessiner et déplacer tous nos objets
move_and_draw_all_game_objects()

# Game loop
Jeu = True
while Jeu:
    # Handle user input
    for event in pygame.event.get():
        # Quit le pg si joueur appuye btn fermeture fenêtre
        if event.type == pygame.QUIT:
            running = False

    # Logique du jeu
    move_and_draw_all_game_objects()

    # Dessiner l'ecran
    screen.fill(NOIR)

    # Code pour dessiner Pacman les ghosts, et la map

    # Dessiner la carte
    #dessiner_carte()

    # Mettre à jour les modifs de la boucle sur l'écran
    pygame.display.update()
'''

# Exit the game
pygame.quit()