#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:39:27 2019

@author: 3700049
"""




from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
from .tools import SuperState
import math

GAME_WIDTH = 150
GAME_HEIGHT = 90
PLAYER_RADIUS = 1.
BALL_RADIUS = 0.65
CAN_SHOOT = PLAYER_RADIUS + BALL_RADIUS

"""joueur qui vise ce que vise la balle"""

class StrategyFonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")

    def compute_strategy(self, state, id_team, id_player):
        #dir_balle = state.ball.position - state.player_state(id_team, id_player).position
        s = SuperState(state, id_team, id_player)
        dir_balle = s.ball - s.player
        # id_team is 1 or 2
        # id_player starts at 0
        if(dir_balle.norm < CAN_SHOOT):
            return SoccerAction(s.dir_ball, (s.goal_e - s.player).normalize().scale(3.8))
        return SoccerAction(dir_balle, Vector2D(0,0))



"""
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(-1, 1),
                            Vector2D.create_random(-1, 1))
    
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team2.add("Fonceur", StrategyFonceur())  # Random strategy
team1.add("Static", RandomStrategy())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
"""