#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:59:16 2019

@author: 3700049
"""
GAME_WIDTH = 150
GAME_HEIGHT = 90
PLAYER_RADIUS = 1.
BALL_RADIUS = 0.65
CAN_SHOOT = PLAYER_RADIUS + BALL_RADIUS


"""si il est plus proche du but que l'ennemie il fonce
pb joeueur proche et tout ca tout ca """

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from .tools import SuperState
from soccersimulator import settings
import math

class StrategyDefenseur(Strategy):
    def __init__(self, test=None):
        Strategy.__init__(self, "Defenseur")
        self.test = test
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        dir_balle = s.ball - s.player
#        Distance_Shoot = (s.ball - s.player).norm 
        pos_cible = ((s.ball - s.goal_a)*0.6 + (s.goal_a - s.player)).scale(5)
        if(s.distance_balle(s.player, CAN_SHOOT)):
            if(s.state.nb_players(id_team) > 1):
                a=s.dir_ball.norm*self.test
                return SoccerAction(((a*s.state.ball.vitesse + s.state.ball.position) - s.state.player_state(s.id_team, s.id_player).position).normalize().scale(5), (s.joueur_proche_a(id_team, id_player) - s.player).normalize().scale(3))
            return SoccerAction(dir_balle, (s.goal_e - s.player).normalize().scale(3.8))
        # id_team is 1 or 2
        # id_player starts at 0
        
        if(s.distance_balle(s.player, 10)):
            return SoccerAction(dir_balle, Vector2D(0., 0.))
        return SoccerAction(pos_cible, Vector2D(0,0))
