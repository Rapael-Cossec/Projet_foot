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
    
    def __getattr__(self, attr):
        return getattr(self.state, attr)
    
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
        return self.ball - self.player
   
    @property
    def dir_point(self, vec):
        return self.state.position - vec
    
    def distance_balle(self, pointB, distance):
        return (self.state.ball.position.distance(pointB) < distance)
    
    def det_team(nb):
        if(nb == 1):
            return 1
        return 0
    
    def det_team_e(nb):
        if(nb == 1):
            return 2
        return 1
    
    
    @property
    def dir_ball_acc(self):
        """direction vers balle + acceleration de balle"""
        return ((6 * self.state.ball.vitesse + self.state.ball.position) - self.state.player_state(self.id_team, self.id_player).position).normalize().scale(5)
    
    
    def joueur_proche(self, id_team, id_player):
        opponents = [self.state.player_state(id_team, id_player) for (id_team, id_player) in self.state.players if id_player != self.id_player]
        return min([(self.player.distance(player.position), player) for player in opponents])[1]

    def joueur_proche_a(self, id_team, id_player):
        opponents = [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team == self.id_team and id_player != self.id_player]
        return min([(self.player.distance(player.position), player) for player in opponents])[1]
    
    def joueur_proche_ball(self, id_team, id_player):
        opponents = [self.state.player_state(id_team, id_player) for (id_team, id_player) in self.state.players]
        return min([(self.ball.distance(player.position), player) for player in opponents])[1]
    
    def joueur_e(self, id_team, id_player):
        return self.players_state(self.det_team_e(id_team, id_player))
    
    def joueur_solo_attaque(self, id_team):
        if(self.player.distance(Vector2D(self.player.x, self.joueur_e(self.det_team_e(id_team), 0).position.y)) < self.joueur_e(self.det_team_e(id_team), 0).distance(Vector2D(self.player.x, self.joueur_e(self.det_team_e(id_team), 0)).position.y)):
            return 1
    
    def passe(self, Vector):
        return Vector.normalize().scale(2.5)
    
    def shoot(self, Vector):
        return Vector.normalize().scale(3.8)
            