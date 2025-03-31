# Ray casting exercise

import pyglet
import math
from pyglet import shapes
import utils

screenHeight = 1024
screenWidth = 2048
window = pyglet.window.Window(screenWidth,screenHeight,'Ray Tracing')

lampRad = 5

pyglet.gl.glClearColor(0.1,0.1,0.1,1.0)
graphicsBatch = pyglet.graphics.Batch()

class ray:
    def __init__(self,x,y,angle):
        # Coordinate for the source of the ray
        self.xSrc = x
        self.ySrc = y
        color = (255,255,160)
        # Angle at which ray propagates, 0 deg is to the right, 90 deg is up 
        self.angle = angle
        self.xEnd, self.yEnd = utils.findEdges(self.xSrc,self.ySrc,self.angle, screenWidth, screenHeight)
        # Check if rays end outside of the screen, if ray outside screen; ray is red.
        if self.xEnd > screenWidth or self.xEnd < 0 or self.yEnd > screenHeight or self.yEnd < 0:
            color = (255,0,0)
        self.shape = shapes.Line(self.xSrc, self.ySrc, self.xEnd, self.yEnd, thickness=2, color=color, batch=graphicsBatch)


    def update(self,x,y,angle):
        self.xSrc = x
        self.ySrc = y
        self.angle = angle
        self.xEnd, self.yEnd = utils.findEdges(self.xSrc,self.ySrc,angle, screenWidth, screenHeight)
        pass


class lamp:
    def __init__(self, x, y, intensity, r):
        self.x = x
        self.y = y
        self.r = lampRad
        self.intensity = intensity
        self.rayList = [0]*self.intensity
        self.shape = shapes.Circle(self.x, self.y, self.r, color=(255,255,143), batch=graphicsBatch)

    def update(self):
        # For future if I want the lamps to be movable, maybe attached to a string in the ceiling?
        pass

l1 = lamp(500,950,500,lampRad)
l2 = lamp(1800,950,300,lampRad)
lamps = [l1, l2]

for l in lamps:
    for i in range(l.intensity):
        l.rayList[i] = ray(l.x, l.y,i*2*math.pi/l.intensity)

def update(dt):
    pass


@window.event
def on_draw():
    window.clear()
    graphicsBatch.draw()
        
# 60 fps
pyglet.clock.schedule_interval(update, 1/60)

pyglet.app.run()