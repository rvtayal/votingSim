from candidate import Candidate
from citizen import Citizen
from votingMachine import VotingMachine
import numpy as np
from collections import defaultdict
import copy
import matplotlib.pyplot as plt


numVoters = int(100000)
numCandidates = 20
methods = ["traditional", "ranked", "approval"] #, "star"]

def voterGraph(voters):
    dec = 1
    pos = [v.position for v in voters]
    plt.hist(x=pos, bins = 100)
    plt.show()

def candidateGraph(cands):
    y = []
    xmin = []
    xmax = []
    for i in range(len(cands)):
        y.append(i)
        b = cands[i].bounds
        xmin.append(b[0])
        xmax.append(b[1])
    plt.hlines(y, xmin, xmax)
    plt.show()

def main():
    voters, candidates = initialize()
    vms = [None] * len(methods)

    # for i in range(len(methods)):
    #     method = methods[i]
    #     vms[i] = VotingMachine(method, candidates.copy())
    #     #voting
    #     for v in voters:
    #         ballot = v.vote(candidates, method)
    #         vms[i].tally(ballot)

    # for vm in vms:
    #     print("\n{}".format(vm.method))
    #     print(vm.getResults())

    # voterGraph(voters)
    candidateGraph(candidates)


def initialize():
    voters = [None] * numVoters
    for i in range(numVoters):
        voters[i] = Citizen("Voter {}".format(i))

    candidates = [None] * numCandidates
    for i in range(numCandidates):
        candidates[i] = Candidate("Candidate {}".format(i))

    return voters, candidates

if __name__ == "__main__":
    main()