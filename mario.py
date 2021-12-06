import sys
import pygame
from joueurmario import Joueurmario
from sol import Sol

class Jeu:
    def __init__(self):

        self.ecran = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption('Mario Jeu')
        self.jeu_encours = True
        self.joueur_x, self.joueur_y = 200, 200
        self.taille = [32, 64]
        self.joueurmario_vitesse_x = 0
        self.joueurmario = Joueurmario(self.joueur_x,self.joueur_x,self.taille)
        self.sol = Sol()
        self.gravite = (0, 10)
        self.resistance = (0, 0)
        self.collision_sol = False
        self.horloge = pygame.time.Clock()
        self.fps = 30

    def boucle_principale(self):

        while self.jeu_encours:

           # dictionnaire_vide ={}
           # dictionnaire_images = self.joueurmario.convertir_rect_surface(self,image_joueur, dictionnaire_vide )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.joueurmario_vitesse_x = 10
                        self.joueurmario.etat = "bouger"

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.joueurmario_vitesse_x = 0
                        self.joueurmario.etat = "debout"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.joueurmario_vitesse_x = -10
                        self.joueurmario.etat = "bouger"

                    if event.key == pygame.K_UP:
                        self.joueurmario.a_sauter = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.joueurmario_vitesse_x = 0
                        self.joueurmario.etat = "debout"

            if self.sol.rect.colliderect(self.joueurmario.rect):
               print("collision")
               self.resistance = (-10, -10)

            else:
                self.resistance = (0,0)

            if self.joueurmario.a_sauter and self.collision_sol:
                if self.joueurmario.nombre_de_saut < 2:
                    self.joueurmario.sauter()


            self.joueurmario.mouvement(self.joueurmario_vitesse_x)
            self.gravite_jeu()
            self.joueurmario.sauter()
            self.ecran.fill("Black")
            self.sol.afficher(self.ecran)
            self.joueurmario.afficher(self.ecran)
            self.horloge.tick(self.fps)
            pygame.display.flip()

    def gravite_jeu(self):

        self.joueurmario.rect.y += self.gravite[1] + self.resistance[1]
        

if __name__ == '__main__':
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()
