import numpy as np
from ew import EW_Player

class SecondPriceAuction:
  def __init__(self, n_rounds, k_actions, alg):
    self.alg = alg
    self.n = n_rounds
    self.k = k_actions
    self.actions = np.linspace(0, 1, k_actions)
    print(list(self.actions))

  def play(self, bidders):
    payoffs = np.empty((n_rounds, k_actions))
    for i in range(self.n):
      data = payoffs[0:i, :]
      action = alg.get_action(data)
      reserve_price = self.actions[action]


if __name__ == "__main__":
  auction = SecondPriceAuction(100, 4, EW_Player)
