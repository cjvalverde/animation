from graphics import *
import random
from math import *


class Fish:
    """Definition for a fish with a body, eye, tail, and fins"""

    def __init__(self, win, position):
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
        p1 = Point(position.getX() + 30, position.getY() - 30)
        p2 = Point(position.getX() + 50, position.getY() + 30)
        self.tail = Oval(p1, p2)
        self.tail.setFill("black")

        # eye
        center2 = Point(position.getX() - 15, position.getY() - 5)
        self.eye = Circle(center2, 5)
        self.eye.setFill("black")

        # fin_top
        p1 = Point(position.getX() - 10, position.getY() - 20)
        p2 = Point(position.getX() + 20, position.getY() - 30)
        p3 = Point(position.getX() + 10, position.getY() - 20)
        poly_points = [p1, p2, p3]
        self.fin_top = Polygon(poly_points)
        self.fin_top.setFill("black")

        # fin_bot
        p1 = Point(position.getX() - 10, position.getY() + 20)
        p2 = Point(position.getX() + 20, position.getY() + 30)
        p3 = Point(position.getX() + 10, position.getY() + 20)
        poly_points = [p1, p2, p3]
        self.fin_bot = Polygon(poly_points)
        self.fin_bot.setFill("black")

    def draw(self, win):
        """draw the fish to the window"""
        self.body.draw(win)
        self.tail.draw(win)
        self.eye.draw(win)
        self.fin_top.draw(win)
        self.fin_bot.draw(win)

    def move(self, dx):
        """move the fish by dx"""
        self.alpha += 10
        if self.alpha > 360:
            self.alpha = self.alpha - 360
        dy = 10 * (sin(self.alpha * 3.14 / 180) - sin((self.alpha - 10) * 3.14 / 180))
        self.body.move(dx, dy)
        self.tail.move(dx, dy)
        self.eye.move(dx, dy)
        self.fin_top.move(dx, dy)
        self.fin_bot.move(dx, dy)

    alpha = 0
