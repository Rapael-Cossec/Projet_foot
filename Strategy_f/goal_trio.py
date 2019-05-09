#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 19:16:46 2019

@author: 3700049
"""

GAME_WIDTH = 150
GAME_HEIGHT = 90
PLAYER_RADIUS = 1.
BALL_RADIUS = 0.65
CAN_SHOOT = PLAYER_RADIUS + BALL_RADIUS


from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from Strategy_f.tools import SuperState
from soccersimulator import settings
import math



class StrategyDefenseur_trio(Strategy):
    
    
    def __init__(self):
        Strategy.__init__(self, "Defenseur Central")
        self.counter = 0
        self.counter2 = 0
    def compute_strategy(self, state, id_team, id_player):
        
        s = SuperState(state, id_team, id_player)
        
        pos_cible = ((s.ball - s.goal_a)/2 + (s.goal_a - s.player)).scale(5)
        dir_balle = s.ball - s.player
        action = s.procheballe()
        
        if(action == 1):
            return SoccerAction(dir_balle, s.shootsafe())
        
        if(s.ball().distance(s.goal_a()) < 10):
            if(s.ennemiebut.distance(dir_balle) > 20):
                if(action == 3):
                    return SoccerAction(dir_balle, Vector2D(0, 0))
                else:
                    return SoccerAction(dir_balle, s.shootsafe())