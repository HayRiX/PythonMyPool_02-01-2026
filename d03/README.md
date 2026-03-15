# Module 03: Command Quest & Data Structures

## 📝 Overview
Welcome to **Day 03**! After learning how to create Objects (Day 01) and handle their Errors (Day 02), today we learn how to **organize** them. We moved from dealing with single variables to handling massive collections of data, and we learned how to interact with our program directly from the Terminal.

---

## 🧠 Core Concepts (Explained with Examples)

### 1. Command Line Arguments (`sys.argv`)
* **What is it?** It allows you to pass data to your script directly from the terminal before it runs.
* **Example:**
```python
import sys

# If you type in terminal: python3 my_script.py apple 42
print(sys.argv[0])  # Output: my_script.py (The file name)
print(sys.argv[1])  # Output: apple (Always a string!)
print(sys.argv[2])  # Output: 42 (Still a string '42')
```

### 2. Data Containers (The 4 Big Families)
Python has 4 main ways to store collections of data:

* 🎒 **List (`[]`) - The Backpack:** Ordered, changeable, and allows duplicates.
```python
my_list = ["apple", "banana", "apple"]
my_list.append("orange")
print(my_list) # ['apple', 'banana', 'apple', 'orange']
```

* 🧊 **Tuple (`()`) - The Sealed Box:** Ordered, but **cannot be changed** (Immutable). Safer and faster.
```python
my_tuple = (10, 20, 30)
# my_tuple[0] = 99  <-- ERROR! You cannot change a tuple.
```

* 💃 **Set (`{}`) - The VIP Club:** Unordered, and **strictly no duplicates**. Great for math operations!
```python
my_set = {1, 2, 2, 2, 3}
print(my_set) # {1, 2, 3} (Duplicates automatically removed)
```

* 📖 **Dictionary (`{key: value}`) - The Phonebook:** Stores data in Key-Value pairs.
```python
phonebook = {"Alice": 123, "Bob": 456}
phonebook["Charlie"] = 789 # Adding a new entry
print(phonebook["Alice"])  # Output: 123
```

### 3. List Comprehensions (The Magic Wand)
A Pythonic way to create a list in a single, elegant line instead of writing multiple lines of a `for` loop.
```python
# The Old Way (C-style):
squares = []
for x in range(1, 6):
    squares.append(x * x)

# The Pythonic Way (List Comprehension):
squares = [x * x for x in range(1, 6)]
print(squares) # [1, 4, 9, 16, 25]
```

### 4. Generators and `yield` (The Lazy Chef)
A normal `return` gives you all the data at once, which can crash your RAM if the data is huge. `yield` gives you one item at a time, pauses, and waits for you to ask for the `next()` one.
```python
def lazy_counter():
    yield 1  # Gives 1 and pauses
    yield 2  # Gives 2 and pauses

gen = lazy_counter()
print(next(gen)) # Output: 1
print(next(gen)) # Output: 2
```

### 5. `*args` and `**kwargs` (The Catch-All Nets)
What if you don't know how many arguments the user will pass to your function?
* `*args`: Catches extra unnamed values into a **Tuple**.
* `**kwargs`: Catches extra named values into a **Dictionary