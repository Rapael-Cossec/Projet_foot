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
        Distance_Shoot = (s.ball - s.player).norm 
        pos_cible = ((s.ball - s.goal_a)/2 + (s.goal_a - s.player)).scale(1/2)
        if(Distance_Shoot < CAN_SHOOT):
            return SoccerAction(pos_cible, s.goal_e - s.player)
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(pos_cible, Vector2D(0,0))

    
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team2.add("Defenseur", StrategyFonceur())  # Random strategy
team1.add("Defenseur", StrategyDefenseur())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
