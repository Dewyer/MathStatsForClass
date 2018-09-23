import random
def isRed():
    return 1 if random.randint(1,4) == 1 else 0

states = [0,0,0]

for tries in range(0,1000000):
    kk = sum([isRed() for ii in range(0,8)])

    if kk <= 2:
        states[0] += 1
    elif kk >= 3 and kk<= 5:
        states[1] += 1
    else:
        states[2] += 1
    

oo = sum(states)
print([float(ii)/oo for ii in states])