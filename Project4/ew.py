import numpy as np
import math
import random

class EW_Player:
    def __init__(self, n, k, e=None):
        if not e:
            self.e = math.sqrt(math.log(k) / n)
        else:
            self.e = e
    
    def __str__(self):
        return "EW"

    def prob_action(self, data, eps, k_i):
        v_sum = 0
        if data.shape[0] > 0:
            v_sum = np.sum(data[:, k_i])
        return (1 + eps) ** v_sum

    def prob_actions(self, data, eps):
        k = np.shape(data)[1]
        return [self.prob_action(data, eps, k_i) for k_i in range(k)]

    ## Get data set and return payoff
    def get_action(self, data):
        k = data.shape[1]
        pi_prob = self.prob_actions(data, self.e)
        sum_prob = sum(pi_prob)
        pi_prob = [x / sum_prob for x in pi_prob]
        seed = random.random()
        temp_prob = 0
        for act in range(k):
            temp_prob += pi_prob[act]
            if seed > temp_prob:
                continue
            return act
