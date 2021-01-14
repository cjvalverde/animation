# challenge Final
from fish import *
from bubble import *
from food import *

def main():
    win = GraphWin("Canvas", 600, 400)
    win.setBackground("deepskyblue")
    #
    # Decorations
    # Ground
    ground = Polygon([Point(0,400), Point(0,370), Point(600,370), Point(600,400)])
    ground.setFill("brown")
    ground.draw(win)
    # Castle
    castle = Polygon([Point(50,370), Point(50,220), Point(80,220), Point(80,250), Point(110,250), Point(110,220), Point(140,220), Point(140,250), Point(170,250), Point(170,220), Point(200,220), Point(200,250), Point(230,250), Point(230,220), Point(260,220), Point(260,370)])
    castle.setFill("grey")
    castle.draw(win)
    # Plant# Ground
    plant = Polygon([Point(450,370), Point(450,320), Point(420,320), Point(420,290), Point(435,290), Point(435,305), Point(450,305), Point(450,260), Point(465,260), Point(465,305), Point(480,305), Point(480,275), Point(495,275), Point(495,320), Point(465,320), Point(465,370)])
    plant.setFill("green")
    plant.draw(win)

    # End of decorations
    #
    clickedPoint = win.getMouse()
    fish1 = Fish(win, clickedPoint, random.randint(0,1))
    fish1.draw(win)
    clickedPoint = win.getMouse()
    fish2 = Fish(win, clickedPoint, random.randint(0,1))
    fish2.draw(win)
    clickedPoint = win.getMouse()
    fish3 = Fish(win, clickedPoint, random.randint(0,1))
    fish3.draw(win)
    bubble1 = Bubble(win, random.randint(0, 120), random.randint(2, 4))
    bubble1.draw(win)
    bubble2 = Bubble(win, random.randint(120, 240), random.randint(2, 4))
    bubble2.draw(win)
    bubble3 = Bubble(win, random.randint(240, 360), random.randint(2, 4))
    bubble3.draw(win)
    bubble4 = Bubble(win, random.randint(360, 480), random.randint(2, 4))
    bubble4.draw(win)
    bubble5 = Bubble(win, random.randint(480, 600), random.randint(2, 4))
    bubble5.draw(win)
    win.getMouse() # Start moving on click
    #
    isMoving = True
    food_there = False
    dfx = 0
    dfy = 0
    # 4. Start animation loop
    while win.checkKey() != "q":
#      if win.checkMouse() != None:
#          isMoving = not isMoving
      if (isMoving):
          if fish1.eating:
              fish1.move(dfx, dfy)
              if (abs(fish1.getCenter().getX() - food.getCenter().getX()) < 20) or (abs(fish1.getCenter().getY() - food.getCenter().getY()) < 20):
                  food.undraw()
                  fish1.setEating(False)
          else:
              fish1.move(2, 0)
          if fish2.eating:
              fish2.move(dfx, dfy)
              if (abs(fish2.getCenter().getX() - food.getCenter().getX()) < 20) or (abs(fish2.getCenter().getY() - food.getCenter().getY()) < 20):
                  food.undraw()
                  fish2.setEating(False)
          else:
              fish2.move(1, 0)
          if fish3.eating:
              fish3.move(dfx, dfy)
              if (abs(fish3.getCenter().getX() - food.getCenter().getX()) < 20) or (abs(fish3.getCenter().getY() - food.getCenter().getY()) < 20):
                  food.undraw()
                  fish3.setEating(False)
          else:
              fish3.move(2, 0)
          #
          # control to toggle direction of fish if hits border
          if (fish1.getCenter().getX() <= 40 and fish1.direction == 1) or (fish1.getCenter().getX() >= 560 and fish1.direction == 0):
              fish1.toggleDirection()
          if (fish2.getCenter().getX() <= 40 and fish2.direction == 1) or (fish2.getCenter().getX() >= 560 and fish2.direction == 0):
              fish2.toggleDirection()
          if (fish3.getCenter().getX() <= 40 and fish3.direction == 1) or (fish3.getCenter().getX() >= 560 and fish3.direction == 0):
              fish3.toggleDirection()
          #
          bubble1.move()
          bubble2.move()
          bubble3.move()
          bubble4.move()
          bubble5.move()
      if win.checkKey() == "f":
          if food_there == False:
              food = Food(win, Point(random.randint(20, 580), random.randint(20, 380)))
              food.draw(win)
              food_there == True
              distance1 = (int((food.getCenter().getX() - fish1.getCenter().getX())))**2 + (int(food.getCenter().getY() - fish1.getCenter().getY()))**2
              distance2 = (int(food.getCenter().getX() - fish2.getCenter().getX()))**2 + (int(food.getCenter().getY() - fish2.getCenter().getY()))**2
              distance3 = (int(food.getCenter().getX() - fish3.getCenter().getX()))**2 + (int(food.getCenter().getY() - fish3.getCenter().getY()))**2
              if distance1 < distance2 and distance1 < distance3:
                  fish1.setEating(True)
                  dfx = food.getCenter().getX() - fish1.getCenter().getX()
                  if ((dfx < 0) and (fish1.direction == 0)) or ((dfx > 0) and (fish1.direction == 1)):
                      fish1.toggleDirection()
                  dfx = abs(dfx)
                  dfy = food.getCenter().getY() - fish1.getCenter().getY()
              elif distance2 < distance1 and distance2 < distance3:
                  fish2.setEating(True)
                  dfx = food.getCenter().getX() - fish2.getCenter().getX()
                  if ((dfx < 0) and (fish2.direction == 0)) or ((dfx > 0) and (fish2.direction == 1)):
                      fish2.toggleDirection()
                  dfx = abs(dfx)
                  dfy = food.getCenter().getY() - fish2.getCenter().getY()
              elif distance3 < distance1 and distance3 < distance2:
                  fish3.setEating(True)
                  dfx = food.getCenter().getX() - fish3.getCenter().getX()
                  if ((dfx < 0) and (fish3.direction == 0)) or ((dfx > 0) and (fish3.direction == 1)):
                      fish3.toggleDirection()
                  dfx = abs(dfx)
                  dfy = food.getCenter().getY() - fish3.getCenter().getY()
              if abs(dfx) <= abs(dfy):
                  shorter = dfx
              else:
                  shorter = dfy
              if(dfy <= 0):    # go up
                  dfx = abs(int(dfx/shorter))
                  dfy = -abs(int(dfy/shorter))
              else:
                  dfx = abs(int(dfx/shorter))
                  dfy = abs(int(dfy/shorter))
    win.close() # Close window when done
main()
