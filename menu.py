# menu.py

import pygame
import sys
from game import Game

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
largeur = 800
hauteur = 600
taille_fenetre = (largeur, hauteur)
ecran = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Écran d'accueil")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Fond (accueil)
fond_accueil = pygame.image.load("menu/ecran_menu.png")
fond_accueil = pygame.transform.scale(fond_accueil, (largeur, hauteur))



# Fond (options)
fond_options = pygame.image.load("menu/ecran_options/ecran_options.png")
fond_options = pygame.transform.scale(fond_options, (largeur, hauteur))

fond_options_an = pygame.image.load("menu/ecran_options/ecran_options_an.png")
fond_options_an = pygame.transform.scale(fond_options_an, (largeur, hauteur))

fond_options_ar = pygame.image.load("menu/ecran_options/ecran_options_ar.png")
fond_options_ar = pygame.transform.scale(fond_options_ar, (largeur, hauteur))

fond_options_i = pygame.image.load("menu/ecran_options/ecran_options_i.png")
fond_options_i = pygame.transform.scale(fond_options_i, (largeur, hauteur))

fond_options_e = pygame.image.load("menu/ecran_options/ecran_options_e.png")
fond_options_e = pygame.transform.scale(fond_options_e, (largeur, hauteur))

fond_options_c = pygame.image.load("menu/ecran_options/ecran_options_c.png")
fond_options_c = pygame.transform.scale(fond_options_c, (largeur, hauteur))


# Fond (score)
fond_score = pygame.image.load("menu/ecran_score/ecran_score.png")
fond_score = pygame.transform.scale(fond_score, (largeur, hauteur))

fond_score_an = pygame.image.load("menu/ecran_score/ecran_score_an.png")
fond_score_an = pygame.transform.scale(fond_score_an, (largeur, hauteur))

fond_score_an = pygame.image.load("menu/ecran_score/ecran_score_an.png")
fond_score_an = pygame.transform.scale(fond_score_an, (largeur, hauteur))

fond_score_ar = pygame.image.load("menu/ecran_score/ecran_score_ar.png")
fond_score_ar = pygame.transform.scale(fond_score_ar, (largeur, hauteur))

fond_score_i = pygame.image.load("menu/ecran_score/ecran_score_i.png")
fond_score_i = pygame.transform.scale(fond_score_i, (largeur, hauteur))

fond_score_e = pygame.image.load("menu/ecran_score/ecran_score_e.png")
fond_score_e = pygame.transform.scale(fond_score_e, (largeur, hauteur))

fond_score_c = pygame.image.load("menu/ecran_score/ecran_score_c.png")
fond_score_c = pygame.transform.scale(fond_score_c, (largeur, hauteur))


# Fond (langues)
fond_langue = pygame.image.load("menu/ecran_langue/ecran_langue.png")
fond_langue = pygame.transform.scale(fond_langue, (largeur, hauteur))

fond_langue_an = pygame.image.load("menu/ecran_langue/ecran_langue_an.png")
fond_langue_an = pygame.transform.scale(fond_langue_an, (largeur, hauteur))

fond_langue_ar = pygame.image.load("menu/ecran_langue/ecran_langue_ar.png")
fond_langue_ar = pygame.transform.scale(fond_langue_ar, (largeur, hauteur))

fond_langue_i = pygame.image.load("menu/ecran_langue/ecran_langue_i.png")
fond_langue_i = pygame.transform.scale(fond_langue_i, (largeur, hauteur))

fond_langue_e = pygame.image.load("menu/ecran_langue/ecran_langue_e.png")
fond_langue_e = pygame.transform.scale(fond_langue_e, (largeur, hauteur))

fond_langue_c = pygame.image.load("menu/ecran_langue/ecran_langue_c.png")
fond_langue_c = pygame.transform.scale(fond_langue_c, (largeur, hauteur))


# Fond (son)
fond_son = pygame.image.load("menu/ecran_son/ecran_son.png")
fond_son = pygame.transform.scale(fond_langue, (largeur, hauteur))

fond_son_an = pygame.image.load("menu/ecran_son/ecran_son_an.png")
fond_son_an = pygame.transform.scale(fond_langue_an, (largeur, hauteur))

fond_son_ar = pygame.image.load("menu/ecran_son/ecran_son_ar.png")
fond_son_ar = pygame.transform.scale(fond_langue_ar, (largeur, hauteur))

fond_son_i = pygame.image.load("menu/ecran_son/ecran_son_i.png")
fond_son_i = pygame.transform.scale(fond_langue_i, (largeur, hauteur))

fond_son_e = pygame.image.load("menu/ecran_son/ecran_son_e.png")
fond_son_e = pygame.transform.scale(fond_langue_e, (largeur, hauteur))

fond_son_c = pygame.image.load("menu/ecran_son/ecran_son_c.png")
fond_son_c = pygame.transform.scale(fond_langue_c, (largeur, hauteur))







# Chargement des images pour les boutons (accueil)
bouton_jouer = pygame.image.load("menu/options/jouer/jouer_f.png")
bouton_jouer_an = pygame.image.load("menu/options/jouer/jouer_an.png")
bouton_jouer_ar = pygame.image.load("menu/options/jouer/jouer_ar.png")
bouton_jouer_i = pygame.image.load("menu/options/jouer/jouer_i.png")
bouton_jouer_e = pygame.image.load("menu/options/jouer/jouer_e.png")
bouton_jouer_c = pygame.image.load("menu/options/jouer/jouer_c.png")

bouton_option = pygame.image.load("menu/options/options/options_f.png")
bouton_option_an = pygame.image.load("menu/options/options/options_an.png")
bouton_option_ar = pygame.image.load("menu/options/options/options_ar.png")
bouton_option_i = pygame.image.load("menu/options/options/options_i.png")
bouton_option_e = pygame.image.load("menu/options/options/options_e.png")
bouton_option_c = pygame.image.load("menu/options/options/options_c.png")

bouton_quitter = pygame.image.load("menu/options/quitter/quitter_f.png")
bouton_quitter_an = pygame.image.load("menu/options/quitter/quitter_an.png")
bouton_quitter_ar = pygame.image.load("menu/options/quitter/quitter_ar.png")
bouton_quitter_i = pygame.image.load("menu/options/quitter/quitter_i.png")
bouton_quitter_e = pygame.image.load("menu/options/quitter/quitter_e.png")
bouton_quitter_c = pygame.image.load("menu/options/quitter/quitter_c.png")


bouton_score = pygame.image.load("menu/options/score.png")


# Chargement des images pour les boutons (options)
bouton_langue = pygame.image.load("menu/options/langue/langue_f.png")
bouton_langue_an = pygame.image.load("menu/options/langue/langue_an.png")
bouton_langue_ar = pygame.image.load("menu/options/langue/langue_ar.png")
bouton_langue_i = pygame.image.load("menu/options/langue/langue_i.png")
bouton_langue_e = pygame.image.load("menu/options/langue/langue_e.png")
bouton_langue_c = pygame.image.load("menu/options/langue/langue_c.png")

bouton_son = pygame.image.load("menu/options/son/son_f.png")
bouton_son_an = pygame.image.load("menu/options/son/son_an.png")
bouton_son_ar = pygame.image.load("menu/options/son/son_ar.png")
bouton_son_i = pygame.image.load("menu/options/son/son_i.png")
bouton_son_e = pygame.image.load("menu/options/son/son_e.png")
bouton_son_c = pygame.image.load("menu/options/son/son_c.png")

bouton_retour = pygame.image.load("menu/options/retour.png")


# Chargement des images pour les boutons (langues)
bouton_français = pygame.image.load ("menu/options/francais/francais.png")
bouton_anglais = pygame.image.load ("menu/options/francais/anglais.png")
bouton_arabe = pygame.image.load ("menu/options/francais/arabe.png")
bouton_italien = pygame.image.load ("menu/options/francais/italien.png")
bouton_espagnol = pygame.image.load ("menu/options/francais/espagnol.png")
bouton_chinois = pygame.image.load ("menu/options/francais/chinois.png")


# Chargement des images pour les boutons (son)
bouton_mute = pygame.image.load("menu/options/mute.png")
bouton_plus = pygame.image.load("menu/options/plus.png")
bouton_moins = pygame.image.load("menu/options/moins.png")



# Redimensionnement des boutons
taille_bouton1 = (250, 70)
taille_bouton2 = (220, 65)
taille_bouton3 = (150, 45)
bouton_jouer = pygame.transform.scale(bouton_jouer, taille_bouton1)
bouton_jouer_an = pygame.transform.scale(bouton_jouer_an, taille_bouton1)
bouton_jouer_i = pygame.transform.scale(bouton_jouer_i, taille_bouton1)
bouton_jouer_e = pygame.transform.scale(bouton_jouer_e, taille_bouton1)


taille_bouton10 = (230, 70)
bouton_jouer_ar = pygame.transform.scale(bouton_jouer_ar, taille_bouton10)

taille_bouton11 = (250, 70)
bouton_jouer_c = pygame.transform.scale(bouton_jouer_c, taille_bouton11)


