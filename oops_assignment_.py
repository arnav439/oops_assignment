# -*- coding: utf-8 -*-
"""oops_assignment .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Pmu3_KHpofqu64vOYPj_TP5nNpfju-0z
"""

# Explain the immportnce of functions.
""" functions plays a very crucial role in programming languages because hey enhances the "readability"
of the code which makes the code more presentable ,also we have some inbuils functions due to which we easily
get the desired result also we can build some functions and store them for future use.
so in conclusion : they saves time,more presentable,enhances readabilty .. """

# 2.) Write a basic function to greet students

def greet(name):
    print(f"hello!!,  welcome to class {name}")

greet("arnav")

#3 What is the difference between print and return statements?
"""PRINT statement is simply used when we want to print something on the screen but RETURN statemnt is used
when we want use the result obtained in the another function we will have to use return (in print
statement we can't use the result obtained in any other function )"""

# What are *args and **kwargs??
""" *args are the variable length argument basically it allows us to put the number of argument we want
**kwargs (keywords arguments) is the argumetns which is used to read the arguments in the form of key value pair
(we should know that args and kwargs is not predefined only * and ** is mandatory)"""

# Explain the iterator function.
'''An iterator in Python is an object that allows you to traverse
through all the elements in a collection (like a list, tuple, or dictionary) one by one'''

#Write a code that generates the squares of numbers from 1 to n using a generator
def square_numbers(n):
    for i in range(1, n+1):
        yield i * i

# Example
n = 5
for square in square_numbers(n):
    print(square)

#Write a code that generates palindromic numbers up to n using a generator
def palindrome_generator(n):
    for num in range(1, n+1):
        if str(num) == str(num)[::-1]:
            yield num

gen =palindrome_generator(90)

next(gen)

#Write a code that generates even numbers from 2 to n using a generator
 def even_numbers_gen(n):
        for i in range(2,n+1):
            if i%2 ==0:
                yield i

gen =even_numbers_gen(10)

next(gen)

# Write a code that generates powers of two up to n using a generator
def powers_of_two(n):
    power = 1
    while power <= n:
        yield power
        power *= 2

gen=powers_of_two(100)

next(gen)

#Write a code that generates prime numbers up to n using a generator
def prime_no(n):
    for i in range(n):
        if (n%i==0)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    for num in range(2, n + 1):
        if is_prime(num):
            yield num

# Example
n = 30
for prime in prime_numbers(n):
    print(prime)

#Write a code that uses a lambda function to calculate the sum of two numbers
sum_of_two = lambda a,b : a+b

sum_of_two(2,3)

#Write a code that uses a lambda function to calculate the square of a given number
square = lambda a : a**2
square(4)

# Write a code that uses a lambda function to check whether a given number is even or odd
even_odd = lambda a : "even" if a%2==0 else "odd"

even_odd(389)

#Write a code that uses a lambda function to concatenate two strings
concat = lambda a,b : a+b
concat("ar","nav")

m = lambda a,b,c : max(a,b,c)

m(23,54,43)

#Write a code that generates the squares of even numbers from a given list.
l= [2,4,34,5,7,3,76]
even_sq =[]
for i in l:
    if (i%2 ==0):
        n=i*i
        even_sq.append(n)

even_sq

#Write a code that calculates the product of positive numbers from a given list
l= [2,3,-5,3,-6,-50,5,]
product =1
for i in l:
        if (i>0):
            product =i*product
print(product)

#Write a code that doubles the values of odd numbers from a given list.
l = [2,1,4,5,6,7,9,4,6]
for i in l:
    if (i%2 !=0):
        d= 2*i
        print(d)

#0 Write a code that calculates the sum of cubes of numbers from a given list
l= [1,2,3]
s=0
for i in l:
    s= s+ (i*i*i)
print(s)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    for num in range(2, n + 1):
        if is_prime(num):
            yield num

#Write a code that filters out prime numbers from a given list
l= [1,2,34,5,6,7,8,9,11]
list(filter(is_prime,l))

#Write a code that uses a lambda function to calculate the sum of two numbers
# question already done 22 to 26 (same question 11 to 16)

# What is encapsulation in OOP(object oriented programming) ?

#Explain the use of access modifiers in Python classes ?

#What is inheritance in OOP?
#inheritance in obejct oriented programming means that aquiring all the properperties of the parent class
# by the child class

