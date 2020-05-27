import random
from distributions import QuadDist, UniDist
from spa import SecondPriceAuction
import numpy as np
import math
import matplotlib.pyplot as plt
from ew import EW_Player
from ftpl import FTPL_Player
from scipy import stats

def graph_rev_price(rev, price, xlabel, ylabel, title, rev_line=None, p_line=None):
  n = np.size(rev)
  new_rev = [sum(rev[max(0, n_i-30):n_i + 1]) / len(rev[max(0, n_i-30):n_i + 1]) for n_i in range(n)]
  new_p = [sum(price[max(0, n_i-30):n_i + 1]) / len(price[max(0, n_i-30):n_i + 1]) for n_i in range(n)]
  plt.clf()
  plt.plot(range(n), new_rev, label="Rev", color="orange")
  plt.plot(range(n), new_p, label="Price", color="green")
  if rev_line:
    plt.hlines(y=rev_line, xmin=0, xmax=n, label="Expected Rev", color="orange", linestyles="dashed")
  if p_line:
    plt.hlines(y=p_line, xmin=0, xmax=n, label="Expected Price", color="green", linestyles="dashed")
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)
  plt.legend()
  plt.savefig("./figures/{}_rev_price".format(title))

def part1():
  def run_experiment(dist_type, k=11, n_bidders=2, theo_rev=None, theo_p=None):
    # auction = SecondPriceAuction(n, k, FTPL_Player)
    auction = SecondPriceAuction(n, k, EW_Player)
    temp_rev, temp_p = auction.play([dist_type for i in range(n_bidders)], theo_rev, theo_p)

    return temp_rev, temp_p

  uni_d = UniDist()
  quad_d = QuadDist()

  # ## Base Simulations
  # n, trials = 1000, 100
  # price, rev = np.array([]), []
  # last10 = int(-n / 10)
  # for _ in range(trials):
  #   temp_rev, temp_p = run_experiment(dist_type=uni_d.random)
  #   rev.append(np.mean(temp_rev[last10:]))
  #   price = np.hstack((price, temp_p[:, 0]))

  # print ("=========================================")
  # print ("Base Simulation")
  # print ("Converged (last 1/10 of rounds) Averages")
  # print ("Mode Res Price", int(100*stats.mode(price)[0][0]) / 100)
  # print ("Avg Revenue", int(1000*np.mean(rev)) / 1000)
  # print ("=========================================\n")

  # ## How long to converge
  # n_rounds = [50, 100, 250, 500, 1000, 2500, 5000, 10000]
  n_rounds = np.logspace(2, 4, 30, dtype=int)
  fins = []
  trials = 100
  for n in n_rounds:
    converg_time = np.empty((trials, 1))
    avg_p, price, avg_rev = np.empty((trials, 1)), np.array([]), np.empty((trials, 1))
    for trial in range(trials):
      temp_rev, temp_p = run_experiment(dist_type=uni_d.random, theo_rev=5/12, theo_p=0.5)
      converg_time[trial] = np.size(temp_rev)
      avg_rev[trial] = np.mean(temp_rev[-20:])
      price = np.hstack((price, temp_p[:, 0]))
      avg_p[trial]  = np.mean(temp_p[-20:])

    avg_fin = np.mean(converg_time)
    fins.append(avg_fin)
    se_fin = np.std(converg_time, ddof=1) / math.sqrt(trials)
    print ("=========================================")
    print ("Total rounds {}".format(n))
    print ("Average time to converge: {}".format(avg_fin))
    # print ("% time to converge: {}".format(avg_fin / n))
    # print ("SE of time to converge: {}".format(se_fin))
    # print ("Mode Res Price: {}".format(round(stats.mode(price)[0][0], 2)))
    # print ("Avg Converged Res Price:  {}".format(round(np.mean(avg_p), 4)))
    # print ("Avg Revenue: {}".format(round(np.mean(avg_rev), 4)))
    print ("=========================================\n")

  plt.clf()
  plt.plot(n_rounds, fins)
  plt.plot([0, n], [0, n])
  plt.title("Num of Rounds to Convergence")
  plt.xlabel("Total Ronds")
  plt.ylabel("Num Rounds to Converge")
  plt.xscale("log")
  plt.yscale("log")
  plt.savefig("./figures/round_converge")

  # ## Changing # Bidders
  # n_bidders = [2, 4, 8, 16, 32, 50, 100]
  # n, trials = 1000, 100
  # last10 = int(-n / 10)
  # for bidders in n_bidders:
  #   avg_p, price, last10_rev, rev = np.empty((trials, 1)), np.array([]), np.empty((trials, 1)), np.array([])
  #   for trial in range(trials):
  #     # print ("Trial {}".format(trial))
  #     temp_rev, temp_p = run_experiment(dist_type=uni_d.random, n_bidders=bidders)
  #     rev = np.hstack((rev, temp_rev[:, 0]))
  #     last10_rev[trial] = np.mean(temp_rev[last10:])
  #     price = np.hstack((price, temp_p[:, 0]))
  #     avg_p[trial]  = np.mean(temp_p[last10:])

  #   print ("=========================================")
  #   print ("Num Bidders: {}".format(bidders))
  #   print ("Mode Res Price: {}".format(round(stats.mode(price)[0][0], 2)))
  #   print ("Avg Converged Res Price:  {}".format(round(np.mean(avg_p), 4)))
  #   print ("Avg Revenue: {}".format(round(np.mean(rev), 4)))
  #   print ("Avg Converged Revenue: {}".format(round(np.mean(last10_rev), 4)))
  #   print ("=========================================\n")

  ## Different Distributions
  # expected reserved price of quad is .578
  # n, k, trials = 1000, 15, 1
  # dists = [quad_d, uni_d]
  # last10 = int(-n / 10)
  # for dist_type in dists:
  #   avg_p, price, rev, last10_rev = np.empty((trials, 1)), [], [], np.empty((trials, 1))
  #   print ("Working with", str(dist_type))
  #   for trial in range(trials):
  #     # print ("Trial {}".format(trial))
  #     temp_rev, temp_p = run_experiment(dist_type=dist_type.random, k=k)
  #     rev = np.hstack((rev, temp_rev[:, 0]))
  #     last10_rev[trial] = np.mean(temp_rev[last10:])
  #     avg_p[trial] = np.mean(temp_p[last10:])
  #     price = np.hstack((price, temp_p[:, 0]))

  #     graph_rev_price(rev, price, "Round", "Dollars", str(dist_type), rev_line=dist_type.rev, p_line=dist_type.price)
  #   print ("=========================================")
  #   print ("Dist Type: {}".format(str(dist_type)))
  #   print ("Converged (last 1/10 of rounds) Averages")
  #   print ("Mode Res Price: {}".format(round(stats.mode(price)[0][0], 2)))
  #   print ("Avg Converged Res Price:  {}".format(round(np.mean(avg_p), 4)))
  #   print ("Avg Revenue: {}".format(round(np.mean(rev), 4)))
  #   print ("Avg Converged Revenue: {}".format(round(np.mean(last10_rev), 4)))
  #   print ("=========================================\n")


if __name__ == "__main__":
  part1()
