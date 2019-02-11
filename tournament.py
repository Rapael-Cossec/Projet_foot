#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:51:52 2019

@author: 3700049
"""

from Strategy_f import SuperState, StrategySolo, StrategyAttaquant, StrategyDefenseur
from soccersimulator import SoccerTeam

def get_team(nb_players):  
    team = SoccerTeam(name="Unknown")
    if nb_players == 1:
        team.add("Billy",StrategySolo())
    if nb_players == 2:
        team.add("Billy", StrategyAttaquant())
        team.add("Footix", StrategyAttaquant())
    return team

if __name__ =='__main__':
    from soccersimulator import Simulation, show_simu
    team1 = get_team(1)
    team2 = get_team(2)
    simu = Simulation (team1,team2)
    show_simu(simu)