bouton_option = pygame.transform.scale(bouton_option, taille_bouton2)
bouton_option_an = pygame.transform.scale(bouton_option_an, taille_bouton2)
bouton_option_ar = pygame.transform.scale(bouton_option_ar, taille_bouton2)
bouton_option_i = pygame.transform.scale(bouton_option_i, taille_bouton2)
bouton_option_e = pygame.transform.scale(bouton_option_e, taille_bouton2)
bouton_option_c = pygame.transform.scale(bouton_option_c, taille_bouton2)


bouton_quitter = pygame.transform.scale(bouton_quitter, taille_bouton3)
bouton_quitter_an = pygame.transform.scale(bouton_quitter_an, taille_bouton3)
bouton_quitter_ar = pygame.transform.scale(bouton_quitter_ar, taille_bouton3)
bouton_quitter_i = pygame.transform.scale(bouton_quitter_i, taille_bouton3)
bouton_quitter_e = pygame.transform.scale(bouton_quitter_e, taille_bouton3)
bouton_quitter_c = pygame.transform.scale(bouton_quitter_c, taille_bouton3)



taille_bouton4 = (230, 60)
bouton_langue = pygame.transform.scale(bouton_langue, taille_bouton4)
bouton_langue_an = pygame.transform.scale(bouton_langue_an, taille_bouton4)
bouton_langue_i = pygame.transform.scale(bouton_langue_i, taille_bouton4)
bouton_langue_e = pygame.transform.scale(bouton_langue_e, taille_bouton4)
bouton_langue_c = pygame.transform.scale(bouton_langue_c, taille_bouton4)

taille_bouton9 = (150,40)
bouton_son = pygame.transform.scale(bouton_son, taille_bouton9)
bouton_son_an = pygame.transform.scale(bouton_son_an, taille_bouton9)
bouton_son_ar = pygame.transform.scale(bouton_son_ar, taille_bouton9)
bouton_son_i = pygame.transform.scale(bouton_son_i, taille_bouton9)
bouton_son_e = pygame.transform.scale(bouton_son_e, taille_bouton9)

taille_bouton12 = (150,40)
bouton_langue_ar = pygame.transform.scale(bouton_langue_ar, taille_bouton12)

taille_bouton13 = (150,40)
bouton_son_c = pygame.transform.scale(bouton_son_c, taille_bouton13)

taille_bouton5 = (120, 62)
bouton_mute = pygame.transform.scale(bouton_mute, taille_bouton5)

taille_bouton6 = (60, 35)
bouton_moins = pygame.transform.scale(bouton_moins, taille_bouton6)
bouton_plus = pygame.transform.scale(bouton_plus, taille_bouton6)

taille_bouton7 = (30, 30)
bouton_retour = pygame.transform.scale(bouton_retour, taille_bouton7)


taille_bouton8 = (150,50)
bouton_français = pygame.transform.scale(bouton_français, taille_bouton8)
bouton_anglais = pygame.transform.scale(bouton_anglais, taille_bouton8)
bouton_arabe = pygame.transform.scale(bouton_arabe, taille_bouton8)
bouton_italien = pygame.transform.scale(bouton_italien, taille_bouton8)
bouton_espagnol = pygame.transform.scale(bouton_espagnol, taille_bouton8)
bouton_chinois = pygame.transform.scale(bouton_chinois, taille_bouton8)

taille_bouton14 = (100,80)
bouton_score = pygame.transform.scale(bouton_score, taille_bouton14)

