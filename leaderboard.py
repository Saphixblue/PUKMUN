# leaderboard.py
import pygame


class LeaderBoard:
    def __init__(self):
        print("init")

        # TODO: Charger les tuples pseudos/scores dans tableauScores dans l'ordre (tableau de tuples String/int) depuis leaderboard.txt
        # self.tableauScores

        # TODO: Déterminer une taille pour la fenêtre du leaderboard (pas plus grande que le menu si possible)
        # self.WINDOW_SIZE

        # self.screen = pygame.display.set_mode(self.WINDOW_SIZE)

    # TODO: Créer la fenêtre du leaderboard et afficher les valeurs de tableauScores (pseudos à gauche, scores à droite)
    # Si pseudo chaîne vide et score à 0, ne pas afficher
    def displayLeaderboard(self):
        print("Display LeaderBoard")

    # TODO: Renvoie True si le score entré est plus élevé que le dernier score de la liste
    def checkHighScore(self, score):
        print("Check High Score")

    # TODO: Appelle checkHighScore(). Si True, vire la dernière valeur de tableauScores, le trie en fonction du score, et update le fichier texte
    def updateLeaderBoard(self, score):
        print("Update LeaderBoard")