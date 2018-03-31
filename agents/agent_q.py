'''
    Maintains a Q-Table across multiple episodes of gameplay.

    gym_env: a gym env instance, i.e. one created by gym.make('MyGame-v0')
    buckets: number of buckets to hash observed states into
     (This value may be less than the total number of states when memory
     constraints exist)
'''

import numpy as np

class AgentQ(object):
    def __init__(self, gym_env, buckets):
        self.gym_env = gym_env
        self.initial_state = self.gym_env.reset()
        self.buckets = buckets # for hashing
        self.state = self.hash(self.initial_state)
        self.action_space_n = self.gym_env.env.action_space.n
        self.Q = np.zeros([self.buckets, self.action_space_n])
        self.lr = .8 # learning rate
        self.y = 1.00 # .95 # discount (don't get too excited there, buddy)

    def resetForNewEpisode(self):
        self.state = self.hash(self.initial_state)
        self.gym_env.reset()

    # Converts vector to one number - credit to JT
    def hash(self, vec):
        l = len(vec)
        bucket = l % self.buckets
        for index in range(l):
            item = ord(vec[index]) if type(vec[index]) is str else vec[index] # handle int and chars
            bucket = (bucket + item) % self.buckets
        return bucket

    def updateQTable(self, episode, step_fn): # Updates the Q-Table - credit to JT
        # Choose an action by greedily (with noise) picking from Q table
       a = np.argmax(
         self.Q[self.state, :] + np.random.randn(1, self.action_space_n) * (
           1. / (episode + 1)))
       # Get new state and reward from environment
       s1, r, done, info = step_fn(a)
       s1 = self.hash(s1)
       # Update Q-Table with new knowledge
       self.Q[self.state, a] = self.Q[self.state, a] + self.lr * (
         r + self.y * np.max(self.Q[s1, :]) - self.Q[self.state, a])
       self.state = s1
       return done

    def learn(self, episode, step_fn):
        done = self.updateQTable(episode, step_fn)
        if done:
            self.resetForNewEpisode()
        return done