# Define polymorphism in OOP
#polymorphoism means  " many states "

#Explain method overriding in Python
#overriding is the method in which child value override over the value of the parent class which states us that
# child class is very very powerfull as compared to parent class

# Define a parent class Animal with a method make_sound that prints "Generic animal sound". Create a
#child class Dog inheriting from Animal with a method make_sound that prints "Woof!
class Animal :
     def make_sound(self):
        print("Generic animal sound")
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Define constructors in both the Animal and Dog classes with different initialization parameters
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor called")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print("Dog constructor called")

#What is abstraction in Python? How is it implemented?
"""The main idea is to reduce complexity by providing a simplified interface, which allows the
developer to interact with an object or system without worrying about the internal workings.
Abstraction can be implemented in several ways:
"""

# 1.) Abstract classes:
#example:
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

dog = Dog()
dog.make_sound()

#2.) Encapsulation (data abstraction):
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance


    def get_balance(self):
        return self.__balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")

account = BankAccount("abc", 1000)

print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.withdraw(200)
print(account.get_balance())

#Explain the importance of abstraction in object-oriented programming
"""In Python, abstraction plays a key role in managing complexity,
improving maintainability, and enhancing flexibility in code.
1.) simplifies complex systems
2.)Promotes code Reusability
3.)improves maintaiblity
4.)Increase modularity
5.)Enhances Security
6.)Enables Polymorphism
"""

#How are abstract methods different from regular methods in Python?
"""In Python, abstract methods and regular methods are both used to define behavior for classes, but they serve
different purposes and have distinct characteristics"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Abstract method: no implementation in the base class."""
        pass

    def sleep(self):
        """Regular method: has an implementation."""
        print("Sleeping...")

class Dog(Animal):
    def make_sound(self):
        print("Woof")

dog = Dog()
dog.make_sound()  # Output: Woof
dog.sleep()       # Output: Sleeping...

##How can you achieve abstraction using interfaces in Python?
"""In Python, interfaces are not natively supported like in some other programming languages (e.g., Java or C#), but you can achieve abstraction through
abstract classes and abstract methods, which can serve as a form of interface"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof")

dog = Dog()
dog.make_sound()

#Can you provide an example of how abstraction can be utilized to create a common interface for a group
#of related classes in Python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# How does Python achieve polymorphism through method overriding
"""In Python, polymorphism is the ability of different objects to respond to the same method call
in a way that's appropriate to their individual types. Method overriding is a key mechanism
through which polymorphism is achieved.
This allows a subclass to provide its own implementation of a method that is already defined in its superclass

class Animal:
    def make_sound(self):
        """General method, to be overridden by subclasses"""
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        """Override the make_sound method for Dog"""
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        """Override the make_sound method for Cat"""
        print("Meow!")

animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()
dog.make_sound()
cat.make_sound()

#Define a base class with a method and a subclass that overrides the method
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

# Define a base class and multiple subclasses with overridden methods

class Vehicle:
    def start_engine(self):
        """Base method to start the engine."""
        print("Vehicle engine started.")

    def stop_engine(self):
        """Base method to stop the engine."""
        print("Vehicle engine stopped.")


class Car(Vehicle):
    def start_engine(self):
        """Override the start_engine method for Car."""
        print("Car engine started. Vroom Vroom!")

    def stop_engine(self):
        """Override the stop_engine method for Car."""
        print("Car engine stopped. Shutting down.")


class Truck(Vehicle):
    def start_engine(self):
        """Override the start_engine method for Truck."""
        print("Truck engine started. Rumble rumble!")

    def stop_engine(self):
        """Override the stop_engine method for Truck."""
        print("Truck engine stopped. Engine off.")


class Motorcycle(Vehicle):
    def start_engine(self):
        """Override the start_engine method for Motorcycle."""
        print("Motorcycle engine started. Vroom!")

    def stop_engine(self):
        """Override the stop_engine method for Motorcycle."""
        print("Motorcycle engine stopped. Turning off.")

car = Car()
truck = Truck()
motorcycle = Motorcycle()

print("\nStarting and stopping engines for each vehicle:")
car.start_engine()
car.stop_engine()

truck.start_engine()
truck.stop_engine()

motorcycle.start_engine()
motorcycle.stop_engine()

