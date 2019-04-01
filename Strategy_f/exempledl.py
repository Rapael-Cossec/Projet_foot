#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:23:22 2019

@author: 3700049
"""
GAME_WIDTH = 150
GAME_HEIGHT = 90
PLAYER_RADIUS = 1.
BALL_RADIUS = 0.65
CAN_SHOOT = PLAYER_RADIUS + BALL_RADIUS
import pickle
from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from Defenseur import StrategyDefenseur
from Attaquant import StrategyAttaquant
from Fonceur import StrategyFonceur
from Solo import StrategySolo
from tools import SuperState, GoTestStrategy
from Defenseur_centrale import StrategyDefenseur_duo
from Attaquant_centrale import StrategyAttaquant_duo
from QLearn import QLearning

# Strategy
QTestStrategy = QStrategy ()
QTestStrategy.add('Attaquant', StrategyAttaquant())
QTestStrategy.add('Defenseur', StrategyDefenseur())
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

def  begin_match(self , team1 , team2 , state):
    self.last_step = 0
    # Step of the  last  round
    self.qtable = dict()
    # Q table
def  begin_round(self , team1 , team2 , state):
    ball = Vector2D.create_random(low=0, high =1)
    ball.x *=  GAME_WIDTH
    ball.y *=  GAME_HEIGHT
    # Player  and  ball  postion (random)
    self.simu.state.states [(1, 0)]. position = ball.copy()
    # Player  position
    self.simu.state.states [(1, 0)]. vitesse = Vector2D ()
    # Player  acceleration
    self.simu.state.ball.position = ball.copy()
    # Ball  position
    # Last  step of the  game
    self.last_step = self.simu.step
    self.last_state = None
    self.last_score = self.simu.score [1]
    # Score  of Team 1
    self.cur_state = self.strategy.get_state(state , id_team=1,  id_player =0)
    self.rewards = []

def  update_round(self , team1 , team2 , state):
    # Q-learning  update
    self.qupdate(state)
    if  state.step > self.last_step + self.max_round_step:
        # Change  action  when  state  doesn't change
        if self.cur_state  == self.last_state:
            self.strategy.strategy = self.next_action(self.cur_state)
            self.last_state = self.cur_state
    
    def  qupdate(self , state):
        qstate_next = self.strategy.get_state(state , id_team=1,  id_player =0)
    if self.cur_state  !=  qstate_next:
        qaction = self.strategy.strategy
        # Strategy  name
    key = (self.cur_state , qaction)
    # Future Q-value
    qvalues_next = [q for k, q in self.qtable.items() \
    if k[0] ==  qstate_next]
    qnext = max(qvalues_next , default =0)
    # Reinforcement
    score = state.score [1]
    if  score  > self.last_score:
        self.last_score = score
        r = 0
    else:
        r = -1 if state.goal == 0 else  -10
        qvalue = r + 0.9 * qnext
        # Update Q-table
    self.rewards.append ((key , r))
    if not  self.monte_carlo:
        if key in self.qtable:
            self.qtable[key] = 0.5 * self.qtable[key] + 0.5 * qvalue
        else:
            self.qtable[key] = qvalue
        # Change  action
    self.strategy.strategy = self.next_action(qstate_next)
    # Update  current  state
    self.cur_state = qstate_next

def  next_action(self , qstate_next ):
    minq = min([q for key , q in self.qtable.items() \
                if key[0] ==  qstate_next], default =0)
    minq = min(minq , 0)
    
    prob = [0.1 if (qstate_next , name) not in self.qtable \
    else  self.qtable [( qstate_next , name)] - minq + 0.1 \
            for  name in self.strategy.strategy_names]
    prob = np.asarray(prob)
    if prob.sum() < 1e-15:
        prob = None
    else:
        prob /= prob.sum()
    return  choice(list(self.strategy.strategy_names), p=prob)

class  QStrategy(Strategy):
    def  __init__(self):
        Strategy.__init__(self , "Q-learning")
        self.strategies = dict()
        self.current_strategy = None
        self.qtable = None
        
    def  add(self , name , strategy ):
        self.strategies[name] = strategy
        if not  self.current_strategy:
            self.current_strategy = name
    
    def  get_state(self , state , id_team , id_player ):
        s = SuperState(state , id_team , id_player)
        x = int(s.player.x / GAME_WIDTH * 3)
        y = int(s.player.y / GAME_HEIGHT * 5)
        return x, y, state.goal > 0

    def  compute_strategy(self , state , id_team , id_player ):
        if self.qtable  is None:
            strat = self.strategies[self.current_strategy]
            return  strat.compute_strategy(state , id_team , id_player)
        else:
            qstate = self.get_state(state , id_team , id_player)
            strategy = max([(q, key [1])  for key , q in self.qtable.items() \
            if key [0]== qstate], default =(None , None ))[1]
            if  strategy  is not  None:
                strat = self.strategies[strategy]
                return  strat.compute_strategy(state , id_team , id_player)
            else:
                return  SoccerAction ()

@property
def  strategy_names(self):
    return  self.strategies.keys()

@property
def  strategy(self):
    return  self.current_strategy

@strategy.setter
def  strategy(self , name):
    self.current_strategy = name
