import numpy as np
from candidate import Candidate

starfactor = 2.5

class Citizen:
    def __init__(self, id, position=None):
        self.id = id
        if position is None:
            self.position = np.random.normal(0, 2)
        else:
            self.position = position

    def __repr__(self):
        return self.id

    def vote(self, candidates, method):
        if method == "traditional":
            minDist = 10
            voteFor = None
            for c in candidates:
                pos = c.position
                bounds = c.bounds
                dist = np.abs(pos - self.position)
                if dist < minDist and (self.position >= bounds[0]) and (self.position <= bounds[1]):
                    minDist = dist
                    voteFor = [c]

        if method == "ranked":
            voteFor = []
            dists = []
            for c in candidates:
                pos = c.position
                dist = np.abs(pos - self.position) 
                bounds = c.bounds
                if (self.position >= bounds[0]) and (self.position <= bounds[1]):
                    voteFor.append(c)
                    dists.append(dist)
            ndx = np.argsort(dists)
            if len(ndx) > 0:
                voteFor2 = []
                for i in ndx:
                    voteFor2.append(voteFor[i])
                voteFor = voteFor2
            else:
                voteFor = []

        if method == "approval":
            voteFor = []
            for c in candidates:
                bounds = c.bounds
                if (self.position >= bounds[0]) and (self.position <= bounds[1]):
                    voteFor.append(c)
        
        # if method == "star":
        #     dists = []
        #     for c in candidates:
        #         d = np.abs(c.position - self.position)
        #         dists.append((c,d))

        #     print(dists)
            
        #     exit(0)
        #     voteFor = []
        
        return voteFor

def main():
    numVoters = 30
    voters = [None] * numVoters
    for i in range(numVoters):
        voters[i] = Citizen("Voter {}".format(i))
    
    numCandidates = 3
    candidates = [None] * numCandidates
    for i in range(numCandidates):
        candidates[i] = Candidate("Candidate {}".format(i))

    for v in voters:
        v.vote(candidates, "approval")

if __name__ == "__main__":
    main()