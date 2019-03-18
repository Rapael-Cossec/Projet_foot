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
from .tools import SuperState, GoTestStrategy
from .Defenseur_centrale import StrategyDefenseur_duo
from .Attaquant_centrale import StrategyAttaquant_duo
from .Attaquant_central_bas import StrategyAttaquant_trio_2
from .Attaquant_central_haut import StrategyAttaquant_trio_1
from .Attaquant_central_milieu import StrategyAttaquant_trio_3


#from Strategy_f import SuperState, StrategySolo, StrategyAttaquant, StrategyDefenseur, StrategyDefenseur_duo, RandomStrategy
from soccersimulator import SoccerTeam

def get_team(nb_players):  
    team = SoccerTeam(name="Unknown")
    if nb_players == 1:
        team.add("StrikeBack",StrategySolo())
    if nb_players == 2:
        team.add("J'attaque", StrategyAttaquant_duo())
        team.add("Je defend", StrategyDefenseur_duo())
    if nb_players == 3:
        team.add("Footix", StrategyAttaquant())
#        team.add("Footix", RandomStrategy())
#        team.add("Billy", StrategyAttaquant_duo())
    if nb_players == 5:
        team.add("Je defend", StrategyDefenseur_duo())
        team.add("DEFENDRE", StrategyAttaquant_trio_1())       
        team.add("DEFENDRE", StrategyAttaquant_trio_2())       
        team.add("je suis ici", StrategyAttaquant_trio_3())
    return team
