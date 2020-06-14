import random
from tkinter import *
import numpy as np
import pygame
from random import randint
from DQN import DQNAgent
import numpy as np
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import seaborn as sns

class Cellule:
    """ Classe cellule représente une case du jeu """
    def __init__(self, vertical, horizontal, diagonal_left, diagonal_right, cliqued, x, y):
        self.vertical = vertical # 1 si la cellule est jouer verticalement, 0 sinon
        self.diagonal_left = diagonal_left # 1 si la cellule est jouer en diagonal gauche, 0 sinon
        self.diagonal_right = diagonal_right # 1 si la cellule est jouer en diagonal droite, 0 sinon
        self.horizontal = horizontal  # 1 si la cellule est jouer horizentalement, 0 sinon
        self.x = x # coordonnée i de la cellule
        self.y = y # coordonnée j de la cellule
        self.cliqued = cliqued # 1 si la cellule est cliqué

    def get_attribut_by_index(self, index):
        """ Retourne valeur d'un attribut de la classe cellule par sa position """
        return [self.vertical, self.horizontal, self.diagonal_left, self.diagonal_right, self.cliqued, self.x, self.y][
            index]

class Game:
    """ La classe Game contient le repértoire des cellules et lignes et lignes jouables """
    def __init__(self, taille):
        self.rep_lines = [] # Initialisation liste des lignes jouées
        self.taille = taille # taille du jeu taille * taille
        # Initialisation du tableau des cellules
        self.rep_cellules = [[Cellule(0, 0, 0, 0, 0, i, j) for i in range(taille)] for j in range(taille)]
        self.grille_depart() # Mise à jour des cellules de departs
        self.rep_playable_lines = [] # Initialisation liste des ligne jouables
        self.crash = False  # s'il reste aucune cellule jouable
        self.padding = 5 # marge du jeu
        self.Croix = []  # Liste des coordonnés cellules departs
        self.x_player=13 # coordonnée x du joueur 
        self.y_player=13 # coodronnée y du joueur 
        self.found=False # si une ligne est trouver
        self.liberte=10 # nombre de déplacement maximum du joueur pour trouver une ligne
        self.cpt_liberte=0 # compteur de déplacemment pour trouver une ligne
        self.move=[] # Dernier deplacememnt
        self.choosed_line=[] # ligne jouable choisis au hasard

    def grille_depart(self):
        """ Mise à jour des cellules de departs """
        self.Croix=[(9, 15), (9, 16), (9, 17), (9, 18), (10, 15), (10, 18), (11, 15), (11, 18), (12, 12), \
         (12, 13), (12, 14), (12, 15), (12, 18), (12, 19), (12, 20), (12, 21), (13, 12), (13, 21), \
         (14, 12), (14, 21), (15, 12), (15, 13), (15, 14), (15, 15), (15, 18), (15, 19), (15, 20), \
         (15, 21), (16, 15), (16, 18), (17, 15), (17, 18), (18, 15), (18, 16), (18, 17), (18, 18)]
        for li, co in self.Croix:
            self.rep_cellules[li][co].cliqued = 1

    def calculer_lignes_jouables(self):
        """ Parcourir du tableau de cellules et ajouter chaque 5 cellules jouables alignées dans List playable_lines"""
        self.rep_playable_lines.clear()  # effacer la liste des cellules jouables
        vect = [[0, 1], [1, 0], [1, -1], [1, 1]]  # vecteurs de deplacememnt [v, h, dl, dr]
        for i in range(self.padding, self.taille - self.padding):
            for j in range(self.padding, self.taille - self.padding):
                direction = ['v', 'h', 'dl', 'dr']
                liste_direction = {}
                for t in range(len(direction)):
                    # [line.direction], is_line_direction, [indexs_line], sum_cliqued_direction, sum_played_direction
                    liste_direction[direction[t]] = [[], 0, [], 0, 0]
                    liste_direction[direction[t]][2].append([i, j])  # add coordonnees cellule i j
                    liste_direction[direction[t]][3] = self.rep_cellules[i][j].cliqued  # init sum cliqued cellule(i,j)
                    liste_direction[direction[t]][4] = self.rep_cellules[i][j].get_attribut_by_index(t)
                for s in range(len(vect)):  # Ajouter les indices de la ligne à liste_direction[2]
                    liste_direction[direction[0]][2].append([i + vect[0][0], j + vect[0][1] + s])
                    liste_direction[direction[1]][2].append([i + vect[1][0] + s, j + vect[1][1]])
                    liste_direction[direction[2]][2].append([i + vect[2][0] + s, j + vect[2][1] - s])
                    liste_direction[direction[3]][2].append([i + vect[3][0] + s, j + vect[3][1] + s])
                    for t in range(len(vect)):
                        # Somme des cellules cliqued et jouer_direction dans liste_direction [3] et [4]
                        liste_direction[direction[t]][3] += \
                        self.rep_cellules[liste_direction[direction[t]][2][s + 1][0]][
                            liste_direction[direction[t]][2][s + 1][1]].cliqued
                        liste_direction[direction[t]][4] += \
                        self.rep_cellules[liste_direction[direction[t]][2][s + 1][0]][
                            liste_direction[direction[t]][2][s + 1][1]].get_attribut_by_index(t)
                for k in range(len(liste_direction[direction[0]][2])):
                    for t in range(len(vect)):  # Si il y a au moins 4 cellules cliqued et 5 libres_direction
                        if liste_direction[direction[t]][3] >= 4 and liste_direction[direction[t]][4] == 0:
                            liste_direction[direction[t]][0].append(
                                self.rep_cellules[liste_direction[direction[t]][2][k][0]][
                                    liste_direction[direction[t]][2][k][1]])
                            if (len(liste_direction[direction[t]][0]) == 5):  # Ajouer la ligne list des lignes jouables
                                self.rep_playable_lines.append([liste_direction[direction[t]][0], direction[t]])
                                
    def jouer_ligne(self, ligne):
        """ Mettre ligne cliquer et jouer, cellule[i].cliqued=1 et cellule[i].direction=1 """
        if (ligne[0] is not None and ligne[1] is not None):
            for i in range(len(ligne[0])):  # Parcours des 5 cellules de la ligne
                ii = ligne[0][i].y
                jj = ligne[0][i].x
                self.rep_cellules[ii][jj].cliqued = 1
                if (ligne[1] == 'v'):
                    self.rep_cellules[ii][jj].vertical = 1  # vertical
                if (ligne[1] == 'h'):
                    self.rep_cellules[ii][jj].horizontal = 1  # horizontal
                if (ligne[1] == 'dl'):
                    self.rep_cellules[ii][jj].diagonal_left = 1  # diagonal_left
                if (ligne[1] == 'dr'):
                    self.rep_cellules[ii][jj].diagonal_right = 1  # diagonal_right