# Position des boutons accueil
pos_bouton_jouer = (largeur // 2 - bouton_jouer.get_width() // 2, hauteur // 2 - 75)
pos_bouton_jouer_an = (largeur // 2 - bouton_jouer_an.get_width() // 2, hauteur // 2 - 75)
pos_bouton_jouer_ar = (largeur // 2 - bouton_jouer_ar.get_width() // 2, hauteur // 2 - 75)
pos_bouton_jouer_i = (largeur // 2 - bouton_jouer_i.get_width() // 2, hauteur // 2 - 75)
pos_bouton_jouer_e = (largeur // 2 - bouton_jouer_e.get_width() // 2, hauteur // 2 - 75)
pos_bouton_jouer_c = (largeur // 2 - bouton_jouer_c.get_width() // 2, hauteur // 2 - 75)

pos_bouton_option = (largeur // 2 - bouton_option.get_width() // 2, hauteur // 2 + 30)
pos_bouton_option_an = (largeur // 2 - bouton_option_an.get_width() // 2, hauteur // 2 + 30)
pos_bouton_option_ar = (largeur // 2 - bouton_option_ar.get_width() // 2, hauteur // 2 + 30)
pos_bouton_option_i = (largeur // 2 - bouton_option_i.get_width() // 2, hauteur // 2 + 30)
pos_bouton_option_e = (largeur // 2 - bouton_option_e.get_width() // 2, hauteur // 2 + 30)
pos_bouton_option_c = (largeur // 2 - bouton_option_c.get_width() // 2, hauteur // 2 + 30)

pos_bouton_quitter = (largeur // 2 - bouton_quitter.get_width() // 2, hauteur // 2 + 130)
pos_bouton_quitter_an = (largeur // 2 - bouton_quitter_an.get_width() // 2, hauteur // 2 + 130)
pos_bouton_quitter_ar = (largeur // 2 - bouton_quitter_ar.get_width() // 2, hauteur // 2 + 130)
pos_bouton_quitter_i = (largeur // 2 - bouton_quitter_i.get_width() // 2, hauteur // 2 + 130)
pos_bouton_quitter_e = (largeur // 2 - bouton_quitter_e.get_width() // 2, hauteur // 2 + 130)
pos_bouton_quitter_c = (largeur // 2 - bouton_quitter_c.get_width() // 2, hauteur // 2 + 130)


pos_bouton_score = (largeur // 2 - bouton_score.get_width() - 180, hauteur // 2 + 95)


# Position des boutons options
pos_bouton_langue = (largeur // 2 - bouton_langue.get_width() // 2, hauteur // 2 - 75)
pos_bouton_langue_an = (largeur // 2 - bouton_langue_an.get_width() // 2, hauteur // 2 - 75)
pos_bouton_langue_ar = (largeur // 2 - bouton_langue_ar.get_width() // 2, hauteur // 2 - 75)
pos_bouton_langue_i = (largeur // 2 - bouton_langue_i.get_width() // 2, hauteur // 2 - 75)
pos_bouton_langue_e = (largeur // 2 - bouton_langue_e.get_width() // 2, hauteur // 2 - 75)
pos_bouton_langue_c = (largeur // 2 - bouton_langue_c.get_width() // 2, hauteur // 2 - 75)

pos_bouton_son = (largeur // 2 - bouton_son.get_width() // 2, hauteur // 2 + 30)
pos_bouton_son_an = (largeur // 2 - bouton_son_an.get_width() // 2, hauteur // 2 + 30)
pos_bouton_son_ar = (largeur // 2 - bouton_son_ar.get_width() // 2, hauteur // 2 + 30)
pos_bouton_son_i = (largeur // 2 - bouton_son_i.get_width() // 2, hauteur // 2 + 30)
pos_bouton_son_e = (largeur // 2 - bouton_son_e.get_width() // 2, hauteur // 2 + 30)
pos_bouton_son_c = (largeur // 2 - bouton_son_c.get_width() // 2, hauteur // 2 + 30)


pos_bouton_mute = (largeur // 2 - bouton_mute.get_width() + 55, hauteur // 2 - 75)
pos_bouton_moins = (largeur // 2 - bouton_mute.get_width() + 30, hauteur // 2 + 30)
pos_bouton_plus = (largeur // 2 + 30, hauteur // 2 + 30)
pos_bouton_retour = (largeur // 6, hauteur // 4)


# Position des boutons langue
pos_bouton_français = (largeur // 2 - bouton_français.get_width() - 20, hauteur // 2 - 75)
pos_bouton_anglais = (largeur // 2 - bouton_anglais.get_width() - 20, hauteur // 2 - 15)
pos_bouton_arabe = (largeur // 2 - bouton_arabe.get_width() - 20, hauteur // 2 + 40)
pos_bouton_italien = (largeur // 2 + 20, hauteur // 2 - 75)
pos_bouton_espagnol = (largeur // 2 + 20, hauteur // 2 - 15)
pos_bouton_chinois = (largeur // 2 + 20, hauteur // 2 + 40)
pos_bouton_retour = (largeur // 6, hauteur // 4)


# Liste des boutons
boutons = ["jouer", "option", "quitter", "score"]
boutons_score = ["retour"]
boutons_options = ["langue", "mute", "son", "retour", "quitter"]
boutons_langues = ["français", "anglais", "arabe", "italien", "espagnol", "chinois", "retour", "quitter"]
boutons_son = ["mute", "plus", "moins", "retour", "quitter"]

langue = "fr"
son = 1.0

# Fonction pour afficher les boutons
def afficher_bouton(image, position):
    ecran.blit(image, position)

# Fonction pour afficher les boutons
def afficher_bouton(image, position):
    ecran.blit(image, position)


def afficher_menu_score_c():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_score_c = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu des options")

    global bouton_actif_score_c  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_score_c = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_score_c = (bouton_actif_score_c + 1) % len(boutons_score)
                elif event.key == pygame.K_UP:
                    bouton_actif_score_c = (bouton_actif_score_c - 1) % len(boutons_score)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_score_c == 0:
                        menu_c()

        ecran_score_c.blit(fond_score_c, (0, 0))

        # Affichage des boutons
        if bouton_actif_score_c == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        pygame.display.flip()

def afficher_menu_score_e():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_score_e = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu des options")

    global bouton_actif_score_e  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_score_e = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_score_e = (bouton_actif_score_e + 1) % len(boutons_score)
                elif event.key == pygame.K_UP:
                    bouton_actif_score_e = (bouton_actif_score_e - 1) % len(boutons_score)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_score_e == 0:
                        menu_e()

        ecran_score_e.blit(fond_score_e, (0, 0))

        # Affichage des boutons
        if bouton_actif_score_e == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        pygame.display.flip()

def afficher_menu_score_i():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_score_i = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu des options")

    global bouton_actif_score_i  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_score_i = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_score_i = (bouton_actif_score_i + 1) % len(boutons_score)
                elif event.key == pygame.K_UP:
                    bouton_actif_score_i = (bouton_actif_score_i - 1) % len(boutons_score)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_score_i == 0:
                        menu_i()

        ecran_score_i.blit(fond_score_i, (0, 0))

        # Affichage des boutons
        if bouton_actif_score_i == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        pygame.display.flip()

def afficher_menu_score_ar():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_score_ar = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu des options")

    global bouton_actif_score_ar  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_score_ar = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_score_ar = (bouton_actif_score_ar + 1) % len(boutons_score)
                elif event.key == pygame.K_UP:
                    bouton_actif_score_ar = (bouton_actif_score_ar - 1) % len(boutons_score)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_score_ar == 0:
                        menu_ar()

        ecran_score_ar.blit(fond_score_ar, (0, 0))

        # Affichage des boutons
        if bouton_actif_score_ar == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        pygame.display.flip()

def afficher_menu_score_an():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_score_an = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu des options")

    global bouton_actif_score_an  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_score_an = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_score_an = (bouton_actif_score_an + 1) % len(boutons_score)
                elif event.key == pygame.K_UP:
                    bouton_actif_score_an = (bouton_actif_score_an - 1) % len(boutons_score)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_score_an == 0:
                        menu_an()

        ecran_score_an.blit(fond_score_an, (0, 0))

        # Affichage des boutons
        if bouton_actif_score_an == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        pygame.display.flip()

def afficher_menu_score():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_score = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu des options")

    global bouton_actif_score  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_score = (bouton_actif_score + 1) % len(boutons_score)
                elif event.key == pygame.K_UP:
                    bouton_actif_score = (bouton_actif_score - 1) % len(boutons_score)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_score == 0:
                        menu()

        ecran_score.blit(fond_score, (0, 0))

        # Affichage des boutons
        if bouton_actif_score == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        pygame.display.flip()


def afficher_menu_son_c():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_son_c = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu son")

    global bouton_actif_options  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_son_c = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_son_c = (bouton_actif_son_c + 1) % len(boutons_son)
                elif event.key == pygame.K_UP:
                    bouton_actif_son_c = (bouton_actif_son_c - 1) % len(boutons_son)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_son_c == 0:
                        global son
                        son = 0.0
                    elif bouton_actif_son_c == 1:
                        sound_down()
                    elif bouton_actif_son_c == 2:
                        sound_up()
                    elif bouton_actif_son_c == 3:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_son_c == 4:
                        afficher_menu_options_e()

        ecran_son_c.blit(fond_son_c, (0, 0))

        # Affichage des boutons

        if bouton_actif_son_c == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_mute[0] - 5, pos_bouton_mute[1] - 5, taille_bouton5[0] + 10, taille_bouton5[1] + 10), 3)
            afficher_bouton(bouton_mute, pos_bouton_mute)
        else:
            afficher_bouton(bouton_mute, pos_bouton_mute)

        if bouton_actif_son_c == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_moins[0] - 5, pos_bouton_moins[1] - 5, taille_bouton6[0] + 10, taille_bouton6[1] + 10), 3)
            afficher_bouton(bouton_moins, pos_bouton_moins)
        else:
            afficher_bouton(bouton_moins, pos_bouton_moins)

        if bouton_actif_son_c == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_plus[0] - 5, pos_bouton_plus[1] - 5, taille_bouton6[0] + 10, taille_bouton6[1] + 10), 3)
            afficher_bouton(bouton_plus, pos_bouton_plus)
        else:
            afficher_bouton(bouton_plus, pos_bouton_plus)

        if bouton_actif_son_c == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_c[0] - 5, pos_bouton_quitter_c[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_c, pos_bouton_quitter_c)
        else:
            afficher_bouton(bouton_quitter_c,pos_bouton_quitter_c)

        if bouton_actif_son_c == 4:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        pygame.display.flip()


def afficher_menu_son_e():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_son_e = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu son")

    global bouton_actif_options  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_son_e = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_son_e = (bouton_actif_son_e + 1) % len(boutons_son)
                elif event.key == pygame.K_UP:
                    bouton_actif_son_e = (bouton_actif_son_e - 1) % len(boutons_son)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_son_e == 0:
                        global son
                        son = 0.0
                    elif bouton_actif_son_e == 1:
                        sound_down()
                    elif bouton_actif_son_e == 2:
                        sound_up()
                    elif bouton_actif_son_e == 3:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_son_e == 4:
                        afficher_menu_options_e()

        ecran_son_e.blit(fond_son_e, (0, 0))

        # Affichage des boutons

        if bouton_actif_son_e == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_mute[0] - 5, pos_bouton_mute[1] - 5, taille_bouton5[0] + 10, taille_bouton5[1] + 10), 3)
            afficher_bouton(bouton_mute, pos_bouton_mute)
        else:
            afficher_bouton(bouton_mute, pos_bouton_mute)

        if bouton_actif_son_e == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_moins[0] - 5, pos_bouton_moins[1] - 5, taille_bouton6[0] + 10, taille_bouton6[1] + 10), 3)
            afficher_bouton(bouton_moins, pos_bouton_moins)
        else:
            afficher_bouton(bouton_moins, pos_bouton_moins)

        if bouton_actif_son_e == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_plus[0] - 5, pos_bouton_plus[1] - 5, taille_bouton6[0] + 10, taille_bouton6[1] + 10), 3)
            afficher_bouton(bouton_plus, pos_bouton_plus)
        else:
            afficher_bouton(bouton_plus, pos_bouton_plus)

        if bouton_actif_son_e == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_e[0] - 5, pos_bouton_quitter_e[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_e, pos_bouton_quitter_e)
        else:
            afficher_bouton(bouton_quitter_e,pos_bouton_quitter_e)

        if bouton_actif_son_e == 4:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        pygame.display.flip()

def afficher_menu_son_i():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_son_i = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu son")

    global bouton_actif_options  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_son_i = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_son_i = (bouton_actif_son_i + 1) % len(boutons_son)
                elif event.key == pygame.K_UP:
                    bouton_actif_son_i = (bouton_actif_son_i - 1) % len(boutons_son)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_son_i == 0:
                        global son
                        son = 0.0
                    elif bouton_actif_son_i == 1:
                        sound_down()
                    elif bouton_actif_son_i == 2:
                        sound_up()
                    elif bouton_actif_son_i == 3:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_son_i == 4:
                        afficher_menu_options_i()

        ecran_son_i.blit(fond_son_i, (0, 0))

        # Affichage des boutons

        if bouton_actif_son_i == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_mute[0] - 5, pos_bouton_mute[1] - 5, taille_bouton5[0] + 10, taille_bouton5[1] + 10), 3)
            afficher_bouton(bouton_mute, pos_bouton_mute)
        else:
            afficher_bouton(bouton_mute, pos_bouton_mute)

        if bouton_actif_son_i == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_moins[0] - 5, pos_bouton_moins[1] - 5, taille_bouton6[0] + 10, taille_bouton6[1] + 10), 3)
            afficher_bouton(bouton_moins, pos_bouton_moins)
        else:
            afficher_bouton(bouton_moins, pos_bouton_moins)

        if bouton_actif_son_i == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_plus[0] - 5, pos_bouton_plus[1] - 5, taille_bouton6[0] + 10, taille_bouton6[1] + 10), 3)
            afficher_bouton(bouton_plus, pos_bouton_plus)
        else:
            afficher_bouton(bouton_plus, pos_bouton_plus)

        if bouton_actif_son_i == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_i[0] - 5, pos_bouton_quitter_i[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_i, pos_bouton_quitter_i)
        else:
            afficher_bouton(bouton_quitter_i,pos_bouton_quitter_i)

        if bouton_actif_son_i == 4:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        pygame.display.flip()


def afficher_menu_son_ar():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_son_ar = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu son")

    global bouton_actif_options  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_son_ar = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_son_ar = (bouton_actif_son_ar + 1) % len(boutons_son)
                elif event.key == pygame.K_UP:
                    bouton_actif_son_ar = (bouton_actif_son_ar - 1) % len(boutons_son)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_son_ar == 0:
                        global son
                        son = 0.0
                    elif bouton_actif_son_ar == 1:
                        sound_down()
                    elif bouton_actif_son_ar == 2:
                        sound_up()
                    elif bouton_actif_son_ar == 3:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_son_ar == 4:
                        afficher_menu_options_ar()

        ecran_son_ar.blit(fond_son_ar, (0, 0))

        # Affichage des boutons

        if bouton_actif_son_ar == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_mute[0] - 5, pos_bouton_mute[1] - 5, taille_bouton5[0] + 10, taille_bouton5[1] + 10), 3)
            afficher_bouton(bouton_mute, pos_bouton_mute)
        else:
            afficher_bouton(bouton_mute, pos_bouton_mute)

        if bouton_actif_son_ar == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_moins[0] - 5, pos_bouton_moins[1] - 5, taille_bouton6[0] + 10, taille_bouton6[1] + 10), 3)
            afficher_bouton(bouton_moins, pos_bouton_moins)
        else:
            afficher_bouton(bouton_moins, pos_bouton_moins)

        if bouton_actif_son_ar == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_plus[0] - 5, pos_bouton_plus[1] - 5, taille_bouton6[0] + 10, taille_bouton6[1] + 10), 3)
            afficher_bouton(bouton_plus, pos_bouton_plus)
        else:
            afficher_bouton(bouton_plus, pos_bouton_plus)

        if bouton_actif_son_ar == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_ar[0] - 5, pos_bouton_quitter_ar[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_ar, pos_bouton_quitter_ar)
        else:
            afficher_bouton(bouton_quitter_ar, pos_bouton_quitter_ar)

        if bouton_actif_son_ar == 4:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        pygame.display.flip()

def afficher_menu_son_an():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_son_an = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu son")

    global bouton_actif_options  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_son_an = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_son_an = (bouton_actif_son_an + 1) % len(boutons_son)
                elif event.key == pygame.K_UP:
                    bouton_actif_son_an = (bouton_actif_son_an - 1) % len(boutons_son)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_son_an == 0:
                        global son
                        son = 0.0
                    elif bouton_actif_son_an == 1:
                        sound_down()
                    elif bouton_actif_son_an == 2:
                        sound_up()
                    elif bouton_actif_son_an == 3:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_son_an == 4:
                        afficher_menu_options_an()

        ecran_son_an.blit(fond_son_an, (0, 0))

        # Affichage des boutons

        if bouton_actif_son_an == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_mute[0] - 5, pos_bouton_mute[1] - 5, taille_bouton5[0] + 10, taille_bouton5[1] + 10), 3)
            afficher_bouton(bouton_mute, pos_bouton_mute)
        else:
            afficher_bouton(bouton_mute, pos_bouton_mute)

        if bouton_actif_son_an == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_moins[0] - 5, pos_bouton_moins[1] - 5, taille_bouton6[0] + 10, taille_bouton6[1] + 10), 3)
            afficher_bouton(bouton_moins, pos_bouton_moins)
        else:
            afficher_bouton(bouton_moins, pos_bouton_moins)

        if bouton_actif_son_an == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_plus[0] - 5, pos_bouton_plus[1] - 5, taille_bouton6[0] + 10, taille_bouton6[1] + 10), 3)
            afficher_bouton(bouton_plus, pos_bouton_plus)
        else:
            afficher_bouton(bouton_plus, pos_bouton_plus)

        if bouton_actif_son_an == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_an[0] - 5, pos_bouton_quitter_an[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_an, pos_bouton_quitter_an)
        else:
            afficher_bouton(bouton_quitter_an, pos_bouton_quitter_an)

        if bouton_actif_son_an == 4:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        pygame.display.flip()

def afficher_menu_son():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_son = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu son")

    global bouton_actif_options  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_son = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_son = (bouton_actif_son + 1) % len(boutons_son)
                elif event.key == pygame.K_UP:
                    bouton_actif_son = (bouton_actif_son- 1) % len(boutons_son)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_son == 0:
                        global son
                        son = 0.0
                    elif bouton_actif_son == 1:
                        sound_down()
                    elif bouton_actif_son == 2:
                        sound_up()
                    elif bouton_actif_son == 3:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_son == 4:
                        afficher_menu_options()

        ecran_son.blit(fond_son, (0, 0))

        # Affichage des boutons

        if bouton_actif_son == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_mute[0] - 5, pos_bouton_mute[1] - 5, taille_bouton5[0] + 10, taille_bouton5[1] + 10), 3)
            afficher_bouton(bouton_mute, pos_bouton_mute)
        else:
            afficher_bouton(bouton_mute, pos_bouton_mute)

        if bouton_actif_son == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_moins[0] - 5, pos_bouton_moins[1] - 5, taille_bouton6[0] + 10, taille_bouton6[1] + 10), 3)
            afficher_bouton(bouton_moins, pos_bouton_moins)
        else:
            afficher_bouton(bouton_moins, pos_bouton_moins)

        if bouton_actif_son == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_plus[0] - 5, pos_bouton_plus[1] - 5, taille_bouton6[0] + 10, taille_bouton6[1] + 10), 3)
            afficher_bouton(bouton_plus, pos_bouton_plus)
        else:
            afficher_bouton(bouton_plus, pos_bouton_plus)

        if bouton_actif_son == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter[0] - 5, pos_bouton_quitter[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter, pos_bouton_quitter)
        else:
            afficher_bouton(bouton_quitter, pos_bouton_quitter)

        if bouton_actif_son == 4:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        pygame.display.flip()


def sound_up():
    global son
    if son < 1.0:
        son = round(son + 0.1, 1)


def sound_down():
    global son
    if son > 0.0:
        son = round(son - 0.1, 1)


# Ajoutez la variable globale pour l'écran des options
bouton_actif_langue = 0


def afficher_menu_langue_c():
    global langue
    langue = "c"

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_langue_c = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu langues chinois")

    global bouton_actif_langue
    bouton_actif_langue_c = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             

            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_langue_c = (bouton_actif_langue_c + 1) % len(boutons_langues)
                elif event.key == pygame.K_UP:
                    bouton_actif_langue_c = (bouton_actif_langue_c - 1) % len(boutons_langues)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_langue_c == 3:
                        afficher_menu_langue()
                    elif bouton_actif_langue_c == 4:
                        afficher_menu_langue_an()
                    elif bouton_actif_langue_c == 5:
                        afficher_menu_langue_ar()
                    elif bouton_actif_langue_c == 6:
                        afficher_menu_langue_i()                 
                    elif bouton_actif_langue_c == 7:
                        afficher_menu_langue_e()  
                    elif bouton_actif_langue_c == 0:
                        afficher_menu_langue_c()
                    elif bouton_actif_langue_c == 1:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_langue_c == 2:
                        afficher_menu_options_c()

        ecran_langue_c.blit(fond_langue_c, (0, 0))

        # Affichage des boutons
        if bouton_actif_langue_c == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_français[0] - 5, pos_bouton_français[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_français, pos_bouton_français)
        else:
            afficher_bouton(bouton_français, pos_bouton_français)

        if bouton_actif_langue_c == 4:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_anglais[0] - 5, pos_bouton_anglais[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_anglais, pos_bouton_anglais)
        else:
            afficher_bouton(bouton_anglais, pos_bouton_anglais)

        if bouton_actif_langue_c == 5:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_arabe[0] - 5, pos_bouton_arabe[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_arabe, pos_bouton_arabe)
        else:
            afficher_bouton(bouton_arabe, pos_bouton_arabe)

        if bouton_actif_langue_c == 6:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_italien[0] - 5, pos_bouton_italien[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_italien, pos_bouton_italien)
        else:
            afficher_bouton(bouton_italien, pos_bouton_italien)
        
        if bouton_actif_langue_c == 7:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_espagnol[0] - 5, pos_bouton_espagnol[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_espagnol, pos_bouton_espagnol)
        else:
            afficher_bouton(bouton_espagnol, pos_bouton_espagnol)

        if bouton_actif_langue_c == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_chinois[0] - 5, pos_bouton_chinois[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_chinois, pos_bouton_chinois)
        else:
            afficher_bouton(bouton_chinois, pos_bouton_chinois)

        if bouton_actif_langue_c == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_c[0] - 5, pos_bouton_quitter_c[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_c, pos_bouton_quitter_c)
        else:
            afficher_bouton(bouton_quitter_c, pos_bouton_quitter_c)

        if bouton_actif_langue_c == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)


        # Rafraîchissement de l'écran
        pygame.display.flip()



def afficher_menu_langue_e():
    global langue
    langue = "e"

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_langue_e = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu langues espagnol")

    global bouton_actif_langue
    bouton_actif_langue_e = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             

            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_langue_e = (bouton_actif_langue_e + 1) % len(boutons_langues)
                elif event.key == pygame.K_UP:
                    bouton_actif_langue_e = (bouton_actif_langue_e - 1) % len(boutons_langues)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_langue_e == 4:
                        afficher_menu_langue()
                    elif bouton_actif_langue_e == 5:
                        afficher_menu_langue_an()
                    elif bouton_actif_langue_e == 6:
                        afficher_menu_langue_ar()
                    elif bouton_actif_langue_e == 7:
                        afficher_menu_langue_i()                 
                    elif bouton_actif_langue_e == 0:
                        afficher_menu_langue_e()  
                    elif bouton_actif_langue_e == 1:
                        afficher_menu_langue_c()
                    elif bouton_actif_langue_e == 2:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_langue_e == 3:
                        afficher_menu_options_e()

        ecran_langue_e.blit(fond_langue_e, (0, 0))

        # Affichage des boutons
        if bouton_actif_langue_e == 4:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_français[0] - 5, pos_bouton_français[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_français, pos_bouton_français)
        else:
            afficher_bouton(bouton_français, pos_bouton_français)

        if bouton_actif_langue_e == 5:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_anglais[0] - 5, pos_bouton_anglais[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_anglais, pos_bouton_anglais)
        else:
            afficher_bouton(bouton_anglais, pos_bouton_anglais)

        if bouton_actif_langue_e == 6:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_arabe[0] - 5, pos_bouton_arabe[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_arabe, pos_bouton_arabe)
        else:
            afficher_bouton(bouton_arabe, pos_bouton_arabe)

        if bouton_actif_langue_e == 7:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_italien[0] - 5, pos_bouton_italien[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_italien, pos_bouton_italien)
        else:
            afficher_bouton(bouton_italien, pos_bouton_italien)
        
        if bouton_actif_langue_e == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_espagnol[0] - 5, pos_bouton_espagnol[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_espagnol, pos_bouton_espagnol)
        else:
            afficher_bouton(bouton_espagnol, pos_bouton_espagnol)

        if bouton_actif_langue_e == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_chinois[0] - 5, pos_bouton_chinois[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_chinois, pos_bouton_chinois)
        else:
            afficher_bouton(bouton_chinois, pos_bouton_chinois)

        if bouton_actif_langue_e == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_e[0] - 5, pos_bouton_quitter_e[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_e, pos_bouton_quitter_e)
        else:
            afficher_bouton(bouton_quitter_e, pos_bouton_quitter_e)

        if bouton_actif_langue_e == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)


        # Rafraîchissement de l'écran
        pygame.display.flip()




def afficher_menu_langue_i():
    global langue
    langue = "i"

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_langue_i = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu langues italien")

    global bouton_actif_langue
    bouton_actif_langue_i = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             

            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_langue_i = (bouton_actif_langue_i + 1) % len(boutons_langues)
                elif event.key == pygame.K_UP:
                    bouton_actif_langue_i = (bouton_actif_langue_i - 1) % len(boutons_langues)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_langue_i == 5:
                        afficher_menu_langue()
                    elif bouton_actif_langue_i == 6:
                        afficher_menu_langue_an()
                    elif bouton_actif_langue_i == 7:
                        afficher_menu_langue_ar()
                    elif bouton_actif_langue_i == 0:
                        afficher_menu_langue_i()                 
                    elif bouton_actif_langue_i == 1:
                        afficher_menu_langue_e() 
                    elif bouton_actif_langue_i == 2:
                        afficher_menu_langue_c()
                    elif bouton_actif_langue_i == 3:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_langue_i == 4:
                        afficher_menu_options_i()

        ecran_langue_i.blit(fond_langue_i, (0, 0))

        # Affichage des boutons
        if bouton_actif_langue_i == 5:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_français[0] - 5, pos_bouton_français[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_français, pos_bouton_français)
        else:
            afficher_bouton(bouton_français, pos_bouton_français)

        if bouton_actif_langue_i == 6:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_anglais[0] - 5, pos_bouton_anglais[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_anglais, pos_bouton_anglais)
        else:
            afficher_bouton(bouton_anglais, pos_bouton_anglais)

        if bouton_actif_langue_i == 7:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_arabe[0] - 5, pos_bouton_arabe[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_arabe, pos_bouton_arabe)
        else:
            afficher_bouton(bouton_arabe, pos_bouton_arabe)

        if bouton_actif_langue_i == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_italien[0] - 5, pos_bouton_italien[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_italien, pos_bouton_italien)
        else:
            afficher_bouton(bouton_italien, pos_bouton_italien)
        
        if bouton_actif_langue_i == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_espagnol[0] - 5, pos_bouton_espagnol[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_espagnol, pos_bouton_espagnol)
        else:
            afficher_bouton(bouton_espagnol, pos_bouton_espagnol)

        if bouton_actif_langue_i == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_chinois[0] - 5, pos_bouton_chinois[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_chinois, pos_bouton_chinois)
        else:
            afficher_bouton(bouton_chinois, pos_bouton_chinois)

        if bouton_actif_langue_i == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_i[0] - 5, pos_bouton_quitter_i[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_i, pos_bouton_quitter_i)
        else:
            afficher_bouton(bouton_quitter_i, pos_bouton_quitter_i)

        if bouton_actif_langue_i == 4:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)


        # Rafraîchissement de l'écran
        pygame.display.flip()


def afficher_menu_langue_ar():
    global langue
    langue = "ar"

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_langue_ar = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu langues arabe")

    global bouton_actif_langue
    bouton_actif_langue_ar = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             

            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_langue_ar = (bouton_actif_langue_ar + 1) % len(boutons_langues)
                elif event.key == pygame.K_UP:
                    bouton_actif_langue_ar = (bouton_actif_langue_ar - 1) % len(boutons_langues)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_langue_ar == 6:
                        afficher_menu_langue()
                    elif bouton_actif_langue_ar == 7:
                        afficher_menu_langue_an()
                    elif bouton_actif_langue_ar == 0:
                        afficher_menu_langue_ar()
                    elif bouton_actif_langue_ar == 1:
                        afficher_menu_langue_i()                    
                    elif bouton_actif_langue_ar == 2:
                        afficher_menu_langue_e() 
                    elif bouton_actif_langue_ar == 3:
                        afficher_menu_langue_c()
                    elif bouton_actif_langue_ar == 4:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_langue_ar == 5:
                        afficher_menu_options_ar()

        ecran_langue_ar.blit(fond_langue_ar, (0, 0))

        # Affichage des boutons
        if bouton_actif_langue_ar == 6:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_français[0] - 5, pos_bouton_français[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_français, pos_bouton_français)
        else:
            afficher_bouton(bouton_français, pos_bouton_français)

        if bouton_actif_langue_ar == 7:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_anglais[0] - 5, pos_bouton_anglais[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_anglais, pos_bouton_anglais)
        else:
            afficher_bouton(bouton_anglais, pos_bouton_anglais)

        if bouton_actif_langue_ar == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_arabe[0] - 5, pos_bouton_arabe[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_arabe, pos_bouton_arabe)
        else:
            afficher_bouton(bouton_arabe, pos_bouton_arabe)

        if bouton_actif_langue_ar == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_italien[0] - 5, pos_bouton_italien[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_italien, pos_bouton_italien)
        else:
            afficher_bouton(bouton_italien, pos_bouton_italien)
        
        if bouton_actif_langue_ar == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_espagnol[0] - 5, pos_bouton_espagnol[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_espagnol, pos_bouton_espagnol)
        else:
            afficher_bouton(bouton_espagnol, pos_bouton_espagnol)

        if bouton_actif_langue_ar == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_chinois[0] - 5, pos_bouton_chinois[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_chinois, pos_bouton_chinois)
        else:
            afficher_bouton(bouton_chinois, pos_bouton_chinois)

        if bouton_actif_langue_ar == 4:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_ar[0] - 5, pos_bouton_quitter_ar[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_ar, pos_bouton_quitter_ar)
        else:
            afficher_bouton(bouton_quitter_ar, pos_bouton_quitter_ar)

        if bouton_actif_langue_ar == 5:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)


        # Rafraîchissement de l'écran
        pygame.display.flip()


def afficher_menu_langue_an():

    global langue
    langue = "an"

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_langue_an = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu langues anglais")

    global bouton_actif_langue
    bouton_actif_langue_an = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             

            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_langue_an = (bouton_actif_langue_an + 1) % len(boutons_langues)
                elif event.key == pygame.K_UP:
                    bouton_actif_langue_an = (bouton_actif_langue_an - 1) % len(boutons_langues)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_langue_an == 7:
                        afficher_menu_langue()
                    elif bouton_actif_langue_an == 0:
                        afficher_menu_langue_an()
                    elif bouton_actif_langue_an == 1:
                        afficher_menu_langue_ar()
                    elif bouton_actif_langue_an == 2:
                        afficher_menu_langue_i()                    
                    elif bouton_actif_langue_an == 3:
                        afficher_menu_langue_e() 
                    elif bouton_actif_langue_an == 4:
                        afficher_menu_langue_c()
                    elif bouton_actif_langue_an == 5:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_langue_an == 6:
                        afficher_menu_options_an()

        ecran_langue_an.blit(fond_langue_an, (0, 0))

        # Affichage des boutons
        if bouton_actif_langue_an == 7:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_français[0] - 5, pos_bouton_français[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_français, pos_bouton_français)
        else:
            afficher_bouton(bouton_français, pos_bouton_français)

        if bouton_actif_langue_an == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_anglais[0] - 5, pos_bouton_anglais[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_anglais, pos_bouton_anglais)
        else:
            afficher_bouton(bouton_anglais, pos_bouton_anglais)

        if bouton_actif_langue_an == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_arabe[0] - 5, pos_bouton_arabe[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_arabe, pos_bouton_arabe)
        else:
            afficher_bouton(bouton_arabe, pos_bouton_arabe)

        if bouton_actif_langue_an == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_italien[0] - 5, pos_bouton_italien[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_italien, pos_bouton_italien)
        else:
            afficher_bouton(bouton_italien, pos_bouton_italien)
        
        if bouton_actif_langue_an == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_espagnol[0] - 5, pos_bouton_espagnol[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_espagnol, pos_bouton_espagnol)
        else:
            afficher_bouton(bouton_espagnol, pos_bouton_espagnol)

        if bouton_actif_langue_an == 4:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_chinois[0] - 5, pos_bouton_chinois[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_chinois, pos_bouton_chinois)
        else:
            afficher_bouton(bouton_chinois, pos_bouton_chinois)

        if bouton_actif_langue_an == 5:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_an[0] - 5, pos_bouton_quitter_an[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_an, pos_bouton_quitter_an)
        else:
            afficher_bouton(bouton_quitter_an, pos_bouton_quitter_an)

        if bouton_actif_langue_an == 6:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)


        # Rafraîchissement de l'écran
        pygame.display.flip()


# Fonction pour afficher le menu des options
def afficher_menu_langue():
    global langue
    langue = "fr"

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_langue = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu langues")

    global bouton_actif_langue
    bouton_actif_langue = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
             

            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_langue = (bouton_actif_langue + 1) % len(boutons_langues)
                elif event.key == pygame.K_UP:
                    bouton_actif_langue = (bouton_actif_langue - 1) % len(boutons_langues)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_langue == 0:
                        afficher_menu_langue()
                    elif bouton_actif_langue == 1:
                        afficher_menu_langue_an()
                    elif bouton_actif_langue == 2:
                        afficher_menu_langue_ar()
                    elif bouton_actif_langue == 3:
                        afficher_menu_langue_i()                  
                    elif bouton_actif_langue == 4:
                        afficher_menu_langue_e() 
                    elif bouton_actif_langue == 5:
                        afficher_menu_langue_c()
                    elif bouton_actif_langue == 6:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_langue == 7:
                        afficher_menu_options()

        ecran_langue.blit(fond_langue, (0, 0))

        # Affichage des boutons
        if bouton_actif_langue == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_français[0] - 5, pos_bouton_français[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_français, pos_bouton_français)
        else:
            afficher_bouton(bouton_français, pos_bouton_français)

        if bouton_actif_langue == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_anglais[0] - 5, pos_bouton_anglais[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_anglais, pos_bouton_anglais)
        else:
            afficher_bouton(bouton_anglais, pos_bouton_anglais)

        if bouton_actif_langue == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_arabe[0] - 5, pos_bouton_arabe[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_arabe, pos_bouton_arabe)
        else:
            afficher_bouton(bouton_arabe, pos_bouton_arabe)

        if bouton_actif_langue == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_italien[0] - 5, pos_bouton_italien[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_italien, pos_bouton_italien)
        else:
            afficher_bouton(bouton_italien, pos_bouton_italien)
        
        if bouton_actif_langue == 4:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_espagnol[0] - 5, pos_bouton_espagnol[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_espagnol, pos_bouton_espagnol)
        else:
            afficher_bouton(bouton_espagnol, pos_bouton_espagnol)

        if bouton_actif_langue == 5:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_chinois[0] - 5, pos_bouton_chinois[1] - 5, taille_bouton8[0] + 10, taille_bouton8[1] + 10), 3)
            afficher_bouton(bouton_chinois, pos_bouton_chinois)
        else:
            afficher_bouton(bouton_chinois, pos_bouton_chinois)

        if bouton_actif_langue == 6:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter[0] - 5, pos_bouton_quitter[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter, pos_bouton_quitter)
        else:
            afficher_bouton(bouton_quitter, pos_bouton_quitter)

        if bouton_actif_langue == 7:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)


        # Rafraîchissement de l'écran
        pygame.display.flip()




