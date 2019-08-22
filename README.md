# vizdoomgymmaze
This package is based on git@github.com:shakenes/vizdoomgym.git. 

This is a wrapper to use [ViZDoom](https://github.com/mwydmuch/ViZDoom "ViZDoom repository") together with [OpenAI Gym](https://github.com/openai/gym "OpenAI Gym repository"). Moreover, a selfmaze.wad is added into the scenarios, which includes 100 simple mazes and is builded from 7x7 gridworld maps.

Later, I will add more maps with different size and shape. Of course, I will pack codes about maze generator into this package.  

## Installation

```python
sudo apt-get install cmake libboost-all-dev libgtk2.0-dev libsdl2-dev python-numpy
git clone git@github.com:WangChen100/vizdoomgymmaze.git
cd vizdoomgymmaze
pip install -e .
```

## Usage

Use one of the environments (see list below for all available envs):
```python
import gym
import vizdoomgymmaze
env = gym.make('VizdoomSelfMaze0-v0')
episodes=10
for i in range(episodes)：
    print("Episodes #" + str(i+1))
    observation = env.reset()
    for step in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print"Episode finished after {} timesteps".format(step+1)
            break
env.close()

```
 ## Environments
List of available environments:
```python
VizdoomBasic-v0
VizdoomCorridor-v0
VizdoomDefendCenter-v0
VizdoomDefendLine-v0
VizdoomHealthGathering-v0
VizdoomMyWayHome-v0
VizdoomPredictPosition-v0
VizdoomTakeCover-v0
VizdoomDeathmatch-v0
VizdoomHealthGatheringSupreme-v0
VizdoomSelfMaze0-V0
VizdoomSelfMaze1-V0
VizdoomSelfMaze2-V0
VizdoomSelfMaze3-V0
VizdoomSelfMaze4-V0
VizdoomSelfMaze5-V0
```
