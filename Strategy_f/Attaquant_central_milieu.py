#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:42:31 2019

@author: cossec
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

class StrategyAttaquant_trio_3(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant Central")
        self.counter_engage = 0
        self.counterstep = 0
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        dir_balle = s.ball - s.player
#        pos_cible = ((s.ball - s.goal_a)*0.6 + (s.goal_a - s.player)).scale(5)
#        mid_goal_e = ((s.ball - s.goal_e)*0.7 + (s.goal_e - s.player)).scale(5)
        if(s.ball.x == GAME_WIDTH/2 and s.ball.y == GAME_HEIGHT/2):
            self.counter_engage = 0
            self.counterstep += 1
            
        if(self.counter_engage == 0):
            if(s.dir_ball.norm < CAN_SHOOT):
                self.counter_engage = 1
                return SoccerAction(dir_balle, (Vector2D(GAME_WIDTH/2, GAME_HEIGHT/2) - s.player).normalize().scale(3.8))
            return SoccerAction(dir_balle, Vector2D(0,0))


        if(s.dir_ball.norm < CAN_SHOOT):
            if(id_team == 1):
                if((s.goal_e - s.player).norm < 50):#a tester
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), s.shoot((s.goal_e - s.player)).normalize().scale(3.8))
                if(s.ball.y >= (GAME_HEIGHT/2)):
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), (Vector2D(state.player_state(id_team, 3).position.x + 20,  state.player_state(id_team, 3).position.x) - s.player).normalize().scale(3.8)) #a tester
#                    return SoccerAction(dir_balle, (state.player_state(id_team, 2).position - s.player).normalize().scale(3.2))
                if(s.ball.y <= (GAME_HEIGHT/2)):
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), (Vector2D(state.player_state(id_team, 3).position.x + 20,  state.player_state(id_team, 3).position.x) - s.player).normalize().scale(3.2)) #a tester
#                    return SoccerAction(dir_balle, (state.player_state(id_team, 1).position - s.player).normalize().scale(3.2))
                return SoccerAction(s.dir_ball.normalize().scale(5.0), s.shoot((s.goal_e - s.player)).normalize().scale(3.8))
            else:
                if((s.goal_e - s.player).norm < 50):#a tester
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), s.shoot((s.goal_e - s.player)).normalize().scale(3.8))
                if(s.ball.y >= (GAME_HEIGHT/2)):
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), (Vector2D(state.player_state(id_team, 3).position.x - 20,  state.player_state(id_team, 3).position.x) - s.player).normalize().scale(3.8)) #a tester
#                    return SoccerAction(dir_balle, (state.player_state(id_team, 2).position - s.player).normalize().scale(3.2))
                if(s.ball.y <= (GAME_HEIGHT/2)):
                    return SoccerAction(s.dir_ball.normalize().scale(5.0), (Vector2D(state.player_state(id_team, 3).position.x - 20,  state.player_state(id_team, 3).position.x) - s.player).normalize().scale(3.2)) #a tester
#                    return SoccerAction(dir_balle, (state.player_state(id_team, 1).position - s.player).normalize().scale(3.2))
                return SoccerAction(s.dir_ball.normalize().scale(5.0), s.shoot((s.goal_e - s.player)).normalize().scale(3.8))

        if(s.ball.y > (GAME_HEIGHT/2 + 10) or s.ball.y < (GAME_HEIGHT/2 - 10)):
            return SoccerAction(Vector2D(s.ball.x, GAME_HEIGHT / 2)-s.player, Vector2D(0, 0))
        return SoccerAction(s.dir_ball.normalize().scale(5.0), Vector2D(0, 0))