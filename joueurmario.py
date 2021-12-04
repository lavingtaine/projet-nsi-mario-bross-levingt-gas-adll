import pygame

class Joueurmario(pygame.sprite.Sprite):

    def __init__(self, x, y, taille):

        super(Joueurmario, self).__init__()
        self.x = x
        self.y = y
        self.taille = taille
        self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])

    def mouvement(self, vitesse):

        self.rect.x += vitesse

    def afficher(self, surface):

        pygame.draw.rect(surface,("Red"),self.rect)
