
# Encapsualtion
Is when we hide complex code in small methods Method 1 and Methods 2 do the same thing , Method 2 loks easier

## Method 1 
``` python  
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
```  

## Method 2 
``` python   
from duckduckgo_search import DDGS

for r in DDGS().text("Sausages", max_results=5):
    print(r['href'] + ' - ' + r['title'])
```  

# Abstractions in OOP 

 Java/C# style:
 In languages like Java or C#, an interface or an abstract base class is the formal way to declare an abstraction. It’s a contract: “any class that implements this must provide these methods.”
 Example (Java-style pseudocode):

``` C#   
    interface Shape
    { 
        double area(); 
        double perimeter();
    }
```

 Python style:
 Python has abc.ABC and @abstractmethod if you want the same behavior. For example:

``` python  
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

Any subclass must implement area and perimeter.

## Duck Typing in Python

But Python is more flexible — it uses duck typing:
“If it walks like a duck and quacks like a duck, it’s a duck.”
You don’t always need a formal ABC. If an object has the methods you expect, you can just use it.
Example:

``` python  
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
```
Both Circle and Square work with print_area because they each provide an .area() method — even though they don’t share a base class.

# Most Common Architecture 3 layer 
    1. Presentaion layer 
    2. Business 
    3. Logic and Database Layer


# SOLID Design Principles Explained: Building Better Software Architecture
    1. S - Single-responsibility Principle Class has 1 responsability
    2. O - Open-closed Principle Class should do one waht it says
    3. L - Liskov Substitution Principle
    4. I - Interface Segregation Principle
    5. D - Dependency Inversion Principle

SOLID is an acronym representing five fundamental object-oriented design principles formulated by Robert C. Martin, also known as Uncle Bob. These principles are:

    1. Single-responsibility Principle (SRP): A class should have one and only one reason to change.
    2. Open-closed Principle (OCP): Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
    3. Liskov Substitution Principle (LSP): Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program.
    4. Interface Segregation Principle (ISP): Clients should not be forced to depend on interfaces they do not use.
    5. Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules; both should depend on abstractions. Also, abstractions should not depend on details; details should depend on abstractions.

# https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design


# Object Classification 
Objects can be classified into two types

## Entities
Entities are objects that have a distinct identity that persists over time. They are defined by their identity, not their attributes. This means that even if the attributes of an entity change, it is still considered the same entity if its identity remains the same.

Key Characteristics of Entities:

 1. Identity: Every entity has a unique identity (e.g., an ID or GUID) that differentiates it from other entities.
 2. Lifecycle: Entities typically have a lifecycle. They may be created, updated, and deleted over time.
 3. Mutable: Entities often change their state (attributes) over time while still being considered the same entity.

Example:

Customer: A customer entity may have attributes like name, address, and email. The customer is identified by their unique customer ID, not by the specific attributes. Even if the customer’s address changes, it is still the same customer as long as the ID remains the same.

## Value Objects

Value objects, on the other hand, are defined by their attributes and do not have an identity. They are considered immutable, meaning once a value object is created, its properties cannot change. If you need a different state, you create a new value object.

Key Characteristics of Value Objects:

No Identity: Value objects are not identified by a unique identity, but by their attributes. If two value objects have the same attributes, they are considered the same.

Immutable: Value objects are immutable, meaning their state cannot be modified after creation.

Interchangeable: If two value objects have the same value, they can be used interchangeably in the domain model.

Example:

Address: An address (street, city, zip code, etc.) is a value object. Two addresses that have the same values for all fields are considered equal, and there is no need to track a unique identity for each one. If you need to change the address, you create a new address object.

# Python identification of classes using hash
Python Hash and Equality go together (https://hynek.me/articles/hashes-and-equality/)

## What is an object hash? 
It is an integer number representing the value of the object and can be obtained using hash() . To make a class hasable you need both __hash__ and __eql__ method. Usally instances of the same class will always have a diffrent hash so most programmers do not notice that a bug will occur.

If you try to add an unhasable object into a set or a dictionary you will get an error. 

``` python 
>>> set().add({})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
unhashable type: 'dict'
```


