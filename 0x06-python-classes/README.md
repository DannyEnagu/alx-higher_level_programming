# 0x06. Python - Classes and Objects

## Resource Links

1. [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet)

2. [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)

3. [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)

4. [Learn to Program 9 : Object Oriented Programming](Learn to Program 9 : Object Oriented Programming)

5. [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)

6. [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

## Tasks

* Write an empty class Square that defines a square:
	* You are not allowed to import any module
* Write a class Square that defines a square by: (based on 0-square.py)
	* Private instance attribute: size
	* Instantiation with size (no type/value verification)
	* You are not allowed to import any module

##### Why?

Why size is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

* Write a class Square that defines a square by: (based on 1-square.py)
	* Private instance attribute: size
	* Instantiation with optional size: def __init__(self, size=0):
		* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
		* if size is less than 0, raise a ValueError exception with the message size must be >= 0
	* You are not allowed to import any module

* Write a class Square that defines a square by: (based on 2-square.py)
	* Private instance attribute: size
	* Instantiation with optional size: def __init__(self, size=0):
		* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
		* if size is less than 0, raise a ValueError exception with the message size must be >= 0
	* Public instance method: def area(self): that returns the current square area
	* You are not allowed to import any module
