import gym
import environments
from agents.agent_q import AgentQ
from game_runner import GameRunner

# Make a gym
env = gym.make('LetterNoose-v0')
env.reset()

# Make an agent
agent = AgentQ(env, 27**5)

# Run games
game = GameRunner(env, agent)
game.trainEpisodes(20)

# View stats
game.printTrainStats()
