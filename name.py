#Maia Reynolds
#2/8/18
#name.py - name and color

from ggame import *
entername=input("Enter your name: ")
colorchoice=input("Enter RGB Color Code: ")

backcolor=Color("0x"+colorchoice,1)
outline=LineStyle(1,backcolor)
black=Color(0x000000,1)
white=Color(0xFFFFFF,1)

back=RectangleAsset(1100,700,outline,backcolor)

if colorchoice=="000000":
    name=TextAsset(entername,fill=white,style="bold 60pt Times")
else:
    name=TextAsset(entername,fill=black,style="bold 60pt Times")

Sprite(back)
Sprite(name,(425,200))

App().run()