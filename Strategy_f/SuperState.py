#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:09:02 2019

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
from soccersimulator import settings
import math
import sys



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
#       return (self.state.ball.position - self.state.player_state(self.id_team, self.id_player).position).normalize().scale(5)
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
    @property
    def dir_ball_acc(self):
        """direction vers balle + acceleration de balle"""
        return ((self.state.ball.vitesse + self.state.ball.position) * 5 - self.state.player_state(self.id_team, self.id_player).position).normalize().scale(5)
    
    @property
    def bait(self):
        if (self.id_team==1):
            return Vector2D(self.player.x, GAME_HEIGHT)
        return Vector2D(self.player.x, 0)
            
    
    def joueur_proche(self, id_team, id_player):
        opponents = [self.state.player_state(id_team, id_player) for (id_team, id_player) in self.state.players if id_player != self.id_player]
        return min([(self.player.distance(player), player) for player in opponents])[1]

    def joueur_proche_a(self, id_team, id_player):
        opponents = [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team == self.id_team and id_player != self.id_player]
        return min([(self.player.distance(player), player) for player in opponents])[1]
    
    def passe(self, Vector):
        return Vector.normalize().scale(2.5)
    
    def shoot(self, Vector):
        return Vector.normalize().scale(3.8)
        
    def element_entre(debut, fin, obst):
        vdebut_fin = debut - fin
        vdebut_fin = obs - src
        return ((abs(vdebut_fin.angle-vdebut_fin.angle) < 0.2) and (debut.distance(obst) < debut.distance(fin)))

    def joueurs_entre(self, debut, fin):
        joueurs = [self.state.player_state(id_team, id_player) for (id_team, id_player) in self.state.players]
        for i in joueurs:
            obst = i
            
            if element_entre(debut, fin, obst):
                return obst
        return False
    
    
    def proche_balle(self):
        joueurs = [self.state.player_state(id_team, id_player) for (id_team, id_player) in self.state.players]
        for i in joueurs:
            if(i.distance(self.state.ball.position) < BALL_RADIUS + PLAYER_RADIUS):
                if i.id_team != self.id_team:
                    return 0 #ennemie le plus proche qui va frapper 
        
        if self.player().distance(self.ball) < BALL_RADIUS + PLAYER_RADIUS:
            return 1#moi qui vait frapper
        
        
        for i in joueurs:
            if(i.distance(self.state.ball.position) < BALL_RADIUS + PLAYER_RADIUS):
                if i.id_team == self.id_team:
                    return 2 #allie qui va frapper
                
        else:
            return 3 #personnne qui va frapper
        
    def shoot_safe(self):
        for i in range(0, GAME_HEIGHT/2):
            cible=Vector2D(GAME_WIDTH/2, i)
            if self.joueurs_entre(self.ball.position, cible) == False:
                return cible
        return Vector2D(self.ball.position.x + 20, GAME_HEIGHT)
        
    def ennemiebut(self):
        joueurs = [self.state.player_state(id_team, id_player) for (id_team, id_player) in self.state.players]
        res = joueur[0]
        for i in joueurs:
            d = i.distance(self.ball())
            if d < res.distance(self.ball()):
                res = d
        return res
    
    
    
    