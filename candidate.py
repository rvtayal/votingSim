import numpy as np

class Candidate:
    def __init__(self, id):
        self.bounds = np.sort(np.random.uniform(-2, 2, (2,)))
        self.position = np.average(self.bounds)
        self.id = id

    def __repr__(self):
        return self.id