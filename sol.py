import pygame


class Sol(pygame.sprite.Sprite):

    def __init__(self):

        super(Sol, self).__init__()
        self.rect = pygame.Rect(0, 700, 1000, 300)

    def afficher(self, surface):

        pygame.draw.rect(surface, ("Green"), self.rect)
