#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 17:34:23 2019

@author: 3700049
"""

from .Random import RandomStrategy
from .Defenseur import StrategyDefenseur
from .Attaquant import StrategyAttaquant
from .Fonceur import StrategyFonceur
from .Solo import StrategySolo
from .tools import SuperState
from .Defenseur_centrale import StrategyDefenseur_duo

#from Strategy_f import SuperState, StrategySolo, StrategyAttaquant, StrategyDefenseur, StrategyDefenseur_duo, RandomStrategy
from soccersimulator import SoccerTeam

def get_team(nb_players):  
    team = SoccerTeam(name="Unknown")
    if nb_players == 1:
        team.add("StrikeBack",StrategySolo())
    if nb_players == 2:
        team.add("Footix", RandomStrategy())
        team.add("Billy", StrategyDefenseur_duo())
    if nb_players == 3:
        team.add("Footix", StrategyAttaquant())
        team.add("Footix", StrategyAttaquant())
#        team.add("Billy", StrategyDefenseur_duo())
    return team