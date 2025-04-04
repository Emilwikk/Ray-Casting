import pyglet
import utils
from pyglet import shapes
import config


graphicsBatch = pyglet.graphics.Batch()

class lamp:
    def __init__(self, x, y, intensity, r):
        self.x = x
        self.y = y
        self.r = config.lampRad
        self.intensity = intensity
        self.rayList = [0]*self.intensity
        self.shape = shapes.Circle(self.x, self.y, self.r, color=(255,255,143), batch=graphicsBatch)

    def update(self):
        # For future if I want the lamps to be movable, maybe attached to a string in the ceiling?
        pass


class ray:
    def __init__(self,x,y,angle,objects):
        # Coordinate for the source of the ray
        self.xSrc = x
        self.ySrc = y
        color = (255,255,160)
        # Angle at which ray propagates, 0 deg is to the right, 90 deg is up 
        self.angle = angle

        #self.xEnd, self.yEnd = utils.findCircle(self.xSrc,self.ySrc,self.angle,circle)
        #self.xEnd, self.yEnd = utils.findEdges(self.xSrc,self.ySrc,self.angle, config.screenWidth, config.screenHeight)
        self.xEnd, self.yEnd = utils.findIntersection(self,objects,config.screenWidth,config.screenHeight)

        # Check if rays end outside of the screen, if ray outside screen; ray is red.
        if self.xEnd > config.screenWidth or self.xEnd < 0 or self.yEnd > config.screenHeight or self.yEnd < 0:
            color = (255,0,0)
        self.shape = shapes.Line(self.xSrc, self.ySrc, self.xEnd, self.yEnd, thickness=2, color=color, batch=graphicsBatch)


    def update(self,x,y,angle):
        self.xSrc = x
        self.ySrc = y
        self.angle = angle
        self.xEnd, self.yEnd = utils.findCircle(self.xSrc,self.ySrc,self.angle,circle)
        self.xEnd, self.yEnd = utils.findEdges(self.xSrc,self.ySrc,angle, config.screenWidth, config.screenHeight)
        pass


class circle:
    def __init__(self,x,y,r,color,moveable):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.moveable = moveable
        self.shape = shapes.Circle(self.x, self.y, self.r, color=self.color, batch=graphicsBatch)


    def update(self,dt):
        if self.moveable:
            pass


class rectangle:
    def __init__(self,x,y,width,height,color,moveable):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.moveable = moveable
        self.shape = shapes.Rectangle(self.x,self.y,width,height,color=color,batch=graphicsBatch)

    def update(self,dt):
        if self.moveable:
            pass
