import random
def isAce():
    return random.randint(1,32) >= 29

states = [0,0,0]

for tries in range(0,1000000):
    kk = 0
    while (isAce()):
        kk+= 1

    if kk <= 5:
        states[0] += 1
    elif kk >= 6 and kk<= 13:
        states[1] += 1
    else:
        states[2] += 1
    

oo = sum(states)
print([float(ii)/oo for ii in states])