"""
A model of the human glucoregulatory system provided by
openaps-predict: https://github.com/loudnate/openaps-predict
which uses the Walsh IOB algorithm to determine effect of
added insulin on glucose level.
"""

import logging
from gym import spaces
from gym.utils import seeding
import numpy as np

import openapscontrib.predict as predict

logging.info("imports succeeded")

class GlucoregulatoryEnv(gym.Env):

    def __init__(self):
        """
        We need to initialize some random BGL and start inserting events.
        """


    def _step(self, action):
        """
        Take an action and update the model

        Returns standard Env._step tuple:
            observation: object
            reward: float
            done: boolean
            info: dict

        Human operators have many observations that we will not allow the
        pancreas operator to have. For example the GlucoregulatoryEnv can
        decide to do exercise and eat, but our pancreas doesn't directly
        observe those actions. The pancreas observes instantaneous blood
        glucose levels and makes an action of how much insulin to dose.

        The reward will need tuning with time, but the idea is that we want
        to live, and ideally stay within some acceptable blood-glucose level.
        Something like inverse square distance from 100 sounds reasonable for
        now.

        If we die (BGL <20ish, > 800ish) then declare done :-(

        I guess we can provide the actions such as eating and exercise as
        info
        """

        return observation, reward, done, info