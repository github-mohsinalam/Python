#Add a method called move that will take two parameters, call them dx and dy.
#The method will cause the point to move in the x and y direction the number of units given.
#(Hint: you will change the values of the state of the point)




class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    # Put your new method here
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


    def __str__(self):
        return str(self.x)+","+str(self.y)


p = Point(7,6)
print(p)
p.move(5,10)
print(p)
