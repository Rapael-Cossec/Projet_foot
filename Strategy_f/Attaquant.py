#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:20:32 2019

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

class StrategyAttaquant(Strategy):
    def __init__(self): 
        Strategy.__init__(self, "Attaquant")
#        self.strength = strength
#        self.vitesse = vitesse
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        # id_team is 1 or 2
        # id_player starts at 0
        if(s.dir_ball.norm < CAN_SHOOT):
            return SoccerAction(s.dir_ball_acc.normalize().scale(5.0), s.shoot((s.goal_e - s.player)).normalize().scale(3.8))
        
        return SoccerAction(s.dir_ball_acc.normalize().scale(5.0), Vector2D(0,0))
"""  
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team2.add("A", StrategyAttaquant())  # Random strategy
team1.add("B", Strategy())   # Static strategy
team1.add("C", StrategyFonceur())  # Random strategy
team2.add("Dr", StrategyDefenseur())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)"""

''', strength=None, vitesse=None'''
