# This is a simple example of a class in python
# This is also an example of object oriented programming

class Rectangle:
    # First I am defining the parameters withe the __init__ function
    def __init__(self, length, breath):
        self.length = int(length)
        self.breath = int(breath)

    # Here is a function you can run to print the area of a defined rectangle
    def area(self):
        area = self.length * self.breath
        print(area)

    # Here is a function you can run to print the perimeter of a defined rectangle
    def perimetre(self):
        peri = 2 * (self.length + self.breath)
        print(peri)

# These lines set a variable to an object with specific parameters
rectOne = Rectangle(10, 10)
rectTwo = Rectangle(5, 5)

# These lines are calling the functions I mentioned above
rectOne.area()
rectTwo.perimetre()
