import random
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askinteger
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
    # vertical,horizontal,diagonal_left,diagonal_right et cliqued peuvent prendre sois 0 ou 1
    def __init__(self, vertical, horizontal, diagonal_left, diagonal_right, cliqued, line_ind, possible_V, possible_H,
                 possible_DL, possible_DR, x, y):
        # 1 si la cellule est jouer verticalement, 0 sinon
        self.vertical = vertical
        # 1 si la cellule est jouer en diagonal gauche, 0 sinon
        self.diagonal_left = diagonal_left
        # 1 si la cellule est jouer en diagonal droite, 0 sinon
        self.diagonal_right = diagonal_right
        # 1 si la cellule est jouer horizentalement, 0 sinon
        self.horizontal = horizontal
        # coordonnée i et j de la cellule
        self.x = x
        self.y = y
        # optionnel
        self.line_ind = line_ind
        # 1 si la cellule est cliqué
        self.cliqued = cliqued
        # 104 ou 115 ou 1113 ou 1331 ou 1222 si elle est jouable verticalement, 0 sinon
        self.possible_V = possible_V
        # 204 ou 215 ou 2113 ou 2331 ou 2222 si elle est jouable horizentalement, 0 sinon
        self.possible_H = possible_H
        # 304 ou 315 ou 3113 ou 3331 ou 3222 si elle est jouable en diagonal gauche (left), 0 sinon
        self.possible_DL = possible_DL
        # 404 ou 415 ou 4113 ou 4331 ou 4222 si elle est jouable diagonal droite (right), 0 sinon
        self.possible_DR = possible_DR

