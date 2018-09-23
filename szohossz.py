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
    indexer = random.randint(0,len(words)-1)
    ll = len(words[indexer])
    
    if (ll <= 3):
        states[0] += 1
    elif ll>= 4 and ll<=6:
        states[1] += 1
    else:
        states[2] += 1


oo = sum(states)
print([float(ii)/oo for ii in states])

