import pygame
import math
import random


class Game:
    def __init__(self):
        self.is_playing = False



def corps(x):#pas encor adapté avec pygame
    if x == 0:
        print(" O")
        print("/|\ ")
        print(" |")
        print("/ \ ")

    if x == 1:
        print(" O")
        print("/|\ ")
        print(" |")
        print("/  ")
    if x == 2:
        print(" O")
        print("/|\ ")
        print(" |")
        print(" ")

    if x == 3:
        print(" O")
        print("/|\ ")
        print(" ")
        print(" ")

    if x == 4:
        print(" O")
        print("/| ")
        print(" ")
        print(" ")

    if x == 5:
        print(" O")
        print(" | ")
        print(" ")
        print(" ")

    if x == 6:
        print(" O")
        print(" ")
        print(" ")
        print(" ")

    if x == 7:
        print("perdu le mot etait", mot)
        exit()


mot = ""
x = 0
hp = 0

lettre = None
alphabet = ["", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
liste_mot = open("C:\Users\zerod\OneDrive\Bureau\prog\python\pendu_V2\assets\liste_francais.txt")
for i in range(random.randint(0, 22740)):
    mot = liste_mot.readline()
mot = mot.lower()
lmot = len(mot)
nmot =[]
for w in range(26):
    for i in range(lmot):
        if alphabet[w] == mot[i]:
            nmot.append(w)
            print(nmot)

playing = False
# window
pygame.display.set_caption("Le pendu")
screen = pygame.display.set_mode((1600, 1000))
#background
background = pygame.image.load('assets/bg.png')
banner = pygame.image.load('assets/banner.png')
#name
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/2.5)
banner_rect.y = math.ceil(screen.get_width()/4)
#play buton
button = pygame.image.load('assets/button.png')
button = pygame.transform.scale(button, (400, 150))
button_rect = banner.get_rect()
button_rect.x = math.ceil(screen.get_width()/2.75)
button_rect.y = math.ceil(screen.get_height()/2)
#alphabet
alphabet_a = pygame.image.load("assets/alphabet/alphabet0000.png")
alphabet_b = pygame.image.load("assets/alphabet/alphabet0001.png")
alphabet_c = pygame.image.load("assets/alphabet/alphabet0002.png")
alphabet_d = pygame.image.load("assets/alphabet/alphabet0003.png")
alphabet_e = pygame.image.load("assets/alphabet/alphabet0004.png")
alphabet_f = pygame.image.load("assets/alphabet/alphabet0005.png")
alphabet_g = pygame.image.load("assets/alphabet/alphabet0006.png")
alphabet_h = pygame.image.load("assets/alphabet/alphabet0007.png")
alphabet_i = pygame.image.load("assets/alphabet/alphabet0008.png")
alphabet_j = pygame.image.load("assets/alphabet/alphabet0009.png")
alphabet_k = pygame.image.load("assets/alphabet/alphabet0010.png")
alphabet_l = pygame.image.load("assets/alphabet/alphabet0011.png")
alphabet_m = pygame.image.load("assets/alphabet/alphabet0012.png")
alphabet_n = pygame.image.load("assets/alphabet/alphabet0013.png")
alphabet_o = pygame.image.load("assets/alphabet/alphabet0014.png")
alphabet_p = pygame.image.load("assets/alphabet/alphabet0015.png")
alphabet_q = pygame.image.load("assets/alphabet/alphabet0016.png")
alphabet_r = pygame.image.load("assets/alphabet/alphabet0017.png")
alphabet_s = pygame.image.load("assets/alphabet/alphabet0018.png")
alphabet_t = pygame.image.load("assets/alphabet/alphabet0019.png")
alphabet_u = pygame.image.load("assets/alphabet/alphabet0020.png")
alphabet_v = pygame.image.load("assets/alphabet/alphabet0021.png")
alphabet_w = pygame.image.load("assets/alphabet/alphabet0022.png")
alphabet_x = pygame.image.load("assets/alphabet/alphabet0023.png")
alphabet_y = pygame.image.load("assets/alphabet/alphabet0024.png")
alphabet_z = pygame.image.load("assets/alphabet/alphabet0025.png")
alphabet__ = pygame.image.load("assets/alphabet/alphabet0026.png")


