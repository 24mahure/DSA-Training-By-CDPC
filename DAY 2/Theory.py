Day 2 Training – Important Theory Notes

Python OOPs and Stack

PART 1: STACK – IMPORTANT THEORY

1. What is a Stack?

A Stack is a linear data structure that follows the LIFO (Last In, First Out) principle.

Iska matlab hai ki jo element sabse last mein insert hota hai, woh sabse pehle remove hota hai.

Example:
Push(10)
Push(20)
Push(30)

Pop() → 30
Pop() → 20
Pop() → 10

2. Real-Life Applications of Stack
1. Browser History – Previous pages ko navigate karna.
2. Undo Operation – Text editor mein previous action ko undo karna.
3. Function Call Stack – Function calls aur return addresses ko manage karna.
4. Expression Evaluation – Mathematical expressions solve karna.
5. Parentheses Matching – Brackets balanced hain ya nahi check karna.
3. What is LIFO?

LIFO stands for Last In, First Out.

Example:
Stack = [10, 20, 30]

Pop() → 30

4. What is Stack Overflow and Underflow?

Stack Overflow:
Jab full stack mein naya element insert karne ki koshish karte hain.

Stack Underflow:
Jab empty stack se element remove karne ki koshish karte hain.

5. How Many Ways to Implement Stack in Python?

Stack ko mainly 2 ways se implement kar sakte hain:

1. Using List
- Easy to implement.
- append() aur pop() methods use hote hain.
- Dynamic resizing support karta hai.
2. Using Linked List
- Nodes aur references use hote hain.
- Dynamic memory allocation hota hai.
- Implementation comparatively complex hota hai.
6. What are the Basic Stack Operations?

Push: Stack mein element insert karna.

Pop: Stack ke top element ko remove karna.

Peek: Stack ke top element ko bina remove kiye access karna.

isEmpty: Check karna ki stack empty hai ya nahi.

isFull: Check karna ki stack full hai ya nahi.

Display: Stack ke elements print karna.

PART 2: PYTHON OOPs – IMPORTANT THEORY

7. What is OOP?

OOP stands for Object-Oriented Programming.

OOP ek programming approach hai jisme program ko classes aur objects ke form mein organize kiya jata hai.

Main Concepts of OOP:
1. Class
2. Object
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction
8. What is a Class?

A class is a blueprint or template used to create objects.

Example:

class Student:
    rollno = 101

Yahan Student ek class hai.

9. What is an Object?

An object is an instance of a class.

Example:

class Student:
    rollno = 101

obj = Student()

Yahan obj ek object hai.

Important MCQ:
Object is an instance of a class.

10. What is a Constructor?

A constructor is a special method that is automatically called when an object is created.

Python mein constructor ke liye init() method use hota hai.

Example:

class Student:
def init(self):
print("Constructor is called")

obj = Student()

Output:
Constructor is called

11. Types of Constructors

Python mein commonly 2 types ke constructors padhaye jate hain:

1. Default Constructor
Arguments ke bina initialize hota hai.

2. Parameterized Constructor
Arguments ke saath initialize hota hai.

12. What is self?

self current object ko refer karta hai.

Iska use class ke instance variables aur methods ko access karne ke liye hota hai.

Example:

class Student:
def init(self, name):
self.name = name

Important MCQ:
self is not a Python keyword. It is a convention.

13. What are Data Members and Methods?

Data Member:
Object ya class ka data store karta hai.

Example:
self.name

Method:
Class ke andar defined function hota hai.

Example:
display_info()

14. What is dict?

dict ek built-in attribute hai jo object ke instance attributes ko dictionary ke form mein return karta hai.

Example:

class Student:
def init(self):
self.name = "Rahul"
self.age = 20

obj = Student()

print(obj.dict)

Day 2 ke important concepts:
1. Class and Object
2. Constructor
3. Default Constructor
4. Parameterized Constructor
5. self
6. dict
7. str()
8. Stack Using List
9. Stack Using Linked List
10. Push, Pop, Peek
11. isEmpty and isFull
12. Stack Overflow and Underflow
13. Maximum Element in Stack