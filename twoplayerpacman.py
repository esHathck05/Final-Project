from ggame import App, Sprite, RectangleAsset, CircleAsset, LineStyle, Color
from math import pi

myapp = App()

black = Color(0, 1)
noline = LineStyle(0, black)
yellow = Color(0xffff00, 1)

myapp = App()

# define colors and line style
black = Color(0, 1)
noline = LineStyle(0, black)
# a rectangle asset and sprite to use as background
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, black)
bg = Sprite(bg_asset, (0,0))

# A ball! This is already in the ggame-tutorials repository
pacmanplayer = CircleAsset(15, noline, yellow)
pacman = Sprite(pacmanplayer, (15, 200))
# custom attributes
pacman.direction = 4
pacman.go = True

pacman.fxcenter = 0.5
pacman.fycenter = 0.5

# pacman goes left
def left(b):
    pacman.rotation = pi
    b.direction = -4
    
def right(b):
    pacman.rotation = pi
    b.direction = 4
    
# Set up function for handling screen refresh
def step():
    if pacman.go:
        pacman.x += pacman.direction
        if pacman.x + pacman.width > myapp.width:
            pacman.x -= pacman.direction
            left(pacman)
        if pacman.x < 0:
            right(pacman)

# Handle the directions
def leftKey(event):
    left(pacman)
    
def rightKey(event):
    right(pacman)


# Set up event handlers for the app
myapp.listenKeyEvent('keydown', 'left arrow', leftKey)
myapp.listenKeyEvent('keydown', 'right arrow', rightKey)

myapp.run(step)
