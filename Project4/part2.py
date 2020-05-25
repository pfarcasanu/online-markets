import numpy as np

class SellingIntroductions:
  def __init__(self, n_rounds, n_actions, alg):
    self.n = rounds
    self.k = n_actions

  def play(self, bidders):
    prices = np.linspace(0, 1, self.k)
    payoffs = np.empty((self.n, ))
    bids = [bidder.get() for bidder in bidders]



if __name__ == "__main__":
  pass