"""Interface graphique """
Fenetre = Tk()
Fenetre.title("Morpion solitaire")
Fenetre.geometry("1000x740")
Fenetre.resizable(height=False, width=False)
tracer = Canvas(Fenetre, width=800, height=700, bg='white', bd=1, relief="groove")
tracer.grid(column=0, row=2, rowspan=100)
label2 = Label(Fenetre, text="Nbr parties", font=("Arial", 10, "bold"), fg="blue")
label2.grid(column=2, row=40)
label3 = Label(Fenetre, text="Meilleur score", font=("Arial", 10, "bold"), fg="#02CC1C")
label3.grid(column=2, row=41)
sco = StringVar()
sco.set(str("").zfill(3))
labelscore = Label(Fenetre, textvariable=sco)
labelscore.config(bg="white", fg='blue')
labelscore.grid(column=3, row=40)
bns = StringVar()
bns.set(str("").zfill(3))
labelbonus = Label(Fenetre, textvariable=bns)
labelbonus.config(bg="white", fg='#02CC1C')

def constructeur(game):
    """ Construction des points de départs sur l'ihm """
    global Tem, Croix
    Tem, B = [], []
    Croix = [(9, 15), (9, 16), (9, 17), (9, 18), (10, 15), (10, 18), (11, 15), (11, 18), (12, 12), \
             (12, 13), (12, 14), (12, 15), (12, 18), (12, 19), (12, 20), (12, 21), (13, 12), (13, 21), \
             (14, 12), (14, 21), (15, 12), (15, 13), (15, 14), (15, 15), (15, 18), (15, 19), (15, 20), \
             (15, 21), (16, 15), (16, 18), (17, 15), (17, 18), (18, 15), (18, 16), (18, 17), (18, 18)]
    r = 4
    for y in range(60, 667, 18):  # placement des repères
        for x in range(48, 661, 18):
            tracer.create_line(x - 1, y, x + 2, y, fill='blue', width=1)
            tracer.create_line(x, y - 1, x, y + 2, fill='blue', width=1)
            B.append((0, 256))
        Tem.append(B)
        B = []
    for li, co in Croix:  # placement des croix initiales et initialisation
        Tem[li][co] = (1, 256)
        y, x = co * 18 + 60, li * 18 + 48
        tracer.create_oval(x - r, y - r, x + r, y + r, fill='black', width=1)
