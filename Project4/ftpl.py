import numpy as np
import math

class FTPL_Player:
    def __init__(self, n, k, e=None):
        if not e:
            self.e = math.sqrt(math.log(k) / n)
        else:
            self.e = e
        self.hallucination = self.hallucinate(self.e, k).reshape(1,-1)
        # print ("FTPL Hallucination values: ", self.hallucination)
        
    def __str__(self):
        return "FTPL"
    
    def hallucinate(self, eps, num_actions):
        hallu = np.random.geometric(p=eps, size=num_actions) - 1
        # print(hallu)
        return hallu

    ## Get data set and return pay off
    # data: k x n
    def get_action(self, data):
        n = np.shape(data)[0]
        new_data = np.vstack((self.hallucination, data))
        # print(np.sum(new_data[0:n+1, :], axis=0))
        action = np.argmax(np.sum(new_data[0:n+1, :], axis=0))
        # print(action)
        return action