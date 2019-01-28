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
from soccersimulator import settings
import math

class StrategyDefenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
#        Distance_Shoot = (s.ball - s.player).norm 
        pos_cible = ((s.ball - s.goal_a)/2 + (s.goal_a - s.player)).scale(5)
        if(s.distance_balle(s.player, CAN_SHOOT)):
            return SoccerAction(pos_cible, (s.joueur_proche(id_team, id_player)).position - s.player)
        # id_team is 1 or 2
        # id_player starts at 0
        if(s.distance_balle(s.player, 20)):
            return SoccerAction(s.dir_ball, Vector2D(0., 0.))
        return SoccerAction(pos_cible, Vector2D(0,0))

    
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team2.add("Defenseur", RandomStrategy())  # Random strategy
#team1.add("Defenseur", StrategyDefenseur())   # Static strategy
team1.add("Defenseur", StrategyFonceur())  # Random strategy
team2.add("Defenseur", StrategyDefenseur())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