# run
running = True
while running:

    screen.blit(background, (0, -200))
    if playing:
        for i in range(lmot-1):
            alphabet___rect = alphabet__.get_rect()
            alphabet___rect.x = math.ceil(screen.get_width() / lmot+i*100)
            alphabet___rect.y = math.ceil(screen.get_height() / 1.3)
            screen.blit(alphabet__, alphabet___rect)
            # réception des touche utilisé par le joueur (je sais pas pourquoi ca marche pas)
            for event in pygame.event.get():
                if event.type == pygame.K_a:
                    lettre = 1
                elif event.type == pygame.K_b:
                    lettre = 2
                elif event.type == pygame.K_c:
                    lettre = 3
                elif event.type == pygame.K_d:
                    lettre = 4
                elif event.type == pygame.K_e:
                    lettre = 5
                elif event.type == pygame.K_f:
                    lettre = 6
                elif event.type == pygame.K_g:
                    lettre = 7
                elif event.type == pygame.K_h:
                    lettre = 8
                elif event.type == pygame.K_i:
                    lettre = 9
                elif event.type == pygame.K_j:
                    lettre = 10
                elif event.type == pygame.K_k:
                    lettre = 11
                elif event.type == pygame.K_l:
                    lettre = 12
                elif event.type == pygame.K_m:
                    lettre = 13
                elif event.type == pygame.K_n:
                    lettre = 14
                elif event.type == pygame.K_o:
                    lettre = 15
                elif event.type == pygame.K_p:
                    lettre = 16
                elif event.type == pygame.K_q:
                    lettre = 17
                elif event.type == pygame.K_r:
                    lettre = 18
                elif event.type == pygame.K_s:
                    lettre = 19
                elif event.type == pygame.K_t:
                    lettre = 20
                elif event.type == pygame.K_u:
                    lettre = 21
                elif event.type == pygame.K_v:
                    lettre = 22
                elif event.type == pygame.K_w:
                    lettre = 23
                elif event.type == pygame.K_x:
                    lettre = 24
                elif event.type == pygame.K_y:
                    lettre = 25
                elif event.type == pygame.K_z:
                    lettre = 26
                #affichage des lettre
                for m in range(lmot-1):

                    for y in range(26):
                        if nmot[m] == lettre:
                            if y == 0:
                                alphabet_a_rect = alphabet_a.get_rect()
                                alphabet_a_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_a_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_a, alphabet_a_rect)
                            if y == 1:
                                alphabet_b_rect = alphabet_b.get_rect()
                                alphabet_b_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_b_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_b, alphabet_b_rect)
                            if y == 2:
                                alphabet_c_rect = alphabet_c.get_rect()
                                alphabet_c_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_c_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_c, alphabet_c_rect)
                            if y == 3:
                                alphabet_d_rect = alphabet_d.get_rect()
                                alphabet_d_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_d_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_d, alphabet_d_rect)
                            if y == 4:
                                alphabet_e_rect = alphabet_e.get_rect()
                                alphabet_e_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_e_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_e, alphabet_e_rect)
                            if y == 5:
                                alphabet_f_rect = alphabet_f.get_rect()
                                alphabet_f_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_f_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_f, alphabet_f_rect)
                            if y == 6:
                                alphabet_g_rect = alphabet_g.get_rect()
                                alphabet_g_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_g_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_g, alphabet_g_rect)
                            if y == 7:
                                alphabet_h_rect = alphabet_h.get_rect()
                                alphabet_h_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_h_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_h, alphabet_h_rect)
                            if y == 8:
                                alphabet_i_rect = alphabet_i.get_rect()
                                alphabet_i_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_i_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_i, alphabet_i_rect)
                            if y == 9:
                                alphabet_j_rect = alphabet_j.get_rect()
                                alphabet_j_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_j_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_i, alphabet_j_rect)
                            if y == 10:
                                alphabet_k_rect = alphabet_k.get_rect()
                                alphabet_k_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_k_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_k, alphabet_k_rect)
                            if y == 11:
                                alphabet_l_rect = alphabet_l.get_rect()
                                alphabet_l_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_l_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_l, alphabet_l_rect)
                            if y == 12:
                                alphabet_m_rect = alphabet_m.get_rect()
                                alphabet_m_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_m_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_m, alphabet_m_rect)
                            if y == 13:
                                alphabet_n_rect = alphabet_n.get_rect()
                                alphabet_n_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_n_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_n, alphabet_n_rect)
                            if y == 14:
                                alphabet_o_rect = alphabet_o.get_rect()
                                alphabet_o_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_o_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_o, alphabet_o_rect)
                            if y == 15:
                                alphabet_p_rect = alphabet_p.get_rect()
                                alphabet_p_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_p_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_p, alphabet_p_rect)
                            if y == 16:
                                alphabet_q_rect = alphabet_q.get_rect()
                                alphabet_q_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_q_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_q, alphabet_q_rect)
                            if y == 17:
                                alphabet_r_rect = alphabet_r.get_rect()
                                alphabet_r_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_r_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_r, alphabet_r_rect)
                            if y == 18:
                                alphabet_s_rect = alphabet_s.get_rect()
                                alphabet_s_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_s_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_s, alphabet_s_rect)
                            if y == 19:
                                alphabet_t_rect = alphabet_t.get_rect()
                                alphabet_t_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_t_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_t, alphabet_t_rect)
                            if y == 20:
                                alphabet_u_rect = alphabet_u.get_rect()
                                alphabet_u_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_u_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_u, alphabet_u_rect)
                            if y == 21:
                                alphabet_v_rect = alphabet_v.get_rect()
                                alphabet_v_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_v_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_v, alphabet_v_rect)
                            if y == 22:
                                alphabet_w_rect = alphabet_w.get_rect()
                                alphabet_w_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_w_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_w, alphabet_w_rect)
                            if y == 23:
                                alphabet_x_rect = alphabet_x.get_rect()
                                alphabet_x_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_x_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_x, alphabet_x_rect)
                            if y == 24:
                                alphabet_y_rect = alphabet_y.get_rect()
                                alphabet_y_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_y_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_y, alphabet_y_rect)
                            if y == 25:
                                alphabet_z_rect = alphabet_z.get_rect()
                                alphabet_z_rect.x = math.ceil(screen.get_width() / lmot + m * 100)
                                alphabet_z_rect.y = math.ceil(screen.get_height() / 1.4)
                                screen.blit(alphabet_z, alphabet_z_rect)
                                #perte de vie quand c'est faux
                            else:
                                x += 1
                            if x == lmot:
                                hp += 1
                                x = 0

#apparition du bouton sur l'écrant
    else:
        screen.blit(button, button_rect)
        screen.blit(banner, banner_rect)

    pygame.display.flip()
#stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            running = False
            pygame.quit()
# acctivation du bouton
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                playing = True


