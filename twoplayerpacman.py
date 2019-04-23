from ggame import App, Sprite, RectangleAsset, CircleAsset, LineStyle, Color

myapp = App()

black = Color(0, 1)
noline = LineStyle(0, black)
yellow = Color(0xffff00, 1)

"""
# THIS IS HOPEFULLY ALL FOR BUILDING THE MAP
class GenericWall(Sprite):
    def __init__(self, x, y, w, h, color):
        snapfunc = lambda X : X - X % w
        super().__init__(
            RectangleAsset(w-1,h-1,LineStyle(0,Color(0, 1.0)), color),
            (snapfunc(x), snapfunc(y))
        # destroy any overlapping walls
        collideswith = self.collidingWithSprites(type(self))
        if len(collideswith):
            collideswith[0].destroy()
            
# impenetrable wall (black)
class Wall(GenericWall):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, Color(0, 1.0))
    def step(self):
        Wall(self.pos[0], self.pos[1])
"""

myapp = App()

# define colors and line style
green = Color(0x00ff00, 1)
black = Color(0, 1)
noline = LineStyle(0, black)
# a rectangle asset and sprite to use as background
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, green)
bg = Sprite(bg_asset, (0,0))

# A ball! This is already in the ggame-tutorials repository
pacmanplayer = CircleAsset(15, noline, yellow)
pacman = Sprite(pacmanplayer, (0, 0))
# custom attributes
pacman.direction = 3
pacman.go = True

# pacman goes left
def left(b):
    b.direction = -3
    
def right(b):
    b.direction = 3
    
# Set up function for handling screen refresh
def step():
    if pacman.go:
        pacman.x += pacman.direction
        if pacman.x + pacman.width > myapp.width:
            pacman.x -= pacman.direction
            left(pacman)
        if pacman.x < 0:
            right(pacman)
            
# Handle the space key
def spaceKey(event):
    pacman.go = not pacman.go

# Handle the directions
def leftKey(event):
    left(pacman)
    
def rightKey(event):
    right(pacman)

# Handle the mouse click
def mouseClick(event):
    pacman.x = event.x
    pacman.y = event.y

# Set up event handlers for the app
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenKeyEvent('keydown', 'left arrow', leftKey)
myapp.listenKeyEvent('keydown', 'right arrow', rightKey)
myapp.listenMouseEvent('click', mouseClick)

myapp.run(step)
