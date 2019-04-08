#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:18:20 2019

@author: 3700049
"""

GAME_WIDTH = 180
GAME_HEIGHT = 90
PLAYER_RADIUS = 1.
BALL_RADIUS = 0.65
CAN_SHOOT = PLAYER_RADIUS + BALL_RADIUS

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from .tools import SuperState
from soccersimulator import settings
import math

class StrategyAttaque2_v(Strategy):
    def __init__(self): 
        Strategy.__init__(self, "Attaquant")
#        self.strength = strength
#        self.vitesse = vitesse
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        dir_balle = s.ball - s.player
        
        joueur_proche = s.joueur_proche_ball_all(id_team, id_player)
        if(id_team == 1):
            if(joueur_proche == s.joueur_proche_ball_a(id_team, id_player) or s.ball.x < 60):
                return SoccerAction(Vector2D(GAME_WIDTH*7/16, s.ball.y) - s.player, Vector2D(0, 0))
        else:
            if(joueur_proche == s.joueur_proche_ball_a(id_team, id_player)or s.ball.x > GAME_WIDTH - 60):
                return SoccerAction(Vector2D(GAME_WIDTH*9/16, s.ball.y) - s.player, Vector2D(0, 0))
        if(id_team == 1):
            if(s.ball.x <= GAME_WIDTH/2):
                if(s.dir_ball.norm < CAN_SHOOT):
                    if(s.ball.x <= GAME_WIDTH/2 - 20):
                        return SoccerAction(dir_balle, (Vector2D(GAME_WIDTH/2 - 10, GAME_HEIGHT/2)-s.player).normalize().scale(3))
                    if(s.joueur_e(2, 0).x > GAME_HEIGHT/2):
                        return SoccerAction(dir_balle, (Vector2D(GAME_WIDTH, 0)-s.player).normalize().scale(3))
                    return SoccerAction(dir_balle, (Vector2D(GAME_WIDTH, GAME_HEIGHT)-s.player).normalize().scale(3))
                return SoccerAction(s.dir_ball.normalize().scale(5.0), Vector2D(0, 0))
        else:
            if(s.ball.x > GAME_WIDTH/2):
                if(s.dir_ball.norm < CAN_SHOOT):
                    if(s.ball.x >= GAME_WIDTH/2 + 20):
                        return SoccerAction(dir_balle, (Vector2D(GAME_WIDTH/2 + 10, GAME_HEIGHT/2)-s.player).normalize().scale(3))
                    if(s.joueur_e(2, 0).x <= GAME_HEIGHT/2):
                        return SoccerAction(dir_balle, (Vector2D(0, 0)-s.player).normalize().scale(3))
                    return SoccerAction(dir_balle, (Vector2D(0, GAME_HEIGHT)-s.player).normalize().scale(3))
                return SoccerAction(s.dir_ball.normalize().scale(5.0), Vector2D(0, 0))
            
            
        if(id_team == 1):
            return SoccerAction(Vector2D(GAME_WIDTH*7/16, s.ball.y) - s.player, Vector2D(0, 0))
        return SoccerAction(Vector2D(GAME_WIDTH*9/16, s.ball.y) - s.player, Vector2D(0, 0))