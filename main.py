# Ray casting exercise

import pyglet
import math
import objects
import config

window = pyglet.window.Window(config.screenWidth,config.screenHeight,'Ray Casting Simulator')

pyglet.gl.glClearColor(config.backgroudColor[0],config.backgroudColor[1],config.backgroudColor[2],config.backgroudColor[3])

l1 = objects.lamp(500,950,500,config.lampRad)
l2 = objects.lamp(1800,950,300,config.lampRad)
lamps = [l1, l2]

o1 = objects.circle(200,200,50,(255,255,255),1)
o2 = objects.circle(500,700,25,(255,255,255),1)
circles = [o1,o2]

r1 = objects.rectangle(700,200,200,50,(255,255,255),1)
r2 = objects.rectangle(900,300,20,500,(255,255,255),1)
rectangles = [r1,r2]

allObjects = [circles, rectangles]

for l in lamps:
    for i in range(l.intensity):
        l.rayList[i] = objects.ray(l.x, l.y,i*2*math.pi/l.intensity,allObjects)

def update(dt):
    pass


@window.event
def on_draw():
    window.clear()
    objects.graphicsBatch.draw()
        
# 60 fps
pyglet.clock.schedule_interval(update, 1/config.fps)

pyglet.app.run()