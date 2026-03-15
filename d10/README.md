# Module 10: Higher Magic
## Functional Programming, Closures & Decorators

## 📝 Overview
Welcome to **Day 10 - The Grand Finale!** 🎉 You made it to the end! 
Today, we unlocked the highest level of Python sorcery: **Functional Programming**. Instead of treating functions as just instructions, we learned to treat them as *Data*. We learned how to pass functions inside other functions, how to make functions remember things (Closures), and how to upgrade them using magical armor (Decorators).

---

## 🧠 Core Concepts (Explained with Examples)

### 1. Lambda Functions (The Quick Spells)
* **What is it?** Sometimes you need a tiny function for just one second, and you don't want to write a full `def` block. A `lambda` is a quick, anonymous, one-line spell.
* Think of `def` as forging a permanent steel sword. Think of `lambda` as an ice dagger you create, use once, and it melts away.

```python
# The Normal Way (Steel Sword)
def double(x):
    return x * 2

# The Lambda Way (Ice Dagger)
double_spell = lambda x: x * 2

print(double_spell(5)) # Output: 10
```

### 2. Higher-Order Functions (The Wizard's Assistants)
* **What is it?** A function that takes *another function* as an argument. Tools like `map()` and `filter()` are your magical assistants. You give them a spell (function) and a list of items, and they cast that spell on every single item.

```python
numbers = [1, 2, 3, 4, 5]

# Using filter() to keep only even numbers:
# "Hey assistant, run this lambda spell on all numbers!"
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens) # Output: [2, 4]
```

### 3. Closures & Scope (The Memory Box)
* **What is it?** Normal functions have amnesia; when they finish running, they forget everything. A **Closure** is a function inside a function that carries a "Memory Box" (using the `nonlocal` keyword).

```python
def create_wallet():
    coins = 0  # The secret memory box

    def add_coin():
        nonlocal coins  # "Let me open the memory box"
        coins += 1
        return coins
    
    return add_coin # We return the inner function itself!

my_wallet = create_wallet()
print(my_wallet()) # Output: 1
print(my_wallet()) # Output: 2 (It remembered!)
```

### 4. Decorators (The Magic Armor)
* **What is it?** Imagine you have a basic sword (a function). You want to give it a "Fire Aura" without breaking the sword or rewriting its code. A Decorator is a wrapper that adds new behavior *around* an existing function using the `@` symbol.

```python
# 1. We forge the Magic Armor (The Decorator)
def fire_armor(func):
    def wrapper():
        print("🔥 Aura activated!")
        func()  # Swing the original sword
        print("🔥 Aura deactivated!")
    return wrapper

# 2. We equip the armor to our normal function
@fire_armor
def attack():
    print("Swinging sword!")

attack()
# Output:
# 🔥 Aura activated!
# Swinging sword!
# 🔥 Aura deactivated!
```

### 5. Functools (The Ancient Artifacts)
Python gives us a built-in module called `functools` containing powerful tools. 
* **`@wraps`:** When you put armor (Decorator) on a function, it loses its original name. `@wraps` fixes this and protects its identity.
* **`reduce`:** Takes a list and crushes it down to a single value using a function (e.g., multiplying all numbers together).

---

## 🛠️ Exercises Breakdown

### 🪄 Exercise 0: Lambda Spells
**Goal:** Master one-liners. We rewrote basic operations using `lambda` functions and used them inside `map()` and `filter()` to process arrays of data cleanly without writing `for` loops.

### 🧙‍♂️ Exercise 1: Higher Magic
**Goal:** Pass functions as arguments. We built our own custom Higher-Order functions that accept other functions to apply dynamic rules.

### 📦 Exercise 2: Scope Mysteries (Closures)
**Goal:** Understand Memory State. We used nested functions and the `nonlocal` keyword to build an internal counter/state that survives even after the outer function has finished executing.

### 🛡️ Exercise 3: Functools Artifacts
**Goal:** Use Python's advanced functional toolkit. We applied `functools.reduce` to aggregate data, and explored other tools that make functional programming elegant.

### ✨ Exercise 4: Decorator Mastery
**Goal:** Build custom wrappers. We created practical decorators (like a `@timer` decorator that calculates how long a function takes to run, or a `@debugger` that prints the function's arguments before it runs).

---

## 🚨 Common Pitfalls (Don't do this!)

1. **Forgetting to return the `wrapper`:** In a decorator, you must `return wrapper` at the very end (without parentheses!). If you do `return wrapper()`, the function executes immediately when it's defined, breaking the logic.
2. **Abusing Lambdas:** Lambdas are for *simple* operations. If your lambda spans 3 lines and has complex `if/else` logic, stop! Just write a normal `def` function. Code readability is more important than looking "clever".
3. **Forgetting `@functools.wraps`:** If you build a decorator without `@wraps`, the decorated function loses its `__name__` and `__doc__` (docstring), making debugging extremely painful later.

---

*Summary created after completing Ex00 - Ex04.*
🎉 **END OF PYTHON PISCINE!** 🎉