from ggame import App, Sprite, RectangleAsset, LineStyle, Color
import pygame

# THIS IS HOPEFULLY ALL FOR BUILDING THE MAP
class GenericWall(Sprite):
    def __init__(self, x, y, w, h, color):
        snapfunc = lambda X : X - X % w
        super().__init__(
            RectangleAsset(w-1,h-1,LineStyle(0,Color(0, 1.0)), color),
            (snapfunc(x), snapfunc(y)))
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