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
from Strategy_f.tools import SuperState
from soccersimulator import settings
import math

class StrategyDefenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        dir_balle = s.ball - s.player
#        Distance_Shoot = (s.ball - s.player).norm 
        pos_cible = ((s.ball - s.goal_a)/2 + (s.goal_a - s.player)).scale(5)
        if(s.distance_balle(s.player, CAN_SHOOT)):
            if(s.state.nb_players(id_team) > 1):
                return SoccerAction(s.dir_ball, (s.joueur_proche_a(id_team, id_player) - s.player).normalize().scale(3))
            return SoccerAction(dir_balle, (s.goal_e - s.player).normalize().scale(3.8))
        # id_team is 1 or 2
        # id_player starts at 0
        
        if(s.distance_balle(s.player, 10)):
            return SoccerAction(dir_balle, Vector2D(0., 0.))
        return SoccerAction(pos_cible, Vector2D(0,0))
"""

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Random")

    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        return SoccerAction(Vector2D.create_random(-1, 1),
                            Vector2D.create_random(-1, 1))
        
        
        
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
            return SoccerAction(dir_balle, (s.goal_e - s.player).normalize().scale(3.8))
        return SoccerAction(dir_balle, Vector2D(0,0))


        
# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team2.add("Fonceur", StrategyFonceur())  # Random strategy
team1.add("Defenseur", Strategy())   # Static strategy
team1.add("Fonceur", StrategyFonceur())  # Random strategy
team2.add("Defenseur", StrategyDefenseur())   # Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)
"""