import numpy as np
from scipy.optimize import minimize

from defineInfluencer import kolRoster

print()
print("Start successful")
listSize = kolRoster.__len__()

# SET CLIENT BUDGET HERE
totalBudget = 5000000


def infObj(initPostNos):# how to restructure this loop such that entry.trueReach can be aliased with other variables. USE Getattr
    '''Sets the new objective'''
    objective = "trueReach"
    finalObjectiveMetric = 0.0
    index1 = 0
    for entry in kolRoster:
        finalObjectiveMetric = finalObjectiveMetric - (getattr(entry, objective)*initPostNos[index1])
        index1 += 1
    return finalObjectiveMetric

def constraintTwo(initPostNos):
    runningCost = 0.0
    index2 = 0
    for entry in kolRoster:
        runningCost = runningCost + (getattr(entry, 'emv')*initPostNos[index2])
        index2 += 1
    runningCost = runningCost - totalBudget
    return runningCost

# INITIAL GUESS
initPostNos = np.ones(listSize)/10


# show initial objective
initialGuessReach = int(-infObj(initPostNos))
print('Reach Initialisation Check: ' + str(initialGuessReach))

# optimize
lb = (0,)*listSize
ub = (1,)*listSize
bnds = tuple(zip(lb,ub))
con1 = {'type': 'eq', 'fun': constraintTwo}
cons = ([con1])
solution = minimize(infObj, initPostNos, method='SLSQP', bounds=bnds, constraints=cons)
x = solution.x


# show final objective
finalReach = int(-infObj(x))
print('Final Reach: ' + str(finalReach))

# print solution while storing it in an array

print('Solution')

for i in range(listSize):
    kolRoster[i].ReachOptPost = bool(x[i])
    if x[i]==1:
        print("{o.name} should post {x:.0f} time.".format(o=kolRoster[i] ,x=x[i]))
    else:
        print("{o.name} should post {x:.0f} times.".format(o=kolRoster[i] ,x=x[i]))


print("End Successful")