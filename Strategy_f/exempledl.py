#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:23:22 2019

@author: 3700049
"""
import pickle
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from QLearn import QLearning
from QStrat import QStrategy
from Defenseur import StrategyDefenseur
from Attaquant import StrategyAttaquant
from Fonceur import StrategyFonceur
from Solo import StrategySolo
from tools import SuperState, GoTestStrategy
from Defenseur_centrale import StrategyDefenseur_duo
from Attaquant_centrale import StrategyAttaquant_duo

# Strategy
QTestStrategy =  QStrategy()
QTestStrategy.add('Attaque', StrategyAttaquant())
QTestStrategy.add('Defense', StrategyDefenseur())
QTestStrategy.add('Solo', StrategySolo())



# Learning
expe = QLearning(strategy=QTestStrategy , monte_carlo=False)
expe.start(fps =1500)
with  open('qstrategy.pkl', 'wb') as fo:
    QTestStrategy.qtable = expe.qtable
    pickle.dump(QTestStrategy , fo)
# Test
with  open('qstrategy.pkl .351', 'rb') as fi:
    QStrategy = pickle.load(fi)
    # Simulate  and  display  the  match
    simu = RandomPos(QStrategy)
    simu.start()
