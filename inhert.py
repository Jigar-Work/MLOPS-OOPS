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



# Super methods/keywort calls the parent methodss, not any perticular variable of attribute.
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")   

class Dog(Animal):
    def __init__(self, breed):
        super().__init__()  # Call the parent class constructor
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks. and it is {self.breed}.")     


dog = Dog("Golden Retriever")
dog.speak()  # Output: Buddy makes a sound. Buddy barks. He is very friendly.

