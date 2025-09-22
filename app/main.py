
# Encapsualtion

# Method 1 
import json
from urllib.request import urlopen
from urllib.parse import urlencode 

params = dict(q='Sausages', format='json')
handle = urlopen('http://api.duckduckgo.com' + '?' + urlencode(params))
raw_text = handle.read().decode('utf8')
parsed = json.loads(raw_text) 

results = parsed['RelatedTopics']
for r in results: 
    if 'Text' in r: 
        print(r['FirstURL'] + ' - ' + r['Text'])

# Method 2 

from duckduckgo_search import DDGS

for r in DDGS().text("Sausages", max_results=5):
    print(r['href'] + ' - ' + r['title'])


# Abstractions in OOP 

# Java/C# style:
# In languages like Java or C#, an interface or an abstract base class is the formal way to declare an abstraction. It’s a contract: “any class that implements this must provide these methods.”
# Example (Java-style pseudocode):

# interface Shape {
#     double area();
#     double perimeter();
# }

# Python style:
# Python has abc.ABC and @abstractmethod if you want the same behavior. For example:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Any subclass must implement area and perimeter.

# Python style:
# Python has abc.ABC and @abstractmethod if you want the same behavior. For example:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Any subclass must implement area and perimeter.

# Duck Typing in Python

# But Python is more flexible — it uses duck typing:
# “If it walks like a duck and quacks like a duck, it’s a duck.”
# You don’t always need a formal ABC. If an object has the methods you expect, you can just use it.
# Example:

def print_area(shape):
    # No need to check class inheritance
    print(shape.area())

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

class Square:
    def __init__(self, s):
        self.s = s
    def area(self):
        return self.s * self.s

print_area(Circle(5))
print_area(Square(4))


# Both Circle and Square work with print_area because they each provide an .area() method — even though they don’t share a base class.

# Most Common Architecture 3 layer Presentaion layer - Business Logic and Database Layer


# SOLID Design Principles Explained: Building Better Software Architecture
# S - Single-responsibility Principle Class has 1 responsability
# O - Open-closed Principle Class should do one waht it says
# L - Liskov Substitution Principle
# I - Interface Segregation Principle
# D - Dependency Inversion Principle

# SOLID is an acronym representing five fundamental object-oriented design principles formulated by Robert C. Martin, also known as Uncle Bob. These principles are:

# Single-responsibility Principle (SRP): A class should have one and only one reason to change.
# Open-closed Principle (OCP): Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
# Liskov Substitution Principle (LSP): Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program.
# Interface Segregation Principle (ISP): Clients should not be forced to depend on interfaces they do not use.
# Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules; both should depend on abstractions. Also, abstractions should not depend on details; details should depend on abstractions.

# https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design