def afficher_menu_options_c():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_options_c = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu des options")

    global bouton_actif_options  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_options_c = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_options_c = (bouton_actif_options_c + 1) % len(boutons_options)
                elif event.key == pygame.K_UP:
                    bouton_actif_options_c = (bouton_actif_options_c - 1) % len(boutons_options)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_options_c == 0:
                        afficher_menu_langue_c()
                    elif bouton_actif_options_c == 1:
                        afficher_menu_son_c()
                    elif bouton_actif_options_c == 2:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_options_c == 3:
                        menu_c()

        ecran_options_c.blit(fond_options_c, (0, 0))

        # Affichage des boutons
        if bouton_actif_options_c == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_langue_c[0] - 5, pos_bouton_langue_c[1] - 5, taille_bouton4[0] + 10, taille_bouton4[1] + 10), 3)
            afficher_bouton(bouton_langue_c, pos_bouton_langue_c)
        else:
            afficher_bouton(bouton_langue_c, pos_bouton_langue_c)

        if bouton_actif_options_c == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_son_c[0] - 5, pos_bouton_son_c[1] - 5, taille_bouton9[0] + 10, taille_bouton9[1] + 10), 3)
            afficher_bouton(bouton_son_c, pos_bouton_son_c)
        else:
            afficher_bouton(bouton_son_c, pos_bouton_son_c)

        if bouton_actif_options_c == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        if bouton_actif_options_c == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_c[0] - 5, pos_bouton_quitter_c[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_c, pos_bouton_quitter_c)
        else:
            afficher_bouton(bouton_quitter_c, pos_bouton_quitter_c)

        pygame.display.flip()


