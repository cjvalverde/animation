# challenge Final
from fish import *
from bubble import *

def main():
    win = GraphWin("Canvas", 600, 400)
    clickedPoint = win.getMouse()
    fish1 = Fish(win, clickedPoint)
    fish1.draw(win)
    clickedPoint = win.getMouse()
    fish2 = Fish(win, clickedPoint)
    fish2.draw(win)
    clickedPoint = win.getMouse()
    fish3 = Fish(win, clickedPoint)
    fish3.draw(win)
    print(random.randint(0, 600))
    bubble1 = Bubble(win, random.randint(0, 600), random.randint(2, 4))
    bubble1.draw(win)
    bubble2 = Bubble(win, random.randint(0, 600), random.randint(2, 4))
    bubble2.draw(win)
    bubble3 = Bubble(win, random.randint(0, 600), random.randint(2, 4))
    bubble3.draw(win)
    bubble4 = Bubble(win, random.randint(0, 600), random.randint(2, 4))
    bubble4.draw(win)
    bubble5 = Bubble(win, random.randint(0, 600), random.randint(2, 4))
    bubble5.draw(win)
    win.getMouse() # Start moving on click
    #
    isMoving = True
    # 4. Start animation loop
    while win.checkKey() != "q":
      if win.checkMouse() != None:
        isMoving = not isMoving
      if (isMoving):
        fish1.move(-2)
        fish2.move(-1)
        fish3.move(-2)
        bubble1.move()
        bubble2.move()
        bubble3.move()
        bubble4.move()
        bubble5.move()
    win.close() # Close window when done
main()
