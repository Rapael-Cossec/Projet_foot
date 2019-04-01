#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:06:02 2019

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
from Strategy_f.tools import SuperState
from soccersimulator import settings
import math

class StrategyAttaquant_trio_2(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant Central")
        self.counter_engage = 0
        self.counterstep = 0
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        dir_balle = s.ball - s.player
#        pos_cible = ((s.ball - s.goal_a)*0.6 + (s.goal_a - s.player)).scale(5)
#        mid_goal_e = ((s.ball - s.goal_e)*0.7 + (s.goal_e - s.player)).scale(5)

        if(s.dir_ball.norm < CAN_SHOOT):
            if(id_team == 1):
                if((s.goal_e - s.player).norm < 40):
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), s.shoot((s.goal_e - s.player)).normalize().scale(3.8))
                if(s.ball.y < (GAME_HEIGHT/2 + 30)):
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), (Vector2D(state.player_state(id_team, 0).position.x + 20,  state.player_state(id_team, 0).position.x) - s.player).normalize().scale(3.2)) #a tester
                if((s.joueur_proche(id_team, id_player).position - s.player).norm < 10):
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), (state.player_state(id_team, 3).position - s.player).normalize().scale(3.8))
                return SoccerAction(s.dir_ball.normalize().scale(5.0), (Vector2D(state.player_state(id_team, 3).position.x + 20,  state.player_state(id_team, 3).position.x) - s.player).normalize().scale(3.2)) #a tester
                return SoccerAction(s.dir_ball.normalize().scale(5.0), Vector2D(0,0)) #petite passe 
            elif(id_team == 2):
                if((s.goal_e - s.player).norm < 40):
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), s.shoot((s.goal_e - s.player)).normalize().scale(3.8))
                if(s.ball.y < (GAME_HEIGHT/2 + 30)):
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), (Vector2D(state.player_state(id_team, 2).position.x - 20,  state.player_state(id_team, 2).position.x) - s.player).normalize().scale(3.2)) #a tester
                if((s.joueur_proche(id_team, id_player).position - s.player).norm < 10):
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), (state.player_state(id_team, 3).position - s.player).normalize().scale(3.8))
                return SoccerAction(s.dir_ball.normalize().scale(5.0), (Vector2D(state.player_state(id_team, 3).position.x - 20,  state.player_state(id_team, 3).position.x) - s.player).normalize().scale(3.2)) #a tester
        
        if(s.ball.y < (GAME_HEIGHT/2 + 10)):
            if((s.goal_e - s.player).norm < 20):
                return SoccerAction(Vector2D(130, GAME_HEIGHT *3/4)-s.player, Vector2D(0, 0))
            return SoccerAction(Vector2D(s.ball.x, GAME_HEIGHT * 3 / 4)-s.player, Vector2D(0, 0))
        return SoccerAction(dir_balle, Vector2D(0, 0))