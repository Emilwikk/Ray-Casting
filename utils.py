import math

def findEdges(x,y,angle, screenWidth, screenHeight):
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
    
    return xEnd, yEnd
    


    