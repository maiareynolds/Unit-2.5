#Maia Reynolds
#3/7/18
#remainder.py - remainder and faces

from random import randint
from ggame import *

yellow=Color(0xFFFF00,1)
one=randint(1,100)
two=randint(1,one)
ans=int(input("Find the remainder of "+str(one)+"/"+str(two)+": "))
if ans==one%two:
    happy=CircleAsset(60,LineStyle(1,yellow),yellow)
    Sprite(happy,(50,50))
else:
    print("yay")

App().run
