import timeit
import random
import numpy as np
from math import *
from sty import fg, bg, ef, rs
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askinteger
from os import getcwd, sep, mkdir, path
import numpy as np


# ---------------------------------   Classe cellule représente une case du jeu   --------------------------------------

class Cellule:
    # vertical,horizontal,diagonal_left,diagonal_right et cliqued SONT DES BOOL
    def __init__(self, vertical, horizontal, diagonal_left, diagonal_right, cliqued, line_ind, possible_V, possible_H,
                 possible_DL, possible_DR, x, y):
        self.vertical = vertical
        self.diagonal_left = diagonal_left
        self.diagonal_right = diagonal_right
        self.horizontal = horizontal
        self.x = x
        self.y = y
        self.line_ind = line_ind
        self.cliqued = cliqued
        self.possible_V = possible_V
        self.possible_H = possible_H
        self.possible_DL = possible_DL
        self.possible_DR = possible_DR

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


# -------------------------------- Classe repertoire représente le repetoire des cellule du jeu   ----------------------
class Rep_cellules(Cellule):
    def __init__(self, cellule):
        self.cellule = cellule
        self.rep_cel = []

    def add_repertoire(self, cel):
        tmp_rep = self.rep_cel
        tmp_rep.append(cel)

    def get_rep(self):
        return self.rep_cel

    def set_rep(self, rep):
        self.rep_cel = rep

    def clear_rep(self):
        self.rep_cel.clear()

    def set_cel_rep(self, cel, ind):
        self.rep_cel[ind] = cel


# -------------------------------------------------    classe Ligne    ------------------------------------------------

class Line(Cellule):
    def __init__(self, cel1, cel2, cel3, cel4, cel5):
        self.line_cels = []
        self.line_cels.clear()
        self.line_cels.append(cel1)
        self.line_cels.append(cel2)
        self.line_cels.append(cel3)
        self.line_cels.append(cel4)
        self.line_cels.append(cel5)

    def get_line(self):
        return self.line_cels

    def set_line(self, pos, cel):
        self.line_cels[pos] = cel

    def to_string(self):
        string = str((self.line_cels[0].to_string()) + '+-+' + (self.line_cels[1].to_string()) + '+-+' + (
            self.line_cels[2].to_string()) + '+-+' + (self.line_cels[3].to_string()) + '+-+' + (
                         self.line_cels[4].to_string()))
        return string


# -------------------------------------------------    Repertoire des lignes    ---------------------------------------

class Rep_line(Line):
    def __init__(self, line):
        self.line = line
        self.rep_line = []

    def add_line(self, l):
        self.rep_line.append(l)

    def get_rep_line(self):
        return self.rep_line

    def clear_rep(self):
        self.rep_line.clear()


# -------------------------------------------------    Moteur du jeu    ------------------------------------------------


