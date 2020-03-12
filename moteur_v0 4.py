import timeit

import numpy as np
from math import *


# ---------------------------------   Classe cellule représente une case du jeu   --------------------------------------

class Cellule:
    # vertical,horizontal,diagonal_left,diagonal_right et cliqued SONT DES BOOL
    def __init__(self, vertical, horizontal, diagonal_left, diagonal_right, cliqued, line_ind, x, y):
        self.vertical = vertical
        self.diagonal_left = diagonal_left
        self.diagonal_right = diagonal_right
        self.horizontal = horizontal
        self.x = x
        self.y = y
        self.line_ind = line_ind
        self.cliqued = cliqued

    def get_vertical(self):
        return self.vertical

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

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
            self.diagonal_right) + '+' + str(self.cliqued) + '+' + str(self.line_ind) + '+' + str(self.x) + '+' + str(
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

    def clear_rep(self):
        self.rep_cel.clear()

    def set_cel_rep(self, cel, ind):
        self.rep_cel[ind] = cel

# -------------------------------------------------    classe Ligne    ------------------------------------------------

class Line(Cellule):
    def __init__(self, cel1, cel2, cel3, cel4, cel5):
        self.line_cels = []
        self.line_cels.append(cel1)
        self.line_cels.append(cel2)
        self.line_cels.append(cel3)
        self.line_cels.append(cel4)
        self.line_cels.append(cel5)

    def get_line(self):
        return self.line_cels

    def set_line(self,pos,cel):
        self.line_cels[pos]=cel


# -------------------------------------------------    Repertoire des lignes    ---------------------------------------

class Rep_line(Line):
    def __init__(self, line):
        self.line = line
        self.rep_line= []

    def add_line(self,l):
        self.rep_line.append(l)

    def get_rep_line(self):
        return self.rep_line

    def clear_rep(self):
        self.rep_line.clear()
# -------------------------------------------------    Moteur du jeu    ------------------------------------------------


class Game(Rep_cellules,Rep_line):
    def __init__(self, rep_cellule,rep_line):
        self.rep_line=rep_line
        self.rep_cellule = rep_cellule
        self.cels_occuped = []
        self.cels_playable = []

    def get_cels_occuped(self):
        return self.cels_occuped

    def get_rep_line(self):
        return self.rep_line

    def get_cels_playable(self):
        return self.cels_playable

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
        j = int(ind / 30)
        i = ind - (j * 30)
        ij = np.array([i, j])
        return ij

    def convert_ij_to_ind(self, i, j):
        ind = j * 30 + i
        return ind

    def convert_ij_to_ihmPosition(self, i, j):
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


    def calculate_playable_cels(self):
        self.clear_rep_playable()
        tmp_rep = self.rep_cellule.get_rep()
        n = len(tmp_rep)
        n = int(sqrt(n))
        cpt=0
        for i in range(0, n - 3):
            for j in range(0, n - 3):
                ind = self.convert_ij_to_ind(i, j)
                ind1 = self.convert_ij_to_ind(i + 1, j)
                ind2 = self.convert_ij_to_ind(i + 2, j)
                ind3 = self.convert_ij_to_ind(i + 3, j)
                ind4 = self.convert_ij_to_ind(i + 4, j)
                ind5 = self.convert_ij_to_ind(i - 1, j)
                try:
                    if ((tmp_rep[ind].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                            tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                        if ((tmp_rep[ind].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                                tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0)):
                            try:
                                if (tmp_rep[ind4].get_vertical() == 0):
                                    cpt += 1
                                    self.cels_playable.append(tmp_rep[ind4])
                                    print(tmp_rep[ind4].to_string())
                                if (tmp_rep[ind5].get_vertical() == 0):
                                    cpt += 1
                                    self.cels_playable.append(tmp_rep[ind5])
                                    print(tmp_rep[ind5].to_string())
                            except Exception as inst:
                                print(type(inst))
                except Exception as inst:
                    print(type(inst))
                ind = self.convert_ij_to_ind(i, j)
                ind1 = self.convert_ij_to_ind(i, j + 1)
                ind2 = self.convert_ij_to_ind(i, j + 2)
                ind3 = self.convert_ij_to_ind(i, j + 3)
                ind4 = self.convert_ij_to_ind(i, j + 4)
                ind5 = self.convert_ij_to_ind(i, j - 1)
                try:
                    if ((tmp_rep[ind].get_horizontal() == 0) and (tmp_rep[ind1].get_horizontal() == 0) and (
                            tmp_rep[ind2].get_horizontal() == 0) and (tmp_rep[ind3].get_horizontal() == 0)):
                        if ((tmp_rep[ind].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                            try:
                                if (tmp_rep[ind4].get_horizontal() == 0):
                                    cpt += 1
                                    self.cels_playable.append(tmp_rep[ind4])
                                    print(tmp_rep[ind4].to_string())
                                if (tmp_rep[ind5].get_horizontal() == 0):
                                    cpt += 1
                                    self.cels_playable.append(tmp_rep[ind5])
                                    print(tmp_rep[ind5].to_string())
                            except Exception as inst:
                                print(type(inst))
                except Exception as inst:
                    print(type(inst))
                ind = self.convert_ij_to_ind(i, j)
                ind1 = self.convert_ij_to_ind(i + 1, j + 1)
                ind2 = self.convert_ij_to_ind(i + 2, j + 2)
                ind3 = self.convert_ij_to_ind(i + 3, j + 3)
                ind4 = self.convert_ij_to_ind(i + 4, j + 4)
                ind5 = self.convert_ij_to_ind(i - 1, j - 1)
                try:
                    if ((tmp_rep[ind].get_diagonal_left() == 0) and (tmp_rep[ind1].get_diagonal_left() == 0) and (
                            tmp_rep[ind2].get_diagonal_left() == 0) and (tmp_rep[ind3].get_diagonal_left() == 0)):
                        if (((tmp_rep[ind].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1))):
                            try:
                                   if (tmp_rep[ind4].get_diagonal_left() == 0):
                                    cpt += 1
                                    self.cels_playable.append(tmp_rep[ind4])
                                    print(tmp_rep[ind4].to_string())
                                    if (tmp_rep[ind5].get_diagonal_left() == 0):
                                        cpt += 1
                                        self.cels_playable.append(tmp_rep[ind5])
                                        print(tmp_rep[ind5].to_string())
                            except Exception as inst:
                                print(type(inst))
                except Exception as inst:
                    print(type(inst))

                    ind = self.convert_ij_to_ind(i, j)
                    ind1 = self.convert_ij_to_ind(i + 1, j - 1)
                    ind2 = self.convert_ij_to_ind(i + 2, j - 2)
                    ind3 = self.convert_ij_to_ind(i + 3, j - 3)
                    ind4 = self.convert_ij_to_ind(i + 4, j - 4)
                    ind5 = self.convert_ij_to_ind(i - 1, j + 1)
                    try:
                        if ((tmp_rep[ind].get_diagonal_right() == 0) and (tmp_rep[ind1].get_diagonal_right() == 0) and (
                                tmp_rep[ind2].get_diagonal_right() == 0) and (tmp_rep[ind3].get_diagonal_right() == 0)):
                            if ((tmp_rep[ind].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                                    tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):

                                    if (tmp_rep[ind4].get_diagonal_right() == 0):
                                        cpt += 1
                                        self.cels_playable.append(tmp_rep[ind4])
                                        print(tmp_rep[ind4].to_string())
                                    if (tmp_rep[ind5].get_diagonal_right() == 0):
                                        cpt += 1
                                        self.cels_playable.append(tmp_rep[ind5])
                                        print(tmp_rep[ind5].to_string())
                    except Exception as inst:
                        print(type(inst))
        return cpt

    def if_cliqued(self):
        tmp_rep = self.rep_cellule.get_rep()
        n = len(tmp_rep)
        n = int(sqrt(n))
        for i in range(0, n):
            for j in range(0, n):
                ind = self.convert_ij_to_ind(i, j)
                # d print('tested'+'---i='+str(i)+'j='+str(j))
                if (tmp_rep[ind].get_cliqued() == 1):
                    # print('cliqued OK-->'+tmp_rep[ind].to_string())
                    self.cels_occuped.append(tmp_rep[ind])
    def clic_cel(self,cel):
        i=cel.get_x()
        j=cel.get_y()
        ind=self.convert_ij_to_ind(j,i)
        tmp_r=self.rep_cellule.get_rep()
        tmp_r[ind].set_cliqued(1)

    def clear_cliqued_cel(self,cel):
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
                cel = Cellule(0, 0, 0, 0, 0, 0, i, j)
                self.rep_cellule.add_repertoire(cel)
    def play_line(self,cel,diretion):
        line=[]
        try:
            tmp_rep = self.rep_cellule.get_rep()
            i=cel.get_x()
            j=cel.get_y()
        except Exception as inst:
            print(type(inst))
        ind = self.convert_ij_to_ind(i, j)
        # --------------------------------- line horizentale --------------------------------------
        ind1 = self.convert_ij_to_ind(j+1,i)
        ind2 = self.convert_ij_to_ind(j + 2,i)
        ind3 = self.convert_ij_to_ind(j + 3,i)
        ind4 = self.convert_ij_to_ind(j + 4,i)
        try:
            if ((tmp_rep[ind4].get_horizontal() == 0) and (tmp_rep[ind1].get_horizontal() == 0) and (
                    tmp_rep[ind2].get_horizontal() == 0) and (tmp_rep[ind3].get_horizontal() == 0) and(diretion=='h')):
                if ((tmp_rep[ind4].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                        tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                    line.append(tmp_rep[ind])
                    lin=self.line(tmp_rep[ind],tmp_rep[ind1],tmp_rep[ind2],tmp_rep[ind3],tmp_rep[ind4])
                    self.rep_line(lin).add_line()
                    print(tmp_rep[ind].to_string(),'+1 +4')
        except Exception as inst:
            print(type(inst))
        ind5 = self.convert_ij_to_ind(j + 1,i)
        ind6 = self.convert_ij_to_ind(j + 2,i)
        ind7 = self.convert_ij_to_ind(j + 3,i)
        ind8 = self.convert_ij_to_ind(j -1,i)
        try:
            if ((tmp_rep[ind8].get_horizontal() == 0) and (tmp_rep[ind5].get_horizontal() == 0) and (
                    tmp_rep[ind6].get_horizontal() == 0) and (tmp_rep[ind7].get_horizontal() == 0) and(diretion=='h')):
                if ((tmp_rep[ind8].get_cliqued() == 1) and (tmp_rep[ind5].get_cliqued() == 1) and (
                        tmp_rep[ind6].get_cliqued() == 1) and (tmp_rep[ind7].get_cliqued() == 1)):
                    line.append(tmp_rep[ind])
                    print(tmp_rep[ind].to_string(),'-1 +3')
        except Exception as inst:
            print(type(inst))
        ind9 = self.convert_ij_to_ind(j + 1,i)

        ind10 = self.convert_ij_to_ind(j + 2,i)
        ind11 = self.convert_ij_to_ind(j -2,i)
        ind12 = self.convert_ij_to_ind(j - 1,i)
        try:
            if ((tmp_rep[ind9].get_horizontal() == 0) and (tmp_rep[ind10].get_horizontal() == 0) and (
                    tmp_rep[ind11].get_horizontal() == 0) and (tmp_rep[ind12].get_horizontal() == 0) and(diretion=='h')):
                if ((tmp_rep[ind9].get_cliqued() == 1) and (tmp_rep[ind10].get_cliqued() == 1) and (
                        tmp_rep[ind11].get_cliqued() == 1) and (tmp_rep[ind12].get_cliqued() == 1)):
                        line.append(tmp_rep[ind])
                        print(tmp_rep[ind].to_string(),'-2 +2')
        except Exception as inst:
            print(type(inst))
        ind13 = self.convert_ij_to_ind(j + 1,i)

        ind14= self.convert_ij_to_ind(j -3,i)
        ind15 = self.convert_ij_to_ind(j -2,i)
        ind16= self.convert_ij_to_ind(j - 1,i)
        try:
            if ((tmp_rep[ind13].get_horizontal() == 0) and (tmp_rep[ind14].get_horizontal() == 0) and (
                    tmp_rep[ind15].get_horizontal() == 0) and (tmp_rep[ind16].get_horizontal() == 0) and(diretion=='h')):
                if ((tmp_rep[ind13].get_cliqued() == 1) and (tmp_rep[ind14].get_cliqued() == 1) and (
                        tmp_rep[ind15].get_cliqued() == 1) and (tmp_rep[ind16].get_cliqued() == 1)):
                    line.append(tmp_rep[ind])
                    print(tmp_rep[ind].to_string(),'+1 -3')
        except Exception as inst:
            print(type(inst))
        ind17 = self.convert_ij_to_ind(j - 4,i)
        ind18 = self.convert_ij_to_ind(j - 2,i)
        ind19= self.convert_ij_to_ind(j - 3,i)
        ind20= self.convert_ij_to_ind(j - 1,i)
        try:
            if ((tmp_rep[ind17].get_horizontal() == 0) and (tmp_rep[ind18].get_horizontal() == 0) and (
                    tmp_rep[ind19].get_horizontal() == 0) and (tmp_rep[ind20].get_horizontal() == 0) and(diretion=='h')):
                if ((tmp_rep[ind17].get_cliqued() == 1) and (tmp_rep[ind18].get_cliqued() == 1) and (
                        tmp_rep[ind19].get_cliqued() == 1) and (tmp_rep[ind20].get_cliqued() == 1)):
                    line.append(tmp_rep[ind])
                    print(tmp_rep[ind].to_string(),'-1 -4')
        except Exception as inst:
            print(type(inst))
        # --------------------------------- line verticale --------------------------------------
        ind1 = self.convert_ij_to_ind(j, i + 1)
        ind2 = self.convert_ij_to_ind(j, i + 2)
        ind3 = self.convert_ij_to_ind(j, i + 3)
        ind4 = self.convert_ij_to_ind(j, i + 4)
        try:
            if ((tmp_rep[ind4].get_vertical() == 0) and (tmp_rep[ind1].get_vertical() == 0) and (
                    tmp_rep[ind2].get_vertical() == 0) and (tmp_rep[ind3].get_vertical() == 0) and (diretion == 'v')):
                if ((tmp_rep[ind4].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                        tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                    lin=Line(tmp_rep[ind1],tmp_rep[ind2],tmp_rep[ind3],tmp_rep[ind4],tmp_rep[ind5])
                    self.rep_line.add_line(lin)
                    line.append(tmp_rep[ind])
                    print(tmp_rep[ind].to_string(), '+1 +4')
        except Exception as inst:
            print(type(inst))
        ind5 = self.convert_ij_to_ind(j, i + 1)
        ind6 = self.convert_ij_to_ind(j, i + 2)
        ind7 = self.convert_ij_to_ind(j, i + 3)
        ind8 = self.convert_ij_to_ind(j, i - 1)
        try:
            if ((tmp_rep[ind8].get_vertical() == 0) and (tmp_rep[ind5].get_vertical() == 0) and (
                    tmp_rep[ind6].get_vertical() == 0) and (tmp_rep[ind7].get_vertical() == 0) and (diretion == 'v')):
                if ((tmp_rep[ind8].get_cliqued() == 1) and (tmp_rep[ind5].get_cliqued() == 1) and (
                        tmp_rep[ind6].get_cliqued() == 1) and (tmp_rep[ind7].get_cliqued() == 1)):
                    line.append(tmp_rep[ind])
                    print(tmp_rep[ind].to_string(), '-1 +3')
        except Exception as inst:
            print(type(inst))
        ind9 = self.convert_ij_to_ind(j, i + 1)
        ind10 = self.convert_ij_to_ind(j, i + 2)
        ind11 = self.convert_ij_to_ind(j, i - 2)
        ind12 = self.convert_ij_to_ind(j, i - 1)
        try:
            if ((tmp_rep[ind9].get_vertical() == 0) and (tmp_rep[ind10].get_vertical() == 0) and (
                    tmp_rep[ind11].get_vertical() == 0) and (tmp_rep[ind12].get_vertical() == 0) and (diretion == 'v')):
                if ((tmp_rep[ind9].get_cliqued() == 1) and (tmp_rep[ind10].get_cliqued() == 1) and (
                        tmp_rep[ind11].get_cliqued() == 1) and (tmp_rep[ind12].get_cliqued() == 1)):
                    line.append(tmp_rep[ind])
                    print(tmp_rep[ind].to_string(), '-2 +2')
        except Exception as inst:
            print(type(inst))
        ind13 = self.convert_ij_to_ind(j, i + 1)
        ind14 = self.convert_ij_to_ind(j, i - 3)
        ind15 = self.convert_ij_to_ind(j, i - 2)
        ind16 = self.convert_ij_to_ind(j, i - 1)
        try:
            if ((tmp_rep[ind13].get_vertical() == 0) and (tmp_rep[ind14].get_vertical() == 0) and (
                    tmp_rep[ind15].get_vertical() == 0) and (tmp_rep[ind16].get_vertical() == 0) and (diretion == 'v')):
                if ((tmp_rep[ind13].get_cliqued() == 1) and (tmp_rep[ind14].get_cliqued() == 1) and (
                        tmp_rep[ind15].get_cliqued() == 1) and (tmp_rep[ind16].get_cliqued() == 1)):
                    line.append(tmp_rep[ind])
                    print(tmp_rep[ind].to_string(), '+1 -3')
        except Exception as inst:
            print(type(inst))
        ind17 = self.convert_ij_to_ind(j, i - 4)
        ind18 = self.convert_ij_to_ind(j, i - 2)
        ind19 = self.convert_ij_to_ind(j, i - 3)
        ind20 = self.convert_ij_to_ind(j, i - 1)

        try:
            if ((tmp_rep[ind17].get_vertical() == 0) and (tmp_rep[ind18].get_vertical() == 0) and (
                tmp_rep[ind19].get_vertical() == 0) and (tmp_rep[ind20].get_vertical() == 0) and (diretion == 'v')):
                if ((tmp_rep[ind17].get_cliqued() == 1) and (tmp_rep[ind18].get_cliqued() == 1) and (
                        tmp_rep[ind19].get_cliqued() == 1) and (tmp_rep[ind20].get_cliqued() == 1)):
                    line.append(tmp_rep[ind])
                    print(tmp_rep[ind].to_string(), '-1 -4')
        except Exception as inst:
            print(type(inst))
            # --------------------------------- line diagonale gauche --------------------------------------
            ind1 = self.convert_ij_to_ind(j + 1, i + 1)
            ind2 = self.convert_ij_to_ind(j + 2, i + 2)
            ind3 = self.convert_ij_to_ind(j + 3, i + 3)
            ind4 = self.convert_ij_to_ind(j + 4, i + 4)
            try:
                if ((tmp_rep[ind4].get_diagonal_left() == 0) and (tmp_rep[ind1].get_diagonal_left() == 0) and (
                        tmp_rep[ind2].get_diagonal_left() == 0) and (tmp_rep[ind3].get_diagonal_left() == 0) and (diretion == 'l')):
                    if ((tmp_rep[ind4].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                            tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                        line.append(tmp_rep[ind])
                        print(tmp_rep[ind].to_string(), '+1 +4')
            except Exception as inst:
                print(type(inst))
            ind5 = self.convert_ij_to_ind(j-1, i - 1)
            ind6 = self.convert_ij_to_ind(j + 2, i + 2)
            ind7 = self.convert_ij_to_ind(j + 3, i + 3)
            ind8 = self.convert_ij_to_ind(j + 1, i + 1)
            try:
                if ((tmp_rep[ind8].get_diagonal_left() == 0) and (tmp_rep[ind5].get_diagonal_left() == 0) and (
                        tmp_rep[ind6].get_diagonal_left() == 0) and (tmp_rep[ind7].get_diagonal_left() == 0) and (diretion == 'l')):
                    if ((tmp_rep[ind8].get_cliqued() == 1) and (tmp_rep[ind5].get_cliqued() == 1) and (
                            tmp_rep[ind6].get_cliqued() == 1) and (tmp_rep[ind7].get_cliqued() == 1)):
                        line.append(tmp_rep[ind])
                        print(tmp_rep[ind].to_string(), '-1 +3')
            except Exception as inst:
                print(type(inst))
            ind9 = self.convert_ij_to_ind(j-1, i - 1)
            ind10 = self.convert_ij_to_ind(j - 2, i - 2)
            ind11 = self.convert_ij_to_ind(j + 2, i + 2)
            ind12 = self.convert_ij_to_ind(j + 1, i + 1)
            try:
                if ((tmp_rep[ind9].get_diagonal_left() == 0) and (tmp_rep[ind10].get_diagonal_left() == 0) and (
                        tmp_rep[ind11].get_diagonal_left() == 0) and (tmp_rep[ind12].get_diagonal_left() == 0) and (diretion == 'l')):
                    if ((tmp_rep[ind9].get_cliqued() == 1) and (tmp_rep[ind10].get_cliqued() == 1) and (
                            tmp_rep[ind11].get_cliqued() == 1) and (tmp_rep[ind12].get_cliqued() == 1)):
                        line.append(tmp_rep[ind])
                        print(tmp_rep[ind].to_string(), '-2 +2')
            except Exception as inst:
                print(type(inst))
            ind13 = self.convert_ij_to_ind(j+1, i + 1)
            ind14 = self.convert_ij_to_ind(j-3, i - 3)
            ind15 = self.convert_ij_to_ind(j-2, i - 2)
            ind16 = self.convert_ij_to_ind(j-1, i - 1)
            try:
                if ((tmp_rep[ind13].get_diagonal_left() == 0) and (tmp_rep[ind14].get_diagonal_left() == 0) and (
                        tmp_rep[ind15].get_diagonal_left() == 0) and (tmp_rep[ind16].get_diagonal_left() == 0) and (diretion == 'l')):
                    if ((tmp_rep[ind13].get_cliqued() == 1) and (tmp_rep[ind14].get_cliqued() == 1) and (
                            tmp_rep[ind15].get_cliqued() == 1) and (tmp_rep[ind16].get_cliqued() == 1)):
                        line.append(tmp_rep[ind])
                        print(tmp_rep[ind].to_string(), '+1 -3')
            except Exception as inst:
                print(type(inst))
            ind17 = self.convert_ij_to_ind(j-4, i - 4)
            ind18 = self.convert_ij_to_ind(j-2, i - 2)
            ind19 = self.convert_ij_to_ind(j-3, i - 3)
            ind20 = self.convert_ij_to_ind(j-1, i - 1)
            try:
                if ((tmp_rep[ind17].get_diagonal_left() == 0) and (tmp_rep[ind18].get_diagonal_left() == 0) and (
                        tmp_rep[ind19].get_diagonal_left() == 0) and (tmp_rep[ind20].get_diagonal_left() == 0) and (diretion == 'l')):
                    if ((tmp_rep[ind17].get_cliqued() == 1) and (tmp_rep[ind18].get_cliqued() == 1) and (
                            tmp_rep[ind19].get_cliqued() == 1) and (tmp_rep[ind20].get_cliqued() == 1)):
                        line.append(tmp_rep[ind])
                        print(tmp_rep[ind].to_string(), '-1 -4')
            except Exception as inst:
                print(type(inst))
            # --------------------------------- line diagonale right  --------------------------------------
            ind1 = self.convert_ij_to_ind(j - 1,i + 1)
            ind2 = self.convert_ij_to_ind(j - 2,i + 2)
            ind3 = self.convert_ij_to_ind(j - 3,i + 3)
            ind4 = self.convert_ij_to_ind(j - 4,i + 4)
            try:
                if ((tmp_rep[ind4].get_diagonal_right() == 0) and (tmp_rep[ind1].get_diagonal_right() == 0) and (
                        tmp_rep[ind2].get_diagonal_right() == 0) and (tmp_rep[ind3].get_diagonal_right() == 0) and (diretion == 'r')):
                    if ((tmp_rep[ind4].get_cliqued() == 1) and (tmp_rep[ind1].get_cliqued() == 1) and (
                            tmp_rep[ind2].get_cliqued() == 1) and (tmp_rep[ind3].get_cliqued() == 1)):
                        line.append(tmp_rep[ind])
                        print(tmp_rep[ind].to_string(), '+1 +4')
            except Exception as inst:
                print(type(inst))
            ind5 = self.convert_ij_to_ind(j + 1,i - 1)
            ind6 = self.convert_ij_to_ind(j - 2,i + 2)
            ind7 = self.convert_ij_to_ind(j - 3,i + 3)
            ind8 = self.convert_ij_to_ind(j - 4,i + 4)
            try:
                if ((tmp_rep[ind8].get_diagonal_right() == 0) and (tmp_rep[ind5].get_diagonal_right() == 0) and (
                        tmp_rep[ind6].get_diagonal_right() == 0) and (tmp_rep[ind7].get_diagonal_right() == 0) and (diretion == 'r')):
                    if ((tmp_rep[ind8].get_cliqued() == 1) and (tmp_rep[ind5].get_cliqued() == 1) and (
                            tmp_rep[ind6].get_cliqued() == 1) and (tmp_rep[ind7].get_cliqued() == 1)):
                        line.append(tmp_rep[ind])
                        print(tmp_rep[ind].to_string(), '-1 +3')
            except Exception as inst:
                print(type(inst))
            ind9 = self.convert_ij_to_ind(j + 1,i - 1)
            ind10 = self.convert_ij_to_ind(j + 2,i - 2)
            ind11 = self.convert_ij_to_ind(j - 3,i + 3)
            ind12 = self.convert_ij_to_ind(j - 4,i + 4)
            try:
                if ((tmp_rep[ind9].get_vertical() == 0) and (tmp_rep[ind10].get_vertical() == 0) and (
                        tmp_rep[ind11].get_vertical() == 0) and (tmp_rep[ind12].get_vertical() == 0) and (diretion == 'r')):
                    if ((tmp_rep[ind9].get_cliqued() == 1) and (tmp_rep[ind10].get_cliqued() == 1) and (
                            tmp_rep[ind11].get_cliqued() == 1) and (tmp_rep[ind12].get_cliqued() == 1)):
                        line.append(tmp_rep[ind])
                        print(tmp_rep[ind].to_string(), '-2 +2')
            except Exception as inst:
                print(type(inst))
            ind13 = self.convert_ij_to_ind(j + 1,i - 1)
            ind14 = self.convert_ij_to_ind(j + 2,i - 2)
            ind15 = self.convert_ij_to_ind(j + 3,i - 3)
            ind16 = self.convert_ij_to_ind(j - 4,i + 4)
            try:
                if ((tmp_rep[ind13].get_diagonal_right() == 0) and (tmp_rep[ind14].get_diagonal_right() == 0) and (
                        tmp_rep[ind15].get_diagonal_right() == 0) and (tmp_rep[ind16].get_diagonal_right() == 0) and (diretion == 'l')):
                    if ((tmp_rep[ind13].get_cliqued() == 1) and (tmp_rep[ind14].get_cliqued() == 1) and (
                            tmp_rep[ind15].get_cliqued() == 1) and (tmp_rep[ind16].get_cliqued() == 1)):
                        line.append(tmp_rep[ind])
                        print(tmp_rep[ind].to_string(), '+1 -3')
            except Exception as inst:
                print(type(inst))
            ind17 = self.convert_ij_to_ind(j + 1,i - 1)
            ind18 = self.convert_ij_to_ind(j + 2,i - 2)
            ind19 = self.convert_ij_to_ind(j + 3,i - 3)
            ind20 = self.convert_ij_to_ind(j +4,i - 4)
            try:
                if ((tmp_rep[ind17].get_diagonal_right() == 0) and (tmp_rep[ind18].get_diagonal_right() == 0) and (
                        tmp_rep[ind19].get_diagonal_right() == 0) and (tmp_rep[ind20].get_diagonal_right() == 0) and (diretion == 'r')):
                    if ((tmp_rep[ind17].get_cliqued() == 1) and (tmp_rep[ind18].get_cliqued() == 1) and (
                            tmp_rep[ind19].get_cliqued() == 1) and (tmp_rep[ind20].get_cliqued() == 1)):
                        line.append(tmp_rep[ind])
                        print(tmp_rep[ind].to_string(), '-1 -4')
            except Exception as inst:
                print(type(inst))
    def console(self):

        Croix = [(9, 15), (9, 16), (9, 17), (9, 18), (10, 15), (10, 18), (11, 15), (11, 18), (12, 12), \
                 (12, 13), (12, 14), (12, 15), (12, 18), (12, 19), (12, 20), (12, 21), (13, 12), (13, 21), \
                 (14, 12), (14, 21), (15, 12), (15, 13), (15, 14), (15, 15), (15, 18), (15, 19), (15, 20), \
                 (15, 21), (16, 15), (16, 18), (17, 15), (17, 18), (18, 15), (18, 16), (18, 17), (18, 18)]
        tmp_rep = self.rep_cellule.get_rep()
        n = len(tmp_rep)
        n = int(sqrt(n))
        t = 0
        x = 0
        y = 0

        for i in range(0, n):
            for j in range(0, n):
                indi=self.convert_ij_to_ind(i,j)
                ce=tmp_rep[indi]
                xx=ce.get_x()
                yy=ce.get_y()
                for li, co in Croix:
                    c = 2
                    if ((li == i and co == j ) or (xx==i and yy==j and tmp_rep[indi].get_cliqued()==1)):
                        print("0   ", end=" "),
                        cel = Cellule(0, 0, 0, 0, 1, 0, i, j)
                        ind = self.convert_ij_to_ind(i, j)
                        self.rep_cellule.set_cel_rep(cel, ind)
                        c = 1
                        break
                f=0
                if (c == 2):
                    for l in range(0, len(self.cels_playable)):

                        f = 1
                        x = self.cels_playable[l].get_x()
                        y = self.cels_playable[l].get_y()
                        if (i == y and j == x):
                            print("#   ", end=" "),
                            f = 3
                            break
                    if (f == 1):
                        if (j == (n - 1)):
                            print("\n",i)
                        else:
                            if(i==0 ):
                                print(j," ", end=" "),
                            else:
                                print(".   ", end=" "),
        tmp = self.rep_cellule.get_rep()
        for i in range(0, n):
            for j in range(0, n):
                ind = self.convert_ij_to_ind(i, j)
                # print(tmp[ind].to_string())

    def relation_game_ihm(self, ihm):
        n = len(self.cels_playable)
        for i in range(0, n):
            x = self.cels_playable[i].get_x()
            y = self.cels_playable[i].get_y()
            print(str(x) + '--' + str(y))
            ihm.trace_curseur(y, x)
            ihm.place_croix()


def main():
    start=timeit.default_timer()
    cel = Cellule(0, 0, 0, 0, 0, 0, 11, 11)
    rep_cel = Rep_cellules(cel)
    line=Line(cel,cel,cel,cel,cel)
    rep_line = Rep_line(line)
    game = Game(rep_cel,rep_line)
    game.initialisation(30, 30)
    game.console()
    game.if_cliqued()
    cpt=game.calculate_playable_cels()
    game.console()
    end=timeit.default_timer()
    rep=game.get_cels_playable()
    print("number of playable positions is =",cpt)
    for i in range(0,len(rep)):
        game.play_line(rep[i],'v')
    print('time= ',end-start)
    game.clic_cel(cel)
    game.console()

main()
