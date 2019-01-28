#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:39:27 2019

@author: 3700049
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math

class StrategieAlea(Strategy):
    def __init__(self, name = "alea"):
        Strategy.__init__(self, name)
    def compute_strategy(self, state, idteam, idplayer):
        if()