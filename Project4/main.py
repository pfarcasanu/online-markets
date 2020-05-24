import random
import numpy as np
import matplotlib.pyplot as plt
from ew import EW_Player

class SecondPriceAuction:
  def __init__(self, n_rounds, k_actions, alg):
    self.n = n_rounds
    self.k = k_actions
    self.alg = alg(n_rounds, k_actions)
    self.actions = np.linspace(0, 1, k_actions)

  def get_revenue(self, bids, reserve_price):
    revenue = 0
    if max(bids) > reserve_price:
      revenue = max(reserve_price, bids[-2])
    return revenue

  def play(self, bidders):
    payoffs = np.empty((self.n, self.k))
    revenues = np.empty((self.n, 1))
    prices = np.empty((self.n, 1))
    for i in range(self.n):
      action = self.alg.get_action(payoffs[0:i, :])
      reserve_price = self.actions[action]
      bids = sorted([f() for f in bidders])

      ## Calculate Revenue
      revenues[i] = self.get_revenue(bids, reserve_price)
      prices[i] = reserve_price

      ## Update Payoffs
      for update_i in range(self.k):
        update_price = self.actions[update_i]
        payoffs[i, update_i] = self.get_revenue(bids, update_price)

    return revenues, prices

def part1():
  n_bidders = 2
  n, k = 100, 10
  auction = SecondPriceAuction(n, k, EW_Player)
  rev, price = auction.play([random.random for i in range(n_bidders)])

  plt.clf()
  plt.plot(range(n), rev)
  plt.plot(range(n), price)
  plt.savefig("./figures/SPA")


if __name__ == "__main__":
  part1()
