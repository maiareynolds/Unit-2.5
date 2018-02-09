#Maia Reynolds
#2/8/18
#germany.py - german flag

from ggame import *
blackcolor=Color(0x000000,1)
blackoutline=LineStyle(1,blackcolor)

black=RectangleAsset(1100,150,blackoutline,blackcolor)

Sprite(black)
App().run()