import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
 id='LetterNoose-v0',
 entry_point='environments.letternoose:LetterNooseGym',
 timestep_limit=10,
 reward_threshold=1.0,
 nondeterministic=True,
)
