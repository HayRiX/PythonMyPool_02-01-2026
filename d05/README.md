# Module 05: Code Nexus
## Advanced OOP, Abstraction & Data Pipelines

## 📝 Overview
Welcome to **Day 05**! In Day 01, we learned the basics of Object-Oriented Programming (Classes and Objects). Today, we take a massive leap into **Advanced OOP Architecture**. We learned how to build strict rules for our code using Abstract Classes, how to make different objects share the same behavior (Polymorphism), and how to link them together in a "Factory Assembly Line" (Pipelines).

---

## 🧠 Core Concepts (Explained with Examples)

### 1. Abstract Base Classes (The Strict Contract)
* **What is it?** Imagine you are a manager, and you tell your team: "Anyone who builds a 'Vehicle' **MUST** include a `start_engine()` method." You don't care *how* they build the engine, you just care that the method exists.
* An Abstract Class (`ABC`) is a blueprint that **cannot be used directly**. It only exists to force other classes to follow the rules.

```python
from abc import ABC, abstractmethod

# The Contract (Cannot create an object from this!)
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# The Worker (Must sign and follow the contract)
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# my_animal = Animal()  <-- ERROR! You can't instantiate an ABC.
my_dog = Dog()
my_dog.make_sound()  # Output: Woof!
```

### 2. Polymorphism (One Button, Many Behaviors)
* **What is it?** Polymorphism means "Many Forms". Because we used an Abstract Class, we guarantee that all our different objects share the exact same method names. 
* Imagine a universal "Speak" button. If you press it on a Dog, it barks. If you press it on a Cat, it meows. You don't need to know what animal it is; you just press the button.

```python
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Polymorphism in action:
my_pets = [Dog(), Cat(), Dog()]

for pet in my_pets:
    pet.make_sound() 
    # Python automatically knows which sound to make!
    # Output: Woof! Meow! Woof!
```

### 3. Data Pipelines (The Assembly Line)
* **What is it?** Instead of having one giant messy function that does 10 things, we create small, independent classes (Processors). 
* Think of a car factory: The raw metal goes in -> Machine 1 shapes it -> Machine 2 paints it -> Machine 3 adds wheels. We pass the data from one class to the next.

```python
# Raw Data -> [Filter Negative] -> [Multiply by 2] -> Final Data
```

---

## 🛠️ Exercises Breakdown

### 🌊 Exercise 0: Stream Processor (The Blueprints)
**Goal:** Learn how to use the `abc` module (Abstract Base Classes).
* We created a base `StreamProcessor` class with an `@abstractmethod` called `process()`.
* We built specific processors that inherit from it (like a processor that filters out bad data, or one that modifies data).
* **Lesson:** Enforcing a strict interface so our program is safe from missing methods.

### 📊 Exercise 1: Data Stream (The Flow)
**Goal:** Handle the movement of data.
* We created a class that generates or reads a continuous flow of data.
* Instead of keeping all data in memory, we processed it step-by-step using what we learned about Generators in Day 03.

### 🔗 Exercise 2: Nexus Pipeline (The Factory Assembly Line)
**Goal:** Bring everything together using Polymorphism.
* We created a `NexusPipeline` class that can accept **any** processor we built in Ex00, as long as it inherits from the base Abstract Class.
* We chained these processors together in a list. When data comes in, it flows through a `for` loop, hitting each processor one by one.
* **Why is this powerful?** If your boss asks you to add a new step tomorrow (e.g., "Translate text to French"), you don't rewrite the pipeline. You just create a new `FrenchTranslator(StreamProcessor)` and add it to the list!

---

## 🚨 Common Pitfalls (Don't do this!)

1. **Instantiating an Abstract Class:** Doing `p = StreamProcessor()` will crash with a `TypeError`. Abstract classes are ghosts; they only exist to be inherited.
2. **Forgetting an Abstract Method:** If your `Cat` class inherits from `Animal(ABC)` but you forget to write the `make_sound` method inside `Cat`, Python will refuse to create the `Cat` object and throw an error immediately.
3. **Overcomplicating the Pipeline:** A processor should do **one** thing perfectly (Single Responsibility Principle). Don't write a processor that cleans, translates, and saves to a file at the same time.

---

*Summary created after completing Ex00 - Ex02.*