def init_ihm(game):
    """ initialisation de l'ihm """
    global bn, sc, xx, yy
    global Tem, curseur
    tracer.delete("all")
    xx, yy, Tem = 318, 204, []
    constructeur(game)
    curseur = tracer.create_polygon(xx-3,yy-3,xx+4,yy+4,xx+4,yy-3,xx-3,yy+4,xx-3,yy-3,fill="green")
    sco.set(str("").zfill(3))
    bns.set(str("").zfill(3))

def afficher_lignes_ihm(list_lines,sc, bn):
    """ list_lines=[[5*cellule], 'Direction'] => Point(i,j)=(cel[0].X,cel[0].Y) rouge + tracer la ligne en Direction"""
    sco.set(str(sc).zfill(3))  # Nombre de parties
    bns.set(str(bn).zfill(3))  # Meilleur score
    for i in range(0,len(list_lines)):
        ii=list_lines[i][0][0].x # coord x cellule de depart de la ligne
        jj=list_lines[i][0][0].y # coord y cellule de depart de la ligne
        direction=list_lines[i][1] # Direction de la ligne
        xx = ((jj + 2.64) * 18) # convertir ii=cellule.X en distance axe y ihm
        yy = ((ii + 3.35) * 18) # convertir jj=cellule.Y en distance axe x ihm
        tracer.coords(curseur,xx-3,yy-3,xx,yy,xx,yy-3,xx-3,yy,xx-3,yy-3)  # placer le curseur dans  i et j de l'ihm
        tracer.create_oval(xx-4, yy-4, xx+4, yy+4,fill='red', width=1) # Déssiné un point rouge sur le curseur width=1
        if(direction=='v'): # Déssiné la ligne selon sa direction
            tracer.create_line(xx,yy,xx,yy+72,fill="blue",width=2) # si vertical
        elif(direction=='h'):
            tracer.create_line(xx,yy,xx,yy,xx+72,yy,fill="green",width=2)  # si horizental
        elif(direction=='dl'):
            tracer.create_line(xx,yy,xx,yy,xx+72,yy-72,fill="black",width=2) # si diagonal left
        elif(direction=='dr'):
            tracer.create_line(xx,yy,xx,yy,xx+72,yy+72,fill="red",width=2) # si diagonal right

def plot_seaborn(array_counter, array_score):
    """ Afficher les scores sur un plan, axe x = partie , axe y = score """
    sns.set(color_codes=True)
    ax = sns.regplot(np.array([array_counter])[0],np.array([array_score])[0],color="b",x_jitter=.1,line_kws={'color':'green'})
    ax.set(xlabel='games', ylabel='score')
    plt.show()

