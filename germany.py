#Maia Reynolds
#2/8/18
#germany.py - german flag

from ggame import *
blackcolor=Color(0x000000,1)
blackoutline=LineStyle(1,blackcolor)
redcolor=Color(0xFF0000,1)
redoutline=LineStyle(1,redcolor)
yellowcolor=Color(0xFFFF00,1)
yellowoutline=LineStyle(1,yellowcolor)

black=RectangleAsset(700,150,blackoutline,blackcolor)
red=RectangleAsset(700,150,redoutline,redcolor)
yellow=RectangleAsset(700,150,yellowoutline,yellowcolor)

Sprite(black)
Sprite(red,(0,150))
Sprite(yellow,(0,300))
App().run()