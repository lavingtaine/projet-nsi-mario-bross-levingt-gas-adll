import sys
import time
import pygame
from pygame.sprite import Group
from joueurmario import Joueurmario
from sol import Sol
from plateforme import Plateforme
from joueurluidji import Joueurluidji
"from projectiles import Projectile"


class Jeu:
    def __init__(self):

        self.ecran = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption('Mario Jeu')
        self.jeu_encours = True
        self.joueur_x, self.joueur_y = 200, 200
        self.taille = [32, 64]
        self.joueurmario_vitesse_x = 0
        self.joueurluidji_vitesse_x = 0
        self.joueurmario = Joueurmario(self.joueur_x,self.joueur_x,self.taille)
        self.joueurluidji = Joueurluidji(self.joueur_x,self.joueur_x,self.taille)
        self.sol = Sol()
        self.gravite = (0, 10)
        self.resistance = (0, 0)
        self.collision_sol = False
        self.horloge = pygame.time.Clock()
        self.fps = 30
        # self.projectile_groupe = Group()
        # self.t1, self.t2 = 0, 0
        # self.delta_temps = 0
        # self.image_arriere_plan = pygame.image.load("background.jpg")
        # self.arriere_plan_rect = [0, 0, 893, 537]
        # self.image_ciel = self.image_arriere_plan.subsurface(self.arriere_plan_rect)
        # self.image_ciel = pygame.transform.scale(self.image_ciel, (1000, 700))
        self.plateforme_groupe = Group()
        self.plateforme_liste_rect = [
            pygame.Rect(0, 400, 300, 50), pygame.Rect(800, 400, 300, 50),
            pygame.Rect(400, 550, 300, 50)
        ]
        self.image_joueur = pygame.image.load("marioracaille.png")
        self.image_joueur_rect = pygame.Rect(0, 0, 111, 145)
        self.debut_time = 90000
        self.bouton = pygame.image.load("lepngquetuveux")
        self.replay_bouton = pygame.image.load('boutonreplay ')
        self.bouton_rect =pygame.Rect (542,501, 84, 82 )
        self.image_bouton = self.bouton.subsurface(self.bouton_rect)
        self.image_bouton = pygame.transform.scale(self.image_bouton, (50, 50))
        self.x_souris, self.y_souris = 0, 0
        self.etat_1 = False
        self.but_du_jeu = False
        # self.image_joueur = self.image_joueur.subsurface(self.image_joueur_rect)

    def boucle_principale(self):

        dictionnaire_vide = {}
        dictionnaire_images = self.joueurmario.convertir_rect_surface(self.image_joueur, dictionnaire_vide)

        while self.jeu_encours:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[3]:
                    self.x_souris, self.y_souris = pygame.mouse.get_pos()
                    print(self.x_souris, self.y_souris)

                    if (self.x_souris < 575 and self.x_souris > 525 and self.y_souris < 70 and self.y_souris > 20):
                        self.etat_1 = True
                        
                    if (self.x_souris < 59 and self.x_souris > 29 and self.y_souris < 480 and self.y_souris > 450) and self.etat_1:
                        self.but_du_jeu = True
                    
                    if (self.x_souris < 901 and self.x_souris > 851 and self.y_souris < 572 and self.y_souris > 533) and self.etat_1:
                        self.recommencer()
                        self.etat_1 = False
                        
                    
                    if (self.x_souris < 884 and self.x_souris > 855 and self.y_souris < 477 and self.y_souris > 437) and self.etat_1:
                        self.etat_1 = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.joueurmario_vitesse_x = 10
                        self.joueurmario.direction = 1
                        self.joueurmario.etat = "bouger"

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.joueurmario_vitesse_x = 0
                        self.joueurmario.etat = "debout"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.joueurmario_vitesse_x = -10
                        self.joueurmario.direction = -1
                        self.joueurmario.etat = "bouger"

                    if event.key == pygame.K_SPACE:
                        self.joueurmario.a_sauter = True
                        self.joueurmario.nombre_de_saut += 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.joueurmario_vitesse_x = 0
                        self.joueurmario.etat = "debout"

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.joueurluidji_vitesse_x = 0

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.joueurluidji_vitesse_x = 0

                    if event.key == pygame.K_a:
                        self.joueurluidji_vitesse_x = 0

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.joueurluidji_vitesse_x = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.joueurluidji_vitesse_x = -10
                        self.joueurluidji.direction = -1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.joueurluidji_vitesse_x = 10
                        self.joueurluidji.direction = 1

                    if event.key == pygame.K_w:
                        self.joueurluidji.a_sauter = True
                        self.joueurluidji.nombre_de_saut += 1


            if self.sol.rect.colliderect(self.joueurmario.rect):

                self.resistance = (0, -10)
                self.collision_sol = True
                self.joueurmario.nombre_de_saut = 0

            else:
                self.resistance = (0, 0)

            if self.joueurmario.a_sauter and self.collision_sol:
                if self.joueurmario.nombre_de_saut < 2:
                    self.joueurmario.sauter()

            secondes = ( self.debut_timer - pygame.time.get_ticks()) // 1000

            if secondes == 0:
                break
            for rectangle in self.plateforme_liste_rect:
               plateforme = Plateforme(rectangle)
               self.plateforme_groupe.add(plateforme)


               if self.joueurmario.rect.midbottom[1] // 10 * 10 == plateforme.rect.top \
                       and self.joueurmario.rect.colliderect(rectangle):
                   self.resistance = (0, -10)
                   self.joueurmario.nombre_de_saut = 0

               if self.etat_1:
                   pygame.draw.rect(self.ecran, (255, 255, 255), (0, 500, 1100, 100), 2)
                   pygame.draw.rect(self.ecran, (0, 0, 0), (0, 400, 1100, 200))
                   self.ecran_menu()
                   if self.but_du_jeu:
                       self.creer_message('petite', f" Le dernier en vie Gagne", (100, 450, 80, 80), (255, 255, 255))

            self.joueurluidji.mouvement(self.joueurluidji_vitesse_x)
            self.joueurmario.mouvement(self.joueurmario_vitesse_x)
            self.gravite_jeu()
            #self.joueurmario.sauter()
            self.ecran.fill("Black")
            self.sol.afficher(self.ecran)
            #self.ecran.blit(self.image_ciel, self.rect)
            #self.joueurmario.rect.clamp_ip(self.rect)
            self.joueurmario.afficher(self.ecran, dictionnaire_images)
            self.horloge.tick(self.fps)
            self.ecran.blit(self.image_bouton,(525, 20, 50, 50))
            self.creer_message('grande','{}'.format(secondes), [535, 60, 20, 20],(255,255,255))

            for plateforme in self.plateforme_groupe:
                plateforme.afficher(self.ecran)
            pygame.display.flip()

    def gravite_jeu(self):

        self.joueurmario.rect.y += self.gravite[1] + self.resistance[1]

    def creer_message(self, font, message, message_rectangle, couleur):
        if font == 'petite':
            font = pygame.font.Sysfont('lato', 20, False)

        elif font == 'moyenne':
            font = pygame.font.Sysfont('lato', 30, False)

        elif font =='grande':
            font = pygame.font.Sysfont('lato', 40, False)

            message = font.render(message, True, couleur)
            self.ecran.blit(message_rectangle)

            self.ecran.blit(message, message_rectangle)

    def ecran_menu (self):
        image_rect = pygame.Rect(11, 7, 69, 67)
        image_restart = self.replay_button.subsurface(image_rect)
        image_restart = pygame.transform.scale(image_restart,(50, 50))
        image_continuer_rect = pygame.Rect( 546, 274, 96, 92)
        image_continuer = self.bouton.subsurface(image_continuer_rect)
        image_continuer = pygame.transform.scale(image_continuer, (50, 50))
        image_info_rect = pygame.Rect ( 924, 432, 58, 60)
        image_info = self.bouton.subsurface(image_info_rect)
        image_info = pygame.transform.scale(image_info, (50, 50))
        
        
        self.ecran.blit(image_restart, (850, 530, 50, 50))
        self.ecran.blit(image_continuer, (850, 430, 50, 50))
        self.ecran.blit(image_info, (20, 440, 50, 50))
    
    def recommencer(self):
        
        self.joueur.vie = 100
        self.ennemie.vie = 100
        self.joueur.rect.x = 400
        self.joueur.rect.y = 100
        self.joueur.etat = 'debout'
        self.enemie.etat = 'vivant'
        



if __name__ == '__main__':
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()
