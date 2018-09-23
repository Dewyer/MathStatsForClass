import random

def dice():
    return random.randint(1,6)

states = [0,0,0]

for ii in range(0,100000):
    xx = [dice() for ii in range(0,5)]
    ss = xx.count(6)
    if ii <= 10:
        print(ss)
    if ss == 0:
        states[0]+=1
    elif ss == 1 or ss == 2:
        states[1] += 1
    else:
        states[2] += 1

oo = sum(states)
print([float(ii)/oo for ii in states])