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
        self.a_attaque_flamme = False
        self.tir_autorise = 1
        self.direction = 1

        self.ninja_debout = [
            pygame.Rect(23, 356, 42, 65),
            pygame.Rect(74, 355, 42, 65),
            pygame.Rect(124, 358, 40, 64),
            pygame.Rect(170, 360, 38, 62),
            pygame.Rect(219, 359, 38, 62),
            pygame.Rect(265, 356, 40, 65),
        ]

        self.ninja_bouge = [
            pygame.Rect(21, 608, 60, 60),
            pygame.Rect(87, 610, 49, 58),
            pygame.Rect(140, 610, 53, 57),
            pygame.Rect(198, 610, 59, 59),
            pygame.Rect(267, 610, 52, 61),
            pygame.Rect(328, 608, 54, 60),
        ]

        self.ninja_saute = [
            pygame.Rect(23, 850, 36, 67),
            pygame.Rect(135, 854, 48, 64),
            #pygame.Rect(),
        ]

        self.ninja_attaque= [
            pygame.Rect(288, 1365, 48, 55),
            pygame.Rect(344, 1367, 52, 53),
            pygame.Rect(405, 1367, 21, 54),
            pygame.Rect(471, 1367, 62, 54),
            pygame.Rect(540, 1367, 51, 54),
        ]

        self.ninja_attaque_flamme = [
            pygame.Rect(20, 4133, 70, 62),
            pygame.Rect(101, 4142, 63, 54),
            pygame.Rect(220, 4133, 86, 60),
            pygame.Rect(317, 4128, 80, 64),
            pygame.Rect(415, 4133, 76, 58),
            pygame.Rect(504, 4125, 78, 67),
            pygame.Rect(595, 4130, 96, 61),
            pygame.Rect(704, 4128, 93, 62),
            pygame.Rect(808, 4133, 79, 58),
        ]

        self.vie = 100
        self.degats_recus = 0

       #self.ninja_mort = [
            #pygame.Rect(514, 1127, 55, 52),
            #pygame.Rect(574, 1123, 52, 56),
            #pygame.Rect(679, 1126, 58, 49),
            #pygame.Rect(729, 1139, 71, 39),
            #pygame.Rect(811, 1141, 68, 40),

       # ]

        #self.ninja_mort = [
            #pygame.Rect(),
            #pygame.Rect(),
            #pygame.Rect(),
            #pygame.Rect(),

        #]

        self.etat = "debout"
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


        surface.blit(image, self.rect)
        pygame.draw.rect(surface, (0, 255, 255), self.rect, 1)
        pygame.draw.rect(surface, (255, 0, 0), (self.rect.x, self.rect.y - 20, 50, 10))
        pygame.draw.rect(surface, (0, 155, 0), (self.rect.x, self.rect.y - 20, self.vie / 2, 10))

    def sauter(self):

        if self.a_sauter:

            if self.saut_montee >= 13:
               self.saut_descente -= 1
               self.saut = self.saut_descente

            else:
                self.saut_montee += 1
                self.saut = self.saut_montee

            if self.saut_descente < 0:
                self.saut_montee = 0
                self.saut_descente = 5
                self.a_sauter = False

            self.rect.y = self.rect.y - (7 * (self.saut / 2))

    def convertir_rect_surface(self, image, dict):

        for image_debout in self.ninja_debout:

            image_rect = self.ninja_debout.pop(0)
            image_ninja = image.subsurface(image_rect)
            image_ninja = pygame.transform.scale(image_ninja, (39, 64))
            self.ninja_debout.append(image_ninja)

        dict["debout"] = self.ninja_debout

        for image_mouvement in self.ninja_bouge:
            image_rect = self.ninja_bouge.pop(0)
            image_ninja = image.subsurface(image_rect)
            image_ninja = pygame.transform.scale(image_ninja, (39, 64))
            self.ninja_bouge.append(image_ninja)

        dict["bouger"] = self.ninja_bouge

        for image_saut in self.ninja_saute:
            image_rect = self.ninja_saute.pop(0)
            image_ninja = image.subsurface(image_rect)
            image_ninja = pygame.transform.scale(image_ninja, (39, 64))
            self.ninja_saute.append(image_ninja)

        dict["saute"] = self.ninja_saute

        #for image_mort in self.ninja_mort:
          #  image_rect = self.ninja_mort.pop(0)
           # image_ninja = image.subsurface(image_rect)
          # image_ninja = pygame.transform.scale(image_ninja, (39, 64))
           # self.ninja_mort.append(image_ninja)

        #dict["mort"] = self.ninja_mort

        for image_attaque in self.ninja_attaque:
            image_rect = self.ninja_attaque.pop(0)
            image_ninja = image.subsurface(image_rect)
            image_ninja = pygame.transform.scale(image_ninja, (39, 64))
            self.ninja_attaque.append(image_ninja)

        dict["attaque"] = self.ninja_attaque

        for image_attaque_flamme in self.ninja_attaque_flamme:
            image_rect = self.ninja_attaque_flamme.pop(0)
            image_ninja = image.subsurface(image_rect)
            image_ninja = pygame.transform.scale(image_ninja, (39, 64))
            self.ninja_attaque_flamme.append(image_ninja)

        dict["attaque de flamme"] = self.ninja_attaque_flamme


        return dict
