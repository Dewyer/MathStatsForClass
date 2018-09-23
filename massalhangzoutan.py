import re
import os
import random

filer = open("lotr.txt","r")
lotrScript = filer.read()

lotr = re.sub( '\s+', ' ', lotrScript ).strip()
filer.close()
words = lotr.split(' ')

states = [0,0,0]

for ii in range(0,100000):
    indexer = random.randint(0,len(lotr)-1)
    ll =0
    while "aeouioőúéáűöüó".count(lotr[indexer+ll]) == 0:
        ll+=1
        if len(lotr) <= indexer+ll:
            ll = -1
            break
    
    kk = 0
    while "aeouioőúéáűöüó".count(lotr[indexer+ll+kk]) == 0:
        kk+=1
        if len(lotr) <= indexer+ll+kk:
            kk = -1
            break


    if kk == 1:
        states[0] += 1
    elif kk == 2:
        states[1] += 1
    elif kk>= 0:
        states[2] += 1


oo = sum(states)
print([float(ii)/oo for ii in states])