def main():
    # Initialisation du reseau
    agent = DQNAgent()
    taille = 30  # Nombre de cellules = taille * taille
    game = Game(taille)  # Initialisation du jeu
    init_ihm(game)  # Initialization IHM
    max_iteration, cpt_iteration = 200, 0  # Nombre de parties à jouer et Compteur de parties
    rep_lines_bestScore, score_plot, counter_plot = [], [], []  # scores, numéros de parties, lignes du meilleur score
    while (cpt_iteration < max_iteration):
        game = Game(taille)  # Initialisation du jeu
        game.calculer_lignes_jouables()  # Calculer les lignes possibles d'etres jouées
        if len(game.rep_playable_lines)>1: # choisir une ligne parmis les lignes jouable au hasard 
            game.choosed_line=game.rep_playable_lines[random.randint(0,len(game.rep_playable_lines)-1)]
        elif len(game.rep_playable_lines)!=0:
            game.choosed_line=game.rep_playable_lines[0]
        while not game.crash and game.cpt_liberte<game.liberte:  # Tant qu'il reste encore des lignes possibles à jouer
            agent.epsilon = 120 - cpt_iteration
            state_old = agent.get_state(game)  # get old state
            # perform random actions based on agent.epsilon, or choose the action
            if randint(0, 200) < agent.epsilon:
                final_move = to_categorical(randint(0, 4), num_classes=8)
            else:  # predict action based on the old state
                prediction = agent.model.predict(state_old.reshape((1, 80)))
                final_move = to_categorical(np.argmax(prediction[0]), num_classes=8)
            game.move=final_move
            vect_move=[] # liste des sorties possibles
            vect_squar=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
            for i in range(len(vect_squar)):
                vect_move.append([0, 0, 0, 0, 0, 0, 0, 0]) # initialisation des sorties
            for i in range(len(vect_squar)):
                vect_move[i][i]=1  # Matrice identité 8*8
            for i in range(len(vect_move)):
                if vect_move[i]==final_move.tolist(): # à quel sortie correspond le final_move
                    game.x_player=int(game.x_player+vect_squar[i][0]) # deplacer le jouer d'après la sortie indiqué par final_move
                    game.y_player=int(game.y_player+vect_squar[i][1])
                    game.move=vect_move[i] # sauvegarder mouvememnt
            game.found=False
            for i in range(len(game.rep_playable_lines)-1): # si une ligne jouable commence par la position du joueur
                if len(game.rep_playable_lines)!=0 and game.rep_playable_lines[i][0][0].x==game.x_player and game.rep_playable_lines[i][0][0].y==game.y_player:
                    game.found=True
                    game.jouer_ligne(game.rep_playable_lines[i])  # Jouer la ligne tmp_line=[[cellule * 5],direction]
                    game.rep_lines.append(game.rep_playable_lines[i])  # Ajouter la ligne à la liste des lignes jouées
                    game.calculer_lignes_jouables()  # Recalcule des lignes jouables
                    if cpt_iteration == 0 or len(game.rep_lines) > max(score_plot):
                        rep_lines_bestScore = game.rep_lines  # Sauvegarder la liste des lignes du meilleur score
                    state_new = agent.get_state(game)
                    reward = agent.set_reward(len(game.rep_playable_lines), game.found)
                    # train short memory base on the new action and state
                    agent.train_short_memory(state_old, final_move, reward, state_new, game.crash)
                    # store the new data into a long term memory
                    agent.remember(state_old, final_move, reward, state_new, game.crash)
                    game.cpt_liberte=0
                    break                    
            if len(game.rep_playable_lines)==0: # s'il reste plus de lignes jouables
                game.crash=True
                state_new = agent.get_state(game) 
                reward = agent.set_reward(0, game.found) 
                # train short memory base on the new action and state
                agent.train_short_memory(state_old, final_move, reward, state_new, game.crash)
                # store the new data into a long term memory
                agent.remember(state_old, final_move, reward, state_new, game.crash)
            elif game.cpt_liberte>game.liberte-2 and not game.found:
                game.x_player=13 # retourr à la case de départ
                game.y_player=13
                game.crash=True
                game.found=False
                state_new = agent.get_state(game)
                reward = agent.set_reward(0, game.found)
                # train short memory base on the new action and state
                agent.train_short_memory(state_old, final_move, reward, state_new, game.crash)
                # store the new data into a long term memory
                agent.remember(state_old, final_move, reward, state_new, game.crash)
            elif game.found==False:
                game.cpt_liberte+=1
        if cpt_iteration == 0 or len(game.rep_lines) > max(score_plot):  # Si c'est le meilleur score atteint
            rep_lines_bestScore = game.rep_lines  # Sauvegarder la liste des lignes du meilleur score
        score_plot.append(len(game.rep_lines))  # Ajouter le score à la liste des scores
        cpt_iteration += 1 # augmenter le nombre de partie
        print(cpt_iteration, "-Score: ", len(game.rep_lines), " -  Best score: ", max(score_plot))
        counter_plot.append(cpt_iteration)  # ajouter le numéro de la partie
        agent.replay_new(agent.memory)
    afficher_lignes_ihm(rep_lines_bestScore,max_iteration,max(score_plot)) # afficher dans l'ihm les lignes du meilleur score
    plot_seaborn(counter_plot, score_plot) # afficher le shéma des scores selon les parties
    mainloop()

main()
