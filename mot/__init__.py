import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='MOT-v0',
    entry_point='mot.envs:MOTEnv',
    reward_threshold=1.0,
    nondeterministic = True,
)
