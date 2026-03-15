# 🌿 Python Piscine - Day 01: Object-Oriented Garden

## 📝 Overview
**Day 01** marks the transition from Procedural Programming (writing scripts) to **Object-Oriented Programming (OOP)**. We built a "Garden System" to understand how to structure complex software using Classes, Objects, Encapsulation, and Inheritance.

---

## 🏗️ 1. Core Concepts (The Basics)

### Class vs. Object
* **Class (The Blueprint):** A definition of how a thing should look and behave. It doesn't exist in memory yet.
* **Object (The House):** A specific instance created from that blueprint.

```python
# The Blueprint
class Plant:
    pass

# The Objects (Instances)
rose = Plant()
oak = Plant()
```

### The `self` Keyword
* In C, we pass the struct pointer explicitly: `function(&my_struct)`.
* In Python, **`self`** is that pointer. It refers to the **current instance** of the class. It allows the code to distinguish between *this* plant's height and *that* plant's height.

---

## 🧬 2. Anatomy of a Class

### The Constructor: `__init__`
This "Magic Method" runs automatically when an object is created. It's used to initialize attributes.

```python
class Plant:
    def __init__(self, name, height):
        self.name = name      # Public attribute
        self.height = height  # Public attribute
```

### Methods (Behavior)
Functions defined inside a class are called **Methods**. They define what an object *can do*.

```python
    def grow(self, size):
        self.height += size   # Modifying internal state
```

### Magic Methods (Printing Objects)
By default, printing an object returns its memory address. To make it readable, we use the `__str__` magic method.

```python
    def __str__(self):
        return f"Plant Object: {self.name}, Height: {self.height}"
```

---

## 🛡️ 3. Encapsulation (Security)

Protecting data from invalid changes (e.g., negative height).

### Access Modifiers
Python doesn't have strict `private` keywords like Java/C++, but it uses conventions:

| Style | Meaning | Behavior |
| :--- | :--- | :--- |
| `self.name` | **Public** | Accessible from anywhere. |
| `self._name` | **Protected** | "Please don't touch" (Convention only). |
| `self.__name` | **Private** | Hard to touch. Python renames it internally (Name Mangling). |

### Getters & Setters (The Classic Way)
The traditional way to access private variables (similar to C++/Java).

```python
class SecurePlant:
    def __init__(self):
        self.__height = 0  # Private

    # Getter
    def get_height(self):
        return self.__height

    # Setter (with validation)
    def set_height(self, value):
        if value < 0:
            print("Error: Negative height!")
        else:
            self.__height = value
```

### The Pythonic Way (`@property`)
Python provides decorators to make Getters and Setters look like normal attributes, which is much cleaner.

```python
class PythonicPlant:
    def __init__(self):
        self.__height = 0

    @property
    def height(self): # This acts as the Getter
        return self.__height

    @height.setter
    def height(self, value): # This acts as the Setter
        if value >= 0:
            self.__height = value
        else:
            print("Error: Negative height!")

# Usage:
# p = PythonicPlant()
# p.height = 10  # Automatically calls the setter!
```

---

## 👨‍👩‍👦 4. Inheritance (The Family Tree)

Creating specialized classes that inherit traits from a base class to avoid code duplication.

### Key Concept: `super()`
Used to call the parent class's methods (usually `__init__`) to ensure the parent is set up correctly before the child adds its own data.

```python
# Base Class (Parent)
class Plant:
    def __init__(self, name):
        self.name = name

# Derived Class (Child)
class Flower(Plant):
    def __init__(self, name, color):
        super().__init__(name)  # Let Parent handle the name
        self.color = color      # Child handles the color

    def bloom(self):
        print(f"{self.name} is {self.color}!")
```

---

## 🛠️ 5. Essential Python Tricks

### The Entry Point Guard
Prevents code from running when the file is imported as a module.
```python
if __name__ == "__main__":
    # Test code goes here
    print("This runs only if executed directly.")
```

### The Shebang
Tells the operating system which interpreter to use.
```python
#!/usr/bin/env python3
```

### Docstrings
Documentation built into the code.
```python
def my_func():
    """This function does something useful."""
    pass
```

---

## 🚨 Common Pitfalls (Don't do this!)

1.  **Forgot `self`:** Defining a method as `def grow(size):` instead of `def grow(self, size):`.
2.  **Mutable Defaults:** Avoid using empty lists `[]` as default arguments in functions.
3.  **Hardcoding:** Don't print fixed strings like `print("Oak")` inside a class; use `print(self.name)`.
4.  **No Return:** Confusing methods that *change* state (void) with methods that *return* values.

---

*Summary created after completing Ex00 - Ex06.*