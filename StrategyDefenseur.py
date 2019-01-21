#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:59:16 2019

@author: 3700049
"""

GAME_WIDTH = 150
GAME_HEIGHT = 90

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math

class StrategyDefenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")

    def compute_strategy(self, state, id_team, id_player):
        centre_panier = Vector2D((id_team - 1) * GAME_WIDTH, GAME_HEIGHT/2)
        pos_cible_y = GAME_HEIGHT/2+((GAME_HEIGHT/2-state.ball.position.y)/2)
        pos_cible = Vector2D((centre_panier.x + state.ball.position.x) / 2, pos_cible_y)
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(pos_cible, Vector2D(0,0))

    
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Defenseur", StrategyDefenseur())  # Random strategy
team2.add("Defenseur", StrategyDefenseur())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
