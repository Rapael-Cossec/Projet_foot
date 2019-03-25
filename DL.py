from Strategy_f import StrategyAttaquant, StrategySolo, StrategyDefenseur
from Strategy_f.QLearn import QLearning
from Strategy_f.QStrat import QStrategy
import pickle as pkl
# Strategy

QTestStrategy = QStrategy()
QTestStrategy.add('Solo', StrategySolo())
QTestStrategy.add('Attaquant', StrategyAttaquant())
QTestStrategy.add('Defenseur', StrategyDefenseur())


# Learning
expe = QLearning(strategy=QTestStrategy , monte_carlo=False)
expe.start(fps=10000)
with  open('qstrategy.pkl', 'wb') as fo:
    QTestStrategy.qtable = expe.qtable
    pkl.dump(QTestStrategy , fo)
    # Test
with  open('qstrategy.pkl', 'rb') as fi:
    QStrategy = pkl.load(fi)
    # Simulate  and  display  the  match

 