from ggame import App, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineStyle, Color
import random

myapp = App()

# add different modes (practice mode, no moving obs mode, moving obs mode), user can choose number of obs
# add powerups for player 1
black = Color(0, 1)
yellow = Color(0xffff00, 1)
blue = Color(0x6495ed, 1)
white = Color(0xfffff0, 1)
red = Color(0xff0000, 0.5)
purple = Color(0x800080, 0.5)
green = Color(0x00ff00, 0.5)
gray = Color(0x888888, 1.0)
noline = LineStyle(0, black)

# define colors and line style
black = Color(0, 1)
noline = LineStyle(0, black)
# a rectangle asset and sprite to use as background
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, white)
bg = Sprite(bg_asset, (0,0))

living = {'Pacman':1}

#wall sprite
class Wall(Sprite):
    rect = RectangleAsset(100, 100, noline, black)
    
    def __init__(self, position):
        super().__init__(Wall.rect, position)
# player 1 sprite
class Pacman(Sprite):
    def __init__(self, x, y, color, app):
        super().__init__(EllipseAsset(12, 12, LineStyle(0,Color(0, 1.0)), color), (x, y))
        self.xdirection = 0
        self.ydirection = 0
        self.go = True
            
    def move(self, key):
        if key == "a":
            self.ydirection = 0
            self.xdirection = -3

        elif key == "d":
            self.ydirection = 0
            self.xdirection = 3
                
        elif key == "w":
            self.xdirection = 0
            self.ydirection = -3
            
        elif key == "s":
            self.xdirection = 0
            self.ydirection = 3
# player 2 sprite
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
            self.xdirection = -3.5

        elif key == "right arrow":
            self.ydirection = 0
            self.xdirection = 3.5
                
        elif key == "up arrow":
            self.xdirection = 0
            self.ydirection = -3.5
            
        elif key == "down arrow":
            self.xdirection = 0
            self.ydirection = 3.5
            
    def step(self):
        collides = self.collidingWithSprites(Pacman)
        if len(collides):
            collides[0].destroy()
            self.pacisalive = False
            living['Pacman'] = living['Pacman'] - 1
            if living['Pacman'] == 0:
                self.stopscore = True
                print("""
Player 2 Wins""")

# base for other enemy "ghosts" sprites
class Obstacle(Sprite):
    def __init__(self, x, y, color, app):
        super().__init__(RectangleAsset(50, 50, LineStyle(0,Color(0, 1.0)), color), (x,y))
        self.xdirection = -5
        self.ydirection = 0
        self.go = True
        
    def step(self):
        collides = self.collidingWithSprites(Pacman)
        if len(collides):
            collides[0].destroy()
            self.pacisalive = False
            living['Pacman'] = living['Pacman'] - 1
            if living['Pacman'] == 0:
                self.stopscore = True
                print("""
Player 2 Wins""")
        collides2 = self.collidingWithSprites(Ghost)
        if len(collides2):
            collides2[0].destroy()
            self.pacisalive = False
            living['Pacman'] = living['Pacman'] - 1
            if living['Pacman'] == 0:
                self.stopscore = True
                print("""
Player 1 Wins""")

