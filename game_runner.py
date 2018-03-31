'''
    Class that runs a game using an agent and environment.
    Expects an agent with a "learn" method.
    Expects an environment with "render" and "step" methods.
'''

class GameRunner():
    def __init__(self, gym_env, agent):
        self.gym_env = gym_env
        self.agent = agent
        self.episodesTrained = 0
        self.stats = []

    def trainEpisodes(self, n=1, verbose=False):
        for episode in range(1, n+1):
            print("Episode", str(episode) + ":")
            self.episodesTrained += 1
            self.stats.append({ "episode": episode, "netReward": 0 })
            done = False
            while not done:
                if verbose:
                    self.gym_env.render()
                def step_fn(action):
                    observation, reward, done, info = self.gym_env.step(action)
                    self.stats[episode - 1]["endState"] = observation
                    rewardsEarned = self.stats[episode - 1]["netReward"]
                    runningReward = rewardsEarned + reward
                    self.stats[episode - 1]["netReward"] = runningReward
                    if verbose:
                        print("action:", action)
                        print("observation:", observation)
                        print("reward:", reward)
                        print("done:", done)
                        print("info:", info)
                    else:
                        print("action:", action, "reward:", reward)
                    return observation, reward, done, info
                done = self.agent.learn(episode, step_fn)

    def printTrainStats(self):
        print("===========================================")
        print("Training Stats:\n")
        print("Trained on", self.episodesTrained, "episodes.")
        print("Stats per Episode:")
        for episode in self.stats:
            print("episode:", episode["episode"], "reward:",
            episode["netReward"], "ending state:", episode["endState"])
        print("===========================================")
