#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:39:27 2019

@author: 3700049
"""

GAME_WIDTH = 150
GAME_HEIGHT = 90

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math

class StrategyFonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")

    def compute_strategy(self, state, id_team, id_player):
        dir_balle = state.ball.position - state.player_state(id_team, id_player).position
        # id_team is 1 or 2
        # id_player starts at 0
        if(dir_balle.norm < 1.75):
            if(id_team == 1):
                return SoccerAction(dir_balle, Vector2D(GAME_WIDTH, GAME_HEIGHT/2)-state.player_state(id_team, id_player).position)
            return SoccerAction(dir_balle, Vector2D(0, GAME_HEIGHT/2)-state.player_state(id_team, id_player).position)
        return SoccerAction(dir_balle, Vector2D(0,0))

    
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Fonceur", StrategyFonceur())  # Random strategy
team2.add("Static", StrategyFonceur())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
