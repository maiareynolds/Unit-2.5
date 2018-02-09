#Maia Reynolds
#2/8/18
#germany.py - german flag

from ggame import *
blackcolor=Color(0x000000,1)
blackoutline=LineStyle(1,blackcolor)
redcolor=Color(0xFF0000,1)
redoutline=LineStyle(1,redcolor)

black=RectangleAsset(1100,150,blackoutline,blackcolor)
red=RectangleAsset(1100,150,redoutline,redcolor)

Sprite(black)
Sprite(red,(0,150))
App().run()