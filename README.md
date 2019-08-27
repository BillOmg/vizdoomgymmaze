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
VizdoomSelfMaze0-v0
VizdoomSelfMaze1-v0
VizdoomSelfMaze2-v0
VizdoomSelfMaze3-v0
VizdoomSelfMaze4-v0
VizdoomSelfMaze5-v0
VizdoomSelfMaze5-v0
# Indoor maze examples as follows:
VizdoomMazeOne1-v0
```

If you want to use indoor mazes, the environment name should like this: "VizdoomMaze\[One/Two/Three/Four][1~20]-v0"

For example,

```env = gym.make('VizdoomMazeOne1-v0')```

"One" means apartment has one bedroom, while "Two" means apartment has two bedroom.

With the bedrooms increasing, the structure of apartment become more and more complex, but the whole size of four style mazes is the same.