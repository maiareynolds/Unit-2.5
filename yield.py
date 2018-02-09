#Maia Reynolds
#2/9/18
#yield.py - displays yield sign

from ggame import *
yellow=Color(0xFFFF00,1)
black=Color(0x000000,1)
yOutline=LineStyle(20,yellow)
bOutline=LineStyle(6,black)

outer=PolygonAsset([(0,0),(200,0),(100,180)],yOutline,black)
inner=PolygonAsset([(0,0),(190,0),(95,170)],bOutline,yellow)
yIeld=TextAsset("YIELD",fill=black,style="bold 30pt Ariel")

Sprite(outer,(390,150))
Sprite(inner,(410,170))
Sprite(yIeld,(445,190))

App().run()