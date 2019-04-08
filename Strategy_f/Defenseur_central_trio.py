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
        if (id_team == 1):
            if(state.ball.position.x >= GAME_WIDTH/4):
                return SoccerAction(Vector2D(GAME_WIDTH/15, pos_cible.y) - s.player, Vector2D(0, 0))
            action = s.proche_balle()
            if(action == 0 or action == 3):
                return SoccerAction(Vector2D(GAME_WIDTH/15, pos_cible.y) - s.player, Vector2D(0, 0))
            if(action == 1):
                return SoccerAction(dir_balle, s.shoot_safe())
            if(action == 2):
                return SoccerAction(s.shoot_safe(), Vector2D(0, 0))
            
        else:
            if(state.ball.position.x >= GAME_WIDTH*14/15):
                return SoccerAction(dir_balle, s.shoot_safe())
            if(state.ball.position.x <= GAME_WIDTH*3/4):
                return SoccerAction(Vector2D(GAME_WIDTH*14/15, pos_cible.y) - s.player, Vector2D(0, 0))
            action = s.proche_balle()
            if(action == 0 or action == 3):
                return SoccerAction(Vector2D(GAME_WIDTH*14/15, pos_cible.y) - s.player, Vector2D(0, 0))
            if(action == 1):
                return SoccerAction(dir_balle, s.shoot_safe())
            if(action == 2):
                return SoccerAction(s.shoot_safe(), Vector2D(0, 0))
            
            
        return SoccerAction(Vector2D(0, 0), Vector2D(0, 0))
        
                
"""
        if((s.ball.x + s.ball_vitesse.x) < 0):
#        Distance_Shoot = (s.ball - s.player).norm 
            pos_cible = ((s.ball - s.goal_a)/2 + (s.goal_a - s.player)).scale(5)
            joueur_proche = s.joueur_proche_ball_all(id_team, id_player)
            if(s.player.distance(s.ball) < s.joueur_e(id_team, id_player).distance(s.ball)):
                if(self.counter2 == 0):
                    if(dir_balle.norm < CAN_SHOOT):
                        return SoccerAction(s.dir_ball.normalize().scale(5.0), (Vector2D(state.player_state(id_team, 3).position.x + 20,  state.player_state(id_team, 3).position.y) - s.player).normalize().scale(3.8))
                    if(s.distance_balle(s.player, 10)):
                        return SoccerAction(dir_balle, Vector2D(0., 0.))
                    return SoccerAction(pos_cible, Vector2D(0,0))
                
                joueur_proche = s.joueur_proche_ball_all(id_team, id_player)
                if(joueur_proche == s.joueur_proche_ball_a(id_team, id_player)):
                    return SoccerAction(pos_cible, Vector2D(0,0))
                
                if(dir_balle.norm < CAN_SHOOT):
                    self.counterstep = 0
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), (Vector2D(state.player_state(id_team, 3).position.x + 20,  state.player_state(id_team, 3).position.y) - s.player).normalize().scale(3.8))
                return SoccerAction(dir_balle, Vector2D(0, 0))
            if(s.distance_balle(s.player, 10)):
                return SoccerAction(dir_balle, Vector2D(0., 0.))
            return SoccerAction(pos_cible, Vector2D(0,0))
        #defenseur qui attend l'adversaire avant de tirer
        
        else:
            pos_cible = ((s.ball - s.goal_a)/2 + (s.goal_a - s.player)).scale(5)
            joueur_proche = s.joueur_proche_ball_all(id_team, id_player)
            if(s.player.distance(s.ball) < s.joueur_e(id_team, id_player).distance(s.ball)):
                if(self.counter2 == 0):
                    if(dir_balle.norm < CAN_SHOOT):
                        return SoccerAction(s.dir_ball.normalize().scale(5.0), (Vector2D(state.player_state(id_team, 3).position.x + 20,  state.player_state(id_team, 3).position.y) - s.player).normalize().scale(3.8))
                    if(s.distance_balle(s.player, 10)):
                        return SoccerAction(dir_balle, Vector2D(0., 0.))
                    return SoccerAction(pos_cible, Vector2D(0,0))
                
                joueur_proche = s.joueur_proche_ball_all(id_team, id_player)
                if(joueur_proche == s.joueur_proche_ball_a(id_team, id_player)):
                    return SoccerAction(pos_cible, Vector2D(0,0))
                
                if(dir_balle.norm < CAN_SHOOT):
                    self.counterstep = 0
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), (Vector2D(state.player_state(id_team, 3).position.x + 20,  state.player_state(id_team, 3).position.y) - s.player).normalize().scale(3.8))
                return SoccerAction(dir_balle, Vector2D(0, 0))
            if(s.distance_balle(s.player, 10)):
                return SoccerAction(dir_balle, Vector2D(0., 0.))
            return SoccerAction(pos_cible, Vector2D(0,0))"""