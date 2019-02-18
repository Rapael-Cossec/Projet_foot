#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:13:38 2019

@author: 3700049
"""

class GoalSearch(Strategy):
    def __init__(self, strategy, params, intervalle):
        Strategy.__init__(self, "Go-test")
        self.strategy = strategy
        self.params = params
        self.intervalle = intervalle
    
    def start():
        