class Twoplayer(App):
    def __init__(self):
        super().__init__()
        self.score = 0
            # where all of the sprites spawn
        self.pac = Pacman(110, 110, yellow, self)
        self.ghost = Ghost(870, 415, blue, self)
        self.obs = Obstacle(400, 250, red, self)
        self.obs2 = Obstacle(400, 250, purple, self)
        self.obs3 = Obstacle(400, 250, green, self)
        
        myapp.listenKeyEvent('keydown', 'a', self.moveKey)
        myapp.listenKeyEvent('keydown', 'd', self.moveKey)
        myapp.listenKeyEvent('keydown', 'w', self.moveKey)
        myapp.listenKeyEvent('keydown', 's', self.moveKey)
        myapp.listenKeyEvent('keydown', 'left arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'right arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'up arrow', self.moveKey)
        myapp.listenKeyEvent('keydown', 'down arrow', self.moveKey)

            # spawning wall sprites
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
        if self.ghost.pacisalive == True:    
            self.score += 0.5
            if self.score % 100 == 0 and self.ghost.stopscore == False:
                print(int(self.score))
            if self.score == 2000:
                self.ghost.stopscore = True
                self.ghost.pacisalive = False
                print("""
Player 1 Wins""")

        self.ghost.step()
        self.obs.step()
        
        if self.ghost.pacisalive == True:
            self.pac.x += self.pac.xdirection
            self.pac.y += self.pac.ydirection
            self.ghost.x += self.ghost.xdirection
            self.ghost.y += self.ghost.ydirection

        # for sprites to bounce off of obstacles        
            if self.pac.collidingWithSprites(Wall):
                self.pac.xdirection *= -1
                self.pac.ydirection *= -1
            if self.ghost.collidingWithSprites(Wall):
                self.ghost.xdirection *= -1
                self.ghost.ydirection *= -1
                
        # for pac and ghost to both spawn on other sides of wall if they touch them        
            if self.pac.x < 0:
                self.pac.x = int(myapp.width) - 30
            if self.pac.x > int(myapp.width) - 30:
                self.pac.x = 0
                
            if self.pac.y < 0:
                self.pac.y = int(myapp.height) - 30
            if self.pac.y > int(myapp.height) - 30:
                self.pac.y = 0
                
            if self.ghost.x < 0:
                self.ghost.x = int(myapp.width) - 30
            if self.ghost.x > int(myapp.width) - 30:
                self.ghost.x = 0
                
            if self.ghost.y < 0:
                self.ghost.y = int(myapp.height) - 30
            if self.ghost.y > int(myapp.height) - 30:
                self.ghost.y = 0
                
        # for first obstacle to bounce off walls        
            if self.obs.x < 0:
                self.obs.xdirection *= -1
            if self.obs.x > int(myapp.width) - 50:
                self.obs.xdirection *= -1
                
            if self.obs.y < 0:
                self.obs.ydirection *= -1
            if self.obs.y > int(myapp.height) - 50:
                self.obs.ydirection *= -1
                
        # for second obstacle to bounce off walls       
            if self.obs2.x < 0:
                self.obs2.xdirection *= -1
            if self.obs2.x > int(myapp.width) - 50:
                self.obs2.xdirection *= -1
                
            if self.obs2.y < 0:
                self.obs2.ydirection *= -1
            if self.obs2.y > int(myapp.height) - 50:
                self.obs2.ydirection *= -1
                
        # for third obstacle to bounce off walls       
            if self.obs3.x < 0:
                self.obs3.xdirection *= -1
            if self.obs3.x > int(myapp.width) - 50:
                self.obs3.xdirection *= -1
                
            if self.obs3.y < 0:
                self.obs3.ydirection *= -1
            if self.obs3.y > int(myapp.height) - 50:
                self.obs3.ydirection *= -1
                
        # for the first random obstacle
        if self.ghost.pacisalive == True:
            self.obs.x += self.obs.xdirection
            self.obs.y += self.obs.ydirection
            if self.obs.y == 100 or self.obs.y == 250 or self.obs.y == 400:
                    # i could make this a range for asthetic purposes
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
                        
        if self.ghost.pacisalive == True:
            collides2 = self.obs.collidingWithSprites(Pacman)
            if len(collides2):
                collides2[0].destroy()
                self.ghost.pacisalive = False
                living['Pacman'] = living['Pacman'] - 1
                if living['Pacman'] == 0:
                    self.stopscore = True
                    print("""
Player 2 Wins""")
            collides3 = self.obs.collidingWithSprites(Ghost)
            if len(collides3):
                collides3[0].destroy()
                self.ghost.pacisalive = False
                living['Pacman'] = living['Pacman'] - 1
                if living['Pacman'] == 0:
                    self.stopscore = True
                    print("""
Player 1 Wins""")

        # for the second random obstacle
        if self.ghost.pacisalive == True:
            self.obs2.x += self.obs2.xdirection
            self.obs2.y += self.obs2.ydirection
            if self.obs2.y == 100 or self.obs2.y == 250 or self.obs2.y == 400:
                if self.obs2.x == 100 or self.obs2.x == 250 or self.obs2.x == 400 or self.obs2.x == 550 or self.obs2.x == 700 or self.obs2.x == 850:
                    secondnumber = int(random.randint(1, 4))
                    if secondnumber == 1:
                        self.obs2.xdirection = 0
                        self.obs2.ydirection = 5
                    elif secondnumber == 2:
                        self.obs2.xdirection = 0
                        self.obs2.ydirection = -5
                    elif secondnumber == 3:
                        self.obs2.xdirection = -5
                        self.obs2.ydirection = 0
                    elif secondnumber == 4:
                        self.obs2.xdirection = 5
                        self.obs2.ydirection = 0
                        
        if self.ghost.pacisalive == True:
            collides4 = self.obs2.collidingWithSprites(Pacman)
            if len(collides4):
                collides4[0].destroy()
                self.ghost.pacisalive = False
                living['Pacman'] = living['Pacman'] - 1
                if living['Pacman'] == 0:
                    self.stopscore = True
                    print("""
Player 2 Wins""")
            collides5 = self.obs2.collidingWithSprites(Ghost)
            if len(collides5):
                collides5[0].destroy()
                self.ghost.pacisalive = False
                living['Pacman'] = living['Pacman'] - 1
                if living['Pacman'] == 0:
                    self.stopscore = True
                    print("""
Player 1 Wins""")
        
        # for third random obstacle
        if self.ghost.pacisalive == True:
            self.obs3.x += self.obs3.xdirection
            self.obs3.y += self.obs3.ydirection
            if self.obs3.y == 100 or self.obs3.y == 250 or self.obs3.y == 400:
                if self.obs3.x == 100 or self.obs3.x == 250 or self.obs3.x == 400 or self.obs3.x == 550 or self.obs3.x == 700 or self.obs3.x == 850:
                    thirdnumber = int(random.randint(1, 4))
                    if thirdnumber == 1:
                        self.obs3.xdirection = 0
                        self.obs3.ydirection = 5
                    elif thirdnumber == 2:
                        self.obs3.xdirection = 0
                        self.obs3.ydirection = -5
                    elif thirdnumber == 3:
                        self.obs3.xdirection = -5
                        self.obs3.ydirection = 0
                    elif thirdnumber == 4:
                        self.obs3.xdirection = 5
                        self.obs3.ydirection = 0
                        
        if self.ghost.pacisalive == True:
            collides6 = self.obs3.collidingWithSprites(Pacman)
            if len(collides6):
                collides6[0].destroy()
                self.ghost.pacisalive = False
                living['Pacman'] = living['Pacman'] - 1
                if living['Pacman'] == 0:
                    self.stopscore = True
                    print("""
Player 2 Wins""")
            collides7 = self.obs3.collidingWithSprites(Ghost)
            if len(collides7):
                collides7[0].destroy()
                self.ghost.pacisalive = False
                living['Pacman'] = living['Pacman'] - 1
                if living['Pacman'] == 0:
                    self.stopscore = True
                    print("""
Player 1 Wins""")
                        
print("To Control Player 1 (yellow): WASD")
print("To Control Player 2 (blue): Arrow Keys")
print("""Player 1 must collect 2000 points to win. Player 2 must destroy Player 1 to win.
Don't run into the colored squares.""")
print("""
Player 1 Score: """)
        
app = Twoplayer()
app.run()
