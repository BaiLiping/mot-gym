import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='MOT-v0',
    entry_point='mot.envs:MOTEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)
