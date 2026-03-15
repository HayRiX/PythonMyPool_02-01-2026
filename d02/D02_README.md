# 🌿 Module 02: Garden Guardian
## Data Engineering and Robust Systems in Python

Today, we moved from simply writing code that "works" under ideal conditions to building **Robust Systems** capable of withstanding errors, corrupt data, and unexpected runtime issues.

This folder contains the solutions for **Module 02**, which focuses primarily on **Exception Handling** and how to protect the program from sudden crashes.

---

## 📚 Theoretical Concepts (What did we learn?)

### 1. The Philosophy of Exception Handling
Computers do not tolerate errors. A simple error like "division by zero" is enough to shut down an entire program instantly. We learned to use the `try...except` structure, which acts as a "safety net"; it allows the program to detect the error, handle it, and then continue working instead of crashing.

### 2. Error Types
Python provides different types of errors to help us diagnose problems accurately:
* **`ValueError`**: The content of the data is invalid (e.g., trying to convert the text "abc" into a number).
* **`ZeroDivisionError`**: A mathematical and architectural error (division by zero).
* **`FileNotFoundError`**: Attempting to access a file that does not exist in the system.
* **`KeyError`**: Attempting to access a key that does not exist within a dictionary.

### 3. Raising Errors Manually (`raise`)
Sometimes data is "technically correct" for the computer (e.g., the number `-100`), but it is "logically catastrophic" for the program (you cannot water a plant with negative water). Here, we use the `raise` keyword to play the role of the referee and stop the operation manually.

### 4. Deterministic Cleanup (`finally`)
There are operations that must always happen whether the code succeeds or fails, such as closing files or closing a database connection. Code placed inside a `finally` block is executed **inevitably** under all circumstances.

### 5. Custom Exceptions (Inheritance)
Instead of using generic Python errors, we created a custom error structure for our project (`GardenError`). This gives us full control over the specific types of errors we want to catch.

---

## 🛠️ Exercises Breakdown

### 🌱 Exercise 0: Agricultural Data Validation Pipeline
**Goal:** Build an initial filter for incoming sensor data.
* We learned how to safely convert strings to numbers using `int()` inside a `try` block.
* Verified that values fall within the allowable range (0 - 40 degrees).
* **Key Lesson:** The function returns a value (`return`) only if it is valid, and implicitly returns `None` if it fails, preventing corrupt data from leaking into the system.

**Output Example:**
```console
Testing temperature: 25
Temperature 25°C is perfect for plants!

Testing temperature: abc
Error: 'abc' is not a valid number

Testing temperature: 100
Error: 100°C is too hot for plants (max 40°C)

All tests completed - program didn't crash!
```

---

### 🕸️ Exercise 1: Different Types of Problems
**Goal:** Handle different types of errors using multiple traps.
* Used multiple `except` blocks, each dedicated to a specific error type.
* Understood **Dictionaries**: A data structure based on (Key: Value), where the common error is `KeyError`.
* Understood **Division by Zero**: Why does the computer reject it? Because memory is finite and cannot represent "infinity," forcing the processor to raise an interrupt.

**Output Example:**
```console
Testing ZeroDivisionError...
Caught ZeroDivisionError: division by zero

Testing KeyError...
Caught KeyError: 'missing_plant'

Testing multiple errors together...
Caught an error, but program continues!
```

---

### 🧬 Exercise 2: Making Your Own Error Types
**Goal:** Create Custom Exceptions using Inheritance.
* We created a `GardenError` class that inherits from `Exception`.
* We created `PlantError` and `WaterError` that inherit from `GardenError`.
* **Benefit:** This allows us to catch all garden errors using `except GardenError` (Polymorphism principle), or to catch a specific error precisely.
* Used the `pass` keyword to copy parent attributes without adding new code.

**Output Example:**
```console
Testing PlantError...
Caught PlantError: The tomato plant is wilting!

Testing catching all garden errors...
Caught a garden error: Not enough water in the tank!
```

---

### 🧹 Exercise 3: Finally Block - Always Clean Up
**Goal:** Ensure Resource Cleanup using `finally`.
* The requirement was not to use `raise`, so we tricked Python into raising a natural error by attempting to concatenate text with `None` using `+`.
* We proved that the phrase "Closing watering system" always appears, even if the program stops in the middle due to an error.

**Output Example:**
```console
Opening watering system
Watering tomato
Error: Cannot water None - invalid plant!
Closing watering system (cleanup)
Cleanup always happens, even with errors!
```

---

### 🚩 Exercise 4: Raising Your Own Errors
**Goal:** Verify Validation Logic and raise errors manually.
* Applied strict rules: Name cannot be empty, Water (1-10), Sun (2-12).
* Used `raise ValueError` to stop the function immediately when rules are violated.
* Used `f-strings` in error messages to explain the invalid value to the user (Debug-friendly).

**Output Example:**
```console
Testing bad water level...
Error: Water level 15 is too high (max 10)

Testing empty plant name...
Error: Plant name cannot be empty!
```

---

### 🏰 Exercise 5: Garden Management System
**Goal:** Integrate all concepts into a complete management system (`GardenManager`).
* **Structure:** A class that manages a list of plants and performs addition, watering, and health check operations.
* **Programming Challenge (Unbound LocalError):** We learned to place `try/except` **inside the loop** rather than outside it. This ensures that if one plant is corrupt, the system logs the error and continues checking the remaining plants instead of stopping completely.
* Used the custom exceptions we created in Exercise 2.

**Final Output Example:**
```console
=== Garden Management System ===

Adding plants to garden...
Added tomato successfully
Added lettuce successfully
Error adding plant: Plant name cannot be empty!

Watering plants...
Opening watering system
Watering tomato
Watering lettuce
Closing watering system (cleanup)

Checking plant health...
tomato: healthy (water: 5, sun: 8)
Error checking lettuce: Water level 15 is too high (max 10)

Testing error recovery...
Caught GardenError: Not enough water in tank
System recovered and continuing.
```
