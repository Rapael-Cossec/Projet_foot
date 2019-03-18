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
        self.counterstep = 0
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
#        dir_balle = s.ball - s.player
#        pos_cible = ((s.ball - s.goal_a)*0.6 + (s.goal_a - s.player)).scale(5)
#        mid_goal_e = ((s.ball - s.goal_e)*0.7 + (s.goal_e - s.player)).scale(5)
        if(s.ball.x == GAME_WIDTH/2 and s.ball.y == GAME_HEIGHT/2):
            self.counter_engage = 0
            self.counterstep += 1
            """
        if(self.attaquant_e == 0):
            joueur_e = s.joueur_proche(id_team, id_player)
            if(joueur_e != s.joueur_proche_a(id_team, id_player)):
                self.id_player_e1 = s.test_joueur_e(id_team, 1, joueur_e)
                self.attaquant_e = state.player_state(s.det_team_e(id_team), self.id_player_e1)
                print(self.id_player_e1)
               """ 
        self.counterstep += 1
        if(self.counter_engage == 0 and self.counterstep<2):
            return SoccerAction(Vector2D(0,0), Vector2D(0,0))
            
        if(self.counter_engage == 0):
            if(s.dir_ball.norm < CAN_SHOOT):
                self.counter_engage = 1
                return SoccerAction(s.dir_ball_acc, s.shoot((s.goal_e - s.player)).normalize().scale(3.8))
                return SoccerAction(s.dir_ball_acc, Vector2D(0,0))
        
    
        joueur_proche = s.joueur_proche_ball_all(id_team, id_player)
        if(id_team == 1):     
            if(joueur_proche == s.joueur_proche_ball_a(id_team, id_player)):
                return SoccerAction(Vector2D(GAME_HEIGHT/2, GAME_WIDTH/2) - s.player, Vector2D(0, 0))
        else:
            if(joueur_proche == s.joueur_proche_ball_a(id_team, id_player)):
                return SoccerAction(Vector2D(GAME_HEIGHT/2, GAME_WIDTH/2) - s.player + Vector2D(GAME_HEIGHT/2, 0), Vector2D(0, 0))
            
#            return SoccerAction(s.player - Vector2D(joueur_proche.position.x + (10 * s.det_team(id_team)), joueur_proche.position.y))
        
        if(joueur_proche == s.joueur_proche_ball_a(id_team, id_player)): #se mettre sur l'axe x de l'attaquant adverse mais avec un y opposé
            if(Vector2D(state.player_state(s.det_team_e(id_team),self.id_player_e1).position.x<10)):
                return SoccerAction(Vector2D(state.player_state(s.det_team_e(id_team),self.id_player_e1).position.x+10, 90-state.player_state(s.det_team_e(id_team),self.id_player_e1).position.y)-s.player, Vector2D(0,0)) #il ne va pas vers la bonne direction
            if(Vector2D(state.player_state(s.det_team_e(id_team),self.id_player_e1).position.x>140)):
                return SoccerAction(Vector2D(state.player_state(s.det_team_e(id_team),self.id_player_e1).position.x-10, 90-state.player_state(s.det_team_e(id_team),self.id_player_e1).position.y)-s.player, Vector2D(0,0)) #il ne va pas vers la bonne direction
            return SoccerAction(Vector2D(state.player_state(s.det_team_e(id_team),self.id_player_e1).position.x-10, 90-state.player_state(s.det_team_e(id_team),self.id_player_e1).position.y)-s.player, Vector2D(0,0)) #il ne va pas vers la bonne direction

        if(s.dir_ball.norm < CAN_SHOOT):
            return SoccerAction(s.dir_ball.normalize().scale(5), s.shoot((s.goal_e - s.player)).normalize().scale(3.8))
        return SoccerAction(s.dir_ball.normalize().scale(5), Vector2D(0,0))
        
    
    
    
    
    
    
    
        """
        if(joueur_proche == s.joueur_proche_ball_a and joueur_proche!=s.player):
            return SoccerAction(s.player - Vector2D(joueur_proche.position.x + (30 * s.det_team(id_team)), joueur_proche.position.y))
#        if(s.dir_ball.norm < CAN_SHOOT):
#            return SoccerAction(s.dir_ball_acc, s.shoot((s.goal_e - s.player)).normalize().scale(3.8))
#        return SoccerAction(s.dir_ball_acc, Vector2D(0,0))
#    
                  
            if(dir_balle.norm < CAN_SHOOT):
                self.counterstep = 0
                self.counter2 +=1
                return SoccerAction(dir_balle, (s.joueur_proche_a(id_team, id_player).position-s.player).normalize().scale(3.8))
            if(s.distance_balle(s.player, 10)):
                return SoccerAction(dir_balle, Vector2D(0., 0.))
                return SoccerAction(pos_cible, Vector2D(0,0))
            """
#        joueur_proche.position.y    s.player -
#            joueur_proche.position.x + (10 * s.det_team(id_team))