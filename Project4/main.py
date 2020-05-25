import random
import numpy as np
import matplotlib.pyplot as plt
from ew import EW_Player
from ftpl import FTPL_Player

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
      bids = sorted([f() for f in bidders])
      action = self.alg.get_action(payoffs[0:i, :])
      reserve_price = self.actions[action]

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
  n, k = 2500, 11

  def run_experiment():
    auction = SecondPriceAuction(n, k, FTPL_Player)
    temp_rev, temp_price = auction.play([random.random for i in range(n_bidders)])

    last10 = int(-n / 10)
    return np.average(temp_rev[last10:]), np.average(temp_price[last10:])
  
  price, rev = [], []
  for i in range(10):
    temp_rev, temp_p = run_experiment()
    rev.append(temp_rev)
    price.append(temp_p)
    
  print ("Converged (last 1/10 of rounds) Averages")
  print ("Average Price", np.average(price))
  print ("Average Revenue", np.average(rev))

  # plt.clf()
  # run_avg_rev = [sum(rev[max(0, n_i-20):n_i + 1]) / len(rev[max(0, n_i-20):n_i + 1]) for n_i in range(n)]
  # run_avg_price = [sum(price[max(0, n_i-20):n_i + 1]) / len(price[max(0, n_i-20):n_i + 1]) for n_i in range(n)]
  # plt.plot(range(n), run_avg_rev, label="Revenue")
  # plt.plot(range(n), run_avg_price, label="Reserve Price")
  # plt.ylabel("Dollars")
  # plt.xlabel("Round")
  # plt.title("Second Price Auction")
  # plt.legend()
  # plt.savefig("./figures/part1_mov_avg.png")


if __name__ == "__main__":
  part1()
