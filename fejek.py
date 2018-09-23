import random

def coin():
    return random.randint(0,1)

statesOne = [0,0,0]
statesTwo = [0,0,0]

for numberOfTry in range(0,100000):
    coins = [coin() for ii in range(0,20)]
    heads = sum(coins)
    tails = len(coins)-heads

    if heads <= 6:
        statesOne[0] += 1
    elif heads >= 7 and heads <= 13:
        statesOne[1] += 1
    else:
        statesOne[2] += 1

    difer = abs(heads-tails)
    if difer == 0:
        statesTwo[0] += 1
    elif difer == 1:
        statesTwo[1] += 1
    else:
        statesTwo[2] += 1

oo1 = sum(statesOne)
print([float(ii)/oo1 for ii in statesOne])
oo2 = sum(statesTwo)
print([float(ii)/oo2 for ii in statesTwo])