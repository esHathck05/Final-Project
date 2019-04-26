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

class Pacman(Sprite):
    def __init__(self, x, y, w, h, color, app):
        super().__init__(CircleAsset(30, LineStyle(0,Color(0, 1.0)), color),
            (snapfunc(x), snapfunc(y)))
        Pacman.direction = 4
        Pacman.go = True

    # pacman goes left
    def left(b):
        Pacman.rotation = pi
        b.direction = -4
        
    def right(b):
        Pacman.rotation = pi
        b.direction = 4
        
    def step():
        if key == "up arrow" and pacman.go == True:
            self.vy = -4


# Set up event handlers for the app
class Twoplayer(App):
    def __init__(self):
        super().__init__()
        self.b = None
        self.pos = (0,0)
        myapp.listenKeyEvent('keydown', 'left arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'right arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'up arrow', self.moveKey)

    def step(self):
        Pacman.x += Pacman.direction
        if Pacman.x + Pacman.width > myapp.width:
            Pacman.x -= Pacman.direction
            left(Pacman)
        if Pacman.x < 0:
            right(Pacman)
    
    # handles directions
    def moveKey(self, event):
            if self.b:
                self.b.move(event.key)
                
    def leftKey(event):
        left(Pacman)
        
    def rightKey(event):
        right(Pacman)

app = Twoplayer()
app.run()