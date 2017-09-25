# How do objects communicate with each other?
# Directly or through main.py?
# Is calling a method from another object or another class object
# good programming?


class Letter():
    def __init__(self,name):
        self.name=name

    def describe_all(self):
        dummy = number.dummy() # calling a method from another class object
        print(self.name)
        print(dummy)


class Number():
    def __init__(self,name):
        self.name = name

    def dummy(self):
        return self.name

a= Letter("A")
number= Number (1)
a.describe_all()

        
