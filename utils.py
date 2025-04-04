import math

def findEdges(ray, screenWidth, screenHeight):
    x = ray.xSrc
    y = ray.ySrc
    angle = ray.angle
    dx = math.cos(angle)
    dy = math.sin(angle)

    # List with [t,xEdge,yEdge], t is "time" for the ray to reach the edge or the length of the ray.
    t_list = []

    # Right edge
    if dx != 0:
        t =  (screenWidth-x)/dx
        if t > 0:
            yEdge = y+t*dy
            if 0 <= yEdge <= screenHeight:
                t_list.append((t,screenWidth,yEdge))

    # Left edge
    if dx != 0:
        t = -x/dx
        if t > 0:
            yEdge = y+t*dy
            if 0 <= yEdge <= screenHeight:
                t_list.append((t,0,yEdge))

    # Bottom edge
    if dy != 0:
        t = -y/dy
        if t > 0:
            xEdge = x+t*dx
            if 0 <= xEdge <= screenWidth:
                t_list.append((t,xEdge,0))

    # Top edge
    if dy != 0:
        t = (screenHeight-y)/dy
        if t > 0:
            xEdge = x+t*dx
            if 0 <= xEdge <= screenWidth:
                t_list.append((t,xEdge,screenHeight))

    if not t_list:
        return x, y  # No intersection, prolly because origin of ray is outside screen
    
    t,xEnd,yEnd = min(t_list, key= lambda item: item[0])
    
    return xEnd, yEnd, t
    
def findCircle(ray,circle):
    x,y,angle = ray.xSrc,ray.ySrc,ray.angle
    dx = math.cos(angle)
    dy = math.sin(angle)

    # Solution to parametrization of line in the equation of a circle
    # Coefficients of At^2+Bt+C=0
    A = dx**2+dy**2
    B = 2*((x-circle.x)*dx+(y-circle.y)*dy)
    C = (x-circle.x)**2+(y-circle.y)**2-circle.r**2

    discriminant = (B/(2*A))**2-C/A

    if discriminant < 0:
        # No intersection
        return None
    
    if abs(discriminant) < 0.0001:
        # One intersection
        t = -B/(2*A)
        if t<0:   # We only want positive t, negative t means intersection is behind the ray.
            return None
        else:
            xEnd = x+t*dx
            yEnd = y+t*dy
            return xEnd, yEnd, t

    else:
        # Two intersections
        t1 = -B/(2*A)+math.sqrt(discriminant)
        if t1>=0:    
            xEnd = x+t1*dx
            yEnd = y+t1*dy
        t2 = -B/(2*A)-math.sqrt(discriminant)
        if t1 < t2:
            return xEnd, yEnd, t1
        else:
            if t2 >= 0:
                xEnd = x+t2*dx
                yEnd = y+t2*dy
                return xEnd, yEnd, t2
            
def findRectangle(ray,rectangle):
    t_list = []
    x,y,angle = ray.xSrc, ray.ySrc, ray.angle
    dx = math.cos(angle)
    dy = math.sin(angle)

    # Upper edge
    if dy != 0:
        yEnd = rectangle.y+rectangle.height
        t = (yEnd-y)/dy
        if t>0:
            xEnd = x+t*dx
            if rectangle.x<xEnd<rectangle.x+rectangle.width:
                t_list.append((xEnd,yEnd,t))

    # Lower edge
    if dy != 0:
        yEnd = rectangle.y
        t = (yEnd-y)/dy
        if t>0:
            xEnd = x+t*dx
            if rectangle.x<xEnd<rectangle.x+rectangle.width:
                t_list.append((xEnd,yEnd,t))
    
    # Right edge
    if dx != 0:
        xEnd = rectangle.x+rectangle.width
        t = (xEnd-x)/dx
        if t>0:
            yEnd = y+t*dy
            if rectangle.y<yEnd<rectangle.y+rectangle.height:
                t_list.append((xEnd,yEnd,t))

    # Left edge
    if dx != 0:
        xEnd = rectangle.x
        t = (xEnd-x)/dx
        if t>0:
            yEnd = y+t*dy
            if rectangle.y<yEnd<rectangle.y+rectangle.height:
                t_list.append((xEnd,yEnd,t))

    if t_list:
        xEnd, yEnd, t = min(t_list, key= lambda item: item[2])
        return xEnd, yEnd, t

    return

        
def findIntersection(ray,objects,screenWidth,screenHeight):

    t_list = []
    # Circles
    for c in objects[0]:
        result = findCircle(ray,c)
        if result:
            t_list.append(result)

    # Rectangles
    for re in objects[1]:
        result = findRectangle(ray,re)
        if result:
            t_list.append(result)

    # Edge of the screen
    result = findEdges(ray, screenWidth, screenHeight)
    if result:
        t_list.append(result)

    xEnd,yEnd,t = min(t_list, key=lambda item: item[2])

    return xEnd, yEnd


    