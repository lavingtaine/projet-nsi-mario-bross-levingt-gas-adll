import pygame

class   Ninja(pygame.sprite.Sprite):

    def __init__(self, x, y, taille):

        super(Ninja, self).__init__()
        self.x = x
        self.y = y
        self.taille = taille
        self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])
        self.saut = 0
        self.saut_montee = 0
        self.saut_descente = 5
        self.nombre_de_saut = 0
        self.a_sauter = False
        self.a_attaque = False
        self.tir_autorise = 1
        self.direction = 2
        self.etat = 'vivant'
        self.index = 0

        self.ninja_vivant = [pygame.Rect(0, 0, 62, 144)]

        self.ninja_mort = [
            pygame.Rect(0, 0, 62, 144),
            pygame.Rect(67, 0, 62, 144),
            pygame.Rect(137, 0, 62, 144),
            pygame.Rect(207, 0, 62, 144),

        ]

        self.ninja_attaque= [
            pygame.Rect(0, 0, 62, 144),
            pygame.Rect(67, 0, 62, 144),
            pygame.Rect(137, 0, 62, 144),
            pygame.Rect(207, 0, 62, 144),
            pygame.Rect(207, 0, 62, 144),

        ]
        self.etat ="bouger"
        self.index = 0

        #self.ninja_saute =

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
        pygame.draw.rect(surface,("Blue"),self.rect, 1)

    def convertir_rect_surface(self, image, dict):

        for image_debout in self.ninja_vivant:

            image_rect = self.ninja_vivant.pop(0)
            image_joueur = image.subsurface(image_rect)
            image_joueur = pygame.transform.scale(image_joueur, (80, 60))
            self.ninja_vivant.append(image_joueur)

        dict['vivant'] = self.ninja_vivant

        for image_attaque in self.ninja_attaque:
            rect_joueur = self.ninja_attaque.pop(0)
            image_joueur = image.subsurface(rect_joueur)
            image_joueur = pygame.transform.scale(image_joueur, (80, 60))
            self.ninja_attaque.append(image_joueur)

        dict['ninja'] = self.ninja_attaque

        return dict

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

        for image_debout in self.ninja_debout:

            ninja_rectangle_supprime = self.ninja_debout.pop(0)
            image_ninja = image.subsurface(ninja_rectangle_supprime)
            image_ninja = pygame.transform.scale(image_ninja, (32, 64))
            self.ninja_debout.append(image_ninja)

        dict["debout"] = self.ninja_debout

        for image_mouvement in self.ninja_bouge:
            image_rect = self.ninja_bouge.pop(0)
            image_ninja = image.subsurface(image_rect)
            image_ninja = pygame.transform.scale(image_ninja, (32, 64))
            self.ninja_bouge.append(image_ninja)

        dict["bouger"] = self.ninja_bouge

        return dict
