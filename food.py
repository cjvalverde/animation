from graphics import *


class Food:
    """Definition for a piece of fish food as an orange square"""

    def __init__(self, win, position):
        """constructs a piece of food as a orange square"""
        # square
        self.food = Rectangle(Point(position.getX() - 10, position.getY() - 10), Point(position.getX() + 10, position.getY() + 10))
        self.food.setFill("orange")

    def draw(self, win):
        """draw the fish to the window"""
        self.food.draw(win)
    
    def undraw(self):
        self.food.undraw()

    def getCenter(self):
        return self.food.getCenter()
    
