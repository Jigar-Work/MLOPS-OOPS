# # Simple inheritance

# # Parent class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # Derived/child class
# class Dog(Animal):

#     def speak(self):
#         self.behaviour = "friendly"

#         print(f"{self.name} barks.He i svery {self.behaviour}.")

# # animal = Animal("Generic Animal")
# # animal.speak()  # Output: Generic Animal makes a sound.

# dog = Dog("Buddy")
# dog.speak()  # Output: Buddy barks.





# # Super methods/keywort calls the parent methodss, not any perticular variable of attribute.
# class Animal:
#     def __init__(self):
#         self.name = "Buddy"

#     def speak(self):
#         print(f"{self.name} makes a sound.")   

# class Dog(Animal):
#     def __init__(self, breed):
#         super().__init__()  # Call the parent class constructor
#         self.breed = breed

#     def speak(self):
#         super().speak()
#         print(f"{self.name} barks. and it is {self.breed}.")     

# dog = Dog("Golden Retriever")
# dog.speak()  # Output: Buddy makes a sound. Buddy barks. He is very friendly.




# There are 5 types of inheritance in python.
# 1.single inheritance
# 2.multilevel inheritance
# 3.hierarchical inheritance
# 4.multiple inheritance <diamonf problem>
# 5.hybrid inheritance


# Single or Basic Inheritance
# Base class
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# # Derived class
# class Child(Parent):

#     def play(self):
#         print(f"{self.name} is playing.")

# # Create an instance of Child
# child = Child("Alice")
# child.greet()  # Output: Hello, my name is Alice.
# child.play()   # Output: Alice is playing.

# ------------------------------------------------------------
# ------------------------------------------------------------

# Multilevel Inheritance

# Base class
# class Grandparent:
#     def __init__(self, name):
#         self.name = name

#     def tell_story(self):
#         print(f"{self.name} tells a story.")

# # Intermediate class
# class Parent(Grandparent):

#     def work(self):
#         print(f"{self.name} is working.")

# # Derived class
# class Child(Parent):

#     def play(self):
#         print(f"{self.name} is playing.")

# # Create an instance of Child
# child = Child("Charlie")
# child.tell_story()  # Output: Charlie tells a story.
# child.work()        # Output: Charlie is working.
# child.play()        # Output: Charlie is playing.

# ------------------------------------------------------------
# ------------------------------------------------------------

# Hierarchical Inheritance

# Base class
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# # Derived class 1
# class Child1(Parent):

#     def play(self):
#         print(f"{self.name} is playing.")

# # Derived class 2
# class Child2(Parent):

#     def study(self):
#         print(f"{self.name} is studying.")

# # Create instances of Child1 and Child2
# child1 = Child1("Dave")
# child2 = Child2("Eve")

# child1.greet()  # Output: Hello, my name is Dave.
# child1.play()   # Output: Dave is playing.

# child2.greet()  # Output: Hello, my name is Eve.
# child2.study()  # Output: Eve is studying.

# ------------------------------------------------------------
# ------------------------------------------------------------

# Multiple Inheritance (Diamond Problem)

# Common base class
# class A:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello from A, {self.name}.")

# # Intermediate class 1
# class B(A):

#     def greet(self):
#         print(f"Hello from B, {self.name}.")
#         super().greet()

# # Intermediate class 2
# class C(A):
#     def greet(self):
#         print(f"Hello from C, {self.name}.")
#         super().greet()

# # Derived class
# class D(B, C):

#     def greet(self):
#         print(f"Hello from D, {self.name}.")
#         super().greet()

# # Create an instance of D
# d = D("Frank")
# d.greet()
# # Output:
# # Hello from D, Frank.
# # Hello from B, Frank.
# # Hello from C, Frank.
# Hello from A, Frank.

# ------------------------------------------------------------
# ------------------------------------------------------------

# Hybrid Inheritance

# Base class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         print(f"{self.name} makes a sound.")

# # Intermediate class 1 (Hierarchical)
# class Mammal(Animal):
#     def feed(self):
#         print(f"{self.name} is feeding milk.")

# # Intermediate class 2 (Multiple)
# class Bird(Animal):
#     def fly(self):
#         print(f"{self.name} is flying.")

# # Derived class (Multiple Inheritance)
# class Bat(Mammal, Bird):
#     def __init__(self, name):
#         Mammal.__init__(self, name)  # Explicitly calling the constructor

#     def nocturnal(self):
#         print(f"{self.name} is nocturnal.")

# # Create an instance of Bat
# bat = Bat("Bruce")
# bat.sound()     # Output: Bruce makes a sound.
# bat.feed()      # Output: Bruce is feeding milk.
# bat.fly()       # Output: Bruce is flying.
# bat.nocturnal() # Output: Bruce is nocturnal.

# ------------------------------------------------------------