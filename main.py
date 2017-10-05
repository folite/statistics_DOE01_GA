#!/usr/bin/python3

import random 

maternal = []

def maternal_produce(): #母體建立 zfill長度不足補0
    temp = bin(random.randint(100,350))[2:].zfill(9)
    press = bin(random.randint(10,50))[2:].zfill(6)
    time = bin(random.randint(10,30))[2:].zfill(5)
    prm = bin(random.randint(2000,3000))[2:].zfill(12)
    maternal.append(temp + press + time + prm)

for x in range(10):
     maternal_produce()
print(maternal)