#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:22:38 2019

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

class StrategyAttaquant_duo(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant Central")
        self.counter_engage = 0
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        if(self.counter_engage == 0):
            if(s.dir_ball.norm < CAN_SHOOT):
                self.counter_engage = 1
                return SoccerAction(s.dir_ball_acc, s.shoot((s.goal_e - s.player)))
            return SoccerAction(s.dir_ball_acc, Vector2D(0,0))
        if(s.ball.x == GAME_WIDTH/2 and s.ball.y == GAME_HEIGHT/2):
            counter_engage = 0
        joueur_proche = s.joueur_proche_ball(id_team, id_player)
        if(joueur_proche.id_team == id_team and joueur_proche.id_player != id_player):
            return SoccerAction(s.player - Vector2D(joueur_proche.position.x + (30 * s.det_team(id_team)), joueur_proche.position.y))