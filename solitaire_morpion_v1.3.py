
import timeit
import random
import numpy as np
from sty import fg, bg, ef, rs
from math import *
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askinteger
from os import getcwd, sep, mkdir, path
import numpy as np

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
        #optionnel 
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
    # --- getter and setter ---
    def set_possible_V(self, val):
        self.possible_V = val

    def set_possible_H(self, val):
        self.possible_H = val

    def set_possible_DL(self, val):
        self.possible_DL = val

    def set_possible_DR(self, val):
        self.possible_DR = val

    def get_possible_V(self):
        return self.possible_V

    def get_possible_H(self):
        return self.possible_H

    def get_possible_DL(self):
        return self.possible_DL

    def get_possible_DR(self):
        return self.possible_DR

    def get_vertical(self):
        return self.vertical

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self,x):
        self.x=x

    def set_y(self,y):
        self.y=y

    def get_horizontal(self):
        return self.horizontal

    def set_horizontal(self, horizontal):
        self.horizontal = horizontal

    def set_vertical(self, vertical):
        self.vertical = vertical

    def get_diagonal_left(self):
        return self.diagonal_left

    def get_diagonal_right(self):
        return self.diagonal_right

    def set_diagonal_left(self, diagonal_l):
        self.diagonal_left = diagonal_l

    def set_diagonal_right(self, right):
        self.diagonal_right = right

    def get_cliqued(self):
        return self.cliqued

    def get_line_ind(self):
        return self.line_ind

    def set_cliqued(self, cliqued):
        self.cliqued = cliqued

    def set_line_ind(self, line_ind):
        self.line_ind = line_ind

    def to_string(self):
        string = str(self.vertical) + '+' + str(self.horizontal) + '+' + str(self.diagonal_left) + '+' + str(
            self.diagonal_right) + '+' + str(self.cliqued) + '+' + str(self.line_ind) + '+' + str(
            self.possible_V) + '+' + str(self.possible_H) + '+' + str(self.possible_DL) + '+' + str(
            self.possible_DR) + '+' + str(self.x) + '+' + str(
            self.y)
        return string


class Rep_cellules(Cellule):
    """ Classe repertoire représentant le repetoire des cellules du jeu """
    def __init__(self, cellule):
        self.cellule = cellule
        # Liste des cellules
        self.rep_cel = []

    def add_repertoire(self, cel):
        """ Ajouter une cellule à la liste rep_cel """
        tmp_rep = self.rep_cel
        tmp_rep.append(cel)
    # --- getter and setter 
    def get_rep(self):
        return self.rep_cel

    def set_rep(self, rep):
        self.rep_cel = rep

    def clear_rep(self):
        """ Effacer la liste des cellules """
        self.rep_cel.clear()

    def set_cel_rep(self, cel, ind):
        """ Modifier une cellule avec son indice dans la liste"""
        self.rep_cel[ind] = cel
        
class Line(Cellule):
    """ classe line represente une ligne jouer dans le jeu """
    def __init__(self, cel1, cel2, cel3, cel4, cel5):
        # initialisation de la liste des cellules de la ligne
        self.line_cels = []
        self.line_cels.clear()
        # Ajouter les cellules de la ligne jouer à la liste
        self.line_cels.append(cel1)
        self.line_cels.append(cel2)
        self.line_cels.append(cel3)
        self.line_cels.append(cel4)
        self.line_cels.append(cel5)
    # -- getter and setter --
    def get_line(self):
        return self.line_cels

    def set_line(self, pos, cel):
        self.line_cels[pos] = cel

    def to_string(self):
        string = str((self.line_cels[0].to_string()) + '+-+' + (self.line_cels[1].to_string()) + '+-+' + (
            self.line_cels[2].to_string()) + '+-+' + (self.line_cels[3].to_string()) + '+-+' + (
                         self.line_cels[4].to_string()))
        return string



class Rep_line(Line):
    """ Classe Rep_line represente le repertoire des lignes """
    def __init__(self, line):
        self.line = line
        # initialisation de la liste qui contient les lignes
        self.rep_line = []

    def add_line(self, l):
        """ Ajouter une ligne à la liste """
        self.rep_line.append(l)

    def get_rep_line(self):
        return self.rep_line

    def clear_rep(self):
        """ Effacer le repertoire """
        self.rep_line.clear()