def afficher_menu_options_e():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_options_e = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu des options")

    global bouton_actif_options  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_options_e = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_options_e = (bouton_actif_options_e + 1) % len(boutons_options)
                elif event.key == pygame.K_UP:
                    bouton_actif_options_e = (bouton_actif_options_e - 1) % len(boutons_options)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_options_e == 0:
                        afficher_menu_langue_e()
                    elif bouton_actif_options_e == 1:
                        afficher_menu_son_e()
                    elif bouton_actif_options_e == 2:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_options_e == 3:
                        menu_e()

        ecran_options_e.blit(fond_options_e, (0, 0))

        # Affichage des boutons
        if bouton_actif_options_e == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_langue_e[0] - 5, pos_bouton_langue_e[1] - 5, taille_bouton4[0] + 10, taille_bouton4[1] + 10), 3)
            afficher_bouton(bouton_langue_e, pos_bouton_langue_e)
        else:
            afficher_bouton(bouton_langue_e, pos_bouton_langue_e)

        if bouton_actif_options_e == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_son_e[0] - 5, pos_bouton_son_e[1] - 5, taille_bouton9[0] + 10, taille_bouton9[1] + 10), 3)
            afficher_bouton(bouton_son_e, pos_bouton_son_e)
        else:
            afficher_bouton(bouton_son_e, pos_bouton_son_e)

        if bouton_actif_options_e == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        if bouton_actif_options_e == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_e[0] - 5, pos_bouton_quitter_e[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_e, pos_bouton_quitter_e)
        else:
            afficher_bouton(bouton_quitter_e, pos_bouton_quitter_e)

        pygame.display.flip()


