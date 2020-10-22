import numpy as np
from candidate import Candidate
from citizen import Citizen
from collections import defaultdict

class VotingMachine:
    def __init__(self, method, candidates):
        self.method = method
        self.count = defaultdict(int)
        self.ballots = []
        self.countVoted = 0
        self.candidates = candidates

    def tally(self, ballot):
        self.ballots.append(ballot)
        if len(ballot) == 0:
            return
        if self.method == "traditional":
            self.tallyTraditional(ballot)
        elif self.method == "ranked":
            self.tallyRanked(ballot)
        elif self.method == "approval":
            self.tallyApproval(ballot)

    def tallyTraditional(self, ballot):
        self.count[ballot[0]] += 1

    def tallyRanked(self, ballot):
        self.count[ballot[0]] += 1
        self.countVoted += 1
    
    def tallyApproval(self, ballot):
        for c in ballot:
            self.count[c] += 1
    
    def resultsCalc(self):
        results = []
        for k in self.count.keys():
            results.append((k, self.count[k]))
        votes = [r[1] for r in results]
        ndx = np.argsort(votes)
        r = []
        for n in reversed(ndx):
            r.append(results[n])
        return r

    def getResults(self):
        if (self.method == "traditional") or (self.method == "approval"):
            return self.resultsCalc()
        
        if self.method == "ranked":
            isWinner = False
            while not isWinner:
                winner = max(self.count, key=lambda key: self.count[key])
                votes = self.count[winner]
                if votes/self.countVoted > 0.5:
                    return self.resultsCalc()
                
                # eliminate lowest votes
                loser = self.calculateLoser()
                self.deleteLoser(loser)

    
    def deleteLoser(self, loser):
        self.count = defaultdict(int)
        self.countVoted = 0
        ballots = self.ballots
        self.ballots = []
        for b in ballots:
            if loser in b:
                b.remove(loser)
            self.tally(b)
        self.candidates.remove(loser)

    def calculateLoser(self):
        minCount = 100000000
        loser = None
        for c in self.candidates:
            if self.count[c] < minCount:
                minCount = self.count[c]
                loser = c
        return loser
