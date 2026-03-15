# 🐍 Python Piscine - Day 00: Growing Code

## 📝 Overview
This repository contains the solutions for **Day 00** of the Python Piscine. The focus of this day is to transition from C to **Python**, understanding its internal architecture, basic syntax, and control flow structures.

## 🧠 Part 1: Python Architecture (Under the Hood)
Unlike C (which compiles to machine code), Python is an **interpreted language** with a unique two-step process:

1.  **Compilation:** The source code (`.py`) is compiled into **Bytecode**.
    * *Artifact:* This generates `__pycache__` folders and `.pyc` files.
    * *Rule:* If there is a syntax error anywhere, no bytecode is generated, and nothing runs.
2.  **Execution (PVM):** The **Python Virtual Machine** reads the Bytecode and executes it on the CPU.

| Feature | C Language | Python |
| :--- | :--- | :--- |
| **Typing** | Static (`int x;`) | Dynamic (`x = 10`) |
| **Blocks** | Braces `{ }` | **Indentation** (4 spaces) |
| **Memory** | Manual (`malloc/free`) | Automatic (Garbage Collector) |
| **Strictness** | Compiler Checks | `flake8` (Linter) & Runtime Checks |

---

## 🛠️ Part 2: The Toolkit (Functions & Methods)

### 1. I/O Operations (Advanced)
* **`print(*objects)`**:
    * Outputs text to the console (adds `\n` automatically).
    * **`end="..."`**: Changes the character printed at the end.
        * *Ex:* `print("Hello", end="")` (No newline, cursor stays on same line).
    * **`sep="..."`**: Changes the separator between multiple arguments.
        * *Ex:* `print("Day", "1", sep="-")` → `Day-1`.
* **`input(prompt)`**:
    * Displays a prompt and pauses for user input.
    * ⚠️ **Crucial:** Always returns a **String (`str`)**. Even if the user types `10`, it returns `"10"`.

### 2. Loops & Sequences (Range Mastery)
* **`range(start, stop, step)`**: Generates a sequence of numbers.
    * **Basic:** `range(1, 5)` → `1, 2, 3, 4` (Stop is exclusive).
    * **With Step:** `range(0, 10, 2)` → `0, 2, 4, 6, 8` (Skips by 2).
    * **Backwards (Negative Step):** `range(5, 0, -1)` → `5, 4, 3, 2, 1`.
        * *Note:* To count down, `step` must be negative, and `start` must be greater than `stop`.

### 3. String Formatting & Methods
* **f-strings** (Python 3.6+):
    * The modern way to embed expressions inside string literals.
    * *Syntax:* `f"Hello {name}, score is {score}"`.
    * **Precision:** `f"Price: {price:.2f}"` → Rounds float to 2 decimal places.
* **Methods:**
    * `.capitalize()`: First char to uppercase (`"tomato"` → `"Tomato"`).
    * `.upper()` / `.lower()`: Converts entire string case.

---

## 💡 Part 3: Logic Patterns & Control Flow

### 1. Conditional Statements
No parentheses `()` required around conditions. Colons `:` are mandatory.
```python
if age > 60:
    print("Ready")
elif age < 0:
    print("Error")
else:
    print("Wait")
```

### 2. Iteration (Loops)
Python uses for ... in ... to iterate over sequences (like range).

```python
for i in range(1, 10):
    print(i)
```

### 3. Recursion (Wrapper Pattern)
To handle recursion without asking for input multiple times, we use an inner function (wrapper):

```python
def ft_recursive_task():
    limit = int(input("Limit: ")) # Input happens once
    
    def inner_runner(current):
        if current > limit: # Base case
            return
        print(current)
        inner_runner(current + 1) # Recursive step
        
    inner_runner(1) # Start the recursion
```

### 4. Type Annotations (Hints)
Introduced in Exercise 7, this brings C-style clarity to Python functions (though it's not enforced by the runtime).

```python
#      variable: type      variable: type    return type
def my_func(name: str,      count: int)    -> None:
    pass
```

## ⚠️ Important Norms
* **Flake8:** The code must strictly follow PEP 8 standards (spaces around operators, indentation, line length).
* **Cleanliness:** No `__pycache__` folders in the repository.
* **Structure:** One function per file, no global scope code.

*Created by aryahi for 1337 / 42 Network Python Piscine.*