class Game:
    """ La classe Game contient le repértoire des cellules et lignes ainsi que les méthodes qui permetent de jouer """
    def __init__(self, taille):
        # Initialisation liste des lignes jouées
        self.rep_lines = []
        # taille du jeu taille * taille
        self.taille =taille
        # Initialisation liste des cellules
        self.rep_cellules = [[Cellule(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, i, j) for i in range(taille)] for j in range(taille)]
        self.grille_depart()
        # Initialisation liste des ligne jouables
        self.rep_playable_lines = []
        # s'il reste aucune cellule jouable
        self.crash = False
        # marge du jeu
        self.padding=5

    def grille_depart(self):
        Croix = [(9, 15), (9, 16), (9, 17), (9, 18), (10, 15), (10, 18), (11, 15), (11, 18), (12, 12), \

                 (12, 13), (12, 14), (12, 15), (12, 18), (12, 19), (12, 20), (12, 21), (13, 12), (13, 21), \
                 (14, 12), (14, 21), (15, 12), (15, 13), (15, 14), (15, 15), (15, 18), (15, 19), (15, 20), \
                 (15, 21), (16, 15), (16, 18), (17, 15), (17, 18), (18, 15), (18, 16), (18, 17), (18, 18)]
        for li, co in Croix:
            self.rep_cellules[li][co].cliqued=1

    def calculer_lignes_jouables(self):
        """ Parcourir la liste des cellules (900) et ajouter les cellules jouables dans la liste playable_cel"""
        # effacher la liste des cellules jouables
        self.rep_playable_lines.clear()
        vect=[[0,1],[1,0],[1,-1],[1,1]]
        for i in range(self.padding, self.taille-self.padding):
            for j in range(self.padding, self.taille-self.padding):
                line_v = []
                line_h=[]
                line_dl=[]
                line_dr=[]
                is_v_line=0
                is_h_line=0
                is_v_line=0
                is_dr_line=0
                is_dl_line=0
                ij_v=[]
                ij_h=[]
                ij_dl=[]
                ij_dr=[]
                ij_v.append([i,j])
                ij_h.append([i,j])
                ij_dl.append([i,j])
                ij_dr.append([i,j])
                tmp_sum_v_clic= self.rep_cellules[i][j].cliqued
                tmp_sum_h_clic= self.rep_cellules[i][j].cliqued
                tmp_sum_dl_clic= self.rep_cellules[i][j].cliqued
                tmp_sum_dr_clic= self.rep_cellules[i][j].cliqued
                tmp_sum_v=self.rep_cellules[i][j].vertical
                tmp_sum_h=self.rep_cellules[i][j].horizontal
                tmp_sum_dl=self.rep_cellules[i][j].diagonal_left
                tmp_sum_dr=self.rep_cellules[i][j].diagonal_right
                for s in range(len(vect)):
                    ij_v.append([i + vect[0][0],j + vect[0][1] + s])
                    ij_h.append([i + vect[1][0] + s, j + vect[1][1]])
                    ij_dl.append([i + vect[2][0] + s,j + vect[2][1] - s])
                    ij_dr.append([i + vect[3][0] + s, j + vect[3][1] + s])
                    tmp_sum_v_clic += self.rep_cellules[i + vect[0][0]][j + vect[0][1] + s].cliqued
                    tmp_sum_h_clic += self.rep_cellules[i + vect[1][0] + s][j + vect[1][1]].cliqued
                    tmp_sum_dl_clic += self.rep_cellules[i + vect[2][0] + s][j + vect[2][1] - s].cliqued
                    tmp_sum_dr_clic += self.rep_cellules[i + vect[3][0] + s][j + vect[3][1] + s].cliqued
                    tmp_sum_v += self.rep_cellules[i + vect[0][0]][j + vect[0][1] + s].vertical
                    tmp_sum_h += self.rep_cellules[i + vect[1][0] + s][j + vect[1][1]].horizontal
                    tmp_sum_dl += self.rep_cellules[i + vect[2][0] + s][j + vect[2][1] - s].diagonal_left
                    tmp_sum_dr += self.rep_cellules[i + vect[3][0] + s][j + vect[3][1] + s].diagonal_right
                for k in range(len(ij_v)):
                    if tmp_sum_v_clic >= 4 and tmp_sum_v==0:
                        self.rep_cellules[ij_v[k][0]][ij_v[k][1]].possible_V = 1
                        line_v.append(self.rep_cellules[ij_v[k][0]][ij_v[k][1]])
                        is_v_line=1
                    if tmp_sum_h_clic >= 4 and tmp_sum_h==0:
                        self.rep_cellules[ij_h[k][0]][ij_h[k][1]].possible_H = 1
                        line_h.append(self.rep_cellules[ij_h[k][0]][ij_h[k][1]])
                        is_h_line = 1
                    if tmp_sum_dl_clic >= 4 and tmp_sum_dl == 0:
                        self.rep_cellules[ij_dl[k][0]][ij_dl[k][1]].possible_DL = 1
                        line_dl.append(self.rep_cellules[ij_dl[k][0]][ij_dl[k][1]])
                        is_dl_line = 1
                    if tmp_sum_dr_clic >= 4 and tmp_sum_dr == 0:
                        self.rep_cellules[ij_dr[k][0]][ij_dr[k][1]].possible_DR = 1
                        line_dr.append(self.rep_cellules[ij_dr[k][0]][ij_dr[k][1]])
                        is_dr_line = 1
                if is_v_line==1 :
                    self.rep_playable_lines.append([line_v, 'v'])
                if is_h_line == 1:
                    self.rep_playable_lines.append([line_h, 'h'])
                if is_dl_line == 1 :
                    self.rep_playable_lines.append([line_dl, 'dl'])
                if is_dr_line == 1 :
                    self.rep_playable_lines.append([line_dr, 'dr'])       
    def save_list(self, liste):
        """ Enregistrer les cellules avec leurs valeurs dans le fichier solitaire.txt"""
        f = open('solitaire.txt', "w+")
        # Chaque ligne contiendra une cellule
        if (len(liste) != 0):
            for i in range(self.taille):
                for j in range(self.taille):
                    f.write("%d," % liste[i][j].vertical)
                    f.write("%d," % liste[i][j].horizontal)
                    f.write("%d," % liste[i][j].diagonal_left)
                    f.write("%d," % liste[i][j].diagonal_right)
                    f.write("%d," % liste[i][j].cliqued)
                    f.write("%d," % liste[i][j].line_ind)
                    f.write("%d," % liste[i][j].possible_V)
                    f.write("%d," % liste[i][j].possible_H)
                    f.write("%d," % liste[i][j].possible_DL)
                    f.write("%d," % liste[i][j].possible_DR)
                    f.write("%d," % liste[i][j].x)
                    f.write("%d\n" % liste[i][j].y)
        f.close()

    def read_list(self):
        """ Lire le fichier solitaire.txt qui contient toutes les cellules et les ajoutées au répétoire cellule 'rep_cellules' """
        lines=[]
        # Chaque ligne contient toutes les valeurs d'une cellule
        with open('solitaire.txt') as file:
            lines = file.readlines()
        file.close()
        for i in range(0,len(lines)):
            line=lines[i]
            cel_as_tab=line.split(",")
            cel=Cellule(0,0,0,0,0,0,0,0,0,0,0,0)
            cel.vertical=int(cel_as_tab[0])
            cel.horizontal=int(cel_as_tab[1])
            cel.diagonal_left=int(cel_as_tab[2])
            cel.diagonal_right=int(cel_as_tab[3])
            cel.cliqued=int(cel_as_tab[4])
            cel.possible_V=int(cel_as_tab[5])
            cel.possible_H=int(cel_as_tab[6])
            cel.line_ind=int(cel_as_tab[7])
            cel.possible_DL=int(cel_as_tab[8])
            cel.possible_DR=int(cel_as_tab[9])
            cel.x=int(cel_as_tab[10])
            cel.y=int(cel_as_tab[11])
            # Mise à jour du tableau de cellules
            self.rep_cellules[cel.y][cel.x]=cel
                       
    def jouer_ligne(self, ligne):
        """ Mettre ligne cliquer et jouer, cellule[i].cliqued=1 et cellule[i].direction=1 """
        if (ligne[0] is not None and ligne[1] is not None):
            for i in range(len(ligne[0])): # Parcours des 5 cellules de la ligne
                ii=ligne[0][i].y
                jj=ligne[0][i].x
                self.rep_cellules[ii][jj].cliqued=1
                if (ligne[1] == 'v'):
                    self.rep_cellules[ii][jj].vertical=1 # vertical
                if (ligne[1] == 'h'):
                    self.rep_cellules[ii][jj].horizontal=1 # horizontal
                if (ligne[1] == 'dl'):
                    self.rep_cellules[ii][jj].diagonal_left = 1 # diagonal_left
                if (ligne[1] == 'dr'):
                    self.rep_cellules[ii][jj].diagonal_right = 1 # diagonal_right

