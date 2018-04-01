## Gym Agent Runner

A helper class that pairs game environments and reinforcement learning agents. Keeps basic stats on the game runs (net reward and end state, per episode). Uses open.ai's gym.

### Files in this project

* `game_runner.py` contains a helper class for pairing a gym and agent, running multiple game episodes, and printing results

* `environments/letternoose.py` is a game environment for "Letter Noose" (aka Hangman)

* `agents/agent_q.py` is a basic Q-Table agent

* `run.py` sets up the gym, agent and game runner to train on episodes and print stats

### How to run this code

`python run.py`
