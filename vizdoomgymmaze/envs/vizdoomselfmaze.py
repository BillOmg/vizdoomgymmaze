from vizdoomgymmaze.envs.vizdoomenv import VizdoomEnv


class VizdoomSelfMaze(VizdoomEnv):

    def __init__(self):
        super(VizdoomSelfMaze, self).__init__(10)
