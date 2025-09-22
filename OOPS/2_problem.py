import math

class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The Square is: {self.n*self.n}")

    def cube(self):
        print(f"The cube is: {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The Square Root: {math.sqrt(self.n)}")

a=int(input("Enter number: "))

n=calculator(a)
n.square()
n.cube()
n.squareroot()       