class Game(Rep_cellules, Rep_line):
    """ La classe Game contient le repértoire des cellules et lignes ainsi que les méthodes qui permetent de jouer """
    def __init__(self, rep_cellule, rep_line):
        self.rep_line = rep_line
        self.rep_cellule = rep_cellule
        # Initialisation de la liste des cellules cliquées
        self.cels_occuped = []
        # Initialisation de la liste des cellules jouables
        self.cels_playable = []
        # (optionnel)
        self.tmp_cels_playable = []
        # s'il reste aucune cellule jouable
        self.crash = False
    # --- getter and setter ---
    def get_rep_cels_game(self):
        return self.rep_cellule

    def get_tmp_cels_playable(self):
        return self.tmp_cels_playable

    def set_tmp_cels_playable(self, cel):
        self.tmp_cels_playable.append(cel)

    def get_cels_occuped(self):
        return self.cels_occuped

    def get_rep_line(self):
        return self.rep_line

    def get_cels_playable(self):
        return self.cels_playable

    def add_cels_playable(self, cel):
        self.cels_playable.append(cel)

    def convert_ind_to_ij(self, ind):
        """ (Optionnel) convertir l'indice de la cellules dans la liste des cellules en des position i et j"""
        i = int(ind / 30)
        j = ind - (i * 30)
        ij = np.array([i, j])
        return ij

    def convert_ij_to_ind(self, i, j):
        """ Convertir la position i et j d'une cellule en son indice dans la liste des cellules rep_cel"""
        ind = i * 30 + j
        return ind

    def convert_ij_to_ihmPosition(self, i, j):
        """ Convertir les position i et j en distance sur l'ihm """
        ci=0
        cy=0
        x=0
        y=0
        pos=None
        ci = 16 * (-18)
        cy = 9 * (-18)
        x = ((i + 1) * 18) + ci
        y = ((j + 1) * 18) + cy
        pos = np.array([x, y])
        return pos

    def clear_rep_occuped(self):
        """ effacer la liste des cellules occupés"""
        self.rep_cel.clear()

    def clear_rep_playable(self):
        """ effacer la liste des cellules jouables"""
        self.cels_playable.clear()

    def decodeur_playable_direction_cel(self, cel, direction):
        """ Decoder comment la cellule en entrer 'cel' est jouable selon son attribut possible_ V ou H ou DL ou DR et retourner les indices de la ligne """
        # lire le fichier solitaire.txt pour ajouter les 900 cellules dans la liste rep_cel ceci afin d'assurer la mise à jour des modifications de chaque cellule
        self.read_list()
        i = cel.get_x()
        j = cel.get_y()
        ind = self.convert_ij_to_ind(i, j)
        self.rep_cellule.get_rep()
        tmp_rep = self.rep_cellule.get_rep()
        #### LES CODES ####
        # -- Vertical --
        # 104 : X0000 
        # 115 : 0000X
        # 1113: 0X000
        # 1331: 000X0
        # 1222: 00X00
        # -- Horizental --
        # 204 : X0000 
        # 215 : 0000X
        # 2113: 0X000
        # 2331: 000X0 
        # 2222: 00X00
        # -- Diagonal left --
        # 304 : X0000 
        # 315 : 0000X
        # 3113: 0X000
        # 3331: 000X0
        # 3222: 00X00
        # -- Diagonal right --
        # 404 : X0000 
        # 415 : 0000X
        # 4113: 0X000
        # 4331: 000X0
        # 4222: 00X00
        
        if (direction == 'v'):
                # -------------------line verticale --------------------------
            code = cel.get_possible_V()
            ind1 = self.convert_ij_to_ind(i + 1, j)
            ind2 = self.convert_ij_to_ind(i + 2, j)
            ind3 = self.convert_ij_to_ind(i + 3, j)
            ind4 = self.convert_ij_to_ind(i + 4, j)
            if ((self.rep_cellule.get_rep()[ind4].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                    tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0) and (
                    tmp_rep[ind].get_vertical() == 0)):
                # jouable comme suite X0000
                if (code == 104):
                    if ((tmp_rep[ind4].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                            tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                        
                        play_in_ihm(j,i,code)
                        pos = np.array([ind, ind1, ind2, ind3, ind4])
                        return pos
            ind1 = self.convert_ij_to_ind(i - 1, j)
            ind2 = self.convert_ij_to_ind(i - 2, j)
            ind3 = self.convert_ij_to_ind(i - 3, j)
            ind5 = self.convert_ij_to_ind(i - 4, j)
            if ((tmp_rep[ind5].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                    tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0) and (
                    tmp_rep[ind].get_vertical() == 0)):
                if (code == 115):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind1, ind2, ind3, ind5])
                    return pos

            if (code == 1113):
                ind1 = self.convert_ij_to_ind(i + 1, j)
                ind2 = self.convert_ij_to_ind(i + 2, j)
                ind3 = self.convert_ij_to_ind(i + 3, j)
                ind5 = self.convert_ij_to_ind(i - 1, j)
                if ((tmp_rep[ind5].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                        tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0) and (
                        tmp_rep[ind].get_vertical() == 0)):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind1, ind2, ind3, ind5])
                    return pos

            if (code == 1222):
                ind1 = self.convert_ij_to_ind(i + 1, j)
                ind2 = self.convert_ij_to_ind(i + 2, j)
                ind3 = self.convert_ij_to_ind(i - 2, j)
                ind5 = self.convert_ij_to_ind(i - 1, j)
                if ((tmp_rep[ind5].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                        tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0) and (
                        tmp_rep[ind].get_vertical() == 0)):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind1, ind2, ind3, ind5])
                    return pos
            if (code == 1331):
                ind1 = self.convert_ij_to_ind(i + 1, j)
                ind2 = self.convert_ij_to_ind(i - 2, j)
                ind3 = self.convert_ij_to_ind(i - 3, j)
                ind5 = self.convert_ij_to_ind(i - 1, j)
                if ((tmp_rep[ind5].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                        tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0) and (
                        tmp_rep[ind].get_vertical() == 0)):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind1, ind2, ind3, ind5])
                    return pos
        # ----------------- line horizentale --------------------------------------
        elif direction == "h":
            code = cel.get_possible_H()
            ind1 = self.convert_ij_to_ind(i, j + 1)
            ind2 = self.convert_ij_to_ind(i, j + 2)
            ind3 = self.convert_ij_to_ind(i, j + 3)
            ind4 = self.convert_ij_to_ind(i, j + 4)
            if ((self.rep_cellule.get_rep()[ind4].get_horizontal() == 0) and (tmp_rep[ind1].get_horizontal() == 0) and (
                    tmp_rep[ind2].get_horizontal() == 0) and (tmp_rep[ind3].get_horizontal() == 0) and (
                    tmp_rep[ind].get_horizontal() == 0)):
                if code == 204:
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind1, ind2, ind3, ind4])
                    return pos

                ind1 = self.convert_ij_to_ind(i, j - 1)
                ind2 = self.convert_ij_to_ind(i, j - 2)
                ind3 = self.convert_ij_to_ind(i, j - 3)
                ind5 = self.convert_ij_to_ind(i, j - 4)
                if (code == 215):
                    if ((tmp_rep[ind5].get_horizontal() == 0) and (tmp_rep[ind1].get_horizontal() == 0) and (
                            tmp_rep[ind2].get_horizontal() == 0) and (tmp_rep[ind3].get_horizontal() == 0) and (
                            tmp_rep[ind].get_horizontal() == 0)):
                        play_in_ihm(j,i,code)
                        pos = np.array([ind, ind1, ind2, ind3, ind5])
                        return pos

                if (code == 2113):
                    ind1 = self.convert_ij_to_ind(i, j + 1)
                    ind2 = self.convert_ij_to_ind(i, j + 2)
                    ind3 = self.convert_ij_to_ind(i, j + 3)
                    ind4 = self.convert_ij_to_ind(i, j - 1)
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind1, ind2, ind3, ind4])
                    return pos

                if (code == 2331):
                    ind1 = self.convert_ij_to_ind(i, j - 1)
                    ind2 = self.convert_ij_to_ind(i, j - 2)
                    ind3 = self.convert_ij_to_ind(i, j - 3)
                    ind4 = self.convert_ij_to_ind(i, j + 1)
                    if ((tmp_rep[ind4].get_horizontal() == 0) and (tmp_rep[ind1].get_horizontal() == 0) and (
                            tmp_rep[ind2].get_horizontal() == 0) and (tmp_rep[ind3].get_horizontal() == 0) and (
                            tmp_rep[ind].get_horizontal() == 0)):
                        play_in_ihm(j,i,code)
                        pos = np.array([ind, ind1, ind2, ind3, ind4])
                        return pos

                if (code == 2222):
                    ind1 = self.convert_ij_to_ind(i, j - 1)
                    ind2 = self.convert_ij_to_ind(i, j - 2)
                    ind3 = self.convert_ij_to_ind(i, j + 1)
                    ind4 = self.convert_ij_to_ind(i, j + 2)
                    if ((tmp_rep[ind5].get_horizontal() == 0) and (tmp_rep[ind1].get_horizontal() == 0) and (
                            tmp_rep[ind2].get_horizontal() == 0) and (tmp_rep[ind3].get_horizontal() == 0) and (
                            tmp_rep[ind].get_horizontal() == 0)):
                        play_in_ihm(j,i,code)
                        pos = np.array([ind, ind1, ind2, ind3, ind4])
                        return pos

            # -------------------- line left --------------------------------------
        elif (direction == 'dl'):
            code = cel.get_possible_DL()
            ind1 = self.convert_ij_to_ind(i - 1, j + 1)
            ind2 = self.convert_ij_to_ind(i - 2, j + 2)
            ind3 = self.convert_ij_to_ind(i - 3, j + 3)
            ind4 = self.convert_ij_to_ind(i - 4, j + 4)
            if (code == 304):
                if ((tmp_rep[ind4].get_diagonal_left() == 0) and (tmp_rep[ind1].get_diagonal_left() == 0) and (
                        tmp_rep[ind2].get_diagonal_left() == 0) and (tmp_rep[ind3].get_diagonal_left() == 0) and (
                        tmp_rep[ind].get_diagonal_left() == 0)):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind1, ind2, ind3, ind4])
                    return pos
            ind1 = self.convert_ij_to_ind(i + 1, j - 1)
            ind2 = self.convert_ij_to_ind(i + 2, j - 2)
            ind3 = self.convert_ij_to_ind(i + 3, j - 3)
            ind5 = self.convert_ij_to_ind(i + 4, j - 4)
            if (code == 315):
                if ((tmp_rep[ind5].get_diagonal_left() == 0) and (tmp_rep[ind1].get_diagonal_left() == 0) and (
                        tmp_rep[ind2].get_diagonal_left() == 0) and (tmp_rep[ind3].get_diagonal_left() == 0) and (
                        tmp_rep[ind].get_diagonal_left() == 0)):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind1, ind2, ind3, ind5])
                    return pos

            if (code == 3113):
                ind1 = self.convert_ij_to_ind(i - 1, j + 1)
                ind2 = self.convert_ij_to_ind(i - 2, j + 2)
                ind3 = self.convert_ij_to_ind(i - 3, j + 3)
                ind5 = self.convert_ij_to_ind(i + 1, j - 1)
                if ((tmp_rep[ind5].get_diagonal_left() == 0) and (tmp_rep[ind1].get_diagonal_left() == 0) and (
                        tmp_rep[ind2].get_diagonal_left() == 0) and (tmp_rep[ind3].get_diagonal_left() == 0) and (
                        tmp_rep[ind].get_diagonal_left() == 0)):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind1, ind2, ind3, ind5])
                    return pos

            if (code == 3331):
                ind1 = self.convert_ij_to_ind(i - 1, j + 1)
                ind2 = self.convert_ij_to_ind(i + 2, j - 2)
                ind3 = self.convert_ij_to_ind(i + 3, j - 3)
                ind5 = self.convert_ij_to_ind(i + 1, j - 1)
                if ((tmp_rep[ind5].get_diagonal_left() == 0) and (tmp_rep[ind1].get_diagonal_left() == 0) and (
                        tmp_rep[ind2].get_diagonal_left() == 0) and (tmp_rep[ind3].get_diagonal_left() == 0) and (
                        tmp_rep[ind].get_diagonal_left() == 0)):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind1, ind2, ind3, ind5])
                    return pos
            if (code == 3222):
                ind1 = self.convert_ij_to_ind(i + 1, j - 1)
                ind2 = self.convert_ij_to_ind(i + 2, j - 2)
                ind3 = self.convert_ij_to_ind(i - 2, j + 2)
                ind5 = self.convert_ij_to_ind(i - 1, j + 1)
                if ((tmp_rep[ind5].get_diagonal_left() == 0) and (tmp_rep[ind1].get_diagonal_left() == 0) and (
                        tmp_rep[ind2].get_diagonal_left() == 0) and (tmp_rep[ind3].get_diagonal_left() == 0) and (
                        tmp_rep[ind].get_diagonal_left() == 0)):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind1, ind2, ind3, ind5])
                    return pos
        # ------------------ line right --------------------------------------
        if (direction == 'dr'):
            code = cel.get_possible_DR()
            ind1 = self.convert_ij_to_ind(i + 1, j + 1)
            ind2 = self.convert_ij_to_ind(i + 2, j + 2)
            ind3 = self.convert_ij_to_ind(i + 3, j + 3)
            ind4 = self.convert_ij_to_ind(i + 4, j + 4)
            if (code == 404):
                if ((tmp_rep[ind4].get_diagonal_right() == 0) and (tmp_rep[ind1].get_diagonal_right() == 0) and (
                        tmp_rep[ind4].get_diagonal_right() == 0) and (tmp_rep[ind3].get_diagonal_right() == 0) and (
                        tmp_rep[ind].get_diagonal_right() == 0)):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind1, ind2, ind3, ind4])
                    return pos
            ind1 = self.convert_ij_to_ind(i - 1, j - 1)
            ind2 = self.convert_ij_to_ind(i - 2, j - 2)
            ind3 = self.convert_ij_to_ind(i - 3, j - 3)
            ind5 = self.convert_ij_to_ind(i - 4, j - 4)
            if (code == 415):
                if ((tmp_rep[ind5].get_diagonal_right() == 0) and (tmp_rep[ind1].get_diagonal_right() == 0) and (
                        tmp_rep[ind4].get_diagonal_right() == 0) and (tmp_rep[ind3].get_diagonal_right() == 0) and (
                        tmp_rep[ind].get_diagonal_right() == 0)):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind1, ind2, ind3, ind5])
                    return pos
            if (code == 4113):
                ind13 = self.convert_ij_to_ind(i - 1, j - 1)
                ind14 = self.convert_ij_to_ind(i + 3, j - 3)
                ind15 = self.convert_ij_to_ind(i + 1, j + 1)
                ind16 = self.convert_ij_to_ind(i + 2, j + 2)
                if ((tmp_rep[ind13].get_diagonal_right() == 0) and (tmp_rep[ind14].get_diagonal_right() == 0) and (
                        tmp_rep[ind15].get_diagonal_right() == 0) and (tmp_rep[ind16].get_diagonal_right() == 0) and (
                        tmp_rep[ind].get_diagonal_right() == 0)):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind13, ind14, ind15, ind16])
                    return pos
            if (code == 4222):
                ind13 = self.convert_ij_to_ind(i - 1, j - 1)
                ind14 = self.convert_ij_to_ind(i - 2, j - 2)
                ind15 = self.convert_ij_to_ind(i + 1, j + 1)
                ind16 = self.convert_ij_to_ind(i + 2, j + 2)
                if ((tmp_rep[ind13].get_diagonal_right() == 0) and (tmp_rep[ind14].get_diagonal_right() == 0) and (
                        tmp_rep[ind15].get_diagonal_right() == 0) and (tmp_rep[ind16].get_diagonal_right() == 0) and (
                        tmp_rep[ind].get_diagonal_right() == 0)):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind13, ind14, ind15, ind16])
                    return pos
            if (code == 4331):
                ind13 = self.convert_ij_to_ind(i - 1, j - 1)
                ind14 = self.convert_ij_to_ind(i - 2, j - 2)
                ind15 = self.convert_ij_to_ind(i - 3, j - 3)
                ind16 = self.convert_ij_to_ind(i + 1, j + 1)
                if ((tmp_rep[ind13].get_diagonal_right() == 0) and (tmp_rep[ind14].get_diagonal_right() == 0) and (
                        tmp_rep[ind15].get_diagonal_right() == 0) and (tmp_rep[ind16].get_diagonal_right() == 0) and (
                        tmp_rep[ind].get_diagonal_right() == 0)):
                    play_in_ihm(j,i,code)
                    pos = np.array([ind, ind13, ind14, ind15, ind16])
                    return pos

    def calculate_playable_cels(self):
        """ Parcourir la liste des cellules (900) et ajouter les cellules jouables dans la liste playable_cel"""
        #effacher la liste des cellules jouables
        self.clear_rep_playable()
        #ajouter la liste des cellules du jeu dans tmp_rep
        tmp_rep = self.rep_cellule.get_rep()
        n = len(tmp_rep)
        n = int(sqrt(n))
        for i in range(0, n - 3):
            for j in range(0, n - 3):
                # equivalent de la position de la cellule i et j en indice dans la liste des cellules
                ind = self.convert_ij_to_ind(i, j)
                ind1 = self.convert_ij_to_ind(i + 1, j)
                ind2 = self.convert_ij_to_ind(i + 2, j)
                ind3 = self.convert_ij_to_ind(i + 3, j)
                ind4 = self.convert_ij_to_ind(i + 4, j)
                try:
                    # si les 5 cellules X0000 ne sont pas deja jouer verticalement 
                    if ((tmp_rep[ind4].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                            tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0) and (
                            tmp_rep[ind].get_vertical() == 0)):
                        # si elles sont cliquer (optionnel)
                        if ((tmp_rep[ind4].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                            try:
                                # modifier l'attribut possble_V possobilité de jouer verticalement comme suite X0000 (104 est juste un code choisis)
                                self.rep_cellule.get_rep()[ind].set_possible_V(104)
                                # ajouter la cellule au reptoire des cellules jouables playable cels 
                                self.add_cels_playable(tmp_rep[ind])
                            except Exception as inst:
                                error="1"
                except Exception as inst:
                    error="1"
                ind1 = self.convert_ij_to_ind(i - 1, j)
                ind2 = self.convert_ij_to_ind(i - 2, j)
                ind3 = self.convert_ij_to_ind(i - 3, j)
                ind5 = self.convert_ij_to_ind(i - 4, j)
                try:
                    if ((tmp_rep[ind5].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                            tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)) and (
                            (tmp_rep[ind5].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                            tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0)):
                        try:
                            if tmp_rep[ind].get_vertical() == 0:
                                # 115 veut dire que la cellule est jouable verticalement en 0000X
                                self.rep_cellule.get_rep()[ind].set_possible_V(115)
                                self.add_cels_playable(tmp_rep[ind])
                        except Exception as inst:
                            error="1"
                except Exception as inst:
                    error="1"
                ind1 = self.convert_ij_to_ind(i + 1, j)
                ind2 = self.convert_ij_to_ind(i + 2, j)
                ind3 = self.convert_ij_to_ind(i + 3, j)
                ind5 = self.convert_ij_to_ind(i - 1, j)
                try:
                    if ((tmp_rep[ind5].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                            tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)) and (
                            (tmp_rep[ind5].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                            tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0)):
                        try:
                            if tmp_rep[ind].get_vertical() == 0:
                                # 1113 veut dire que la cellule est jouable verticalement en 0X000
                                self.rep_cellule.get_rep()[ind].set_possible_V(1113)
                                self.cels_playable.append(tmp_rep[ind])
                        except Exception as inst:
                            error="1"
                except Exception as inst:
                    error="1"
                ind1 = self.convert_ij_to_ind(i + 1, j)
                ind2 = self.convert_ij_to_ind(i + 2, j)
                ind3 = self.convert_ij_to_ind(i - 2, j)
                ind5 = self.convert_ij_to_ind(i - 1, j)
                try:

                    if ((tmp_rep[ind5].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                            tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)) and (
                            (tmp_rep[ind5].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                            tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0)):
                        try:
                            if tmp_rep[ind].get_vertical() == 0:
                            # 1222 veut dire que la cellule est jouable verticalement en 00X00
                                self.rep_cellule.get_rep()[ind].set_possible_V(1222)
                                self.add_cels_playable(tmp_rep[ind])
                        except Exception as inst:
                            error="1"
                except Exception as inst:
                    error="1"
                ind1 = self.convert_ij_to_ind(i + 1, j)
                ind2 = self.convert_ij_to_ind(i - 2, j)
                ind3 = self.convert_ij_to_ind(i - 3, j)
                ind5 = self.convert_ij_to_ind(i - 1, j)
                try:
                    if ((tmp_rep[ind5].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                            tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)) and (
                            (tmp_rep[ind5].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                            tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0)):
                        try:
                            if tmp_rep[ind].get_vertical() == 0:
                                # 115 veut dire que la cellule est jouable verticalement en 000X0
                                self.rep_cellule.get_rep()[ind].set_possible_V(1331)
                                self.add_cels_playable(tmp_rep[ind])
                        except Exception as inst:
                            error="1"
                except Exception as inst:
                    error="1"
                # --------------------------------- line horizentale --------------------------------------
                ind = self.convert_ij_to_ind(i, j)
                ind1 = self.convert_ij_to_ind(i, j + 1)
                ind2 = self.convert_ij_to_ind(i, j + 2)
                ind3 = self.convert_ij_to_ind(i, j + 3)
                ind5 = self.convert_ij_to_ind(i, j + 4)

                try:
                    if ((tmp_rep[ind5].get_horizontal() == 0) and (tmp_rep[ind1].get_horizontal() == 0) and (
                            tmp_rep[ind2].get_horizontal() == 0) and (tmp_rep[ind3].get_horizontal() == 0) and (
                            tmp_rep[ind].get_horizontal() == 0)):
                        if ((tmp_rep[ind5].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                            try:

                                self.rep_cellule.get_rep()[ind].set_possible_H(204)
                                self.add_cels_playable(tmp_rep[ind])

                            except Exception as inst:
                                error="1"
                except Exception as inst:
                    error="1"
                ind1 = self.convert_ij_to_ind(i, j - 1)
                ind2 = self.convert_ij_to_ind(i, j - 2)
                ind3 = self.convert_ij_to_ind(i, j - 3)
                ind5 = self.convert_ij_to_ind(i, j - 4)
                try:
                    if ((tmp_rep[ind5].get_horizontal() == 0) and (tmp_rep[ind1].get_horizontal() == 0) and (
                            tmp_rep[ind2].get_horizontal() == 0) and (tmp_rep[ind3].get_horizontal() == 0) and (
                            tmp_rep[ind].get_horizontal() == 0)):
                        if ((tmp_rep[ind5].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                            try:

                                self.rep_cellule.get_rep()[ind].set_possible_H(215)
                                self.add_cels_playable(tmp_rep[ind])
                            except Exception as inst:
                                error="1"
                except Exception as inst:
                    error="1"
                ind1 = self.convert_ij_to_ind(i, j + 1)
                ind2 = self.convert_ij_to_ind(i, j + 2)
                ind3 = self.convert_ij_to_ind(i, j + 3)
                ind4 = self.convert_ij_to_ind(i, j - 1)
                try:
                    if ((tmp_rep[ind4].get_horizontal() == 0) and (tmp_rep[ind1].get_horizontal() == 0) and (
                            tmp_rep[ind2].get_horizontal() == 0) and (tmp_rep[ind3].get_horizontal() == 0) and tmp_rep[
                        ind].get_horizontal() == 0):
                        if ((tmp_rep[ind4].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                            try:

                                self.rep_cellule.get_rep()[ind].set_possible_H(2113)
                                self.add_cels_playable(tmp_rep[ind])
                            except Exception as inst:
                                error="1"
                except Exception as inst:
                    error="1"
                ind1 = self.convert_ij_to_ind(i, j - 1)
                ind2 = self.convert_ij_to_ind(i, j - 2)
                ind3 = self.convert_ij_to_ind(i, j - 3)
                ind4 = self.convert_ij_to_ind(i, j + 1)
                try:
                    if ((tmp_rep[ind4].get_horizontal() == 0) and (tmp_rep[ind1].get_horizontal() == 0) and (
                            tmp_rep[ind2].get_horizontal() == 0) and (tmp_rep[ind3].get_horizontal() == 0) and tmp_rep[
                        ind].get_horizontal() == 0):
                        if ((tmp_rep[ind4].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                            try:

                                self.rep_cellule.get_rep()[ind].set_possible_H(2331)
                                self.add_cels_playable(tmp_rep[ind])


                            except Exception as inst:
                                error="1"
                except Exception as inst:
                    error="1"

                ind1 = self.convert_ij_to_ind(i, j - 1)
                ind2 = self.convert_ij_to_ind(i, j - 2)
                ind3 = self.convert_ij_to_ind(i, j + 1)
                ind4 = self.convert_ij_to_ind(i, j + 2)

                try:
                    if ((tmp_rep[ind4].get_horizontal() == 0) and (tmp_rep[ind1].get_horizontal() == 0) and (
                            tmp_rep[ind2].get_horizontal() == 0) and (tmp_rep[ind3].get_horizontal() == 0) and (tmp_rep[ind].get_horizontal() == 0)):
                        if ((tmp_rep[ind4].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                            try:

                                self.rep_cellule.get_rep()[ind].set_possible_H(2222)
                                self.add_cels_playable(tmp_rep[ind])

                            except Exception as inst:
                                error="1"
                except Exception as inst:
                    error="1"
                    # --------------------------------- line left --------------------------------------
                ind1 = self.convert_ij_to_ind(i - 1, j + 1)
                ind2 = self.convert_ij_to_ind(i - 2, j + 2)
                ind3 = self.convert_ij_to_ind(i - 3, j + 3)
                ind4 = self.convert_ij_to_ind(i - 4, j + 4)

                try:
                    if ((tmp_rep[ind4].get_diagonal_left() == 0) and (tmp_rep[ind1].get_diagonal_left() == 0) and (
                            tmp_rep[ind2].get_diagonal_left() == 0) and (tmp_rep[ind3].get_diagonal_left() == 0)) and (
                            ((tmp_rep[ind4].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                    tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1))):
                        try:
                            if tmp_rep[ind].get_diagonal_left() == 0:
                                self.rep_cellule.get_rep()[ind].set_possible_DL(304)
                                self.cels_playable.append(tmp_rep[ind])

                        except Exception as inst:
                            error="1"
                except Exception as inst:
                    error="1"
                    ind1 = self.convert_ij_to_ind(i + 1, j - 1)
                    ind2 = self.convert_ij_to_ind(i + 2, j - 2)
                    ind3 = self.convert_ij_to_ind(i + 3, j - 3)
                    ind5 = self.convert_ij_to_ind(i + 4, j - 4)
                    try:
                        if ((tmp_rep[ind5].get_diagonal_left() == 0) and (tmp_rep[ind1].get_diagonal_left() == 0) and (
                                tmp_rep[ind2].get_diagonal_left() == 0) and (
                                    tmp_rep[ind3].get_diagonal_left() == 0)) and (
                                ((tmp_rep[ind5].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                        tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1))):
                            try:
                                if tmp_rep[ind].get_diagonal_left() == 0:
                                    tmp_rep[ind].set_possible_DL(315)
                                    self.cels_playable.append(tmp_rep[ind])

                            except Exception as inst:
                                error="1"
                    except Exception as inst:
                        error="1"
                    ind1 = self.convert_ij_to_ind(i - 1, j + 1)
                    ind2 = self.convert_ij_to_ind(i - 2, j + 2)
                    ind3 = self.convert_ij_to_ind(i - 3, j + 3)
                    ind5 = self.convert_ij_to_ind(i + 1, j - 1)
                    try:
                        if ((tmp_rep[ind5].get_diagonal_left() == 0) and (tmp_rep[ind1].get_diagonal_left() == 0) and (
                                tmp_rep[ind2].get_diagonal_left() == 0) and (
                                    tmp_rep[ind3].get_diagonal_left() == 0)) and (
                                ((tmp_rep[ind5].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                        tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1))):
                            try:
                                if tmp_rep[ind].get_diagonal_left() == 0:
                                    self.rep_cellule.get_rep()[ind].set_possible_DL(3113)
                                    self.cels_playable.append(tmp_rep[ind])

                            except Exception as inst:
                                error="1"

                    except Exception as inst:
                        error="1"
                ind1 = self.convert_ij_to_ind(i - 1, j + 1)
                ind2 = self.convert_ij_to_ind(i + 2, j - 2)
                ind3 = self.convert_ij_to_ind(i + 3, j - 3)
                ind5 = self.convert_ij_to_ind(i + 1, j - 1)
                try:
                    if ((tmp_rep[ind5].get_diagonal_left() == 0) and (tmp_rep[ind1].get_diagonal_left() == 0) and (
                            tmp_rep[ind2].get_diagonal_left() == 0) and (tmp_rep[ind3].get_diagonal_left() == 0)):
                        if (((tmp_rep[ind5].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1))):
                            try:
                                if (tmp_rep[ind].get_diagonal_left() == 0):
                                    self.rep_cellule.get_rep()[ind].set_possible_DL(3331)
                                    self.cels_playable.append(tmp_rep[ind])
                            except Exception as inst:
                                error="1"

                except Exception as inst:
                    error="1"
                ind1 = self.convert_ij_to_ind(i + 1, j - 1)
                ind2 = self.convert_ij_to_ind(i + 2, j - 2)
                ind3 = self.convert_ij_to_ind(i - 2, j + 2)
                ind5 = self.convert_ij_to_ind(i - 1, j + 1)
                try:
                    if ((tmp_rep[ind5].get_diagonal_left() == 0) and (tmp_rep[ind1].get_diagonal_left() == 0) and (
                            tmp_rep[ind2].get_diagonal_left() == 0) and (tmp_rep[ind3].get_diagonal_left() == 0)) and (
                            ((tmp_rep[ind5].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                    tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1))):
                        try:
                            if tmp_rep[ind].get_diagonal_left() == 0:
                                self.rep_cellule.get_rep()[ind].set_possible_DL(3222)
                                self.cels_playable.append(tmp_rep[ind])
                        except Exception as inst:
                            error="1"
                except Exception as inst:
                    error="1"
                # --------------------------------- line right --------------------------------------

                ind1 = self.convert_ij_to_ind(i + 1, j + 1)
                ind2 = self.convert_ij_to_ind(i + 2, j + 2)
                ind3 = self.convert_ij_to_ind(i + 3, j + 3)
                ind4 = self.convert_ij_to_ind(i + 4, j + 4)
                try:
                    if ((tmp_rep[ind4].get_diagonal_right() == 0) and (tmp_rep[ind1].get_diagonal_right() == 0) and (
                            tmp_rep[ind2].get_diagonal_right() == 0) and (tmp_rep[ind3].get_diagonal_right() == 0)):
                        if ((tmp_rep[ind4].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):

                            if (tmp_rep[ind].get_diagonal_right() == 0):
                                self.rep_cellule.get_rep()[ind].set_possible_DR(404)
                                self.cels_playable.append(tmp_rep[ind])

                except Exception as inst:
                    error="1"

                ind1 = self.convert_ij_to_ind(i - 1, j - 1)
                ind2 = self.convert_ij_to_ind(i - 2, j - 2)
                ind3 = self.convert_ij_to_ind(i - 3, j - 3)
                ind5 = self.convert_ij_to_ind(i - 4, j - 4)
                try:
                    if ((tmp_rep[ind5].get_diagonal_right() == 0) and (tmp_rep[ind1].get_diagonal_right() == 0) and (
                            tmp_rep[ind2].get_diagonal_right() == 0) and (tmp_rep[ind3].get_diagonal_right() == 0)):
                        if (tmp_rep[ind].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1 and tmp_rep[ind].get_diagonal_right())== 0:
                            self.rep_cellule.get_rep()[ind].set_possible_DR(415)
                            self.cels_playable.append(tmp_rep[ind])
                except Exception as inst:
                    error="1"
                ind13 = self.convert_ij_to_ind(i - 1, j - 1)
                ind14 = self.convert_ij_to_ind(i - 2, j - 2)
                ind15 = self.convert_ij_to_ind(i + 1, j + 1)
                ind16 = self.convert_ij_to_ind(i + 2, j + 2)
                try:
                    if ((tmp_rep[ind13].get_diagonal_right() == 0) and (
                            tmp_rep[ind14].get_diagonal_right() == 0) and (
                            tmp_rep[ind15].get_diagonal_right() == 0) and (
                            tmp_rep[ind16].get_diagonal_right() == 0)):
                        if ((tmp_rep[ind13].get_cliqued() == 1) and (tmp_rep[ind14].get_cliqued() == 1) and (
                                tmp_rep[ind15].get_cliqued() == 1) and (tmp_rep[ind16].get_cliqued() == 1)):
                            if (tmp_rep[ind].get_diagonal_right() == 0):
                                self.rep_cellule.get_rep()[ind].set_possible_DR(4222)
                                self.cels_playable.append(tmp_rep[ind])

                except Exception as inst:
                    error="1"
                ind13 = self.convert_ij_to_ind(i - 1, j - 1)
                ind14 = self.convert_ij_to_ind(i + 3, j - 3)
                ind15 = self.convert_ij_to_ind(i + 1, j + 1)
                ind16 = self.convert_ij_to_ind(i + 2, j + 2)
                try:
                    if ((tmp_rep[ind13].get_diagonal_right() == 0) and (
                            tmp_rep[ind14].get_diagonal_right() == 0) and (
                            tmp_rep[ind15].get_diagonal_right() == 0) and (
                            tmp_rep[ind16].get_diagonal_right() == 0)):
                        if ((tmp_rep[ind13].get_cliqued() == 1) and (tmp_rep[ind14].get_cliqued() == 1) and (
                                tmp_rep[ind15].get_cliqued() == 1) and (tmp_rep[ind16].get_cliqued() == 1)) and \
                                tmp_rep()[ind].get_diagonal_right() == 0:
                            self.rep_cellule.get_rep()[ind].set_cliqued(1)
                            self.rep_cellule.get_rep()[ind].set_diagonal_right(1)
                            self.rep_cellule.get_rep()[ind13].set_diagonal_right(1)
                            self.rep_cellule.get_rep()[ind14].set_diagonal_right(1)
                            self.rep_cellule.get_rep()[ind15].set_diagonal_right(1)
                            self.rep_cellule.get_rep()[ind16].set_horizontal(1)
                            LINE = Line(self.rep_cellule.get_rep()[ind], self.rep_cellule.get_rep()[ind13],
                                        self.rep_cellule.get_rep()[ind14], self.rep_cellule.get_rep()[ind15],
                                        self.rep_cellule.get_rep()[ind16])
                            line = LINE.get_line()
                            self.rep_line.add_line(line)
                            self.rep_cellule.get_rep()[ind].set_possible_DR(4113)
                            self.cels_playable.append(tmp_rep[ind])
                except Exception as inst:
                    error="1"
                ind13 = self.convert_ij_to_ind(i - 1, j - 1)
                ind14 = self.convert_ij_to_ind(i - 2, j - 2)
                ind15 = self.convert_ij_to_ind(i - 3, j - 3)
                ind16 = self.convert_ij_to_ind(i + 1, j + 1)
                try:
                    if ((tmp_rep[ind13].get_diagonal_right() == 0) and (
                            tmp_rep[ind14].get_diagonal_right() == 0) and (
                            tmp_rep[ind15].get_diagonal_right() == 0) and (
                            tmp_rep[ind16].get_diagonal_right() == 0)):
                        if ((tmp_rep[ind13].get_cliqued() == 1) and (tmp_rep[ind14].get_cliqued() == 1) and (
                                tmp_rep[ind15].get_cliqued() == 1) and (tmp_rep[ind16].get_cliqued() == 1)) and \
                                tmp_rep[ind].get_diagonal_right() == 0:
                            self.rep_cellule.get_rep()[ind].set_possible_DR(4331)
                            self.cels_playable.append(tmp_rep[ind])
                except Exception as inst:
                    error="1"
        # Sauvegarder les cellules avec toutes les modifications faites dans le fichier 'solitaire.txt'
        self.save_list(tmp_rep)

    def save_list(self, liste):
        """ Enregistrer les cellules avec leurs valeurs dans le fichier solitaire.txt"""
        f = open('solitaire.txt', "w+")
        # Chaque ligne contiendra une cellule
        if (len(liste) != 0):
            for i in range(len(liste)):
                f.write("%d," % liste[i].get_vertical())
                f.write("%d," % liste[i].get_horizontal())
                f.write("%d," % liste[i].get_diagonal_left())
                f.write("%d," % liste[i].get_diagonal_right())
                f.write("%d," % liste[i].get_cliqued())
                f.write("%d," % liste[i].get_line_ind())
                f.write("%d," % liste[i].get_possible_V())
                f.write("%d," % liste[i].get_possible_H())
                f.write("%d," % liste[i].get_possible_DL())
                f.write("%d," % liste[i].get_possible_DR())
                f.write("%d," % liste[i].get_x())
                f.write("%d\n" % liste[i].get_y())

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
            cel.set_vertical(int(cel_as_tab[0]))
            cel.set_horizontal(int(cel_as_tab[1]))
            cel.set_diagonal_left(int(cel_as_tab[2]))
            cel.set_diagonal_right(int(cel_as_tab[3]))
            cel.set_cliqued(int(cel_as_tab[4]))
            cel.set_possible_V(int(cel_as_tab[5]))
            cel.set_possible_H(int(cel_as_tab[6]))
            cel.set_line_ind(int(cel_as_tab[7]))
            cel.set_possible_DL(int(cel_as_tab[8]))
            cel.set_possible_DR(int(cel_as_tab[9]))
            cel.set_x(int(cel_as_tab[10]))
            cel.set_y(int(cel_as_tab[11]))
            # modifier chaque cellule dans le repertoire cellule avec son indice dans la liste
            self.rep_cellule.set_cel_rep(cel,i)

    def play_line(self, cel, direction):
        """ Creer une ligne (Ajouter line à rep_lines) qui passe par la cellule cel et
mettre toutes les cellule de cette ligne en jouées dans la direction choisie"""
        # Mise à jour du répertoire cellules
        self.read_list()
        # Décoder comment la cellule 'cel' est jouable: X0000 ou 0X000 ou 00X00 ou 000X0 ou 0000X
        tab = self.decodeur_playable_direction_cel(cel, direction)
        # 'tab' contient les indices des cellules dans la liste 'rep_cellules' de la ligne qu'on veut jouer  
        if (tab is not None):
            self.rep_cellule.get_rep()[tab[0]].set_line_ind(0)
            self.rep_cellule.get_rep()[tab[1]].set_line_ind(0)
            self.rep_cellule.get_rep()[tab[2]].set_line_ind(0)
            self.rep_cellule.get_rep()[tab[3]].set_line_ind(0)
            self.rep_cellule.get_rep()[tab[4]].set_line_ind(0)
            if (direction == 'v'):
                # si la direction est vertical mettre les 5 cellules de la lignes en cliquées et jouées verticalement 
                self.rep_cellule.get_rep()[tab[1]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[2]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[3]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[4]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[0]].set_cliqued(1)

                self.rep_cellule.get_rep()[tab[0]].set_vertical(1)
                self.rep_cellule.get_rep()[tab[1]].set_vertical(1)
                self.rep_cellule.get_rep()[tab[2]].set_vertical(1)
                self.rep_cellule.get_rep()[tab[3]].set_vertical(1)
                self.rep_cellule.get_rep()[tab[4]].set_vertical(1)
                # mettre les 5 cellule, possible de jouer verticalement à 0
                self.rep_cellule.get_rep()[tab[0]].set_possible_V(0)
                self.rep_cellule.get_rep()[tab[1]].set_possible_V(0)
                self.rep_cellule.get_rep()[tab[2]].set_possible_V(0)
                self.rep_cellule.get_rep()[tab[3]].set_possible_V(0)
                self.rep_cellule.get_rep()[tab[4]].set_possible_V(0)
                # creer la ligne avec les 5 cellules 
                LINE = Line(self.rep_cellule.get_rep()[tab[0]], self.rep_cellule.get_rep()[tab[1]],
                            self.rep_cellule.get_rep()[tab[2]], self.rep_cellule.get_rep()[tab[3]],
                            self.rep_cellule.get_rep()[tab[4]])
                line = LINE.get_line()
                # ajouter la ligne crée 'line' dans le répértoire des lignes 'rep_line'
                self.rep_line.add_line(line)

            elif (direction == 'h'):
                self.rep_cellule.get_rep()[tab[0]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[1]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[2]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[3]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[4]].set_cliqued(1)

                self.rep_cellule.get_rep()[tab[1]].set_horizontal(1)
                self.rep_cellule.get_rep()[tab[2]].set_horizontal(1)
                self.rep_cellule.get_rep()[tab[3]].set_horizontal(1)
                self.rep_cellule.get_rep()[tab[4]].set_horizontal(1)
                self.rep_cellule.get_rep()[tab[0]].set_horizontal(1)

                self.rep_cellule.get_rep()[tab[0]].set_possible_H(0)
                self.rep_cellule.get_rep()[tab[1]].set_possible_H(0)
                self.rep_cellule.get_rep()[tab[2]].set_possible_H(0)
                self.rep_cellule.get_rep()[tab[3]].set_possible_H(0)
                self.rep_cellule.get_rep()[tab[4]].set_possible_H(0)
                LINE = Line(self.rep_cellule.get_rep()[tab[0]], self.rep_cellule.get_rep()[tab[1]],
                            self.rep_cellule.get_rep()[tab[2]], self.rep_cellule.get_rep()[tab[3]],
                            self.rep_cellule.get_rep()[tab[4]])
                line = LINE.get_line()
                self.rep_line.add_line(line)
            elif (direction == 'dl'):
                self.rep_cellule.get_rep()[tab[1]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[2]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[3]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[4]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[0]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[0]].set_diagonal_left(1)
                self.rep_cellule.get_rep()[tab[1]].set_diagonal_left(1)
                self.rep_cellule.get_rep()[tab[2]].set_diagonal_left(1)
                self.rep_cellule.get_rep()[tab[3]].set_diagonal_left(1)
                self.rep_cellule.get_rep()[tab[4]].set_diagonal_left(1)
                self.rep_cellule.get_rep()[tab[0]].set_possible_DL(0)
                self.rep_cellule.get_rep()[tab[1]].set_possible_DL(0)
                self.rep_cellule.get_rep()[tab[2]].set_possible_DL(0)
                self.rep_cellule.get_rep()[tab[3]].set_possible_DL(0)
                self.rep_cellule.get_rep()[tab[4]].set_possible_DL(0)
                LINE = Line(self.rep_cellule.get_rep()[tab[0]], self.rep_cellule.get_rep()[tab[1]],
                            self.rep_cellule.get_rep()[tab[2]], self.rep_cellule.get_rep()[tab[3]],
                            self.rep_cellule.get_rep()[tab[4]])
                line = LINE.get_line()
                self.rep_line.add_line(line)
            elif (direction == 'dr'):
                self.rep_cellule.get_rep()[tab[0]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[1]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[2]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[3]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[4]].set_cliqued(1)
                self.rep_cellule.get_rep()[tab[0]].set_diagonal_right(1)
                self.rep_cellule.get_rep()[tab[1]].set_diagonal_right(1)
                self.rep_cellule.get_rep()[tab[2]].set_diagonal_right(1)
                self.rep_cellule.get_rep()[tab[3]].set_diagonal_right(1)
                self.rep_cellule.get_rep()[tab[4]].set_diagonal_right(1)
                self.rep_cellule.get_rep()[tab[0]].set_possible_DR(0)
                self.rep_cellule.get_rep()[tab[1]].set_possible_DR(0)
                self.rep_cellule.get_rep()[tab[2]].set_possible_DR(0)
                self.rep_cellule.get_rep()[tab[3]].set_possible_DR(0)
                self.rep_cellule.get_rep()[tab[4]].set_possible_DR(0)
                LINE = Line(self.rep_cellule.get_rep()[tab[0]], self.rep_cellule.get_rep()[tab[1]],
                            self.rep_cellule.get_rep()[tab[2]], self.rep_cellule.get_rep()[tab[3]],
                            self.rep_cellule.get_rep()[tab[4]])
                line = LINE.get_line()
                self.rep_line.add_line(line)

            #print(self.convert_ind_to_ij(tab[0]), '+', self.convert_ind_to_ij(tab[1]), '+',
             #     self.convert_ind_to_ij(tab[2]), '+', self.convert_ind_to_ij(tab[3]), '+',
              #    self.convert_ind_to_ij(tab[4]))"""
            self.save_list(self.rep_cellule.get_rep())

    def if_cliqued(self):
        """ recherche des points déja joués et les ajoutés dans la liste rep_occ """
        # tmp_rep correspont au repertoire des cellules du jeu (900)
        tmp_rep = self.rep_cellule.get_rep()
        tmp_rep_occ = self.get_cels_occuped()
        n = len(tmp_rep)
        n = int(sqrt(n))
        # chercher pour tout les points i et j etles covertir en position de la liste et voir pour chaque cellule si son attribu cliqued==1
        for i in range(0, n):
            for j in range(0, n):
                c = 0
                ind = self.convert_ij_to_ind(i, j)
                if (tmp_rep[ind].get_cliqued() == 1):
                    for k in range(0, len(tmp_rep_occ)):
                        # test condition : print(" x: ",tmp_rep[ind].get_x()," y: ",tmp_rep[ind].get_y(), "¡¡¡¡¡¡¡¡¡¡¡¡¡¡", tmp_rep_occ[k].get_x(),"-y: ",tmp_rep_occ[k].get_x())
                        if (tmp_rep[ind].get_x() == tmp_rep_occ[k].get_x() and tmp_rep[ind].get_y() == tmp_rep_occ[
                            k].get_y()):
                            c = 1
                            break
                    if (c == 0):
                        # print('cliqued OK-->'+tmp_rep[ind].to_string())get_rep_cels_game
                        self.cels_occuped.append(tmp_rep[ind])

    def clic_cel(self, cel):
        """ Mettre la cellule cel en jouer """
        i = cel.get_x()
        j = cel.get_y()
        ind = self.convert_ij_to_ind(i, j)
        self.rep_cellule.get_rep()[ind].set_cliqued(1)

    def clear_cliqued_cel(self, cel):
        """ mettre un point jouer en non-jouer """
        i = cel.get_x()
        j = cel.get_y()
        ind = self.convert_ij_to_ind(i, j)
        tmp_r = self.rep_cellule.get_rep()
        tmp_r[ind].set_cliqued(0)

    def initialisation(self, lin, col):
        """ Initialisation du repertoire cellules avec 900 cellules vide avec leurs coordonnées i et j"""
        self.rep_cellule.clear_rep()
        for i in range(0, col):
            for j in range(0, lin):
                cel = Cellule(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, i, j)
                self.rep_cellule.add_repertoire(cel)
                
    def initialisation_first_cels(self):
        """ Ajouter tout les points jouer au repértoire cellule et peu aussi afficher (optionnel) l'etat du jeu en console"""
        # tmp_rep -> repértoire des cellule du jeu
        tmp_rep = self.rep_cellule.get_rep()
        self.if_cliqued()
        # les coordonnées des points du début du jeu
        Croix = [(9, 15), (9, 16), (9, 17), (9, 18), (10, 15), (10, 18), (11, 15), (11, 18), (12, 12), \
                 (12, 13), (12, 14), (12, 15), (12, 18), (12, 19), (12, 20), (12, 21), (13, 12), (13, 21), \
                 (14, 12), (14, 21), (15, 12), (15, 13), (15, 14), (15, 15), (15, 18), (15, 19), (15, 20), \
                 (15, 21), (16, 15), (16, 18), (17, 15), (17, 18), (18, 15), (18, 16), (18, 17), (18, 18)]

        n = len(tmp_rep)
        n = int(sqrt(n))
        for i in range(0, n):
            for j in range(0, n):
                indi = self.convert_ij_to_ind(i, j)
                ce = tmp_rep[indi]
                xx = ce.get_x()
                yy = ce.get_y()
                for li, co in Croix:
                    c = 2
                    if ((li == i and co == j) or (tmp_rep[indi].get_cliqued() == 1)):
                        #print(bg.red + ' 0 ' + bg.rs + ' ', end=" "),
                        cel = Cellule(0, 0, 0, 0, 1, 0, 0, 0, 0, 0, i, j)
                        self.rep_cellule.set_cel_rep(cel, indi)
                        c = 1
                        break
    def console(self):
        """ Affichage de l'etat du jeu en console """
        # tmp_rep -> repértoire des cellule du jeu
        tmp_rep = self.rep_cellule.get_rep()
        self.if_cliqued()
        # les coordonnées des points du début du jeu
        Croix = [(9, 15), (9, 16), (9, 17), (9, 18), (10, 15), (10, 18), (11, 15), (11, 18), (12, 12), \
                 (12, 13), (12, 14), (12, 15), (12, 18), (12, 19), (12, 20), (12, 21), (13, 12), (13, 21), \
                 (14, 12), (14, 21), (15, 12), (15, 13), (15, 14), (15, 15), (15, 18), (15, 19), (15, 20), \
                 (15, 21), (16, 15), (16, 18), (17, 15), (17, 18), (18, 15), (18, 16), (18, 17), (18, 18)]
        
        n = len(tmp_rep)
        n = int(sqrt(n))
        for i in range(0, n):
            for j in range(0, n):
                indi = self.convert_ij_to_ind(i, j)
                ce = tmp_rep[indi]
                xx = ce.get_x()
                yy = ce.get_y()
                for li, co in Croix:
                    c = 2
                    if ((li == i and co == j) or (tmp_rep[indi].get_cliqued() == 1)):
                        print(bg.red + ' 0 ' + bg.rs + ' ', end=" "),
                        cel = Cellule(0, 0, 0, 0, 1, 0, 0, 0, 0, 0, i, j)
                        self.rep_cellule.set_cel_rep(cel, indi)
                        c = 1
                        break
                f = 0
                if (c == 2):
                    # afficher en console en vert les points jouables 
                    for l in range(0, len(self.cels_playable)):
                        f = 1
                        x = self.cels_playable[l].get_x()
                        y = self.cels_playable[l].get_y()
                        if (j == y and i == x):
                            print(bg.green + " # " + bg.rs, '', end=" "),
                            f = 3
                            break
                    if (f == 1):
                        if (j == (n - 1)):
                            k=0
                            print("\n", i)
                        else:
                            if (i == 0):
                                print(" ", j, end=" "),
                                k=0
                            else:
                                k=0
                                print(" .  ", end=" "),
                                

"""----- Interface graphique -----"""
        
Fenetre = Tk()
Fenetre.title("Morpion solitaire")
Fenetre.geometry("1000x740")
Fenetre.resizable(height=False, width=False)

tracer = Canvas(Fenetre, width=800, height=700, bg='white', bd=1, relief="groove")
tracer.grid(column=0, row=2, rowspan=100)
label2 = Label(Fenetre, text="Score", font=("Arial", 10, "bold"), fg="blue")
label2.grid(column=2, row=40)
label3 = Label(Fenetre, text="Coups possibles", font=("Arial", 10, "bold"), fg="#02CC1C")
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

def score(sc,bn):
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
        y, x = li * 18 + 60, co * 18 + 48
        tracer.create_oval(x - r, y - r, x + r, y + r, fill='black', width=1)

    
def init_jeu(cas):
    """ initialisation de l'ihm """

    global bn, sc, flag, xx, yy
    global Tem, curseur, nomfich
    tracer.delete("all")
    xx, yy, Tem = 318, 204, []
    constructeur()
    curseur = tracer.create_polygon(xx - 3, yy - 3, xx + 4, yy + 4, xx + 4, yy - 3, xx - 3, yy + 4, xx - 3, yy - 3,
                                    fill="green")
    if cas == 0:
        sc, bn, flag = 0, 0, 0
    sco.set(str("").zfill(3))
    bns.set(str("").zfill(3))


class Player(object):

    def __init__(self, game):
        self.x = x - x % 20
        self.y = y - y % 20
        self.position = []
        self.position.append([self.x, self.y])
        self.food = 1
        self.eaten = False
        self.x_change = 20
        self.y_change = 0

    def update_position(self, x, y):
        if self.position[-1][0] != x or self.position[-1][1] != y:
            if self.food > 1:
                for i in range(0, self.food - 1):
                    self.position[i][0], self.position[i][1] = self.position[i]
            self.position[-1][0] = x
            self.position[-1][1] = y

    def do_move(self, move, x, y, game, food,agent):
        move_array = [self.x_change, self.y_change]
        if self.eaten:
            self.position.append([self.x, self.y])
            self.eaten = False
            self.food = self.food + 1
        if np.array_equal(move ,[1, 0, 0]):
            move_array = self.x_change, self.y_change
        elif np.array_equal(move,[0, 1, 0]) and self.y_change == 0:  # right - going horizontal
            move_array = [0, self.x_change]
        elif np.array_equal(move,[0, 1, 0]) and self.x_change == 0:  # right - going vertical
            move_array = [-self.y_change, 0]
        elif np.array_equal(move, [0, 0, 1]) and self.y_change == 0:  # left - going horizontal
            move_array = [0, -self.x_change]
        elif np.array_equal(move,[0, 0, 1]) and self.x_change == 0:  # left - going vertical
            move_array = [self.y_change, 0]
        self.x_change, self.y_change = move_array
        self.x = x + self.x_change
        self.y = y + self.y_change

        if self.x < 20 or self.x > game.game_width-40 or self.y < 20 or self.y > game.game_height-40 or [self.x, self.y] in self.position:
            game.crash = True
        eat(self, food, game)

        self.update_position(self.x, self.y)

    def display_player(self, x, y, food, game):
        self.position[-1][0] = x
        self.position[-1][1] = y

        if game.crash == False:
            for i in range(food):
                x_temp, y_temp = self.position[len(self.position) - 1 - i]
                game.gameDisplay.blit(self.image, (x_temp, y_temp))

            update_screen()
        else:
            pygame.time.wait(300)


class Food(object):

    def __init__(self):
        self.x_food = 240
        self.y_food = 200

    def food_coord(self, game, player):
        len_list_playable_cels=len(game.get_cels_playable())
        indice_rand=randit(len_list_playable_cels)
        self.x_food = game.get_cels_playable()[indice_rand].get_x()
        self.y_food = game.get_cels_playable()[indice_rand].get_y()
        if [self.x_food, self.y_food] not in player.position:
            return self.x_food, self.y_food
        else:
            self.food_coord(game,player)

    def display_food(self, x, y, game):
        game.gameDisplay.blit(self.image, (x, y))
        update_screen()

def convert_ij_to_ihmPosition(i,j):
    """ Convertir les position de la matrice i et j en leurs equivalent en distance sur l'IHM """
    ci=3*(18)
    cy=1*(18)
    x=((i+2.64)*18)
    y=((j+3.35)*18)
    pos=np.array([x,y])
    return pos


def inventaire(nbr_pos_playable, nbr_cels, nbr_occ_cels, nbr_lines):
    """ Afficher en console les valeurs en entrer """
    
    print("Nombre de positions possible à jouer  ----> ", nbr_pos_playable)
    print("Nombre de cellules ----> ", nbr_cels)
    print("Nombre de cellules occupées ----> ", nbr_occ_cels)
    print("Nombre de lignes créer ----> ", nbr_lines)

def play_in_ihm(i,j,ind):
    """ Mettre le point de coordonnées i et j en rouge sur IHM et dessiner la ligne selon l'indice ind """
    # convertir les position i et j en distances sur l'ihm
    tmp_pos=convert_ij_to_ihmPosition(i,j)
    xx=tmp_pos[0]
    yy=tmp_pos[1]
    # placer le curseur dans les positions i et j correspendant sur l'ihm
    tracer.coords(curseur,xx-3,yy-3,xx,yy,xx,yy-3,xx-3,yy,xx-3,yy-3)
    # Créer un point rouge sur le curseur
    tracer.create_oval(xx-4, yy-4, xx+4, yy+4,fill='red', width=1)
    # largeur de la ligne sur l'ihm
    w=2
    # couleurs des lignes sur l'ihm
    color1="blue"
    color2="green"
    color3="orange"
    color4="red"
    color5="black"
    # tracer la ligne sur l'ihm avec les mesures corrependantes selon le code 'ind' de la cellule
    # ------------- vertical ---------------
    """ ind c'est un code qui décris comment la cellulle est jouable """
    if(ind==104):
        """ 104 veut dire qu'elle est jouable comme suite: X 0 0 0 0 """
        tracer.create_line(xx,yy,xx,yy+72,fill=color1,width=w)
    elif(ind==115):
        """ 115 correspond à: 0 0 0 0 X """
        tracer.create_line(xx,yy,xx,yy-72,fill=color2,width=w)
    elif(ind==1113):
        """ 1113 correspond: 0 X 0 0 0 """
        tracer.create_line(xx,yy,xx,yy+54,xx,yy-18,fill='blue',width=1)
    elif(ind==1222):
        """ 1222 correspond à: 0 0 X 0 0 """
        tracer.create_line(xx,yy,xx,yy,xx-36,yy+36,fill=color4,width=w)
    elif(ind==1331):
        """ 1331 correspond à: 0 0 0 X 0 """
        tracer.create_line(xx,yy,xx,yy-54,xx,yy+18,fill=color5,width=w)
    #-------------- horizental  --------------------------
    elif(ind==204):
        """ Horizentale : X 0 0 0 0 """
        tracer.create_line(xx,yy,xx,yy,xx+72,yy,fill=color1,width=w)
    elif(ind==215):
        """ Horizentale : 0 0 0 0 X """
        tracer.create_line(xx,yy,xx,yy,xx-72,yy,fill=color2,width=w)
    elif(ind==2113):
        """ Horizentale : 0 X 0 0 0 """
        tracer.create_line(xx,yy,xx-18,yy,xx+54,yy,fill=color3,width=w)
    elif(ind==2222):
        """ Horizentale : 0 0 X 0 0 """
        tracer.create_line(xx,yy,xx-36,yy,xx+36,yy,fill=color4,width=w)
    elif(ind==2331):
        """ Horizentale : 0 0 0 X 0 """
        tracer.create_line(xx,yy,xx+18,yy,xx-54,yy,fill=color5,width=w)
    #-------------  diagonal left -----------------------
    elif(ind==304):
        """ Diagonale gauche : X 0 0 0 0 """
        tracer.create_line(xx,yy,xx,yy,xx+72,yy-72,fill=color2,width=w)
    elif(ind==315):
        """ Diagonale gauche : 0 0 0 0 X """
        tracer.create_line(xx,yy,xx,yy,xx-72,yy+72,fill=color1,width=w)
    elif(ind==3113):
        """ Diagonale gauche : 0 X 0 0 0 """
        tracer.create_line(xx,yy,xx-18,yy+18,xx+54,yy-54,fill=color5,width=w)
    elif(ind==3222):
        """ Diagonale gauche : 0 0 X 0 0 """
        tracer.create_line(xx,yy,xx-36,yy+36,xx+36,yy-36,fill=color4,width=w)
    elif(ind==3331):
        """ Diagonale gauche : 0 0 0 X 0 """
        tracer.create_line(xx,yy,xx+18,yy-18,xx-54,yy+54,fill=color3,width=w)

    #---------------- diagonal right ------------------------
    elif(ind==404):
        """ Diagonale right : X 0 0 0 0 """
        tracer.create_line(xx,yy,xx,yy,xx+72,yy+72,fill=color1,width=w)
    elif(ind==415):
        """ Diagonale right : 0 0 0 0 X """
        tracer.create_line(xx,yy,xx,yy,xx-72,yy-72,fill=color2,width=w)
    elif(ind==4113):
        """ Diagonale right : 0 X 0 0 0 """
        tracer.create_line(xx,yy,xx-18,yy-18,xx+54,yy+54,fill=color3,width=w)
    elif(ind==4222):
        """ Diagonale right : 0 0 X 0 0 """
        tracer.create_line(xx,yy,xx+36,yy+36,xx-36,yy-36,fill=color4,width=w)
    elif(ind==4331):
        """ Diagonale right : 0 0 0 X 0 """
        tracer.create_line(xx,yy,xx-54,yy-54,xx+18,yy+18,fill=color5,width=w)

def initialize_game(player, game, food, agent):
    state_init1 = agent.get_state(game, player, food)  # [0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0]
    action = [1, 0, 0]
    player.do_move(action, player.x, player.y, game, food, agent)
    state_init2 = agent.get_state(game, player, food)
    reward1 = agent.set_reward(player, game.crash)
    agent.remember(state_init1, action, reward1, state_init2, game.crash)
    agent.replay_new(agent.memory)
def play():
    """-----------------------Reseau ----------------------
    pygame.init()
    agent = DQNAgent()
    counter_games = 0
    score_plot = []
    counter_plot =[]
    record = 0
    # Perform first move
    initialize_game(player1, game, food1, agent)
    if display_option:
            display(player1, food1, game, record)
     while not game.crash:
            #agent.epsilon is set to give randomness to actions
            agent.epsilon = 80 - counter_games
            
            #get old state
            state_old = agent.get_state(game, player1, food1)
            
            #perform random actions based on agent.epsilon, or choose the action
            # reseau ----
            if randint(0, 200) < agent.epsilon:
                final_move = to_categorical(randint(0, 2), num_classes=3)
            else:
                # predict action based on the old state
                prediction = agent.model.predict(state_old.reshape((1,11)))
                final_move = to_categorical(np.argmax(prediction[0]), num_classes=3)
                
            #perform new move and get new state
            player1.do_move(final_move, player1.x, player1.y, game, food1, agent)
            state_new = agent.get_state(game, player1, food1)
            
            #set treward for the new state
            reward = agent.set_reward(player1, game.crash)
            
            #train short memory base on the new action and state
            agent.train_short_memory(state_old, final_move, reward, state_new, game.crash)
            
            # store the new data into a long term memory
            agent.remember(state_old, final_move, reward, state_new, game.crash)
            record = get_record(game.score, record)
            if display_option:
                display(player1, food1, game, record)
                pygame.time.wait(speed)
        
        agent.replay_new(agent.memory)
        counter_games += 1
        print('Game', counter_games, '      Score:', game.score)
        score_plot.append(game.score)
        counter_plot.append(counter_games)
    agent.model.save_weights('weights.hdf5')
    plot_seaborn(counter_plot, score_plot)
    """
    #--------------------------------------------------------
    # Creer une cellule
    cel = Cellule(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 7)
    # initialisation repertoire des cellules
    rep_cel = Rep_cellules(cel)
    # initalisation classe line    
    line = Line(cel, cel, cel, cel, cel)
    # initialisation du repertoire lines
    rep_line = Rep_line(line)
    # initialisation de Game avec un repertoire cellule et un repertoire ligne
    game = Game(rep_cel, rep_line)
    # donner nombre de cellule en largeur et longueur
    game.initialisation(30, 30)
    # Mettre les cellules du début du jeu en 'cliqued' et afficher en console (optionnel)
    game.initialisation_first_cels()      
    # Recherche des cellules jouables les ajoutées dans la liste rep
    game.calculate_playable_cels()
    # ajouter la liste des cellules jouables dans le repertoire 'rep_cellules_jouable'
    rep_cellules_jouables = game.get_cels_playable()
    # ajouter la liste des cellules dans rep_cellules
    rep_cellules = game.rep_cellule.get_rep()
    # initialisation du nombre de cellules jouable
    tmp_nbr_cel_jouables=0
    # tant qu'il reste des cellules jouables faire
    while (len(rep_cellules_jouables) > 0):
        ancien_nbr_ligne_creer=len(game.rep_line.get_rep_line())
        game.calculate_playable_cels()
        rep_cellules_jouables = game.get_cels_playable()
        # Parcours de la liste des cellules jouables
        for i in range(0, len(rep_cellules_jouables)):
            # Choisir aléatoirement une cellule jouable
            cellule=random.choice(rep_cellules_jouables)
            # jouer la cellule dans toutes les directions possibles
            # Vertival
            game.play_line(cellule, 'v')
            # Horizental
            game.play_line(cellule, 'h')
            # Diagonal left
            game.play_line(cellule, 'dl')
            # Diagonal right
            game.play_line(cellule, 'dr')
        # recalcule des cellules jouables    
        game.calculate_playable_cels()
        # mise à jour du repertoire cellule
        game.initialisation_first_cels()
        # afficher l'etat du jeu en console (optionnel)
        game.console()
        nouveau_nbr_ligne_creer=len(game.rep_line.get_rep_line())
        if(nouveau_nbr_ligne_creer==ancien_nbr_ligne_creer):
            break
        # Mise à jour de la liste des cellules
        game.read_list()
        try:
            # afficher en console de l'etat du jeu (optionnel)
            #inventaire(len(rep_cellules_jouable), len(rep_cellules), len(set(game.get_cels_occuped())), nouveau_nbr_ligne_creer)
            # mise à jour du nombre de cellules jouable
            tmp_nbr_cel_jouables=len(rep_cellules_jouables)
        except Exception as inst:
            error="1"
    #retourner le tableau de resultats avec le nombre de ligne creer et les positions qu'il reste à jouées         
    score = np.array([len(game.rep_line.get_rep_line()), tmp_nbr_cel_jouables])
    return score

def run():
    pygame.init()
    agent = DQNAgent()
    counter_games = 0
    score_plot = []
    counter_plot =[]
    record = 0
    while counter_games < 150:
        # Initialize classes
        game = Game(440, 440)
        player1 = game.player
        food1 = game.food

        # Perform first move
        initialize_game(player1, game, food1, agent)
        if display_option:
            display(player1, food1, game, record)

        while not game.crash:
            #agent.epsilon is set to give randomness to actions
            agent.epsilon = 80 - counter_games
            
            #get old state
            state_old = agent.get_state(game, player1, food1)
            
            #perform random actions based on agent.epsilon, or choose the action
            # reseau ----
            if randint(0, 200) < agent.epsilon:
                final_move = to_categorical(randint(0, 2), num_classes=3)
            else:
                # predict action based on the old state
                prediction = agent.model.predict(state_old.reshape((1,11)))
                final_move = to_categorical(np.argmax(prediction[0]), num_classes=3)
                
            #perform new move and get new state
            player1.do_move(final_move, player1.x, player1.y, game, food1, agent)
            state_new = agent.get_state(game, player1, food1)
            
            #set treward for the new state
            reward = agent.set_reward(player1, game.crash)
            
            #train short memory base on the new action and state
            agent.train_short_memory(state_old, final_move, reward, state_new, game.crash)
            
            # store the new data into a long term memory
            agent.remember(state_old, final_move, reward, state_new, game.crash)
            record = get_record(game.score, record)
            if display_option:
                display(player1, food1, game, record)
                pygame.time.wait(speed)
        
        agent.replay_new(agent.memory)
        counter_games += 1
        print('Game', counter_games, '      Score:', game.score)
        score_plot.append(game.score)
        counter_plot.append(counter_games)
    agent.model.save_weights('weights.hdf5')
    plot_seaborn(counter_plot, score_plot)
    
def main():
    start = timeit.default_timer()
    print("\n running ...\n")
    # initialisation ihm
    init_jeu(0)
    # resultat est un tableau qui contient 2 valeur: nbr de ligne crées et nbr de cellules jouables 
    resultat=play()
    # initialisation du nbr maxi de ligne crées
    max_nbr_lignes_crees=0
    # nombre itérations choisis
    nbr_iterations=5
    # initialisation du compteur d'itération
    cpt=0
    # chaque itération est equivalent => nombre de lignes creer est max et qu'il reste 0 cellule jouable
    while cpt<nbr_iterations:
        # Si le nombre de lignes créer est maximum depuis le début du jeu
        if(max_nbr_lignes_crees<resultat[0]):
            # modifier le meilleur score
            max_nbr_lignes_crees=resultat[0]
            # afficher le meilleur score dans l'ihm
            score(resultat[0],0)
        print(cpt, " score : ", resultat[0]," best score : ",max_nbr_lignes_crees)
        # jouer une autre partie
        resultat=play()
        cpt+=1
    # affichage ihm
    mainloop()
    end = timeit.default_timer()
    print('Temps execution  ----> ', end - start, '  secondes')

main()