#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 19:16:46 2019

@author: 3700049
"""
from copy import copy
from soccersimulator import Simulation, show_simu
from Strategy_f.tools import GoTestStrategy
from Strategy_f.GoalSearch import GoalSearch
from Strategy_f.SoloSearch import SoloSearch
from Strategy_f import SuperState, StrategySolo, StrategyAttaquant, StrategyDefenseur, StrategyDefenseur_duo, RandomStrategy
from random import *



def frange(start, stop, step):
     i = start
     while i < stop:
         yield i
         i += step
         
def SelectionNaturelle(expe):
    expe.start()
    print(expe.get_best())
    res = copy(expe.get_res())
    res2 = copy(expe.get_res())
    print("Res initial")
    print(res)
    best = res.get(expe.get_best())
    for i in res2:
       if(random()>res2.get(i)/best):
           del res[i]
           
    print("Res final")
    print(res)     
    return res

def Reproduction(dico):
    listevit=[]
    listestr=[]   
    listevit2=[]
    listestr2=[]
    for i in dico:
        listevit.append(i[0][1])
        listestr.append(i[1][1])
    print(listevit)
    print(listestr)
    for i in dico:
        if(random()<0.01):
            listevit2.append(i[0][1]*0.9+(random()*0.2))
        else: 
            listevit2.append(i[0][1])
        if(random()<0.01):
            listevit2.append(i[0][1] * 0.9+(random()*0.2))
        else:
            listestr2.append(i[1][1])
    shuffle(listevit2)
    shuffle(listestr2)
    print(listevit2)
    print(listestr2)
    listevit = listevit + listevit2
    listestr = listestr + listestr2
    return [listevit, listestr]

print(0.9+(random()*0.2))
expe = GoalSearch(strategy= StrategyAttaquant(),params={'strength':frange(3, 4, 0.1), 'vitesse':frange(3,4,1)})
test = SelectionNaturelle(expe)
listerep = Reproduction(test)