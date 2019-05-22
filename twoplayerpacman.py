from ggame import App, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineStyle, Color
import math
import random

myapp = App()

black = Color(0, 1)
yellow = Color(0xffff00, 1)
blue = Color(0x6495ed, 1)
white = Color(0xfffff0, 1.0)
noline = LineStyle(0, black)

# define colors and line style
black = Color(0, 1)
noline = LineStyle(0, black)
# a rectangle asset and sprite to use as background
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, white)
bg = Sprite(bg_asset, (0,0))

gamestart = False

class Wall(Sprite):
    # Create asset
    black = Color(0,1)
    noline = LineStyle(0,black)
    rect = RectangleAsset(95, 100, noline, black)
    
    def __init__(self, position):
        super().__init__(Wall.rect, position)

class Pacman(Sprite):
    def __init__(self, x, y, color, app):
        super().__init__(EllipseAsset(15, 15, LineStyle(0,Color(0, 1.0)), color), (x, y))
        self.xdirection = 0
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
    def __init__(self, x, y, color, app):
        super().__init__(EllipseAsset(15, 15, LineStyle(0,Color(0, 1.0)), color), (x,y))
        self.xdirection = 0
        self.ydirection = 0
        self.go = True
        self.pacisalive = True
            
    def move(self, key):
        if key == "a":
            self.ydirection = 0
            self.xdirection = -4.20

        elif key == "d":
            self.ydirection = 0
            self.xdirection = 4.20
                
        elif key == "w":
            self.xdirection = 0
            self.ydirection = -4.20
            
        elif key == "s":
            self.xdirection = 0
            self.ydirection = 4.20
            
    def step(self):
        collides = self.collidingWithSprites(Pacman)
        if len(collides):
            collides[0].destroy()
            self.pacisalive = False


# Set up event handlers for the app
class Twoplayer(App):
    def __init__(self):
        super().__init__()
        self.pac = Pacman(random.randint(0, myapp.width), random.randint(0, myapp.height), yellow, self)
        self.ghost = Ghost(300, 100, blue, self)
        myapp.listenKeyEvent('keydown', 'left arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'right arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'up arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'down arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'a', self.moveKey)
        myapp.listenKeyEvent('keydown', 'd', self.moveKey)
        myapp.listenKeyEvent('keydown', 'w', self.moveKey)
        myapp.listenKeyEvent('keydown', 's', self.moveKey)
        
        for x in range(0, int(myapp.width/60)):
            Wall((random.randint(30, int(myapp.width - 30) - 100), random.randint(30, int(30) - 100)))
     
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
        self.ghost.step()
        gamestart = True
        
        if self.ghost.pacisalive == True:
            self.pac.x += self.pac.xdirection
            self.pac.y += self.pac.ydirection
            self.ghost.x += self.ghost.xdirection
            self.ghost.y += self.ghost.ydirection
        
            if self.pac.x + self.pac.width > myapp.width or self.pac.x < 0:
                self.pac.xdirection *= -1
        
            if self.pac.y + self.pac.height > myapp.height or self.pac.y < 0:
                self.pac.ydirection *= -1
                
            if self.ghost.x + self.ghost.width > myapp.width or self.ghost.x < 0:
                self.ghost.xdirection *= -1
                
            if self.ghost.y + self.ghost.height > myapp.height or self.ghost.y < 0:
                self.ghost.ydirection *= -1
                
        if self.pac.collidingWithSprites(Wall):
            self.pac.xdirection *= -1
            self.pac.ydirection *= -1
        if self.ghost.collidingWithSprites(Wall):
            self.ghost.xdirection *= -1
            self.ghost.ydirection *= -1
        
        
app = Twoplayer()
app.run()