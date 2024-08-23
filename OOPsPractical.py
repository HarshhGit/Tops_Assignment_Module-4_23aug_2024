import math
# Q.22] How to Define a Class in Python? What Is Self? Give An Example Of A Python Class
"""Class is a user-defined blueprint for an object. like real world entity has some properties
or behavior which is represented by class variables and methods in programming"""

"""In python "Self"is a reference to the instance of the class.
   Whenever defining a method in class self is mandatory as first parameter this allows the method to
   access the attributes and other methods of the instance it belongs to.
"""

"""class syntax"""

# class ClassName:
#     def hello(self):
#         age = 10
#         print("Q.22 answer: ",age)
#         #methods
    
# obj = ClassName()
# obj.hello()
# --------------------------------------------------------------------------------------------------------------------

"""Q.23] Write a Python class named Rectangle constructed by a length and
width and a method which will compute the area of a rectangle.
"""
# class Rectangle:
#     def __init__(self,length,width):
#         self.len = length
#         self.wid = width
#     def area(self):
#         return self.len * self.wid 

# obj = Rectangle(int(input("Enter length: ")),int(input("Enter width: ")))
# print("Area of rectangle is : ",obj.area())

"""In above code def __init__ is a constructor which will run everytime 
automatic whenever the class Rectangle is called."""
# --------------------------------------------------------------------------------------------------------------------

"""Q.24] Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle """ 

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius ** 2
#     def perimeter(self):
#         return 2 * math.pi * self.radius
# obj2 = Circle(int(input("Enter radius: ")))
# print("Area of Circle is: ",obj2.area())
# print("Perimeter of circle is: ",obj2.perimeter())

"""in above code we have used math inbuilt module to take exact value of pi using math.pi
__init__ is a constructor which will be run after creating an object of that class automatic
"""
# --------------------------------------------------------------------------------------------------------------------
"""Q.25] Explain Inheritance in Python with an example? What is init? Or What
Is A Constructor In Python?"""

"""Inheritance:- When one class inherits some features from another class then it is called Inheritance
   In python Multiple Inheritance is supported.
"""

"""__init__:- init is method known as the constructor.
    it is called automatic when a object of a class is created.
    init initialize the instance's attributes with values provided during object creation.

"""
# class A:
#     def greet(self):
#         print("Hello!!!")

# class B(A):
#     def ask(self):
#         print("How are you doing....?")

# obj = B()
# obj.greet()
# obj.ask()

#in above code class B is accessing properties of class A greet()
"""Using inheritance common functionality can be written once in the base class
    and reused in derived classes.
"""



