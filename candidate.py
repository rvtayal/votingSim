import numpy as np

class Candidate:
    def __init__(self, id):
        self.bounds = [0, 10]
        while (self.bounds[1] - self.bounds[0]) > 3:
            self.bounds = np.sort(np.random.uniform(-2, 2, (2,)))
        self.position = np.average(self.bounds)
        self.id = id

    def __repr__(self):
        return self.id

    def reset_pos(self):
        self.position = np.average(self.bounds)

if __name__ == "__main__":
    c = Candidate("lol")
    print(c.bounds)