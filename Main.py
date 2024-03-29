map = [[0 for _ in range(20)] for _ in range(23)]


def DrawAngle(x, y, longeur, positionAngle, longeurAngle=1, directionAngle="bas"):
    """Dessine une forme de T avec directionAngle haut ou bas"""
    for i in range(longeur):
        map[x + i][y] = 3
    for j in range(longeurAngle):
        if directionAngle == "haut":
            direction = -j
        else:
            direction = j
        map[x + positionAngle - 1][y + direction + 1] = 3


def DrawRectangle(x, y, longeur, largeur=1):
    for i in range(longeur):
        for j in range(largeur):
            map[x + i][y + j] = 3


def InitMap():
    DrawAngle(8, 8, 3, 1, 2)
    DrawAngle(9, 10, 6, 6, 2)
    DrawRectangle(12, 8, 2)
    DrawRectangle(0, 8, 5, 2)
    DrawRectangle(0, 11, 5, 2)
    DrawRectangle(18, 8, 5, 2)
    DrawRectangle(18, 11, 5, 2)
