#!/usr/bin/python3

import random 

maternal = [] #母體
maternalYield = [] #產出率

def maternal_produce(): #母體建立 zfill長度不足補0
    temp = random.randint(100,350)
    press = random.randint(10,50)
    time = random.randint(10,30)
    prm = random.randint(2000,3000)
    print(temp)
    print(press)
    print(time)
    print(prm)
    #maternal.append(temp + press + time + prm)

def test(temp, press, time, prm):
    f = 1 - abs(temp - 285) / 195 - abs(press * time - 60) / 90 - abs(time - 18) / 13 - 0.03
    print(f)
    a = f + 0.03 * prm - 1000 / 2000 
    print(a)

#for x in range(10):
#maternal_produce()
test(285, 3.3333, 18, 3000)