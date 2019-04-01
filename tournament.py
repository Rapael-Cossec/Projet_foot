#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:51:52 2019

@author: 3700049
"""

#from Strategy_f import SuperState, StrategySolo, StrategyAttaquant, StrategyDefenseur, StrategyDefenseur_duo, RandomStrategy
#from soccersimulator import SoccerTeam
#
#def get_team(nb_players):  +++++
#    team = SoccerTeam(name="Unknown")
#    if nb_players == 1:
#        team.add("StrikeBack",StrategySolo())
#    if nb_players == 2:
#        team.add("Footix", RandomStr++ategy())
#        team.add("Billy", StrategyDefenseur_duo())
#    if nb_players == 3:
#        team.add("Footix", StrategyAttaquant())----
#        team.add( a"Footix", StrategyAttaquant())
#        team.add("Billy", StrategyDefenseur_duo())
#    return team

#if __name__ =='__main__':
from soccersimulator import Simulation, show_simu
from Strategy_f import get_team

team1 = get_team(5)
team2 = get_team(2)
simu = Simulation (team1,team2) 
show_simu(simu)
