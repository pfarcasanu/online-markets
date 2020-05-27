import numpy as np
import random
import math
import matplotlib.pyplot as plt

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

  def play(self, bidders, threshold_rev=None, threshold_price=None):
    payoffs = np.empty((self.n, self.k))
    revenues = np.empty((self.n, 1))
    prices = np.empty((self.n, 1))
    total_bids = []
    converge = []

    for i in range(self.n): 
      bids = sorted([f() for f in bidders])
      total_bids += bids

      ## Get Actions
      action = self.alg.get_action(payoffs[0:i, :])
      reserve_price = self.actions[action]

      ## Calculate Revenue
      revenues[i] = self.get_revenue(bids, reserve_price)
      prices[i] = reserve_price

      ## Check Convergence
      if threshold_rev and threshold_price and i >= 20:
        if abs(prices[i]  - threshold_price) / threshold_price < 1e-2:
          converge.append(True)
          if all(converge[-3:]) and i >= 6:
            return revenues[:i+1], prices[:i+1]
        else:
          converge.append(False)
      else:
        converge.append(False)

      ## Update Payoffs
      for update_i in range(self.k):
        update_price = self.actions[update_i]

    return revenues, prices
