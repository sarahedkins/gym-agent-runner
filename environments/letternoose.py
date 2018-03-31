from collections import defaultdict
from gym import spaces
import gym
import string
import random

alphabet = ["abcdefghijklmnopqrstuvwxyz"]
singleThreeLetterWord = ["cat"]
threeLetterWords = ["cat", "dog", "man", "wok", "rot"]
fiveLetterWords = ["socks", "birds", "album", "olive", "angry", "beach"]
longerWords = ["giraffe", "umbrella", "elephant", "chalkboard"] # too long for memory

class LetterNooseGym(gym.Env):
 words = singleThreeLetterWord
 letters = list(string.ascii_lowercase)
 metadata = {'render.modes': ['human', 'ansi']}
 def __init__(self):
   super(LetterNooseGym).__init__()
   self.letters_guessed = []
   self.gameover = False
   self.solution = LetterNooseGym.words[random.randint(0, len(LetterNooseGym.words)-1)]
   self.solution_length = len(self.solution)
   self.attempts_remaining = self.calcAttemptsAllowed()
   self.board = ['_'] * self.solution_length # _ _ _
   self.action_space = spaces.Discrete(26) # 26 letters, selecting a letter is the action
   self.observation_space = spaces.Discrete(self.solution_length) # _ _ _

 def _reset(self):
   self.letters_guessed = []
   self.gameover = False
   self.solution = LetterNooseGym.words[random.randint(0, len(LetterNooseGym.words)-1)]
   self.solution_length = len(self.solution)
   self.attempts_remaining = self.calcAttemptsAllowed()
   self.board = ['_'] * self.solution_length
   self.action_space = spaces.Discrete(26)
   self.observation_space = spaces.Discrete(self.solution_length)
   return self.board

 def _render(self, mode='human', close=False):
    print('\n')
    print('Already guessed:', self.letters_guessed)
    print('Attempts remaining:', self.attempts_remaining)
    print("Board", self.board)

 def calcAttemptsAllowed(self):
    # number of unique letters in solution word + 20%
    unique_letters_count = len(set(self.solution))
    return unique_letters_count + int(unique_letters_count * .2)

 def decrementAttemptsRemaining(self):
     self.attempts_remaining -= 1

 def updateBoard(self, char):
     for index, letter in enumerate(self.solution):
         if letter == char:
             self.board[index] = char
             return True
     return False

 def updateObservationSpace(self, char):
     for letter in self.letters_guessed:
         if letter == char:
             self.board[idx] = char

 def isWon(self):
     for idx, letter in enumerate(self.solution):
         if letter != self.board[idx]:
             return False
     return True

 def _step(self, action):
    reward = 0
    char = LetterNooseGym.letters[action]
    self.decrementAttemptsRemaining()
    if not char or char in self.letters_guessed:
        reward = -1 # invalid action
        self.letters_guessed.append(char)
    else:
        updated = self.updateBoard(char)
        self.letters_guessed.append(char)
        if updated:
            reward = 1
        if self.isWon():
            reward = 2
            self.gameover = True
        elif self.attempts_remaining <= 0:
            self.gameover = True
            # print("Game Over")
    return self.board, reward, self.gameover, {}
