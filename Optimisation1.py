#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 19:16:46 2019

@author: 3700049
"""
from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math

from Strategy_f import SuperState, StrategySolo, StrategyAttaquant, StrategyDefenseur
from soccersimulator import SoccerTeam

class GoTestStrategy(Strategy):
    def __init__(self, strength=None):
        Strategy.__init__(self, "Go-getter")
        self.strength = strength
    
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        return s.dir_ball + s.goal_e
    
expe = GoalSearch(strategy= GoTestStrategy(), 'strength',[0.1 , 5])
expe.start()
print(expe.get_res())
print(expe.get_best())