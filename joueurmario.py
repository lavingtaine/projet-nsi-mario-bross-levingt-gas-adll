import pygame

class   Joueurmario(pygame.sprite.Sprite):

    def __init__(self, x, y, taille):

        super(Joueurmario, self).__init__()
        self.x = x
        self.y = y
        self.taille = taille
        self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])
        self.saut = 0
        self.saut_montee = 0
        self.saut_descente = 5
        self.nombre_de_saut = 0
        self.a_sauter = False
        self.a_tire = False
        self.tir_autorise = 1
        self.direction = 2
        self.joueur_debout = [pygame.Rect(110, 0 , 16, 33)]
        self.joueur_bouge = [
            pygame.Rect(114, 80, 27, 33),
            pygame.Rect(154, 81, 25, 30),
            pygame.Rect(196, 82, 21, 31),
            pygame.Rect(235, 81, 24, 33),
            pygame.Rect(273, 81, 28, 32),
            pygame.Rect(313, 81, 25, 31),
            pygame.Rect(349, 40, 35, 32),

        ]
        self.etat ="debout"
        self.index = 0
    def mouvement(self, vitesse):

        self.rect.x += vitesse

    def afficher(self, surface):

       pygame.draw.rect(surface,("Red"),self.rect)

    def sauter(self):
        if self.a_sauter:

            if self.saut_montee >= 10:
                self.saut_descente -= 1
                self.saut = self.saut_descente

            else:
                self.saut_montee += 1
                self.saut = self.saut_montee

            if self.saut_descente < 0:
                self.saut_montee = 0
                self.saut_descente= 5
                self.a_sauter = False

        self.rect.y = self.rect.y - (10*(self.saut/2))

    def convertir_rect_surface(self, image, dict):
        for image_debout in self.joueurmario.debout:

            joueur_rectangle_supprime =self.joueur_debout.pop(0)
            image_joueur = image.subsurface(joueur_rectangle_supprime)
            image_joueur = pygame.transform.scale(image_joueur, (32, 64))
            self.joueur_debout.append(image_joueur)

            dict["debout"] = self.joueur_debout

        for image_mouvement in self.joueur.bouge:
            image_rect = self.joueur_bouge.pop(0)
            image_joueur = image.subsurface(joueur_rectangle_supprime)
            image_joueur = pygame.transform.scale(image_joueur, (32, 64))
            self.joueur_bouge.append(image_joueur)
