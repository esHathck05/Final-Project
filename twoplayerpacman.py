from ggame import App, Sprite, RectangleAsset, CircleAsset, LineStyle, Color
from math import pi

myapp = App()

black = Color(0, 1)
noline = LineStyle(0, black)
yellow = Color(0xffff00, 1)
blue = Color(0x6495ed, 1)

myapp = App()

# define colors and line style
black = Color(0, 1)
noline = LineStyle(0, black)
# a rectangle asset and sprite to use as background
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, black)
bg = Sprite(bg_asset, (0,0))

class Pacman(Sprite):
    def __init__(self, x, y, w, h, color, app):
        super().__init__(CircleAsset(30, LineStyle(0,Color(0, 1.0)), color))
        self.xdirection = 4
        self.ydirection = 0
        self.go = True
            
    def move(self, key):
        if key == "left arrow":
            self.ydirection = 0
            self.xdirection = -4

        elif key == "right arrow":
            self.ydirection = 0
            self.xdirection = 4
                
        elif key == "up arrow":
            self.xdirection = 0
            self.ydirection = -4
            
        elif key == "down arrow":
            self.xdirection = 0
            self.ydirection = 4
            
class Ghost(Sprite):
    def __init__(self, x, y, w, h, color, app):
        super().__init__(CircleAsset(30, LineStyle(0,Color(0, 1.0)), color))
        self.xdirection = 4
        self.ydirection = 0
        self.go = True
            
    def move(self, key):
        if key == "a":
            self.ydirection = 0
            self.xdirection = -4

        elif key == "d":
            self.ydirection = 0
            self.xdirection = 4
                
        elif key == "w":
            self.xdirection = 0
            self.ydirection = -4
            
        elif key == "s":
            self.xdirection = 0
            self.ydirection = 4


# Set up event handlers for the app
class Twoplayer(App):
    def __init__(self):
        super().__init__()
        self.pac = Pacman(50, 50, 10, 10, yellow, self)
        self.ghost = Ghost(50, 50, 10, 10, blue, self)
        myapp.listenKeyEvent('keydown', 'left arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'right arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'up arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'down arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'a', self.moveKey)
        myapp.listenKeyEvent('keydown', 'd', self.moveKey)
        myapp.listenKeyEvent('keydown', 'w', self.moveKey)
        myapp.listenKeyEvent('keydown', 's', self.moveKey)
    
    # handles directions
    def moveKey(self, event):
        if self.pac:
            self.pac.move(event.key)
        if self.ghost:
            self.ghost.move(event.key)
            
    def leftKey(event):
        left(Pacman)
        
    def rightKey(event):
        right(Pacman)
        
    def upKey(event):
        up(Pacman)
        
    def downKey(event):
        down(Pacman)
        
    
    def leftKey(event):
        left(Ghost)
        
    def rightKey(event):
        right(Ghost)
        
    def upKey(event):
        up(Ghost)
        
    def downKey(event):
        down(Ghost)

    def step(self):
        self.pac.x += self.pac.xdirection
        self.pac.y += self.pac.ydirection
        self.ghost.x += self.ghost.xdirection
        self.ghost.y += self.ghost.ydirection
        
        if self.pac.x > myapp.width:
            self.pac.xdirection *= -1
        
        """
        if self.pac.x + self.pac.width > myapp.width:
            self.pac.x -= self.pac.xdirection
            left(Pacman)
        if self.pac.x < 0:
            right(Pacman)
        
        self.pac.y += self.pac.ydirection
        if self.pac.y + self.pac.height > myapp.height:
            self.pac.y -= self.pac.ydirection
            down(Pacman)
        if self.pac.y < 0:
            up(Pacman)
            
        self.ghost.x += self.ghost.xdirection
        if self.ghost.x + self.ghost.width > myapp.width:
            self.ghost.x -= self.ghost.xdirection
            left(Ghost)
        if self.ghost.x < 0:
            right(Ghost)
        
        self.ghost.y += self.ghost.ydirection
        if self.ghost.y + self.ghost.height > myapp.height:
            self.ghost.y -= self.ghost.ydirection
            down(Ghost)
        if self.ghost.y < 0:
            up(Ghost)
        """

app = Twoplayer()
app.run()