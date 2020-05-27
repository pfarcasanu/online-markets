import numpy as np
import random
import math
import matplotlib.pyplot as plt

class UniDist:
    def __init__(self):
        self.price = 1/2
        self.rev = 5/12

    def __str__(self):
        return "Uniform Distribution"

    def random(self):
        return random.random()

class QuadDist:
    def __init__(self):
        self.price = 1 / math.sqrt(3)
        self.rev = None
        
    def __str__(self):
        return "Quadratic Distribution"

    def random(self):
        q = random.random()
        return math.sqrt(q)

class ExpDist:
    def random(self):
        q = 0
        while q >= (math.e - 1) / math.e or q == 0:
            q = random.random()
        return -1 * math.log(1-q)


if __name__ == "__main__":
    dist = QuadDist()
    # dist = ExpDist()
    x = []
    trials = 1000
    for t in range(trials):
        x.append(dist.random())

    x.sort()
    plt.clf()
    plt.scatter(x, range(trials))
    plt.plot([0,1],[0,1000])
    plt.ylabel("Count")
    plt.xlabel("Value")
    plt.savefig("./figures/geodist")