"""----- Interface graphique -----"""
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
labelbonus.grid(column=3, row=41)

def score_ihm(sc, bn):
    """ Modification du score et les points possible sur l'ihm """
    sco.set(str(sc).zfill(3))
    bns.set(str(bn).zfill(3))

def constructeur():
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

def init_ihm():
    """ initialisation de l'ihm """
    global bn, sc, xx, yy
    global Tem, curseur
    tracer.delete("all")
    xx, yy, Tem = 318, 204, []
    constructeur()
    curseur = tracer.create_polygon(xx-3,yy-3,xx+4,yy+4,xx+4,yy-3,xx-3,yy+4,xx-3,yy-3,fill="green")
    sc, bn = 0, 0, 0
    sco.set(str("").zfill(3))
    bns.set(str("").zfill(3))

def afficher_lignes_ihm(list_lines):
    """ Mettre le point (i,j) en rouge et tracer la ligne """
    for i in range(0,len(list_lines)):
        ii=list_lines[i][0][0].x # coord x point de depart ligne
        jj=list_lines[i][0][0].y # coord y point de depart ligne
        direction=list_lines[i][1] # Direction de la ligne
        tmp_pos=convert_ij_to_ihmPosition(jj,ii) # convertir (ii,jj) en distances sur l'ihm
        xx=tmp_pos[0]
        yy=tmp_pos[1]
        # placer le curseur dans les positions i et j correspendant sur l'ihm
        tracer.coords(curseur,xx-3,yy-3,xx,yy,xx,yy-3,xx-3,yy,xx-3,yy-3)
        # Créer un point rouge sur le curseur
        tracer.create_oval(xx-4, yy-4, xx+4, yy+4,fill='red', width=1)
        if(direction=='v'):
            tracer.create_line(xx,yy,xx,yy+72,fill="blue",width=2) # vertical
        elif(direction=='h'):
            tracer.create_line(xx,yy,xx,yy,xx+72,yy,fill="green",width=2)  # horizental
        elif(direction=='dl'):
            tracer.create_line(xx,yy,xx,yy,xx+72,yy-72,fill="black",width=2) # diagonal left
        elif(direction=='dr'):
            tracer.create_line(xx,yy,xx,yy,xx+72,yy+72,fill="red",width=2) # diagonal right

