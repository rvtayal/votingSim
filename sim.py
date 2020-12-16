from candidate import Candidate
from citizen import Citizen
from votingMachine import VotingMachine
import numpy as np
from collections import defaultdict
import copy
import matplotlib.pyplot as plt


numVoters = 100000
numCandidates = 5
methods = ["traditional", "ranked", "approval"] #, "star"]

def voterGraph(voters, ax=None):
    if ax is None:
        ax = plt.gca()
    dec = 1
    pos = [v.position for v in voters]
    ax.hist(x=pos, bins = 100)
    ax.set_xlim(-10, 10)
    return ax

def candidateGraph(cands, ax=None):
    if ax is None:
        ax = plt.gca()
    y = []
    xmin = []
    xmax = []
    p = []
    names = []
    for i in range(len(cands)):
        y.append(i)
        b = cands[i].bounds
        xmin.append(b[0])
        xmax.append(b[1])
        p.append(cands[i].position)
        names.append(cands[i].id)
    
    ndx = np.array(np.argsort(p))
    xmin = [xmin[i] for i in ndx]
    xmax = [xmax[i] for i in ndx]
    names = [names[i] for i in ndx]
    ax.hlines(y, xmin, xmax)
    plt.yticks(range(len(cands)), names)
    plt.xticks([-10, 0, 10], ['far left', 'neutral', 'far right'])
    return ax

def main():
    voters, candidates = load_2016()
    vms = [None] * len(methods)

    for i in range(len(methods)):
        method = methods[i]
        print(method)
        vms[i] = VotingMachine(method, candidates.copy())
        #voting
        for v in voters:
            # print(v)
            ballot = v.vote(candidates, method)
            # print(ballot)
            vms[i].tally(ballot)

    for vm in vms:
        print("\n{}".format(vm.method))
        print(vm.getResults())

    fig, (ax1, ax2) = plt.subplots(2)
    g1 = voterGraph(voters, ax1)
    g2 = candidateGraph(candidates, ax2)
    plt.show()


def initialize():
    voters = [None] * numVoters
    for i in range(numVoters):
        voters[i] = Citizen("Voter {}".format(i))

    candidates = [None] * numCandidates
    for i in range(numCandidates):
        candidates[i] = Candidate("Candidate {}".format(i))

    return voters, candidates


def load_2016():
    voters = [None] * numVoters
    for i in range(numVoters):
        voters[i] = Citizen("Voter {}".format(i))

    candidates = [None] * 2
    candidates[0] = Candidate("Trump")
    candidates[1] = Candidate("Clinton")
    candidates[0].bounds = [0.5, 8]
    candidates[1].bounds = [-3, -0.1]
    candidates[0].reset_pos()
    candidates[1].reset_pos()

    return voters, candidates

if __name__ == "__main__":
    main()