def afficher_menu_options_i():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_options_i = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu des options")

    global bouton_actif_options  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_options_i = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_options_i = (bouton_actif_options_i + 1) % len(boutons_options)
                elif event.key == pygame.K_UP:
                    bouton_actif_options_i = (bouton_actif_options_i - 1) % len(boutons_options)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_options_i == 0:
                        afficher_menu_langue_i()
                    elif bouton_actif_options_i == 1:
                        afficher_menu_son_i()
                    elif bouton_actif_options_i == 2:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_options_i == 3:
                        menu_i()

        ecran_options_i.blit(fond_options_i, (0, 0))

        # Affichage des boutons
        if bouton_actif_options_i == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_langue_i[0] - 5, pos_bouton_langue_i[1] - 5, taille_bouton4[0] + 10, taille_bouton4[1] + 10), 3)
            afficher_bouton(bouton_langue_i, pos_bouton_langue_i)
        else:
            afficher_bouton(bouton_langue_i, pos_bouton_langue_i)

        if bouton_actif_options_i == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_son_i[0] - 5, pos_bouton_son_i[1] - 5, taille_bouton9[0] + 10, taille_bouton9[1] + 10), 3)
            afficher_bouton(bouton_son_i, pos_bouton_son_i)
        else:
            afficher_bouton(bouton_son_i, pos_bouton_son_i)

        if bouton_actif_options_i == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        if bouton_actif_options_i == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_i[0] - 5, pos_bouton_quitter_i[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_i, pos_bouton_quitter_i)
        else:
            afficher_bouton(bouton_quitter_i, pos_bouton_quitter_i)

        pygame.display.flip()



