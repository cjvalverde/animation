from graphics import *
import random
from math import *


class Fish:
    """Definition for a fish with a body, eye, tail, and fins"""

    def __init__(self, win, position, direction):
        """constructs a fish made of 1 oval centered at `position`,
    a second oval for the tail, and a circle for the eye"""

        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        # body
        p1 = Point(position.getX() - 40, position.getY() - 20)
        p2 = Point(position.getX() + 40, position.getY() + 20)
        self.body = Oval(p1, p2)
        self.body.setFill(color_rgb(red, green, blue))

        # tail
        if direction == 0:
            p1 = Point(position.getX() - 30, position.getY() - 30)
            p2 = Point(position.getX() - 50, position.getY() + 30)
        else:
            p1 = Point(position.getX() + 50, position.getY() - 30)
            p2 = Point(position.getX() + 30, position.getY() + 30)
        self.tail = Oval(p1, p2)
        self.tail.setFill("black")

        # eye
        if direction == 0:
            center2 = Point(position.getX() + 15, position.getY() - 5)
        else:
            center2 = Point(position.getX() - 15, position.getY() - 5)
        self.eye = Circle(center2, 5)
        self.eye.setFill("black")

        # fin_top
        if direction == 0:
            p1 = Point(position.getX() + 10, position.getY() - 20)
            p2 = Point(position.getX() - 20, position.getY() - 30)
            p3 = Point(position.getX() - 10, position.getY() - 20)
        else:
            p1 = Point(position.getX() - 10, position.getY() - 20)
            p2 = Point(position.getX() + 20, position.getY() - 30)
            p3 = Point(position.getX() + 10, position.getY() - 20)
        poly_points = [p1, p2, p3]
        self.fin_top = Polygon(poly_points)
        self.fin_top.setFill("black")

        # fin_bot
        if direction == 0:
            p1 = Point(position.getX() + 10, position.getY() + 20)
            p2 = Point(position.getX() - 20, position.getY() + 30)
            p3 = Point(position.getX() - 10, position.getY() + 20)
        else:
            p1 = Point(position.getX() - 10, position.getY() + 20)
            p2 = Point(position.getX() + 20, position.getY() + 30)
            p3 = Point(position.getX() + 10, position.getY() + 20)
        poly_points = [p1, p2, p3]
        self.fin_bot = Polygon(poly_points)
        self.fin_bot.setFill("black")

        self.direction = direction

    def draw(self, win):
        """draw the fish to the window"""
        self.body.draw(win)
        self.tail.draw(win)
        self.eye.draw(win)
        self.fin_top.draw(win)
        self.fin_bot.draw(win)
    
    def move( self , dx, dy):
        """move the fish by dx and dy + an autonomus waving movement on axis y"""
        self.alpha += 10
        if self.alpha > 360:
            self.alpha = self.alpha -360
        dyi = dy + 10 * (sin(self.alpha * 3.14 / 180) - sin((self.alpha -10) * 3.14 / 180))
        if self.direction == 0:
            dxi = dx
        else:
            dxi = - dx
        self.body.move( dxi, dyi )
        self.tail.move( dxi, dyi )
        self.eye.move( dxi, dyi )
        self.fin_top.move( dxi, dyi )
        self.fin_bot.move( dxi, dyi )
    
    def getCenter(self):
        return self.body.getCenter()
    
    def setEating(self, eating):
        self.eating = eating
    
    def toggleDirection(self):
        if self.direction == 0:
            self.direction = 1
            self.tail.move( 80, 0)
            self.eye.move( -30, 0 )
            self.fin_top.undraw()
            p1 = Point(self.body.getCenter().getX() - 10, self.body.getCenter().getY() - 20)
            p2 = Point(self.body.getCenter().getX() + 20, self.body.getCenter().getY() - 30)
            p3 = Point(self.body.getCenter().getX() + 10, self.body.getCenter().getY() - 20)
            self.fin_top = Polygon([p1, p2, p3])
            self.fin_top.setFill("black")
            self.fin_bot.undraw()
            p1 = Point(self.body.getCenter().getX() - 10, self.body.getCenter().getY() + 20)
            p2 = Point(self.body.getCenter().getX() + 20, self.body.getCenter().getY() + 30)
            p3 = Point(self.body.getCenter().getX() + 10, self.body.getCenter().getY() + 20)
            self.fin_bot = Polygon([p1, p2, p3])
            self.fin_bot.setFill("black")
        else:
            self.direction = 0
            self.tail.move( -80, 0)
            self.eye.move( 30, 0 )
            self.fin_top.undraw()
            p1 = Point(self.body.getCenter().getX() + 10, self.body.getCenter().getY() - 20)
            p2 = Point(self.body.getCenter().getX() - 20, self.body.getCenter().getY() - 30)
            p3 = Point(self.body.getCenter().getX() - 10, self.body.getCenter().getY() - 20)
            self.fin_top = Polygon([p1, p2, p3])
            self.fin_top.setFill("black")
            self.fin_bot.undraw()
            p1 = Point(self.body.getCenter().getX() + 10, self.body.getCenter().getY() + 20)
            p2 = Point(self.body.getCenter().getX() - 20, self.body.getCenter().getY() + 30)
            p3 = Point(self.body.getCenter().getX() - 10, self.body.getCenter().getY() + 20)
            self.fin_bot = Polygon([p1, p2, p3])
            self.fin_bot.setFill("black")
        
    
    alpha = 0
    direction = 0
    eating = False
