
selectedObject = None

def mouseControl(window,objects):
    @window.event
    def on_mouse_press(x,y,button,modifiers):
        global selectedObject
        for o in objects[0]:
            if (x-o.x)**2+(y-o.y)**2<o.r**2:
                selectedObject = o

        for o in objects[1]:
            if (o.x<x<o.x+o.width and o.y<y<o.y+o.height):
                selectedObject = o

    @window.event
    def on_mouse_drag(x,y,dx,dy,button,modifiers):
        global selectedObject
        if selectedObject:
            selectedObject.x += dx
            selectedObject.y += dy
            selectedObject.shape.x = selectedObject.x
            selectedObject.shape.y = selectedObject.y

    @window.event
    def on_mouse_release(x,y,button,modifiers):
        global selectedObject
        selectedObject = None
        
    