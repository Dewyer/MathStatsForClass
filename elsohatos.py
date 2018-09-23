import random
def dice():
    return random.randint(1,6)

states = [0,0,0]

for tries in range(0,1000000):
    already = []
    dropped =dice()
    kk = 0
    while (dropped != 6):
        kk+= 1
        already.append(dropped)
        dropped=dice()

    if kk <= 3:
        states[0] += 1
    elif kk == 4 or kk == 5:
        states[1] += 1
    else:
        states[2] += 1
    

oo = sum(states)
print([float(ii)/oo for ii in states])