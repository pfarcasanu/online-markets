import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations_with_replacement
from ftpl import FTPL_Player
from ew import EW_Player

class Bidder:
  def __init__(self, value):
    self.value = value
  
  def bid(self, price):
    if price < self.value:
      return price
    return 0

class SellingIntroductions:
  def __init__(self, n_rounds, n_actions, alg):
    self.n = n_rounds
    self.k = n_actions
    self.alg = alg
  
  def calc_revenue(self, bids, prices):
    revenue = 0
    for bid, price in zip(bids, prices):
      if price > bid: return 0
      revenue += price
    return revenue

  def play(self, bidders):
    ## Generate Once
    prices = np.linspace(0, 1, self.k)
    actions = list(combinations_with_replacement(prices, len(bidders)))
    alg = self.alg(self.n, len(actions))
    payoffs = np.empty((self.n, len(actions)))
    revenues = np.empty((self.n, 1))
    prices = [None] * self.n

    for i in range(self.n):
      action_ind = alg.get_action(payoffs[0:i, :])
      action = actions[action_ind]
      bids = [bidder.bid(price) for bidder, price in zip(bidders, action)]

      ## Update Revenue
      revenues[i] = self.calc_revenue(bids, action)
      prices[i] = action

      ## Update Payoffs
      payoffs[i] = 0
      payoffs[i, action_ind] = revenues[i]
    
    return revenues, prices

if __name__ == "__main__":
  ## 0.9, 0.6
  n, k = 500, 5
  introductions = SellingIntroductions(n, k, FTPL_Player)
  rev, price = introductions.play([Bidder(0.9), Bidder(0.3)])

  plt.clf()
  plt.plot(range(n), list(map(lambda x: x[0], price)), label="bidder=0.6")
  plt.plot(range(n), list(map(lambda x: x[1], price)), label="bidder=0.6")
  plt.show()