def convert_ij_to_ihmPosition(i,j):
    """ Convertir les position de la matrice i et j en leurs equivalent en distance sur l'IHM """
    ci=3*(18)
    cy=1*(18)
    x=((i+2.64)*18)
    y=((j+3.35)*18)
    pos=[x,y]
    return pos

def plot_seaborn(array_counter, array_score):
    """ Afficher les scores sur un plan"""
    sns.set(color_codes=True)
    ax = sns.regplot(np.array([array_counter])[0], np.array([array_score])[0], color="b", x_jitter=.1, line_kws={'color':'green'})
    ax.set(xlabel='games', ylabel='score')
    plt.show()
    
def main():
    # Initialisation du reseau
    pygame.init()
    agent = DQNAgent()
    score_plot = []
    counter_plot =[]
    record = 0
    taille=30 # Nombre de cellules = taille * taille
    init_ihm() # Initialization IHM
    max_iteration=10 # Nombre de parties
    cpt_iteration=0 # Compteur de parties
    best_score=0 # Meilleur score
    rep_lines_bestScore=[] # Liste des lignes du meilleur score
    while(cpt_iteration<max_iteration):
        game=Game(taille) # Initialisation du jeu
        nbr_lignes_crees = 0 # Nombre de lignes crées
        game.rep_lines.clear() # Mettre la liste des lignes crées à 0
        game.calculer_lignes_jouables() # Calculer les lignes possibles d'etres jouées
        while not game.crash:  # Tant qu'il reste encore des lignes possibles à jouer
            agent.epsilon = 80 - cpt_iteration
            state_old = agent.get_state(game) # get old state
            #perform random actions based on agent.epsilon, or choose the action
            if randint(0, 200) < agent.epsilon:
                final_move = to_categorical(randint(0, 2), num_classes=3)
            else: # predict action based on the old state
                prediction = agent.model.predict(state_old.reshape((1,13)))
                final_move = to_categorical(np.argmax(prediction[0]), num_classes=3)  
            if np.array_equal(final_move ,[1, 0, 0]):
                tmp_line=game.rep_playable_lines[random.randint(0,int((len(game.rep_playable_lines)-1)/3))]
            elif np.array_equal(final_move,[0, 1, 0]) : 
                tmp_line=game.rep_playable_lines[random.randint(int((len(game.rep_playable_lines)-1)/3),int((len(game.rep_playable_lines)-1)*2/3))]
            elif np.array_equal(final_move, [0, 0, 1]):  
                tmp_line=game.rep_playable_lines[random.randint(int((len(game.rep_playable_lines)-1)*2/3),int(len(game.rep_playable_lines)-1))]
            game.jouer_ligne(tmp_line) # Jouer la ligne tmp_line=[[cellule * 5],direction]
            game.rep_lines.append(tmp_line) # Ajouter la ligne à la liste des lignes jouées
            game.calculer_lignes_jouables() # Recalcule des lignes jouables
            best=0
            if(len(game.rep_lines)>best_score):
                best_score=len(game.rep_lines) # Modifier le meilleur score
                # Sauvegarder la liste des lignes du meilleur score
                rep_lines_bestScore=game.rep_lines
                best=1
            if(len(game.rep_playable_lines)==0):
                game.crash=True
            else:
                state_new = agent.get_state(game)        
                reward = agent.set_reward(game.crash,best)
                #train short memory base on the new action and state
                agent.train_short_memory(state_old, final_move, reward, state_new, game.crash)
                # store the new data into a long term memory
                agent.remember(state_old, final_move, reward, state_new, game.crash)
        print("Score: ", len(game.rep_lines), " -  Best score: ", best_score)
        score_plot.append(len(game.rep_lines))
        counter_plot.append(cpt_iteration)    
        cpt_iteration+=1
        agent.replay_new(agent.memory)
    score_ihm(max_iteration,best_score)
    agent.model.save_weights('weights.hdf5')
    plot_seaborn(counter_plot, score_plot)
    afficher_lignes_ihm(rep_lines_bestScore)

main()