def afficher_menu_options_ar():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_options_ar = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu des options")

    global bouton_actif_options  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_options_ar = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_options_ar = (bouton_actif_options_ar + 1) % len(boutons_options)
                elif event.key == pygame.K_UP:
                    bouton_actif_options_ar = (bouton_actif_options_ar - 1) % len(boutons_options)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_options_ar == 0:
                        afficher_menu_langue_ar()
                    elif bouton_actif_options_ar == 1:
                        afficher_menu_son_ar()
                    elif bouton_actif_options_ar == 2:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_options_ar == 3:
                        menu_ar()

        ecran_options_ar.blit(fond_options_ar, (0, 0))

        # Affichage des boutons
        if bouton_actif_options_ar == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_langue_ar[0] - 5, pos_bouton_langue_ar[1] - 5, taille_bouton4[0] + 10, taille_bouton4[1] + 10), 3)
            afficher_bouton(bouton_langue_ar, pos_bouton_langue_ar)
        else:
            afficher_bouton(bouton_langue_ar, pos_bouton_langue_ar)

        if bouton_actif_options_ar == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_son_ar[0] - 5, pos_bouton_son_ar[1] - 5, taille_bouton9[0] + 10, taille_bouton9[1] + 10), 3)
            afficher_bouton(bouton_son_ar, pos_bouton_son_ar)
        else:
            afficher_bouton(bouton_son_ar, pos_bouton_son_ar)

        if bouton_actif_options_ar == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        if bouton_actif_options_ar == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_ar[0] - 5, pos_bouton_quitter_ar[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_ar, pos_bouton_quitter_ar)
        else:
            afficher_bouton(bouton_quitter_ar, pos_bouton_quitter_ar)

        pygame.display.flip()



# Fonction pour afficher le menu des options
def afficher_menu_options_an():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_options_an = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu des options")

    global bouton_actif_options  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_options_an = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_options_an = (bouton_actif_options_an + 1) % len(boutons_options)
                elif event.key == pygame.K_UP:
                    bouton_actif_options_an = (bouton_actif_options_an - 1) % len(boutons_options)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_options_an == 0:
                        afficher_menu_langue_an()
                    elif bouton_actif_options_an == 1:
                        afficher_menu_son_an()
                    elif bouton_actif_options_an == 2:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_options_an == 3:
                        menu_an()

        ecran_options_an.blit(fond_options_an, (0, 0))

        # Affichage des boutons
        if bouton_actif_options_an == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_langue_an[0] - 5, pos_bouton_langue_an[1] - 5, taille_bouton4[0] + 10, taille_bouton4[1] + 10), 3)
            afficher_bouton(bouton_langue_an, pos_bouton_langue_an)
        else:
            afficher_bouton(bouton_langue_an, pos_bouton_langue_an)

        if bouton_actif_options_an == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_son_an[0] - 5, pos_bouton_son_an[1] - 5, taille_bouton9[0] + 10, taille_bouton9[1] + 10), 3)
            afficher_bouton(bouton_son_an, pos_bouton_son_an)
        else:
            afficher_bouton(bouton_son_an, pos_bouton_son_an)

        if bouton_actif_options_an == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        if bouton_actif_options_an == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_an[0] - 5, pos_bouton_quitter_an[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_an, pos_bouton_quitter_an)
        else:
            afficher_bouton(bouton_quitter_an, pos_bouton_quitter_an)

        pygame.display.flip()



# Fonction pour afficher le menu des options
def afficher_menu_options():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_options = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu des options")

    global bouton_actif_options  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_options = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_options = (bouton_actif_options + 1) % len(boutons_options)
                elif event.key == pygame.K_UP:
                    bouton_actif_options = (bouton_actif_options - 1) % len(boutons_options)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_options == 0:
                        afficher_menu_langue()
                    elif bouton_actif_options == 1:
                        afficher_menu_son()
                    elif bouton_actif_options == 2:
                        pygame.quit()
                        sys.exit()
                    elif bouton_actif_options == 3:
                        menu()

        ecran_options.blit(fond_options, (0, 0))

        # Affichage des boutons
        if bouton_actif_options == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_langue[0] - 5, pos_bouton_langue[1] - 5, taille_bouton4[0] + 10, taille_bouton4[1] + 10), 3)
            afficher_bouton(bouton_langue, pos_bouton_langue)
        else:
            afficher_bouton(bouton_langue, pos_bouton_langue)

        if bouton_actif_options == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_son[0] - 5, pos_bouton_son[1] - 5, taille_bouton9[0] + 10, taille_bouton9[1] + 10), 3)
            afficher_bouton(bouton_son, pos_bouton_son)
        else:
            afficher_bouton(bouton_son, pos_bouton_son)

        if bouton_actif_options == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter[0] - 5, pos_bouton_quitter[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter, pos_bouton_quitter)
        else:
            afficher_bouton(bouton_quitter, pos_bouton_quitter)

        if bouton_actif_options == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_retour[0] - 5, pos_bouton_retour[1] - 5, taille_bouton7[0] + 10, taille_bouton7[1] + 10), 3)
            afficher_bouton(bouton_retour, pos_bouton_retour)
        else:
            afficher_bouton(bouton_retour, pos_bouton_retour)

        pygame.display.flip()




def menu_c():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_c = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu anglais")

    global bouton_actif  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_c = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_c = (bouton_actif_c + 1) % len(boutons)
                elif event.key == pygame.K_UP:
                    bouton_actif_c = (bouton_actif_c - 1) % len(boutons)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_c == 0:
                        start_game()
                    elif bouton_actif_c == 1:
                        afficher_menu_options_c()
                    elif bouton_actif_c == 2:
                        afficher_menu_score_c()
                    elif bouton_actif_c == 3:
                        pygame.quit()
                        sys.exit()

        # Affichage de l'image de fond
        ecran_c.blit(fond_accueil, (0, 0))

        # Affichage des boutons
        if bouton_actif_c == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_jouer_c[0] - 5, pos_bouton_jouer_c[1] - 5, taille_bouton1[0] + 10, taille_bouton1[1] + 10), 3)
            afficher_bouton(bouton_jouer_c, pos_bouton_jouer_c)
        else:
            afficher_bouton(bouton_jouer_c, pos_bouton_jouer_c)
        if bouton_actif_c == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_option_c[0] - 5, pos_bouton_option_c[1] - 5, taille_bouton2[0] + 10, taille_bouton2[1] + 10), 3)
            afficher_bouton(bouton_option_c, pos_bouton_option_c)
        else:
            afficher_bouton(bouton_option_c, pos_bouton_option_c)

        if bouton_actif_c == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_score[0] - 5, pos_bouton_score[1] - 5, taille_bouton14[0] + 10, taille_bouton14[1] + 10), 3)
            afficher_bouton(bouton_score, pos_bouton_score)
        else:
            afficher_bouton(bouton_score, pos_bouton_score)

        if bouton_actif_c == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_c[0] - 5, pos_bouton_quitter_c[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_c, pos_bouton_quitter_c)
        else:
            afficher_bouton(bouton_quitter_c, pos_bouton_quitter_c)


        # Rafraîchissement de l'écran
        pygame.display.flip()


def menu_e():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_e = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu anglais")

    global bouton_actif  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_e = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_e = (bouton_actif_e + 1) % len(boutons)
                elif event.key == pygame.K_UP:
                    bouton_actif_e = (bouton_actif_e - 1) % len(boutons)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_e == 0:
                        start_game()
                    elif bouton_actif_e == 1:
                        afficher_menu_options_e()
                    elif bouton_actif_e == 2:
                        afficher_menu_score_e()
                    elif bouton_actif_e == 3:
                        pygame.quit()
                        sys.exit()

        # Affichage de l'image de fond
        ecran_e.blit(fond_accueil, (0, 0))

        # Affichage des boutons
        if bouton_actif_e == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_jouer_e[0] - 5, pos_bouton_jouer_e[1] - 5, taille_bouton1[0] + 10, taille_bouton1[1] + 10), 3)
            afficher_bouton(bouton_jouer_e, pos_bouton_jouer_e)
        else:
            afficher_bouton(bouton_jouer_e, pos_bouton_jouer_e)
        if bouton_actif_e == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_option_e[0] - 5, pos_bouton_option_e[1] - 5, taille_bouton2[0] + 10, taille_bouton2[1] + 10), 3)
            afficher_bouton(bouton_option_e, pos_bouton_option_e)
        else:
            afficher_bouton(bouton_option_e, pos_bouton_option_e)

        if bouton_actif_e == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_score[0] - 5, pos_bouton_score[1] - 5, taille_bouton14[0] + 10, taille_bouton14[1] + 10), 3)
            afficher_bouton(bouton_score, pos_bouton_score)
        else:
            afficher_bouton(bouton_score, pos_bouton_score)

        if bouton_actif_e == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_e[0] - 5, pos_bouton_quitter_e[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_e, pos_bouton_quitter_e)
        else:
            afficher_bouton(bouton_quitter_e, pos_bouton_quitter_e)


        # Rafraîchissement de l'écran
        pygame.display.flip()


