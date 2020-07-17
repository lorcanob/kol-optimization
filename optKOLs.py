import numpy as np
from scipy.optimize import minimize

import importKOLCSV
from defineInfluencer import kolRoster

print()
print("Start successful")
listSize = kolRoster.__len__()


totalBudget = 500000


def infObj(PostNos):
    '''Sets the new objective'''
    finalReach = 0.0
    index1 = 0
    for entry in kolRoster:
        finalReach = finalReach - (entry.trueReach*PostNos[index1])
        index1 += 1
    return finalReach

def constraintTwo(PostNos):
    runningCost = 0.0
    index2 = 0
    for entry in kolRoster:
        runningCost = runningCost + (entry.emv*PostNos[index2])
        index2 += 1
    runningCost = runningCost - totalBudget
    return runningCost

# INITIAL GUESS
PostNos = np.ones(listSize)


# show initial objective
initialGuessReach = int(-infObj(PostNos))
print('Initial Guess Reach: ' + str(initialGuessReach))

# optimize
lb = (0,)*listSize
ub = (10,)*listSize
bnds = tuple(zip(lb,ub))
con1 = {'type': 'eq', 'fun': constraintTwo}
cons = ([con1])
solution = minimize(infObj, PostNos, method='SLSQP', bounds=bnds, constraints=cons)
x = solution.x


# show final objective
finalReach = int(-infObj(x))
print('Final Reach: ' + str(finalReach))

# print solution
print('Solution')
for i in range(listSize):
    print("{o.name} should post {x:.1f} times.".format(o=kolRoster[i] ,x=x[i]))

print("End Successful")