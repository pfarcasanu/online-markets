import numpy as np
import matplotlib.pyplot as plt
from random import random, randint
from itertools import permutations
from ew import EW_Player

class Bidder:
  def __init__(self, value):
    self.value = value
  
  def bid(self, price):
    if price < self.value:
      return price
    return 0

class SellingIntroductions:
  def __init__(self, n_rounds, n_actions, alg, eps=0.02):
    self.n = n_rounds
    self.k = n_actions
    self.alg = alg
    self.eps = eps
  
  def calc_revenue(self, bids, prices):
    revenue = 0
    for bid, price in zip(bids, prices):
      if price > bid: return 0
      revenue += price
    return revenue

  def play(self, bidders):
    ## Generate Once
    prices = list(np.linspace(0, 1, self.k))
    actions = list(set(permutations(prices + prices, len(bidders))))
    alg = self.alg(self.n, len(actions), e=0.3)
    payoffs = np.empty((self.n, len(actions)))
    revenues = np.empty((self.n, 1))
    prices = [None] * self.n

    for i in range(self.n):
      ## Pick an action
      action_ind = randint(0, len(actions) - 1) if random() < self.eps else alg.get_action(payoffs[0:i, :])
      action = actions[action_ind]

      bids = [bidder.bid(price) for bidder, price in zip(bidders, action)]

      ## Update Revenue
      revenues[i] = self.calc_revenue(bids, action)
      prices[i] = action

      ## Update Payoffs
      payoffs[i] = 0
      payoffs[i, action_ind] = revenues[i, 0]

    return revenues, prices

def avg(lst):
  n = len(lst)
  factor = 100
  return [sum(lst[max(0, n-factor):n + 1]) / len(lst[max(0, n-factor):n + 1]) for n in range(n)]

if __name__ == "__main__":
  n, k = 1500, 9

  # 0.9, 0.3
  introductions = SellingIntroductions(n, k, EW_Player)
  rev, price = introductions.play([Bidder(0.9), Bidder(0.3)])

  plt.clf()
  plt.plot(range(n), avg(list(map(lambda x: x[0], price))))
  plt.plot(range(n), avg(list(map(lambda x: x[1], price))))
  plt.legend(["val=0.9", "val=0.3"])
  plt.ylabel("Price Charged")
  plt.savefig("./figures/part2_high_low.png")

  ## 0.4, 0.8
  introductions = SellingIntroductions(n, k, EW_Player)
  rev, price = introductions.play([Bidder(0.4), Bidder(0.8)])

  plt.clf()
  plt.plot(range(n), avg(list(map(lambda x: x[0], price))))
  plt.plot(range(n), avg(list(map(lambda x: x[1], price))))
  plt.legend(["val=0.4", "val=0.8"])
  plt.ylabel("Price Charged")
  plt.savefig("./figures/part2_low_high.png")

  ## 0.6, 0.6
  introductions = SellingIntroductions(n, k, EW_Player)
  rev, price = introductions.play([Bidder(0.6), Bidder(0.6)])

  plt.clf()
  plt.plot(range(n), avg(list(map(lambda x: x[0], price))))
  plt.plot(range(n), avg(list(map(lambda x: x[1], price))))
  plt.legend(["val=0.6", "val=0.6"])
  plt.ylabel("Price Charged")
  plt.savefig("./figures/part2_med_med.png")

  ## 0.9, 0.9
  introductions = SellingIntroductions(n, k, EW_Player)
  rev, price = introductions.play([Bidder(0.9), Bidder(0.9)])

  plt.clf()
  plt.plot(range(n), avg(list(map(lambda x: x[0], price))))
  plt.plot(range(n), avg(list(map(lambda x: x[1], price))))
  plt.legend(["val=0.9", "val=0.9"])
  plt.ylabel("Price Charged")
  plt.savefig("./figures/part2_high_high.png")

  ## 0.9, 0.9
  introductions = SellingIntroductions(n, k, EW_Player)
  rev, price = introductions.play([Bidder(0.3), Bidder(0.3)])

  plt.clf()
  plt.plot(range(n), avg(list(map(lambda x: x[0], price))))
  plt.plot(range(n), avg(list(map(lambda x: x[1], price))))
  plt.legend(["val=0.2", "val=0.2"])
  plt.ylabel("Price Charged")
  plt.savefig("./figures/part2_low_low.png")

  ## Multiple
  introductions = SellingIntroductions(n, k, EW_Player)
  rev, price = introductions.play([Bidder(0.9), Bidder(0.3), Bidder(0.3)])

  plt.clf()
  plt.plot(range(n), avg(list(map(lambda x: x[0], price))))
  plt.plot(range(n), avg(list(map(lambda x: x[1], price))))
  plt.plot(range(n), avg(list(map(lambda x: x[2], price))))
  plt.legend(["val=0.9", "val=0.3", "val=0.3"])
  plt.ylabel("Price Charged")
  plt.savefig("./figures/part2_multiple.png")