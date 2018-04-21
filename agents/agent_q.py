'''
    Maintains a Q-Table across multiple episodes of gameplay.

    gym_env: a gym env instance, i.e. one created by gym.make('MyGame-v0')
    buckets: number of buckets to hash observed states into
     (This value may be less than the total number of states when memory
     constraints exist)
'''

import numpy as np
import pandas as pd
from utils import word_to_state

class AgentQ(object):
    def __init__(self, gym_env, buckets):
        self.gym_env = gym_env
        self.initial_state = self.gym_env.reset()
        self.buckets = buckets # for hashing
        self.state = word_to_state(self.initial_state)
        self.action_space_n = self.gym_env.env.action_space.n
        self.Q = np.zeros([self.buckets, self.action_space_n])
        self.cols = gym_env.env.getColumns()
        self.rows = gym_env.env.getRows()
        self.lr = .80 # learning rate
        self.y = .95 # discount (don't get too excited there, buddy)

    def resetForNewEpisode(self):
        self.initial_state = self.gym_env.reset()
        self.state = word_to_state(self.initial_state)

    def chooseAction(self, episode):
        # Choose an action by greedily (with noise) picking from Q table
        # Add episode number to reduce noise over time
        return np.argmax(self.Q[self.state, :] + np.random.randn(1, self.action_space_n) * (1.0/episode))

    def updateQTable(self, episode, step_fn): # Updates the Q-Table - credit to JT
       a = self.chooseAction(episode)
       # Get new state and reward from environment
       # print("action:", a, "state", self.state)
       s1, r, done, info = step_fn(a)
       # Update Q-Table with new knowledge
       s1 = word_to_state(s1)
       self.Q[self.state, a] = self.Q[self.state, a] + self.lr * (
         r + (self.y * np.max(self.Q[s1, :])) - self.Q[self.state, a])
       self.state = s1
       return done

    def getTable(self):
        df = pd.DataFrame(self.Q, index=self.rows, columns=self.cols)
        return df.loc[(df!=0).any(axis=1)]

    def learn(self, episode, step_fn):
        done = self.updateQTable(episode, step_fn)
        if done:
            self.resetForNewEpisode()
        return done
