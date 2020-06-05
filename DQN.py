from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
import random
import numpy as np
import pandas as pd
from operator import add

class DQNAgent(object):

    def __init__(self):
        self.reward = 0
        self.gamma = 0.9
        self.dataframe = pd.DataFrame()
        self.short_memory = np.array([])
        self.agent_target = 1
        self.agent_predict = 0
        self.learning_rate = 0.0005
        self.model = self.network()
        #self.model = self.network("weights.hdf5")
        self.epsilon = 0
        self.actual = []
        self.memory = []


    def get_state(self,game):
        line=game.rep_playable_lines[0]
        game.save_list(game.rep_cellules)
        score=0
        score_max=0
        for i in range(len(game.rep_playable_lines)):
            tmp_line=game.rep_playable_lines[i]
            game.jouer_ligne(tmp_line)
            game.calculer_lignes_jouables()
            score=len(game.rep_playable_lines)
            if(score>score_max):
                score_max=score
                line=tmp_line
            game.read_list()    
            game.calculer_lignes_jouables()
        state=[line[1]=='v',
               line[1]=='h',
               line[1]=='dl',
               line[1]=='dr',
               line[0][0].x<10 and line[0][0].y<10,
               line[0][0].x<20 and line[0][0].y<20 and line[0][0].x>9 and line[0][0].y>9,
               line[0][0].x<30 and line[0][0].y<30 and line[0][0].x>19 and line[0][0].y>19,
               line[0][0].x<20 and line[0][0].y<10 and line[0][0].x>9,
               line[0][0].x<10 and line[0][0].y<20 and line[0][0].y>9,
               line[0][0].x<10 and line[0][0].y<30 and line[0][0].y>19,
               line[0][0].x<20 and line[0][0].y<30 and line[0][0].x>10 and line[0][0].y>19,
               line[0][0].x<30 and line[0][0].y<10 and line[0][0].x>19,
               line[0][0].x<30 and line[0][0].y<20 and line[0][0].x>19 and line[0][0].y>9,
               ]
        for i in range(13):
            if state[i]:
                state[i]=1
            else:
                state[i]=0
        return np.asarray(state)

    def set_reward(self, crash, score):
        self.reward = 0
        if crash:
            self.reward = -10
        if score==1:
            self.reward = 10
        return self.reward
    
    def network(self, weights=None):
        model = Sequential()
        model.add(Dense(output_dim=120, activation='relu', input_dim=13))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=120, activation='relu'))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=120, activation='relu'))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=3, activation='softmax'))
        opt = Adam(self.learning_rate)
        model.compile(loss='mse', optimizer=opt)

        if weights:
            model.load_weights(weights)
        return model

    def remember(self, state, action, reward, next_state, done):
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
        target = reward
        if not done:
            target = reward + self.gamma * np.amax(self.model.predict(next_state.reshape((1, 13)))[0])
        target_f = self.model.predict(state.reshape((1, 13)))
        target_f[0][np.argmax(action)] = target
        self.model.fit(state.reshape((1, 13)), target_f, epochs=1, verbose=0)