class Game(Rep_cellules, Rep_line):
    def __init__(self, rep_cellule, rep_line):
        self.rep_line = rep_line
        self.rep_cellule = rep_cellule
        self.cels_occuped = []
        self.cels_playable = []
        self.tmp_cels_playable = []

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

    def calculate_best_cel_toPlay(self):
        return 0

    # Position occuper
    def positions_occuped(self):
        pos_occuped = []
        return pos_occuped

    def calcule_position_possible(self, i, j, position_occuper):
        positions = []
        return positions

    def initialisation_jeu(self):
        cel = Cellule()
        # rep_cel=Rep_cellule(cel)

    # Pour jouer aléatoirement
    def rand_play(self):
        return 0

    def convert_ind_to_ij(self, ind):
        i = int(ind / 30)
        j = ind - (i * 30)
        ij = np.array([i, j])
        return ij

    def convert_ij_to_ind(self, i, j):
        ind = i * 30 + j
        return ind

    def convert_ij_to_ihmPosition(self, i, j):
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
        self.rep_cel.clear()

    def clear_rep_playable(self):
        self.cels_playable.clear()

    # ------ Décode how the cel can be played his attribute V H DL DR possible ----------------------------------
    def decodeur_playable_direction_cel(self, cel, direction):

        # --------------------------------- line verticale --------------------------------------

        i = cel.get_x()
        j = cel.get_y()
        ind = self.convert_ij_to_ind(i, j)
        self.rep_cellule.get_rep()
        tmp_rep = self.rep_cellule.get_rep()
        if (direction == 'v'):
            code = cel.get_possible_V()
            
                
            ind1 = self.convert_ij_to_ind(i + 1, j)
            ind2 = self.convert_ij_to_ind(i + 2, j)
            ind3 = self.convert_ij_to_ind(i + 3, j)
            ind4 = self.convert_ij_to_ind(i + 4, j)
            if ((self.rep_cellule.get_rep()[ind4].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                    tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0) and (
                    tmp_rep[ind].get_vertical() == 0)):

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
        # --------------------------------- line horizentale --------------------------------------
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

            # --------------------------------- line left --------------------------------------
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
        # --------------------------------- line right --------------------------------------
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

    # ------ Search all cels that can be played and add them to list plaable cels ----------------------------------
    def set_one(self, ind, val):
        self.rep_cellule.get_rep()[ind].set_possible_V(val)

    def calculate_playable_cels(self):
        self.clear_rep_playable()
        self.rep_cellule.get_rep()

        self.rep_cellule.get_rep()
        tmp_rep = self.rep_cellule.get_rep()
        n = len(tmp_rep)
        n = int(sqrt(n))
        for i in range(0, n - 3):
            for j in range(0, n - 3):
                ind = self.convert_ij_to_ind(i, j)
                ind1 = self.convert_ij_to_ind(i + 1, j)
                ind2 = self.convert_ij_to_ind(i + 2, j)
                ind3 = self.convert_ij_to_ind(i + 3, j)
                ind4 = self.convert_ij_to_ind(i + 4, j)
                try:
                    if ((tmp_rep[ind4].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                            tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0) and (
                            tmp_rep[ind].get_vertical() == 0)):
                        if ((tmp_rep[ind4].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                            try:
                                self.rep_cellule.get_rep()[ind].set_possible_V(104)
                                self.add_cels_playable(tmp_rep[ind])
                                self.rep_cellule.set_cal_rep(tmp_rep[ind])


                            except Exception as inst:
                                print(type(inst))
                except Exception as inst:
                    print(type(inst))
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
                                self.rep_cellule.get_rep()[ind].set_possible_V(115)
                                self.add_cels_playable(tmp_rep[ind])


                        except Exception as inst:
                            print(type(inst))
                except Exception as inst:
                    print(type(inst))
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
                                self.rep_cellule.get_rep()[ind].set_possible_V(1113)
                                self.cels_playable.append(tmp_rep[ind])
                        except Exception as inst:
                            print(type(inst))
                except Exception as inst:
                    print(type(inst))
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
                                self.rep_cellule.get_rep()[ind].set_possible_V(1222)
                                self.add_cels_playable(tmp_rep[ind])
                        except Exception as inst:
                            print(type(inst))
                except Exception as inst:
                    print(type(inst))
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
                                self.rep_cellule.get_rep()[ind].set_possible_V(1331)
                                self.add_cels_playable(tmp_rep[ind])
                        except Exception as inst:
                            print(type(inst))
                except Exception as inst:
                    print(type(inst))
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
                                print(self.convert_ind_to_ij(ind), "==",
                                      self.rep_cellule.get_rep()[ind].get_horizontal(), self.convert_ind_to_ij(ind1),
                                      "==", self.rep_cellule.get_rep()[ind1].get_horizontal(),
                                      self.convert_ind_to_ij(ind2), "==",
                                      self.rep_cellule.get_rep()[ind2].get_horizontal(), self.convert_ind_to_ij(ind3),
                                      "==", self.rep_cellule.get_rep()[ind3].get_horizontal(),
                                      self.convert_ind_to_ij(ind4), "==",
                                      self.rep_cellule.get_rep()[ind4].get_horizontal())

                            except Exception as inst:
                                print(type(inst))
                except Exception as inst:
                    print(type(inst))
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
                                print(type(inst))
                except Exception as inst:
                    print(type(inst))
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
                                print(type(inst))
                except Exception as inst:
                    print(type(inst))
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
                                print(type(inst))
                except Exception as inst:
                    print(type(inst))

                ind1 = self.convert_ij_to_ind(i, j - 1)
                ind2 = self.convert_ij_to_ind(i, j - 2)
                ind3 = self.convert_ij_to_ind(i, j + 1)
                ind4 = self.convert_ij_to_ind(i, j + 2)

                try:
                    if ((tmp_rep[ind4].get_horizontal() == 0) and (tmp_rep[ind1].get_horizontal() == 0) and (
                            tmp_rep[ind2].get_horizontal() == 0) and (tmp_rep[ind3].get_horizontal() == 0)):
                        if ((tmp_rep[ind4].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                            try:

                                self.rep_cellule.get_rep()[ind].set_possible_H(2222)
                                self.add_cels_playable(tmp_rep[ind])

                            except Exception as inst:
                                print(type(inst))
                except Exception as inst:
                    print(type(inst))
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
                            if self.rep_cellule.get_rep()[ind].get_diagonal_left() == 0:
                                self.rep_cellule.get_rep()[ind].set_possible_DL(304)
                                self.cels_playable.append(tmp_rep[ind])

                        except Exception as inst:
                            print(type(inst))
                except Exception as inst:
                    print(type(inst))
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
                                print(type(inst))
                    except Exception as inst:
                        print(type(inst))
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
                                if self.rep_cellule.get_rep()[ind].get_diagonal_left() == 0:
                                    self.rep_cellule.get_rep()[ind].set_possible_DL(3113)
                                    self.cels_playable.append(tmp_rep[ind])

                            except Exception as inst:
                                print(type(inst))

                    except Exception as inst:
                        print(type(inst))
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
                                if (self.rep_cellule.get_rep()[ind].get_diagonal_left() == 0):
                                    self.rep_cellule.get_rep()[ind].set_possible_DL(3331)
                                    self.cels_playable.append(tmp_rep[ind])
                            except Exception as inst:
                                print(type(inst))

                except Exception as inst:
                    print(type(inst))
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
                            if self.rep_cellule.get_rep()[ind].get_diagonal_left() == 0:
                                self.rep_cellule.get_rep()[ind].set_possible_DL(3222)
                                self.cels_playable.append(tmp_rep[ind])
                        except Exception as inst:
                            print(type(inst))
                except Exception as inst:
                    print(type(inst))
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

                            if (self.rep_cellule.get_rep()[ind].get_diagonal_right() == 0):
                                self.rep_cellule.get_rep()[ind].set_possible_DR(404)
                                self.cels_playable.append(tmp_rep[ind])

                except Exception as inst:
                    print(type(inst))

                ind1 = self.convert_ij_to_ind(i - 1, j - 1)
                ind2 = self.convert_ij_to_ind(i - 2, j - 2)
                ind3 = self.convert_ij_to_ind(i - 3, j - 3)
                ind5 = self.convert_ij_to_ind(i - 4, j - 4)
                try:
                    if ((tmp_rep[ind5].get_diagonal_right() == 0) and (tmp_rep[ind1].get_diagonal_right() == 0) and (
                            tmp_rep[ind2].get_diagonal_right() == 0) and (tmp_rep[ind3].get_diagonal_right() == 0)):
                        if ((tmp_rep[ind].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)) and \
                                self.rep_cellule.get_rep()[ind].get_diagonal_right() == 0:
                            self.rep_cellule.get_rep()[ind].set_possible_DR(415)
                            self.cels_playable.append(tmp_rep[ind])
                except Exception as inst:
                    print(type(inst))
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
                            if (self.rep_cellule.get_rep()[ind].get_diagonal_right() == 0):
                                self.rep_cellule.get_rep()[ind].set_possible_DR(4222)
                                self.cels_playable.append(tmp_rep[ind])

                except Exception as inst:
                    print(type(inst))
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
                                self.rep_cellule.get_rep()[ind].get_diagonal_right() == 0:
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
                    print(type(inst))
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
                                self.rep_cellule.get_rep()[ind].get_diagonal_right() == 0:
                            self.rep_cellule.get_rep()[ind].set_possible_DR(4331)
                            self.cels_playable.append(tmp_rep[ind])
                except Exception as inst:
                    print(type(inst))

        self.save_list(tmp_rep)

    def save_list(self, liste):
        f = open('solitaire.txt', "w+")
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
        lines=[]
        with open('solitaire.txt') as f:
            lines = f.readlines()
        f.close()
        for i in range(0,len(lines)):
            a=lines[i]
            a1=a.split(",")
            cel=Cellule(0,0,0,0,0,0,0,0,0,0,0,0)
            cel.set_vertical(int(a1[0]))
            cel.set_horizontal(int(a1[1]))
            cel.set_diagonal_left(int(a1[2]))
            cel.set_diagonal_right(int(a1[3]))
            cel.set_cliqued(int(a1[4]))
            cel.set_possible_V(int(a1[5]))
            cel.set_possible_H(int(a1[6]))
            cel.set_line_ind(int(a1[7]))
            cel.set_possible_DL(int(a1[8]))
            cel.set_possible_DR(int(a1[9]))
            cel.set_x(int(a1[10]))
            cel.set_y(int(a1[11]))
            self.rep_cellule.set_cel_rep(cel,i)

    def play_line(self, cel, direction):
        tab = self.decodeur_playable_direction_cel(cel, direction)
        if (tab is not None):
            self.rep_cellule.get_rep()[tab[0]].set_line_ind(0)
            self.rep_cellule.get_rep()[tab[1]].set_line_ind(0)
            self.rep_cellule.get_rep()[tab[2]].set_line_ind(0)
            self.rep_cellule.get_rep()[tab[3]].set_line_ind(0)
            self.rep_cellule.get_rep()[tab[4]].set_line_ind(0)
            if (direction == 'v'):
                print(tab)
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

                self.rep_cellule.get_rep()[tab[0]].set_possible_V(0)
                self.rep_cellule.get_rep()[tab[1]].set_possible_V(0)
                self.rep_cellule.get_rep()[tab[2]].set_possible_V(0)
                self.rep_cellule.get_rep()[tab[3]].set_possible_V(0)
                self.rep_cellule.get_rep()[tab[4]].set_possible_V(0)
                LINE = Line(self.rep_cellule.get_rep()[tab[0]], self.rep_cellule.get_rep()[tab[1]],
                            self.rep_cellule.get_rep()[tab[2]], self.rep_cellule.get_rep()[tab[3]],
                            self.rep_cellule.get_rep()[tab[4]])
                line = LINE.get_line()
                self.rep_line.add_line(line)

            elif (direction == 'h'):
                print(tab)
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

            print(self.convert_ind_to_ij(tab[0]), '+', self.convert_ind_to_ij(tab[1]), '+',
                  self.convert_ind_to_ij(tab[2]), '+', self.convert_ind_to_ij(tab[3]), '+',
                  self.convert_ind_to_ij(tab[4]))

    # ------ search cliqued cels and edit their cliqued attribute ----------------------------------
    def if_cliqued(self):

        tmp_rep = self.rep_cellule.get_rep()
        tmp_rep_occ = self.get_cels_occuped()
        n = len(tmp_rep)
        n = int(sqrt(n))

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
        i = cel.get_x()
        j = cel.get_y()
        ind = self.convert_ij_to_ind(i, j)
        self.rep_cellule.get_rep()[ind].set_cliqued(1)

    def clear_cliqued_cel(self, cel):
        i = cel.get_x()
        j = cel.get_y()
        ind = self.convert_ij_to_ind(i, j)
        tmp_r = self.rep_cellule.get_rep()
        tmp_r[ind].set_cliqued(0)

    def score(self):
        global sc, bn, flag
        sc += 1
        self.sco.set(str(sc).zfill(3))
        if flag == 0:
            bn += 1
            self.bns.set(str(bn).zfill(3))
        flag = 0

    def initialisation(self, lin, col):
        self.rep_cellule.clear_rep()
        for i in range(0, col):
            for j in range(0, lin):
                cel = Cellule(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, i, j)
                self.rep_cellule.add_repertoire(cel)

    def console(self):
        tmp_rep = self.rep_cellule.get_rep()
        self.if_cliqued()
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
                            print("\n", i)
                        else:
                            if (i == 0):
                                print(" ", j, end=" "),
                            else:
                                print(" .  ", end=" "),




# ------------------------------         Interface graphique           --------------------------
        
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

# ---- mise à jour du score ------

def score(sc,bn):
    sco.set(str(sc).zfill(3))
    bns.set(str(bn).zfill(3))
    
def constructeur():
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


# ---------  Convertir les position de la matrice i et j en leurs equivalent en distance sur l'IHM ------------
def convert_ij_to_ihmPosition(i,j):

    ci=3*(18)
    cy=1*(18)
    x=((i+2.64)*18)
    y=((j+3.35)*18)
    pos=np.array([x,y])
    return pos


def inventaire(nbr_pos_playable, nbr_cels, nbr_occ_cels, nbr_lines):
    print("Nombre de positions possible à jouer  ----> ", nbr_pos_playable)
    print("Nombre de cellules ----> ", nbr_cels)
    print("Nombre de cellules occupées ----> ", nbr_occ_cels)
    print("Nombre de lignes créer ----> ", nbr_lines)

def play_in_ihm(i,j,ind):
    tmp_pos=convert_ij_to_ihmPosition(i,j)
    xx=tmp_pos[0]
    yy=tmp_pos[1]
    tracer.coords(curseur,xx-3,yy-3,xx,yy,xx,yy-3,xx-3,yy,xx-3,yy-3)
    tracer.create_oval(xx-4, yy-4, xx+4, yy+4,fill='red', width=1)
    w=2
    color1="blue"
    color2="green"
    color3="orange"
    color4="red"
    color5="black"
    
    # ------------- vertical ---------------
    if(ind==104):
        tracer.create_line(xx,yy,xx,yy+72,fill=color1,width=w)
    elif(ind==115):
        tracer.create_line(xx,yy,xx,yy-72,fill=color2,width=w)
    elif(ind==1113):
        tracer.create_line(xx,yy,xx,yy+54,xx,yy-18,fill='blue',width=1)
    elif(ind==1222):
        tracer.create_line(xx,yy,xx,yy,xx-36,yy+36,fill=color4,width=w)
    elif(ind==1331):
        tracer.create_line(xx,yy,xx,yy-54,xx,yy+18,fill=color5,width=w)
    #-------------- horizental  --------------------------
    elif(ind==204):
        tracer.create_line(xx,yy,xx,yy,xx+72,yy,fill=color1,width=w)
    elif(ind==215):
        tracer.create_line(xx,yy,xx,yy,xx-72,yy,fill=color2,width=w)
    elif(ind==2113):
        tracer.create_line(xx,yy,xx-18,yy,xx+54,yy,fill=color3,width=w)
    elif(ind==2222):
        tracer.create_line(xx,yy,xx-36,yy,xx+36,yy,fill=color4,width=w)
    elif(ind==2331):
        tracer.create_line(xx,yy,xx+18,yy,xx-54,yy,fill=color5,width=w)
    #-------------  diagonal left -----------------------
    elif(ind==304):
        tracer.create_line(xx,yy,xx,yy,xx+72,yy-72,fill=color2,width=w)

    elif(ind==315):
        tracer.create_line(xx,yy,xx,yy,xx-72,yy+72,fill=color1,width=w)

    elif(ind==3113):
        tracer.create_line(xx,yy,xx-18,yy+18,xx+54,yy-54,fill=color5,width=w)

    elif(ind==3222):
        tracer.create_line(xx,yy,xx-36,yy+36,xx+36,yy-36,fill=color4,width=w)
    elif(ind==3331):
        tracer.create_line(xx,yy,xx+18,yy-18,xx-54,yy+54,fill=color3,width=w)

    #---------------- diagonal right ------------------------
    elif(ind==404):
        tracer.create_line(xx,yy,xx,yy,xx+72,yy+72,fill=color1,width=w)
    elif(ind==415):
        tracer.create_line(xx,yy,xx,yy,xx-72,yy-72,fill=color2,width=w)
    elif(ind==4113):
        tracer.create_line(xx,yy,xx-18,yy-18,xx+54,yy+54,fill=color3,width=w)
    elif(ind==4222):
        tracer.create_line(xx,yy,xx+36,yy+36,xx-36,yy-36,fill=color4,width=w)
    elif(ind==4331):
        tracer.create_line(xx,yy,xx-54,yy-54,xx+18,yy+18,fill=color5,width=w)



def main():
    #---------------- init IHM ------------------
    
    #---------------- init moteur ---------------
    start = timeit.default_timer()
    cel = Cellule(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 7)
    rep_cel = Rep_cellules(cel)
    line = Line(cel, cel, cel, cel, cel)
    rep_line = Rep_line(line)
    game = Game(rep_cel, rep_line)
    game.initialisation(30, 30)
    game.console()
  
# ---------- Placer un point ---------------
 
      
    # ---------- Inventaire du jeu ---------------
    game.calculate_playable_cels()
    rep = game.get_cels_playable()
    a = game.rep_cellule.get_rep()
    itération=0
    while (len(rep) > 0):
        scores=len(game.rep_line.get_rep_line())
        itération+=1
        game.calculate_playable_cels()
        rep = game.get_cels_playable()
        possi=len(rep)
        for i in range(0, len(rep)): 
            c=random.choice(rep)
            game.play_line(c, 'v')
            game.play_line(c, 'h')
            game.play_line(c, 'dl')
            game.play_line(c, 'dr')
        scr=len(game.rep_line.get_rep_line())
        if(scr==scores):
            break
        game.calculate_playable_cels()
        game.console()
       
        print("itération numéro :", itération)
        itération+=1
        game.read_list()
        try:
            inventaire(len(rep), len(a), len(set(game.get_cels_occuped())), len(game.rep_line.get_rep_line()))
        except Exception as inst:
            print(type(inst))
        sco = np.array([len(game.rep_line.get_rep_line()), possi])

    end = timeit.default_timer()
    return sco

    print('Temps execution  ----> ', end - start, '  secondes')

    
init_jeu(0)
max_score=50
scores=main()
while scores[0]<max_score:
    scores=main()
    score(scores[0],scores[1])
        
mainloop()
