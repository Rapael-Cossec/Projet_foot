#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 18:45:53 2019

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
from .tools import SuperState
from soccersimulator import settings
import math



class StrategySolo(Strategy):
    
    
    def __init__(self, succ=None):
        Strategy.__init__(self, "Solo")
        self.counter = 0
        self.counterstep = 0
        self.counter_engage = 0
        self.score1=0
        self.score2=0
        self.succ=succ
    def compute_strategy(self, state, id_team, id_player):
        if(state.step==0):
            self.counterstep = 0
            self.counter = 0
            self.counter_engage = 0
#        self.counter=0    #retirer pour la contre attaque
        
        self.counterstep += 1
        s = SuperState(state, id_team, id_player)
        dir_balle = s.ball - s.player
        #        Distance_Shoot = (s.ball - s.player).norm 
        pos_cible = ((s.ball - s.goal_a)*0.6 + (s.goal_a - s.player)).scale(5)
        
        if(s.ball.x>GAME_WIDTH/2 and self.counter_engage == 1):
            if(dir_balle.norm < CAN_SHOOT):
                return SoccerAction(dir_balle, (s.goal_e - s.player).normalize().scale(3.8))
            return SoccerAction(dir_balle, Vector2D(0, 0))
        
        if(s.ball_vitesse.norm==0):
            self.counter = 0
            self.counter_engage = 0
            self.score1=s.state.score_team1
            self.score2=s.state.score_team2

      
#        if(self.counter_engage == 0):
#            if(s.dir_ball.norm < CAN_SHOOT+1.784):
#                self.counter_engage = 1
#                return SoccerAction(dir_balle, s.shoot((s.goal_e - s.player)).normalize().scale(3.8))
#            return SoccerAction(dir_balle, Vector2D(0,0))

#            
#        if(dir_balle.norm < CAN_SHOOT):
#            return SoccerAction(dir_balle, (s.goal_e - s.player).normalize().scale(3.8) )
#        return SoccerAction(dir_balle, Vector2D(0, 0))
#        
            """
        if(dir_balle.norm < CAN_SHOOT):
            return SoccerAction(dir_balle, (s.goal_e - s.player).normalize().scale(3.8))
        return SoccerAction(dir_balle, Vector2D(0, 0))
        """

        if(self.counter == 1):
            if(dir_balle.norm < CAN_SHOOT):
                return SoccerAction(dir_balle, (s.goal_e - s.player).normalize().scale(3.8))
            return SoccerAction(dir_balle, Vector2D(0, 0))
        
        
        if(self.counterstep >= 1900):
            if(dir_balle.norm < CAN_SHOOT):
                return SoccerAction(dir_balle, (s.goal_e - s.player).normalize().scale(5.0))
            return SoccerAction(dir_balle, Vector2D(0, 0))
        
        
        if(id_team==1):
            if((s.ball - s.player).norm + (s.ball - s.goal_e).norm < (s.ball - s.joueur_e(id_team, id_player)).norm + (s.ball - s.goal_e).norm and (s.player.x > s.joueur_e(id_team, id_player).x)):
                if(dir_balle.norm < CAN_SHOOT):
                    self.counterstep = 0
                    self.counter = 1
                    return SoccerAction(dir_balle, (s.goal_e - s.player).normalize().scale(3.8))
                if(s.distance_balle(s.player, 10)):
                    return SoccerAction(dir_balle, Vector2D(0., 0.))
                return SoccerAction(pos_cible, Vector2D(0,0))
            
        if(id_team==2):
           if((s.ball - s.player).norm + (s.ball - s.goal_e).norm < (s.ball - s.joueur_e(id_team, id_player)).norm + (s.ball - s.goal_e).norm and (s.player.x < s.joueur_e(id_team, id_player).x)):
               if(dir_balle.norm < CAN_SHOOT):
                   """, strength=None, vitesse=None"""
                   self.counterstep = 0
                   self.counter = 1
                   return SoccerAction(dir_balle, (s.goal_e - s.player).normalize().scale(3.8))
               if(s.distance_balle(s.player, 10)):
                   return SoccerAction(dir_balle, Vector2D(0., 0.))
               return SoccerAction(pos_cible, Vector2D(0,0))
           
    
        if(s.distance_balle(s.player, CAN_SHOOT)):
            if(s.dir_ball.norm < CAN_SHOOT):
                self.counterstep = 0
                if(s.player.x < GAME_WIDTH*0.5 and s.player.y < GAME_HEIGHT*0.5): #en bas à gauche
                        return SoccerAction(dir_balle,(Vector2D(0,0)-s.player).normalize().scale(3.8))
                if(s.player.x < GAME_WIDTH*0.5 and s.player.y > GAME_HEIGHT*0.5): #en haut à gauche
                    return SoccerAction(dir_balle,(Vector2D(0,GAME_HEIGHT)-s.player).normalize().scale(3.8))
                if(s.player.x > GAME_WIDTH*0.5 and s.player.y > GAME_HEIGHT*0.5): #en haut à droite
                    return SoccerAction(dir_balle,(Vector2D(GAME_WIDTH,GAME_HEIGHT)-s.player).normalize().scale(3.8))
                if(s.player.x > GAME_WIDTH*0.5 and s.player.y < GAME_HEIGHT*0.5): #en bas à droite
                    return SoccerAction(dir_balle,(Vector2D(GAME_WIDTH,0)-s.player).normalize().scale(3.8))
                if(s.joueur_e(id_team, id_player).y > s.player.y):
                    return SoccerAction(dir_balle, (Vector2D(0, -GAME_HEIGHT).normalize().scale(3.8)))
                return SoccerAction(dir_balle, Vector2D(0, GAME_HEIGHT).normalize().scale(2.5))
            return SoccerAction(dir_balle, Vector2D(0,0))
        
        # id_team is 1 or 2
        # id_player starts at 0
        

        if(s.distance_balle(s.player, 10)):
            return SoccerAction(dir_balle, Vector2D(0., 0.))
        return SoccerAction(pos_cible, Vector2D(0,0))
    
    
    
    
    
    
    
    
    
"""
        if s.joueur_proche_ball(id_team, id_player) == s.player:
            if(dir_balle.norm < CAN_SHOOT):
                return SoccerAction(s.dir_ball, (s.goal_e - s.player).normalize().scale(3.8))
            return SoccerAction(dir_balle, Vector2D(0,0))
"""
