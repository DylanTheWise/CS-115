from math import *
from graphics import *
# Dylan Wise
# Section 001
# 10/6/13
# Write the definition of a function called distance
#  with the parameters of 2 points
# which returns the distance between the two points
#  you may NOT use the distance method which exists
def distance (pt1, pt2):
        a = pt1.getX()      #Define each of the x and y's as variables
        b = pt2.getX()
        c = pt1.getY()
        d = pt2.getY()
        return sqrt(((b - a)**2)+((d - c)**2))  #Use variables above in distance formula
#  fill out the body

def main():
        win = GraphWin("Heron's Formula",500, 500)
        win.setCoords (0,0, 499, 499)
        t = Text(Point(250,480),"Click 3 points")
        t.draw(win)
        p1 = win.getMouse()
        c1 = Circle(p1, 5)
        c1.setFill("red")
        c1.draw(win)
        p2 = win.getMouse()
        c2 = Circle(p2,5)
        c2.setFill("red")
        c2.draw(win)
        p3 = win.getMouse()
        c3 = Circle(p3,5)
        c3.setFill("red")
        c3.draw(win)
        line1 = Line(p1, p2)
        line1.draw(win)
        line2 = Line(p2, p3)
        line2.draw(win)
        line3 = Line(p1, p3)
        line3.draw(win)

        d1 = distance(p1, p2)
        d2 = distance(p2, p3)
        d3 = distance(p1, p3)
        mystr = "The total perimeter is "+str(d1+d2+d3)
        t2 = Text(Point(250, 20),mystr)
        t2.draw(win)
        Text(Point(250, 100),"click to exit").draw(win)

        win.getMouse()
        win.close()
main()
