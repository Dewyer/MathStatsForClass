import random

def dice():
    return random.randint(1,6)

states = [0,0,0]

for ii in range(0,10000):
    xx = [dice() for ii in range(0,5)]
    ss = sum(xx)
    if ii <= 10:
        print(ss)
    if ss <= 9:
        states[0]+=1
    elif ss >= 10 and ss>=17:
        states[1] += 1
    else:
        states[2] += 1

oo = sum(states)
print([float(ii)/oo for ii in states])