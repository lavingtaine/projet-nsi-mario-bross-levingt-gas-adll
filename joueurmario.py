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
                self.saut_descentev= 5
                self.a_sauter = False

        self.rect.y = self.rect.y - (10*(self.saut/2))

    def convertir_rect_surface(self, image, dict):
        for image_debout in self.joueur.debout:

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

            dict["bouger"] = self.joueur_bouge
