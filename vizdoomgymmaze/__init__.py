from gym.envs.registration import register

register(
    id='VizdoomBasic-v0',
    entry_point='vizdoomgymmaze.envs:VizdoomBasic'
)

register(
    id='VizdoomCorridor-v0',
    entry_point='vizdoomgymmaze.envs:VizdoomCorridor'
)

register(
    id='VizdoomDefendCenter-v0',
    entry_point='vizdoomgymmaze.envs:VizdoomDefendCenter'
)

register(
    id='VizdoomDefendLine-v0',
    entry_point='vizdoomgymmaze.envs:VizdoomDefendLine'
)

register(
    id='VizdoomHealthGathering-v0',
    entry_point='vizdoomgymmaze.envs:VizdoomHealthGathering'
)

register(
    id='VizdoomMyWayHome-v0',
    entry_point='vizdoomgymmaze.envs:VizdoomMyWayHome'
)

register(
    id='VizdoomPredictPosition-v0',
    entry_point='vizdoomgymmaze.envs:VizdoomPredictPosition'
)

register(
    id='VizdoomTakeCover-v0',
    entry_point='vizdoomgymmaze.envs:VizdoomTakeCover'
)

register(
    id='VizdoomDeathmatch-v0',
    entry_point='vizdoomgymmaze.envs:VizdoomDeathmatch'
)

register(
    id='VizdoomHealthGatheringSupreme-v0',
    entry_point='vizdoomgymmaze.envs:VizdoomHealthGatheringSupreme'
)

register(
    id='VizdoomSelfMaze-v0',
    entry_point='vizdoomgymmaze.envs:VizdoomSelfMaze'
)