#Describe how Python supports polymorphism with duck typing.
"""Duck typing is a programming style in Python (and other dynamic languages) that allows an object’s
suitability for a particular operation to be
determined by the presence of certain methods or behaviors, rather than its actual type"""
class Dog:
    def speak(self):
        print("Woof! Woof!")

class Bird:
    def speak(self):
        print("Chirp! Chirp!")

class Car:
    def speak(self):
        print("Car engine starts... Vroom!")


def animal_speak(animal):
    animal.speak()


animal_speak(Dog())
animal_speak(Bird())
animal_speak(Car())

# How do you achieve encapsulation in Python?
class Student:
    def __init__(self,name,degree):
        self.name = name
        self.__degree = degree
        """ in the upper written code we have achieved encapsulation in pyhton by using __ in the degree which
        make it as a private varible which can be accessed only within the class"""

#Can encapsulation be bypassed in Python? If so, how?
"""Yes, encapsulation can be bypassed in Python. While Python does provide mechanisms for encapsulation,
 such as private and protected variables and methods, Python does not enforce strict access control
 like some other programming languages (e.g., Java or C++).
This is because Python relies heavily on conventions and responsibility rather than strict enforcement"""

#1.) Public memebers
class MyClass:
    def __init__(self):
        self.public_var = 10

#2.) private members
class MyClass:
    def __init__(self):
        self._protected_var = 20

#3.) Private members
class MyClass:
    def __init__(self):
        self.__private_var = 30

#Implement a class BankAccount with a private balance attribute. Include methods to deposit, withdraw,
#and check the balance
class BankAccount:
    def __init__(self, initial_balance=0):
        # Private attribute: balance
        self.__balance = initial_balance

    # Deposit method to add money to the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw method to take money from the account
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew ${amount}. Current balance: ${self.__balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")

    # Method to check the current balance
    def get_balance(self):
        return self.__balance


# Test the BankAccount class
account = BankAccount(1000)  # Creating an account with an initial balance of $1000

# Check the balance
print(f"Initial Balance: ${account.get_balance()}")

# Deposit some money
account.deposit(500)

# Withdraw some money
account.withdraw(200)

# Try to withdraw more than the balance
account.withdraw(1500)

# Check the final balance
print(f"Final Balance: ${account.get_balance()}")

# Develop a Person class with private attributes name and email, and methods to set and get the email.
class Person:
    def __init__(self,name,email):
        self.__name = name
        self.__email = email
    def get_email(self):
        return self.__email

    def set_email(self,email):
        if "@" in email:
            self.get_email = email
        else :
            raise ValueError("Invalid email address")
    def get_name(self):
        return self.__name

person =Person("xyz","xyz434@gmail.com")
print(f"Name: {person.get_name()}")
print(f"Email: {person.get_email()}")

person.set_email("xyz4367@gmail.com")
print(f"Updated Email: {person.get_email()}")

#Why is encapsulation considered a pillar of object-oriented programming (OOP)?
""" Encapsulation plays a crucial role in promoting the key principles of OOP, such as modularity,
reusability, and maintainability.
encapsulation is considered so important in oop because:
1.)protection of data (data hiding)
2.)modularity and separation of concern  >>making code easier to manage and maintain
3.)improved maintainability and flexibilty
4>)controlled access to Object State (Getter/setter)
"""

#Create a decorator in Python that adds functionality to a simple function by printing a message before
#and after the function execution
def print_messages_decorator(func):
    """Decorator that adds functionality to print a message before and after the function execution."""
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}...")
        return result
    return wrapper

@print_messages_decorator
def greet(name):
    """Function that greets a person by their name."""
    print(f"Hello, {name}!")

# Call the decorated function
greet("David")

#/ Modify the decorator to accept arguments and print the function name along with the message.
import functools

def decorator_with_args(message):
    """Decorator with arguments """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print(f"{message} {func.__name__}")
            result = func(*args,**kwargs)

@decorator_with_args("Starting execution")
def greet(name, message="Hello"):
    """Greet a person by name with a custom message."""
    print(f"{message}, {name}!")

# Call the decorated function
greet("Alice", message="Good morning")

#Create two decorators, and apply them to a single function. Ensure that they execute in the order they are applied.

def decorator_one(func):
    """first decorator"""
    def wrapper(*args,**kwargs):
        print("decorator one: before calling the function")
        result = func(*args,**kwargs)
        print("decorator one: after calling the function")
        return result
    return wrapper

