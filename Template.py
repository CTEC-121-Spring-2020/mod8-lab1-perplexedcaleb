"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from graphics import *
from dog import Dog
from msdie import MSDie
from docTest import DocTest
def main():
    # section 1
    '''
    win = GraphWin("demo", 1000, 1000)
    myCircle = Circle(Point(500,500), 200)
    myCircle.setFill("green")
    myCircle.draw(win)
    win.getMouse()
    '''
    # section 2
    '''
    d = Dog("Dog")
    print(d)
    print(d.getName())
    d.setName("Godzilla")
    print(d.getName())

    d.bark()
    '''
    '''
    # section 3
    die = MSDie(6)
    print("number of sides", die.getSides())
    print("value:", die.getValue())
    die.setValue(5)
    print("value:", die.getValue())
    die.roll()
    print("value:", die.getValue())
    die.roll()
    print("value:", die.getValue())
    '''
    print()
    # print module
    print()
    print(DocTest.__doc__)

    

main()    