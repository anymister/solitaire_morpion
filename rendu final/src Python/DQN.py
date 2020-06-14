from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
import random
import numpy as np
import pandas as pd
from operator import add

class DQNAgent(object):

    def __init__(self):
        self.reward = 0 # initialisation de la récompense
        self.gamma = 0.9
        self.dataframe = pd.DataFrame()
        self.short_memory = np.array([])
        self.agent_target = 1
        self.agent_predict = 0
        self.learning_rate = 0.0005
        self.model = self.network() # initialisation du reseau
        self.epsilon = 0
        self.actual = []
        self.memory = []


    def get_state(self,game):
        state=[] # liste des états
        direction=[] # liste de bool dans les 8 directions
        vect_last_move=[] # le dernier déplacememnt
        vect_mvt=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]] # vecteur de déplacement
        for i in range(len(vect_mvt)):
            vect_last_move.append([0, 0, 0, 0, 0, 0, 0, 0]) # initialisation des sorties
        for i in range(len(vect_mvt)):
            vect_last_move[i][i]=1 # Matrice identité 8*8 
        for i in range(len(vect_mvt)):
            direction.append(False) # initialisés les 8 directions
        for i in range(len(game.rep_playable_lines)):
            for j in range(len(vect_mvt)): # si une ligne est jouable d'après sa premiere cellule dans chaque direction 
                if (game.rep_playable_lines[i][0][0].x==game.x_player+vect_mvt[j][0] and game.rep_playable_lines[i][0][0].y==game.y_player+vect_mvt[j][1]):
                    direction[j]=True   
        for i in range(80): # initialiser tt les états
            state.append(False)
        state[game.x_player]=True # x du joueur
        state[game.y_player+30]=True # y du joueur
        state[60]= game.choosed_line[0][0].x<game.x_player # indication de la cellule jouable choisi aléatoirement
        state[61]= game.choosed_line[0][0].x>game.x_player 
        state[62]= game.choosed_line[0][0].y<game.y_player 
        state[63]= game.choosed_line[0][0].y>game.y_player
        for i in range(len(vect_mvt)):
            state[62+i]=direction[i] # indication des lignes jouables dans les 8 direction alignées du joueur
        for i in range(len(vect_mvt)):
            if vect_last_move[i]==game.move: # dernier mouvement réaliser
                state[70+i]=True
        state[79]=game.cpt_liberte>game.liberte-3 # danger il lui reste plus que 1 mouvement avant de crashé
        for i in range(len(state)): # Convert False to 0 and True to 1
            if state[i]:
                state[i]=1 # True
            else:
                state[i]=0 # False
        return np.asarray(state) # Convert states to array

    def set_reward(self, crash, found):
        """ Calcule de Récompense"""
        self.reward = 0 # initialiser la récompense à 0
        if crash==0: # si aucune ligne est trouver après 10 mouvement ou aucune ligne est jouable
            self.reward = -10
        if found: # si une ligne est trouvé
            self.reward = 10

        return self.reward
    
    def network(self, weights=None):
        """ Initialisation du réseau de neurones"""
        model = Sequential()
        model.add(Dense(output_dim=120, activation='relu', input_dim=80)) # premiere couche avec 80 entrées
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=120, activation='relu')) # couches intermediaires
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=120, activation='relu'))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=8, activation='softmax')) # Dérniere Couche avec 8 sortie
        opt = Adam(self.learning_rate)
        model.compile(loss='mse', optimizer=opt)

        if weights: # Si on veut chargé des poids existants
            model.load_weights(weights)
        return model

    def remember(self, state, action, reward, next_state, done):
        """ Sauvegardes del'etat du jeu avec tout les parametres indispensables"""
        self.memory.append((state, action, reward, next_state, done))

    def replay_new(self, memory):
        if len(memory) > 1000:
            minibatch = random.sample(memory, 1000)
        else:
            minibatch = memory
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(np.array([next_state]))[0])
            target_f = self.model.predict(np.array([state]))
            target_f[0][np.argmax(action)] = target
            self.model.fit(np.array([state]), target_f, epochs=1, verbose=0)

    def train_short_memory(self, state, action, reward, next_state, done):
        """ Edition des poids avec les nouvelles entrées """
        target = reward
        if not done:
            target = reward + self.gamma * np.amax(self.model.predict(next_state.reshape((1, 80)))[0])
        target_f = self.model.predict(state.reshape((1, 80)))
        target_f[0][np.argmax(action)] = target
        self.model.fit(state.reshape((1, 80)), target_f, epochs=1, verbose=0)