def decorator_two(func):
    """Second decorator"""
    def wrapper(*args,**kwargs):
        print("decorator two: before calling the function")
        result = func(*args,**kwargs)
        print("decorator two: after calling the function")
        return result
    return wrapper

@decorator_one
@decorator_two
def greet(name):
    print(f"Hello, {name}!")

greet("Arnav")

#/ Modify the decorator to accept and pass function arguments to the wrapped function
import functools

def preserve_metadata(func):
    """Decorator to preserve the metadata of the original function and pass arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned {result}")

        return result
    return wrapper

@preserve_metadata
def greet(name, message="Hello"):
    """Greet a person by name with a custom message."""
    return f"{message}, {name}!"

print(greet("Arnav", message="Good morning"))

print(f"Function name: {greet.__name__}")
print(f"Function docstring: {greet.__doc__}")

# Create a decorator that preserves the metadata of the original function/
""" In python ,when you wrap a function using a decorator, the metadata of the
original funcion (like its name, docstring and other attributes) is usually lost.To preserve this data, you can
use functools.wraps decorator from the standard library"""

import functools

def preserve_metadata(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        return func(*args,**kwargs)
    return wrapper

@preserve_metadata
def greet(name):
    """This function greets the given name."""
    return f"Hello, {name}!"

print(greet("David"))

print(f"function name : {greet.__name__}")
print(f"docstring : {greet.__doc__}")

#Create a Python class `Calculator` with a static method `add` that takes in two numbers and returns their sum
class Calculator:
    @staticmethod
    def add(a,b):
        return a+b

addition = Calculator.add(2,4)
print(addition)

#Create a Python class `Employee` with a class `method get_employee_count` that returns the total
#number of employees created/

class Employee:
    count = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.count +=1

    @classmethod
    def get_employee_count(cls):
        return cls.count

emp1 = Employee("arnav", "Data_scientist")
emp2 = Employee("ravi","ML Engineer")
emp3 = Employee("Priya","Data_analyst")

print(f"Total number of employees: {Employee.get_employee_count()}")

emp4 = Employee("David","Data_analyst")
print(f"Total number of employees: {Employee.get_employee_count()}(after modification)")

# Create a Python class `StringFormatter` with a static method `reverse_string` that takes a string as input
#and returns its reverse

class StringFormatter:
    @staticmethod
    def reverse_string(input_string):
        return input_string[::-1]

string = "Hello World!!"
reverse_string = StringFormatter.reverse_string(string)
print(reverse_string)

#/ Create a Python class `Circle` with a class method `calculate_area` that calculates the area of a circle
#given its radius.

class Circle:
    @classmethod
    def calculate_area(cls,radius):
        return 3.14159*(radius**2)

radius =5
area = Circle.calculate_area(radius)
print(f"the area of the circle with radius {radius} is {area}")

#Create a Python class `TemperatureConverter` with a static method `celsius_to_fahrenheit` that converts
#Celsius to Fahrenheit.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
            return (celsius * 9/5) + 32

celsius_temp=25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp} celsius is equal to {fahrenheit} fahrenheit")

#What is the purpose of the __str__() method in Python classes? Provide an example
""" __str__() method is dunder or magic method in pyton which is used to return the string representation of the
of an objectwhen it is converted to string typically through  the str method."""

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"person (name={self.name},age{self.age})"

p= Person("Alice",30)
print(p)

#How does the __len__() method work in Python? Provide an example.
""" __len__() method in python is also a magic method which actually provides the length of the object"""
class Customlist:
    def __init__(self,*args):
        self.items = list(args)

    def __len__(self):
        return len(self.items)

l1 = Customlist(1,2,46,7,8,9,0)
print(len(l1))

#/ Explain the usage of the __add__() method in Python classes. Provide an example.
""" In pyhton, the add() method is a special method which is also known as magic or dunder method )
that allows us to define addition(+) operator for objects for your custom class"""

class Vector:
    def __init__(self,x,y):
        self.x= x
        self.y = y
    def __add__(self,other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("both operands must be vectors")
    def __repr__(self):                     # allow us to access the result in a readable format
        return f"Vector({self.x},{self.y})"

v1 = Vector(1,2)
v2 = Vector(3,2)
v3= v1 + v2
print(v3)

# What is the purpose of the __getitem__() method in Python? Provide an example.
"""The __getitem__() method in python is part of the container protocol and is used to define how objcts behave
when indexing or accessing  items using using square brackets []"""

class Customlist:
    def __init__(self,*args):
        self.items = list(args)

    def __getitem__(self,index):

        if isinstance(index,slice):
            raise IndexError("index out of range")
        return self.items[index]

c1 = Customlist(10,20,30,40,50,60)
print(c1[0])
print(c1[4])

try :
    print(c1[10])
except IndexError as e:
    print(e)

#Explain the usage of the __iter__() and __next__() methods in Python. Provide an example using iterators.
""" In python, the __iter__() method and __next__ methods are used to create iterrator
which is used to iterate over the elements of the object"""


class Counter:
    def __init__ (self, start , end ):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self
    def __next__(self):
        if self.current >self.end:
            raise StopIteration
        else :
            self.current +=1
            return self.current -1

counter = Counter(1,9)

for number in counter :
    print(number)

#What is the purpose of a getter method in Python? Provide an example demonstrating the use of a getter
#method using property decorators
"""In python , getter method is used to retrieve the value of the attribute. it provide the control
state of an object ."""
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <0:
            raise ValueError("width cannnot be negative")
            self._width = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <0:
            raise ValueError("height cannnot be negative")
            self._height = value

rect = Rectangle(5,20)
print(f"area = {rect.area}")
print(f"width = {rect.width}")
print(f"height = {rect.height}")

rect._width = 20
rect._height = 30
print(f"area = {rect.area}")

#/ Explain the role of setter methods in Python. Demonstrate how to use a setter method to modify a class
#attribute using property decorators.
""" in python, setter methods  are used to define how an attribute is modified .
They allow us to controlthe assignment of the values to an attribute , ofhen enforcing validation rules.
the @property decorator , when combined with @property_name.setter decorator , enables the functionality."""

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <0:
            raise ValueError("radius cannot be negative")
        self._radius = value
    @property
    def area(self):
        return 3.14159*(self._radius**2)

circle = Circle(5)
print(circle.radius)
print("area",circle.area)

circle.radius = 10
print(circle.radius)
print("area after modifications",circle.area)

#What is the purpose of the @property decorator in Python? Provide an example illustrating its usage
""" the @property decorator is used to define a getter for an attribute ,allowing it to be accessed
like a regular attribute while actually invkoing a method ."""

class Circle:
    def __init__(self,radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius

    @radius.deleter
    def radius(self, value):
        if value <0:
            raise ValueError("radius cannot be negative.")
        self._radius = value

    @property
    def area(self):
        return 3.14159*(self._radius**2)

circle = Circle(10)
print(circle.radius)
print(circle.area)

#Explain the use of the @deleter decorator in Python property decorators. Provide a code example
#demonstrating its application.
""" @deleter decorator is a decorator of python propery decorator which is used to perform
deletion of the attribute using del statement"""

class Person:
    def __init__(self , name , age):
        self._name = name
        self._age = age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <0:
            raise ValueError("age cannot be negative")
        self._age= value

    @age.deleter
    def age(self):
        print(f"deleting the age of {self._name}")
        del self._age

person=  Person("Alice", 30)
print(person.age)

person.age =35
print(person.age)

del person.age

##How does encapsulation relate to property decorators in Python? Provide an example showcasing
#encapsulation using property decorators.
""" encapsulation is a fundamental method which is used to restrict direct access to the intenal's
state and requiring interction with well defined methods .It can be achieved by using underscore (__ or _).

PROPERTY decorator in python used to encapsulate in more pythonic way by allowing them to be accesed like
a regular attribute while they are controlling their direct access amd modification via mehtods.
"""

#Provide an example showcasing
#encapsulation using property decorators.
class circle:
    def __init__(self,radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value<=0:
            raise ValueError("Radius must be positive.")
        self._radius = value

    def area(self):
        return 3.14159*(self._radius**2)

circle = Circle(5)
print(circle.radius)
print(circle.area)

try:
    circle.radius = -5
except ValueError as e:
    print(e)

pip install colab-xterm

# Commented out IPython magic to ensure Python compatibility.
# %load_ext colabxterm

# Commented out IPython magic to ensure Python compatibility.
# %xterm

