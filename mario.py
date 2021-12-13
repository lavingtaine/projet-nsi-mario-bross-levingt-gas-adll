import sys, time
import pygame
from pygame.sprite import Group
from joueurmario import Joueurmario
from sol import Sol
from plateforme import Plateforme


from projectiles import Projectile


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
        #self.projectile_groupe = Group()
        #self.t1, self.t2 = 0, 0
        #self.delta_temps = 0
        self.plateforme_groupe = Group()
        self.plateforme_liste_rect = [
            pygame.Rect(0, 400, 300, 50), pygame.Rect(800, 400, 300, 50),
            pygame.Rect(400, 500, 300, 50)
        ]
        #self.image_joueur = pygame.image.load("WonderSwan WSC - MegaManEXE Heat Style.png")
        #self.image_joueur_rect =  pygame.Rect (124, 453, 8, 9)
       # self.image_joueur = self.image_joueur.subsurface(self.image_joueur_rect)


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

                self.resistance = (0, -10)

            else:
                self.resistance = (0, 0)

            if self.joueurmario.a_sauter and self.collision_sol:
                if self.joueurmario.nombre_de_saut < 2:
                    self.joueurmario.sauter()

            for rectangle in self.plateforme_liste_rect:
               plateforme = Plateforme(rectangle)
               self.plateforme_groupe.add(plateforme)
               if self.joueurmario.rect.midbottom[1] // 10 * 10 == plateforme.rect.top \
                       and self.joueurmario.rect.collidirect(rectangle):
                   self.resistance = (0, -10)
                   self.joueurmario.nombre_de_saut = 0

            self.joueurmario.mouvement(self.joueurmario_vitesse_x)
            self.gravite_jeu()
            self.joueurmario.sauter()
            self.ecran.fill("Black")
            self.sol.afficher(self.ecran)
            self.joueurmario.afficher(self.ecran)
            self.horloge.tick(self.fps)
            for plateforme in self.plateforme_groupe:
                plateforme.afficher(self.ecran)
            pygame.display.flip()

    def gravite_jeu(self):

        self.joueurmario.rect.y += self.gravite[1] + self.resistance[1]


if __name__ == '__main__':
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()
