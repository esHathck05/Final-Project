from ggame import App, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineStyle, Color
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

living = {'Pacman':1}

class Wall(Sprite):
    rect = RectangleAsset(100, 100, noline, black)
    
    def __init__(self, position):
        super().__init__(Wall.rect, position)

class Pacman(Sprite):
    def __init__(self, x, y, color, app):
        super().__init__(EllipseAsset(12, 12, LineStyle(0,Color(0, 1.0)), color), (x, y))
        self.xdirection = 0
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

class Ghost(Sprite):
    def __init__(self, x, y, color, app):
        super().__init__(EllipseAsset(12, 12, LineStyle(0,Color(0, 1.0)), color), (x,y))
        self.xdirection = 0
        self.ydirection = 0
        self.go = True
        self.pacisalive = True
        self.stopscore = False
            
    def move(self, key):
        if key == "left arrow":
            self.ydirection = 0
            self.xdirection = -4.25

        elif key == "right arrow":
            self.ydirection = 0
            self.xdirection = 4.25
                
        elif key == "up arrow":
            self.xdirection = 0
            self.ydirection = -4.25
            
        elif key == "down arrow":
            self.xdirection = 0
            self.ydirection = 4.25
            
    def step(self):
        collides = self.collidingWithSprites(Pacman)
        if len(collides):
            collides[0].destroy()
            self.pacisalive = False
            living['Pacman'] = living['Pacman'] - 1
            if living['Pacman'] == 0:
                self.stopscore = True
                print("""
Player 2 Wins!""")

class Obstacle(Sprite):
    def __init__(self, x, y, color, app):
        super().__init__(RectangleAsset(50, 50, LineStyle(0,Color(0, 1.0)), color), (x,y))
        self.xdirection = -5
        self.ydirection = 0
        self.go = True

class Twoplayer(App):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pac = Pacman(110, 110, yellow, self)
        self.ghost = Ghost(int(myapp.width) - 157, int(myapp.height) - 150, blue, self)
        self.obs = Obstacle(int(myapp.width)/2 - 8.5, int(myapp.height)/2 - 29.5, black, self)
        myapp.listenKeyEvent('keydown', 'a', self.moveKey)
        myapp.listenKeyEvent('keydown', 'd', self.moveKey)
        myapp.listenKeyEvent('keydown', 'w', self.moveKey)
        myapp.listenKeyEvent('keydown', 's', self.moveKey)
        myapp.listenKeyEvent('keydown', 'left arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'right arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'up arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'down arrow', self.moveKey)

        for x in range(0, 1000, 150):
            Wall((0, x))
        for x in range(0, 1000, 150):
            Wall((150, x))
        for x in range(0, 1000, 150):
            Wall((300, x))
        for x in range(0, 1000, 150):
            Wall((450, x))
        for x in range(0, 1000, 150):
            Wall((600, x))            
        for x in range(0, 1000, 150):
            Wall((750, x))
        for x in range(0, 1000, 150):
            Wall((900, x))            
            
    def moveKey(self, event):
        if self.pac:
            self.pac.move(event.key)
        if self.ghost:
            self.ghost.move(event.key)
            
    def leftKey(event):
        left(Ghost)
        
    def rightKey(event):
        right(Ghost)
        
    def upKey(event):
        up(Ghost)
        
    def downKey(event):
        down(Ghost)
        
    
    def leftKey(event):
        left(Pacman)
        
    def rightKey(event):
        right(Pacman)
        
    def upKey(event):
        up(Pacman)
        
    def downKey(event):
        down(Pacman)
        
    def step(self):
        self.score += 1
        if self.score % 100 == 0 and self.ghost.stopscore == False:
            print(int(self.score))
        if self.score == 2000:
            self.ghost.stopscore = True
            self.ghost.pacisalive = False
            print("""
Player 1 Wins!""")

        self.ghost.step()
        
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
                
            if self.pac.x < 0:
                self.pac.x = int(myapp.width) - 30
                self.pac.xdirection *= -1
            if self.pac.x > int(myapp.width) - 30:
                self.pac.x = 0
                
            if self.pac.y < 0:
                self.pac.y = int(myapp.height) - 30
                self.pac.ydirection *= -1
            if self.pac.y > int(myapp.height) - 30:
                self.pac.y = 0
                
            if self.ghost.x < 0:
                self.ghost.x = int(myapp.width) - 30
                self.ghost.xdirection *= -1
            if self.ghost.x > int(myapp.width) - 30:
                self.ghost.x = 0
                
            if self.ghost.y < 0:
                self.ghost.y = int(myapp.height) - 30
                self.ghost.ydirection *= -1
            if self.ghost.y > int(myapp.height) - 30:
                self.ghost.y = 0
                
            if self.obs.x < 0:
                self.obs.xdirection *= -1
            if self.obs.x > int(myapp.width) - 50:
                self.obs.xdirection *= -1
                
            if self.obs.y < 0:
                self.obs.ydirection *= -1
            if self.obs.y > int(myapp.height) - 50:
                self.obs.ydirection *= -1
        
        if self.ghost.pacisalive == True:
            self.obs.x += self.obs.xdirection
            self.obs.y += self.obs.ydirection
            if self.obs.y == int(myapp.height)/2 - 179.5 or self.obs.y == int(myapp.height)/2 - 29.5 or self.obs.y == int(myapp.height)/2 + 120.5:
                if self.obs.x == 100 or self.obs.x == 250 or self.obs.x == 400 or self.obs.x == 550 or self.obs.x == 700 or self.obs.x == 850:
                    firstnumber = int(random.randint(1, 4))
                    if firstnumber == 1:
                        self.obs.xdirection = 0
                        self.obs.ydirection = 5
                    elif firstnumber == 2:
                        self.obs.xdirection = 0
                        self.obs.ydirection = -5
                    elif firstnumber == 3:
                        self.obs.xdirection = -5
                        self.obs.ydirection = 0
                    elif firstnumber == 4:
                        self.obs.xdirection = 5
                        self.obs.ydirection = 0
                        
print("To Control Player 1 (yellow): WASD")
print("To Control Player 2 (blue): Arrow Keys")
print("Player 1 must collect 2000 points to win. Player 2 must destroy Player 1 to win.")
print("""
Player 1 Score: """)
        
app = Twoplayer()
app.run()