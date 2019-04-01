#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:05:09 2019

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



class StrategySoloGen(Strategy):
    
    def __init__(self, a_T=None, a_F=None, b_T=None, b_F=None, c_T=None, c_F=None, d_T=None, d_F=None, e_T=None, e_F=None, f_T=None, f_F=None, g_T=None, g_F=None, h_T=None, h_F=None, i_T=None, i_F=None, j_T=None, j_F=None, k_T=None, k_F=None, l_T=None, l_F=None, m_T=None, m_F=None, n_T=None, n_F=None, o_T=None, o_F=None, a_V=None, a_U=None, b_V=None, b_U=None, c_V=None, c_U=None, d_V=None, d_U=None, e_V=None, e_U=None, f_V=None, f_U=None, g_V=None, g_U=None, h_V=None, h_U=None, i_V=None, i_U=None, j_V=None, j_U=None, k_V=None, k_U=None, l_V=None, l_U=None, m_V=None, m_U=None, n_V=None, n_U=None, o_V=None, o_U=None):
        Strategy.__init__(self, "Genetique")
        self.a_T=a_T
        self.a_F=a_F
        self.b_T=b_T 
        self.b_F=b_F
        self.c_T=c_T 
        self.c_F=c_F
        self.d_T=d_T 
        self.d_F=d_F
        self.e_T=e_T 
        self.e_F=e_F
        self.f_T=f_T 
        self.f_F=f_F
        self.g_T=g_T 
        self.g_F=g_F
        self.h_T=h_T 
        self.h_F=h_F
        self.i_T=i_T  
        self.i_F=i_F
        self.j_T=j_T 
        self.j_F=j_F
        self.k_T=k_T 
        self.k_F=k_F
        self.l_T=l_T 
        self.l_F=l_F
        self.m_T=m_T 
        self.m_F=m_F
        self.n_T=n_T 
        self.n_F=n_F
        self.o_T=o_T 
        self.o_F=o_F
        
        self.a_V=a_V
        self.a_U=a_U
        self.b_V=b_V 
        self.b_U=b_U
        self.c_V=c_V 
        self.c_U=c_U
        self.d_V=d_V 
        self.d_U=d_U
        self.e_V=e_V 
        self.e_U=e_U
        self.f_V=f_V 
        self.f_F=f_U
        self.g_V=g_V 
        self.g_U=g_U
        self.h_V=h_V 
        self.h_U=h_U
        self.i_V=i_V  
        self.i_U=i_U
        self.j_V=j_V 
        self.j_U=j_U
        self.k_V=k_V 
        self.k_U=k_U
        self.l_V=l_V 
        self.l_U=l_U
        self.m_V=m_V 
        self.m_U=m_U
        self.n_V=n_V 
        self.n_U=n_U
        self.o_V=o_V 
        self.o_U=o_U

        self.score1=0
        self.score2=0
    def choix_mouv(self,argument,state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        dir_balle = s.ball - s.player
        pos_cible = ((s.ball - s.goal_a)*0.6 + (s.goal_a - s.player)).scale(5) 
        switcher = {
            0: SoccerAction(Vector2D(0,0),Vector2D(0,0)),
            1: SoccerAction(dir_balle, Vector2D(0, 0)),
            2: SoccerAction(dir_balle, (s.goal_e - s.player).normalize().scale(3.8)),
            3: SoccerAction(pos_cible, Vector2D(0,0))
        }
        return switcher.get(argument, "nothing")

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        dir_balle = s.ball - s.player
        pos_cible = ((s.ball - s.goal_a)*0.6 + (s.goal_a - s.player)).scale(5)       
        joueur_proche = s.joueur_proche_ball_all(id_team, id_player)
        if(s.ball.x == GAME_WIDTH/2 and s.ball.y == GAME_HEIGHT/2):
            self.score1=s.state.score_team1
            self.score2=s.state.score_team2
        if(joueur_proche==s.joueur_proche_ball_all):
            if(s.bloc1):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.a_T, state, id_team, id_player)
                return self.choix_mouv(self.a_F, state, id_team, id_player)
            if(s.bloc2):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.b_T, state, id_team, id_player)
                return self.choix_mouv(self.b_F, state, id_team, id_player)
            if(s.bloc3):
                if(dir_balle.norm < CAN_SHOOT):                
                    return self.choix_mouv(self.c_T, state, id_team, id_player)
                return self.choix_mouv(self.c_F, state, id_team, id_player)
            if(s.bloc4):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.d_T, state, id_team, id_player)
                return self.choix_mouv(self.d_F, state, id_team, id_player)
            if(s.bloc5):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.e_T, state, id_team, id_player)
                return self.choix_mouv(self.e_F, state, id_team, id_player)
            if(s.bloc6):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.f_T, state, id_team, id_player)
                return self.choix_mouv(self.f_F, state, id_team, id_player)
            if(s.bloc7):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.g_T, state, id_team, id_player)
                return self.choix_mouv(self.g_F, state, id_team, id_player)
            if(s.bloc8):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.h_T, state, id_team, id_player)
                return self.choix_mouv(self.h_F, state, id_team, id_player)
            if(s.bloc9):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.i_T, state, id_team, id_player)
                return self.choix_mouv(self.i_F, state, id_team, id_player)
            if(s.bloc10):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.j_T, state, id_team, id_player)
                return self.choix_mouv(self.j_F, state, id_team, id_player)
            if(s.bloc11):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.k_T, state, id_team, id_player)
                return self.choix_mouv(self.k_F, state, id_team, id_player)
            if(s.bloc12):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.l_T, state, id_team, id_player)
                return self.choix_mouv(self.l_F, state, id_team, id_player)
            if(s.bloc13):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.m_T, state, id_team, id_player)
                return self.choix_mouv(self.m_F, state, id_team, id_player)
            if(s.bloc14):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.n_T, state, id_team, id_player)
                return self.choix_mouv(self.n_F, state, id_team, id_player)
            if(s.bloc15):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.o_T, state, id_team, id_player)
                return self.choix_mouv(self.o_F, state, id_team, id_player)              
        else:
            if(s.bloc1):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.a_V, state, id_team, id_player)
                return self.choix_mouv(self.a_U, state, id_team, id_player)
            if(s.bloc2):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.b_V, state, id_team, id_player)
                return self.choix_mouv(self.b_U, state, id_team, id_player)
            if(s.bloc3):
                if(dir_balle.norm < CAN_SHOOT):                
                    return self.choix_mouv(self.c_V, state, id_team, id_player)
                return self.choix_mouv(self.c_U, state, id_team, id_player)
            if(s.bloc4):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.d_V, state, id_team, id_player)
                return self.choix_mouv(self.d_U, state, id_team, id_player)
            if(s.bloc5):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.e_V, state, id_team, id_player)
                return self.choix_mouv(self.e_U, state, id_team, id_player)
            if(s.bloc6):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.f_V, state, id_team, id_player)
                return self.choix_mouv(self.f_U, state, id_team, id_player)
            if(s.bloc7):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.g_V, state, id_team, id_player)
                return self.choix_mouv(self.g_U, state, id_team, id_player)
            if(s.bloc8):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.h_V, state, id_team, id_player)
                return self.choix_mouv(self.h_U, state, id_team, id_player)
            if(s.bloc9):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.i_V, state,  id_team, id_player)
                return self.choix_mouv(self.i_U,  state, id_team, id_player)
            if(s.bloc10):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.j_V, state, id_team, id_player)
                return self.choix_mouv(self.j_U)
            if(s.bloc11):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.k_V, state, id_team, id_player)
                return self.choix_mouv(self.k_U, state, id_team, id_player)
            if(s.bloc12):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.l_V, state, id_team, id_player)
                return self.choix_mouv(self.l_U, state, id_team, id_player)
            if(s.bloc13):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.m_V, state, id_team, id_player)
                return self.choix_mouv(self.m_U, state, id_team, id_player)
            if(s.bloc14):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.n_V, state, id_team, id_player)
                return self.choix_mouv(self.n_U, state, id_team, id_player)
            if(s.bloc15):
                if(dir_balle.norm < CAN_SHOOT):
                    return self.choix_mouv(self.o_V, state, id_team, id_player)
                return self.choix_mouv(self.o_U, state, id_team, id_player) 