def menu_i():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_i = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu anglais")

    global bouton_actif  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_i = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_i = (bouton_actif_i + 1) % len(boutons)
                elif event.key == pygame.K_UP:
                    bouton_actif_i = (bouton_actif_i - 1) % len(boutons)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_i == 0:
                        start_game()
                    elif bouton_actif_i == 1:
                        afficher_menu_options_i()
                    elif bouton_actif_i == 2:
                        afficher_menu_score_i()
                    elif bouton_actif_i == 3:
                        pygame.quit()
                        sys.exit()

        # Affichage de l'image de fond
        ecran_i.blit(fond_accueil, (0, 0))

        # Affichage des boutons
        if bouton_actif_i == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_jouer_i[0] - 5, pos_bouton_jouer_i[1] - 5, taille_bouton1[0] + 10, taille_bouton1[1] + 10), 3)
            afficher_bouton(bouton_jouer_i, pos_bouton_jouer_i)
        else:
            afficher_bouton(bouton_jouer_i, pos_bouton_jouer_i)
        if bouton_actif_i == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_option_i[0] - 5, pos_bouton_option_i[1] - 5, taille_bouton2[0] + 10, taille_bouton2[1] + 10), 3)
            afficher_bouton(bouton_option_i, pos_bouton_option_i)
        else:
            afficher_bouton(bouton_option_i, pos_bouton_option_i)

        if bouton_actif_i == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_score[0] - 5, pos_bouton_score[1] - 5, taille_bouton14[0] + 10, taille_bouton14[1] + 10), 3)
            afficher_bouton(bouton_score, pos_bouton_score)
        else:
            afficher_bouton(bouton_score, pos_bouton_score)

        if bouton_actif_i == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_i[0] - 5, pos_bouton_quitter_i[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_i, pos_bouton_quitter_i)
        else:
            afficher_bouton(bouton_quitter_i, pos_bouton_quitter_i)


        # Rafraîchissement de l'écran
        pygame.display.flip()


def menu_ar():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_ar = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu anglais")

    global bouton_actif  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_ar = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_ar = (bouton_actif_ar + 1) % len(boutons)
                elif event.key == pygame.K_UP:
                    bouton_actif_ar = (bouton_actif_ar - 1) % len(boutons)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_ar == 0:
                        start_game()
                    elif bouton_actif_ar == 1:
                        afficher_menu_options_ar()
                    elif bouton_actif_ar == 2:
                        afficher_menu_score_ar()
                    elif bouton_actif_ar == 3:
                        pygame.quit()
                        sys.exit()

        # Affichage de l'image de fond
        ecran_ar.blit(fond_accueil, (0, 0))

        # Affichage des boutons
        if bouton_actif_ar == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_jouer_ar[0] - 5, pos_bouton_jouer_ar[1] - 5, taille_bouton1[0] + 10, taille_bouton1[1] + 10), 3)
            afficher_bouton(bouton_jouer_ar, pos_bouton_jouer_ar)
        else:
            afficher_bouton(bouton_jouer_ar, pos_bouton_jouer_ar)
        if bouton_actif_ar == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_option_ar[0] - 5, pos_bouton_option_ar[1] - 5, taille_bouton2[0] + 10, taille_bouton2[1] + 10), 3)
            afficher_bouton(bouton_option_ar, pos_bouton_option_ar)
        else:
            afficher_bouton(bouton_option_ar, pos_bouton_option_ar)

        if bouton_actif_ar == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_score[0] - 5, pos_bouton_score[1] - 5, taille_bouton14[0] + 10, taille_bouton14[1] + 10), 3)
            afficher_bouton(bouton_score, pos_bouton_score)
        else:
            afficher_bouton(bouton_score, pos_bouton_score)

        if bouton_actif_ar == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_ar[0] - 5, pos_bouton_quitter_ar[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_ar, pos_bouton_quitter_ar)
        else:
            afficher_bouton(bouton_quitter_ar, pos_bouton_quitter_ar)


        # Rafraîchissement de l'écran
        pygame.display.flip()

def menu_an():

    pygame.init()
    largeur = 800
    hauteur = 600
    taille_fenetre = (largeur, hauteur)
    ecran_an = pygame.display.set_mode(taille_fenetre)
    pygame.display.set_caption("Menu anglais")

    global bouton_actif  # Déclaration de la variable bouton_actif comme globale
    bouton_actif_an = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif_an = (bouton_actif_an + 1) % len(boutons)
                elif event.key == pygame.K_UP:
                    bouton_actif_an = (bouton_actif_an - 1) % len(boutons)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif_an == 0:
                        start_game()
                    elif bouton_actif_an == 1:
                        afficher_menu_options_an()
                    elif bouton_actif_an == 2:
                        afficher_menu_score_an()
                    elif bouton_actif_an == 3:
                        pygame.quit()
                        sys.exit()

        # Affichage de l'image de fond
        ecran_an.blit(fond_accueil, (0, 0))

        # Affichage des boutons
        if bouton_actif_an == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_jouer_an[0] - 5, pos_bouton_jouer_an[1] - 5, taille_bouton1[0] + 10, taille_bouton1[1] + 10), 3)
            afficher_bouton(bouton_jouer_an, pos_bouton_jouer_an)
        else:
            afficher_bouton(bouton_jouer_an, pos_bouton_jouer_an)

        if bouton_actif_an == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_option_an[0] - 5, pos_bouton_option_an[1] - 5, taille_bouton2[0] + 10, taille_bouton2[1] + 10), 3)
            afficher_bouton(bouton_option_an, pos_bouton_option_an)
        else:
            afficher_bouton(bouton_option_an, pos_bouton_option_an)

        if bouton_actif_an == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_score[0] - 5, pos_bouton_score[1] - 5, taille_bouton14[0] + 10, taille_bouton14[1] + 10), 3)
            afficher_bouton(bouton_score, pos_bouton_score)
        else:
            afficher_bouton(bouton_score, pos_bouton_score)

        if bouton_actif_an == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter_an[0] - 5, pos_bouton_quitter_an[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter_an, pos_bouton_quitter_an)
        else:
            afficher_bouton(bouton_quitter_an, pos_bouton_quitter_an)


        # Rafraîchissement de l'écran
        pygame.display.flip()



'''
# Fonction pour quitter le jeu
def quit_game():
    pygame.quit()
    sys.exit()
'''


# Fonction pour lancer le jeu principal
def start_game():
    # pygame.quit()
    global son
    global langue
    game = Game(son, langue)
    game.game()


# Boucle principale du jeu
def menu():
    global bouton_actif  # Déclaration de la variable bouton_actif comme globale
    bouton_actif = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Si l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bouton_actif = (bouton_actif + 1) % len(boutons)
                elif event.key == pygame.K_UP:
                    bouton_actif = (bouton_actif - 1) % len(boutons)
                elif event.key == pygame.K_RETURN:
                    if bouton_actif == 0:
                        start_game()
                    elif bouton_actif == 1:
                        afficher_menu_options()
                    elif bouton_actif == 2:
                        afficher_menu_score()
                    elif bouton_actif == 3:
                        pygame.quit()
                        sys.exit()

        # Affichage de l'image de fond
        ecran.blit(fond_accueil, (0, 0))

        # Affichage des boutons

        if bouton_actif == 0:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_jouer[0] - 5, pos_bouton_jouer[1] - 5, taille_bouton1[0] + 10, taille_bouton1[1] + 10), 3)
            afficher_bouton(bouton_jouer, pos_bouton_jouer)
        else:
            afficher_bouton(bouton_jouer, pos_bouton_jouer)

        if bouton_actif == 1:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_option[0] - 5, pos_bouton_option[1] - 5, taille_bouton2[0] + 10, taille_bouton2[1] + 10), 3)
            afficher_bouton(bouton_option, pos_bouton_option)
        else:
            afficher_bouton(bouton_option, pos_bouton_option)

        if bouton_actif == 2:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_score[0] - 5, pos_bouton_score[1] - 5, taille_bouton14[0] + 10, taille_bouton14[1] + 10), 3)
            afficher_bouton(bouton_score, pos_bouton_score)
        else:
            afficher_bouton(bouton_score, pos_bouton_score)

        if bouton_actif == 3:
            pygame.draw.rect(ecran, (255, 255, 255), (pos_bouton_quitter[0] - 5, pos_bouton_quitter[1] - 5, taille_bouton3[0] + 10, taille_bouton3[1] + 10), 3)
            afficher_bouton(bouton_quitter, pos_bouton_quitter)
        else:
            afficher_bouton(bouton_quitter, pos_bouton_quitter)


        # Rafraîchissement de l'écran
        pygame.display.flip()

        
# Lancer le menu
# Cette partie du code ne sera pas exécutée lorsqu'on lance menu.py comme programme principal,
# car elle est déjà couverte par le bloc précédent.
# Cependant, elle pourrait être utile si ce script est importé comme module dans un autre script,
# permettant de lancer le menu directement depuis un autre module.
if __name__ == "__main__":
    menu()


'''
# Appel de la fonction de l'écran d'accueil
ecran_accueil()
'''