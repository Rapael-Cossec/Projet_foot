#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:09:02 2019

@author: 3700049
"""
GAME_WIDTH = 150
GAME_HEIGHT = 90

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math

class SuperState(SoccerState):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
    @property
    def ball(self):
        return self.state.ball.position
    
    @property
    def player(self):
        return self.state.player_state(self.id_team, self.id_player).position
    @property
    def goal_e(self):
        if (self.id_team==1):
            return Vector2D(GAME_WIDTH, GAME_HEIGHT/2)
        return Vector2D(0, GAME_HEIGHT/2)
    
    @property
    def goal_a(self):
        if (self.id_team==2):
            return Vector2D(GAME_WIDTH, GAME_HEIGHT/2)
        return Vector2D(0, GAME_HEIGHT/2)
    
    @property
    def dir_ball(self):
       return (self.state.ball.position - self.state.player_state(self.id_team, self.id_player).position).normalize().scale(5)
   
    @property
    def dir_point(self, vec):
        return self.state.position - vec
    
    def distance_balle(self, pointB, distance):
        return (self.state.ball.position.distance(pointB) < distance)
    
    def det_team(nb):
        if(nb == 1):
            return 1
        return 0

    def joueur_proche(self, id_team, id_player):
        proche = self.state.player_state(id_team, 0)
        for i in range (self.state.nb_players(id_team)):
            print(i)
            if(self.state.player_state(id_team, i).position.distance(proche.position) < 2):
                continue
            if(self.state.player_state(id_team, i).position.distance(self.player)< proche.position.distance(self.player)):
                proche = self.state.player_state(id_team, i)
                print(id_player)
        print(proche)
        return proche
    