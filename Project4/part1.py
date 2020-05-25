import random
from distributions import QuadDist, UniDist
from spa import SecondPriceAuction
import numpy as np
import math
import matplotlib.pyplot as plt
from ew import EW_Player
from ftpl import FTPL_Player

def part1():
  def run_experiment(dist_type, n_bidders=2, theo_rev=None, theo_p=None):
    k = 11
    # auction = SecondPriceAuction(n, k, FTPL_Player)
    auction = SecondPriceAuction(n, k, EW_Player)
    temp_rev, temp_p = auction.play([dist_type for i in range(n_bidders)], theo_rev, theo_p)

    return temp_rev, temp_p

  # ## Base Simulations
  # n, n_bidders, trials = 2, 50
  # d = UniDist()
  # price, rev = [], []
  # last10 = int(-n / 10)
  # for trial in range(trials):
  #   # print ("Trial {}".format(trial))
  #   temp_rev, temp_p = run_experiment(dist_type=d.random)
  #   rev.append(np.mean(temp_rev[last10:]))
  #   price.append(np.mean(temp_p[last10:]))

  # print ("=========================================")
  # print ("Converged (last 1/10 of rounds) Averages")
  # print ("Average Reserved Price", int(100*np.mean(price)) / 100)
  # print ("Average Revenue", int(1000*np.mean(rev)) / 1000)
  # print ("=========================================\n")

  # ## How long to converge
  # n, n_bidders, trials = 1000, 2, 50
  # n = [some array]
  # d = UniDist()
  # converg_time = np.empty((trials, 1))
  # theo_p, theo_rev = .5, 5/12
  # for trial in range(trials):
  #   print ("Trial {}".format(trial))
  #   temp_rev, temp_p = run_experiment(dist_type=d.random, theo_rev=theo_rev, theo_p=theo_p)
  #   tot_rounds = np.size(temp_rev)
  #   converg_time[trial] = tot_rounds
  #   print ("% of Rounds Completed: {}".format(100 * tot_rounds / n))

  #   print ("Converged Revenue: {}".format(round(np.mean(temp_rev[-20:]), 4)))
  #   print ("Converged Price: {}".format(round(np.mean(temp_p[-20:]), 4)))
  #   print ()

  # avg_fin = np.mean(converg_time)
  # se_fin = np.std(converg_time, ddof=1) / math.sqrt(trials)
  # print ("=========================================")
  # print ("Average time to converge: {}".format(avg_fin))
  # print ("SE of time to converge: {}".format(se_fin))
  # print ("=========================================\n")  

  # ## Changing # Bidders
  n_bidders = [2, 4, 8, 16, 32, 50, 100]
  n, n_bidders, trials = 1000, 2, 50
  d = UniDist()
  last10 = int(-n / 10)
  for bidders in n_bidders:
    price, rev = [], []
    for trial in range(trials):
      # print ("Trial {}".format(trial))
      temp_rev, temp_p = run_experiment(dist_type=d.random, n_bidders=bidders)
      rev.append(np.mean(temp_rev[last10:]))
      price.append(np.mean(temp_p[last10:]))

    print ("=========================================")
    print ("Num Bidders: {}".format(bidders))
    print ("Converged (last 1/10 of rounds) Averages")
    print ("Average Reserved Price", int(100*np.mean(price)) / 100)
    print ("Average Revenue", int(1000*np.mean(rev)) / 1000)
    print ("=========================================\n")

  ## Different Distributions
  # expected reserved price of quad is .578
  # n, k, n_bidders, trials = 1000, 15, 2, 20
  # dists = [QuadDist]
  # last10 = int(-n / 10)
  # for dist_type in dists:
  #   price, rev = [], []
  #   d = dist_type()
  #   print ("Working with", str(d))
  #   for trial in range(trials):
  #     # print ("Trial {}".format(trial))
  #     temp_rev, temp_p = run_experiment(dist_type=d.random, n_bidders=n_bidders)
  #     # print ("Rounds completed", np.size(temp_p))
  #     rev.append(np.mean(temp_rev[last10:]))
  #     price.append(np.mean(temp_p[last10:]))
  
  #   print ("=========================================")
  #   print ("Dist Type: {}".format(str(d)))
  #   print ("Converged (last 1/10 of rounds) Averages")
  #   print ("Average Reserved Price", int(1000*np.mean(price)) / 1000)
  #   print ("Average Revenue", int(1000*np.mean(rev)) / 1000)
  #   print ("=========================================\n")

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
