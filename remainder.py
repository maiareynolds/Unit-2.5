#Maia Reynolds
#3/7/18
#remainder.py - remainder and faces

from random import randint
from ggame import *

yellow=Color(0xFFFF00,1)
black=Color(0x0000FF,1)
one=randint(1,100)
two=randint(1,one)
ans=int(input("Find the remainder of "+str(one)+"/"+str(two)+": "))
if ans==one%two:
    happy=CircleAsset(200,LineStyle(1,yellow),yellow)
    smile1=EllipseAsset(500,10,LineStyle(1,black),black)
    Sprite(smile1,(50,50))
    Sprite(happy,(300,70))
else:
    print("yay")

App().run()