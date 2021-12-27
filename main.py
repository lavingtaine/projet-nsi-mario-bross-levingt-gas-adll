

import sys
#import time
import pygame
from pygame.sprite import Group
from joueurmario import Joueurmario
from sol import Sol
from plateforme import Plateforme
from ninja import Ninja
from projectiles import Projectile, Slash


class Jeu:
    def __init__(self):

        self.ecran = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption('Mario Jeu')
        self.jeu_encours = True
        self.joueur_x, self.joueur_y = 200, 200
        self.taille = [32, 64]
        self.joueurmario_vitesse_x = 0
        self.ninja_vitesse_x = 0
        self.joueurmario = Joueurmario(self.joueur_x,self.joueur_x,self.taille)
        self.ninja_x, self.ninja_y = 100, 400
        self.ninja_taille = [80, 60]
        self.image_ninja = pygame.image.load('tu mets le gimp')

        self.ninja = Ninja(self.joueur_x,self.joueur_y,self.ninja_taille)

        self.image_arriere_plan = pygame.image.load("lunatic-mauvais-oeil (2).jpg")
        self.arriere_plan_rect = [0, 0, 949, 693]
        self.image_mur = self.image_arriere_plan.subsurface(self.arriere_plan_rect)
        self.image_mur = pygame.transform.scale(self.image_mur, (1000, 700))

        self.image_sol_brique = pygame.image.load("solenbrique.jpg")
        self.image_sol_rect = [0, 0, 450, 300]
        self.image_sol = self.image_sol_brique.subsurface(self.image_sol_rect)
        self.image_sol = pygame.transform.scale(self.image_sol, (1000, 300))
        self.sol = Sol(self.image_sol)

        self.image_plat_rect = [0, 0, 300, 50]
        self.image_plat = self.image_sol_brique.subsurface(self.image_plat_rect)
        self.image_plat = pygame.transform.scale(self.image_plat, (300, 50))

        self.gravite = (0, 10)
        self.resistance = (0, 0)
        self.collision_sol = False

        self.horloge = pygame.time.Clock()
        self.fps = 30
        self.slash = Group()
        self.projectile = Group()
        self.t1, self.t2 = 0, 0
        self.delta_temps = 0
        # self.image_arriere_plan = pygame.image.load("background.jpg")
        # self.arriere_plan_rect = [0, 0, 893, 537]
        # self.image_ciel = self.image_arriere_plan.subsurface(self.arriere_plan_rect)
        # self.image_ciel = pygame.transform.scale(self.image_ciel, (1000, 700))



        self.projectile_groupe = Group()
        self.image_joueur = pygame.image.load("marioracaille.png")
        self.image_joueur_rect = pygame.Rect(0, 0, 111, 145)
        self.image_boule_de_feu = self.image_joueur.subsurface(self.image_joueur_rect)
        self.plateforme_groupe = Group()
        self.plateforme_liste_rect = [
        pygame.Rect(0, 550, 300, 50), pygame.Rect(700, 550, 300, 50),
        pygame.Rect(340, 400, 300, 50)
            ]
        self.slash_groupe = Group()
        self.slash_image_rect = pygame.Rect(108,232,24,43)
        self.image_ninja = pygame.image.load("ninja.png")
        self.image_ninja_rect = pygame.Rect(0, 0, 62, 144)
        self.slash_image = self.image_ninja.subsurface(self.slash_image_rect)
        self.image_slash = pygame.transform.scale(self.image_slash(30,30))
        #self.image_joueur1 = pygame.image.load("")

        #self.debut_time = 90000
        #self.bouton = pygame.image.load("play_button.png")
        #self.bouton_rect = pygame.Rect(0, 0, 148, 148)
        #self.image_bouton = self.bouton.subsurface(self.bouton_rect)
        #self.image_bouton = pygame.transform.scale(self.image_bouton, (50, 50))
        # self.image_joueur = self.image_joueur.subsurface(self.image_joueur_rect)

    def boucle_principale(self):

        dictionnaire_vide_joueur = {}
        dictionnaire_images_joueur = self.joueurmario.convertir_rect_surface(self.image_joueur, dictionnaire_vide_joueur)
        dictionnaire_vide_ninja = {}
        dictionnaire_images_ninja = self.ninja.image_liste(self.image_ninja, dictionnaire_vide_ninja)

        while self.jeu_encours:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.joueurmario_vitesse_x = 10
                        self.joueurmario.direction = 1
                        self.joueurmario.etat = "bouger"

                    if event.key == pygame.K_LEFT:
                        self.joueurmario_vitesse_x = -10
                        self.joueurmario.direction = -1
                        self.joueurmario.etat = "bouger"

                    if event.key == pygame.K_SPACE:
                        self.joueurmario.a_sauter = True
                        self.joueurmario.nombre_de_saut += 1

                    #if event.key == pygame.K_p:
                        #self.t1 = time.time()
                        #self.joueurmario.etat = 'attaque'

                    if event.key == pygame.K_e:
                        self.ninja.a_attaque = True
                        self.ninja.etat = "attaque"


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.joueurmario_vitesse_x = 0
                        self.joueurmario.etat = "debout"


                    if event.key == pygame.K_LEFT:
                        self.joueurmario_vitesse_x = 0
                        self.joueurmario.etat = "debout"

                    #if event.key == pygame.K_p:
                        #self.t2 = time.time()
                        #self.joueurmario.a_tire =  True
                        #self.joueurmario.etat = 'debout'

                    if event.key ==  pygame.K_e:
                        self.ninja.etat = 'vivant'




            if self.sol.rect.colliderect(self.joueurmario.rect):

                self.resistance = (0, -10)
                self.collision_sol = True
                self.joueurmario.nombre_de_saut = 0

            else:
                self.resistance = (0, 0)

            if self.joueurmario.a_sauter and self.collision_sol:
                if self.joueurmario.nombre_de_saut < 2:
                    self.joueurmario.sauter()

            if self.joueurmario.a_tire:
                if len (self.projectile_groupe) < self.joueurmario.tir_autorise and self.delta_temps > 0.05 :

                    projectile= Projectile ( self.joueurmario.rect.x + 20, self.joueurmario.rect.y - 5, [10, 10], self.joueurmario.direction,
                                             self.image_boule_de_feu)
                    self.projectile_groupe.remove(projectile)
                    self.joueurmario.a_tire = False

                if self.ninja.a_attaque:
                    if len(self.slash_groupe) < self.ninja.tir_autorise :
                        slash = Slash (self.ninja.rect.x + 20, self.ninja.rect.y - 5, [30, 30], self.image_slash)
                    self.slash_groupe.remove(slash)
                    self.ninja.a_attaque = False

            for projectile in self. projectile_groupe:
                projectile.mouvement(50)
                if projectile.rect.right >= self.rect.right or projectile.rect.left <= self.rect.left:
                    self.projectile_groupe.remove(projectile)

            for slash in self.slash_groupe:
                slash.mouvement(50)
                if slash.rect.right >= self.rect.right or slash.rect.left <= self.rect.left:
                    self.slash_groupe.remove(slash)


            #secondes = (self.debut_time - pygame.time.get_ticks()) // 1000

            for rectangle in self.plateforme_liste_rect:
               plateforme = Plateforme(rectangle, self.image_plat)
               self.plateforme_groupe.add(plateforme)
               if self.joueurmario.rect.midbottom[1] // 10 * 10 == plateforme.rect.top \
                       and self.joueurmario.rect.colliderect(rectangle):
                   self.resistance = (0, -10)
                   self.joueurmario.nombre_de_saut = 0



            self.delta_temps = self.t2 - self.t1
            self.ninja.mouvement(self.ninja_vitesse_x)
            self.joueurmario.mouvement(self.joueurmario_vitesse_x)
            self.gravite_jeu()
            #self.joueurmario.sauter()
            self.ecran.fill("Black")
            self.ecran.blit(self.image_mur, self.arriere_plan_rect)
            self.sol.afficher(self.ecran)
            #self.ecran.blit(self.image_ciel, self.rect)
            #self.joueurmario.rect.clamp_ip(self.rect)
            self.joueurmario.afficher(self.ecran, dictionnaire_images_joueur)
            self.ninja.afficher(self.ecran, dictionnaire_images_ninja)
            #self.horloge.tick(self.fps)
            #self.ecran.blit(self.image_bouton, (525, 20, 50, 50))
            #self.creer_message('grande', '()'.format(secondes), [535, 60, 20, 20], (255, 255, 255))
            for plateforme in self.plateforme_groupe:
                plateforme.afficher(self.ecran)


            for slash in self.slash_groupe:
                slash.afficher(self.ecran)

            pygame.display.flip()


    def gravite_jeu(self):

        self.joueurmario.rect.y += self.gravite[1] + self.resistance[1]




    #def creer_message(self, font, message, message_rectangle, couleur):
        #if font == 'petite':
            #font = pygame.font.SysFont('lato', 20, False)

        #elif font == 'moyenne':
            #font = pygame.font.SysFont('lato', 30, False)

        #elif font == 'grande':
            #font = pygame.font.SysFont('lato', 40, False)

            #message = font.render(message, True, couleur)
            #self.ecran.blit(message_rectangle)


if __name__ == '__main__':
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()
