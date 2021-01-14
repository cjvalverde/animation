from graphics import *
import random
from math import *


class Bubble:
    """Definition for a bubble as a white circle"""

    def __init__(self, win, x_position, speed):
        """constructs a bubble as a white circle"""

        # bubble
        center1 = Point(x_position, 400)
        self.bubble = Circle(center1, 7)
        self.bubble.setFill("azure")
        if x_position > 360:
            self.alpha = x_position - 360
        else:
            self.alpha = x_position
        self.speed = speed

    def draw(self, win):
        """draw the fish to the window"""
        self.bubble.draw(win)

    def move(self):
        """move the fish by dx"""
        self.alpha += 10
        if self.alpha > 360:
            self.alpha = self.alpha - 360
        dx = 10 * (sin(self.alpha * 3.14 / 180) - sin((self.alpha - 10) * 3.14 / 180))
        self.y -= self.speed
        if self.y < 4:
            self.bubble.move(random.randint(-20, 20), 400 - self.y)
            self.y = 400
        self.bubble.move(dx, - self.speed)

    alpha = 0
    speed = 3
    y = 400
