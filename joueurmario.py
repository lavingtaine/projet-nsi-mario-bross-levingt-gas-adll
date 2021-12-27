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

        self.joueur_debout = [pygame.Rect(0, 0, 111, 145)]

        self.joueur_bouge = [
            pygame.Rect(0, 0, 111, 145),
            pygame.Rect(111, 0, 121, 146),
            pygame.Rect(231, 0, 124, 149),
            pygame.Rect(360, 0, 102, 145),
            pygame.Rect(477, 0, 114, 146),
            pygame.Rect(598, 0, 122, 142),
            pygame.Rect(727, 0, 117, 145),

        ]
        self.etat ='debout'
        self.index = 0

        #self.joueur_saute =

    def mouvement(self, vitesse):

        self.rect.x += vitesse

    def afficher(self, surface, dict):

        self.index += 1

        if self.index >= len(dict[self.etat]):
            self.index = 0

        image = dict[self.etat][self.index]

        if self.direction == -1:
             image = pygame.transform.flip(image, True, False)

        #image = dict[self.etat][self.index]
        surface.blit(image, self.rect)
        pygame.draw.rect(surface,("Red"),self.rect, 1)

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

        for image_debout in self.joueur_debout:

            joueur_rectangle_supprime = self.joueur_debout.pop(0)
            image_joueur = image.subsurface(joueur_rectangle_supprime)
            image_joueur = pygame.transform.scale(image_joueur, (32, 64))
            self.joueur_debout.append(image_joueur)

        dict["debout"] = self.joueur_debout

        for image_mouvement in self.joueur_bouge:
            image_rect = self.joueur_bouge.pop(0)
            image_joueur = image.subsurface(image_rect)
            image_joueur = pygame.transform.scale(image_joueur, (32, 64))
            self.joueur_bouge.append(image_joueur)

        dict["bouger"] = self.joueur_bouge

        return dict
