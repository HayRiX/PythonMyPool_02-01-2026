# Module 07: DataDeck Game
## Design Patterns, Interfaces & Advanced OOP

## 📝 Overview
Welcome to **Day 07**! Today, we didn't just write code; we learned how to **design** it. We built a Trading Card Game (like Yu-Gi-Oh! or Hearthstone) to understand how professional software engineers structure large systems. We moved beyond basic Classes and learned about **Composition**, **Interfaces (Protocols)**, and famous **Design Patterns** (Factory & Strategy).

---

## 🧠 Core Concepts (Explained with Examples)

### 1. Composition ("Has-A" vs "Is-A")
* **What is it?** In Day 01, we learned Inheritance ("A Dog **IS A**n Animal"). But what if we want to build a Car? A Car is not an Engine. A Car **HAS AN** Engine. This is Composition.
* In our game, a `Deck` is not a `Card`. A `Deck` **HAS** a list of `Cards`.

```python
class Card:
    def __init__(self, name):
        self.name = name

class Deck:
    def __init__(self):
        # The Deck OWNS a list of Cards (Composition)
        self.cards = [Card("Dragon"), Card("Goblin")]
```

### 2. Interfaces / Protocols (The Job Description)
* **What is it?** Imagine a job posting for a Chef: *"Must be able to `cook()`"*. The restaurant doesn't care if you are a human, an alien, or a robot. If you have the `cook()` method, you are hired!
* In Python, we use `typing.Protocol` (or ABCs) to create these strict job descriptions. If a card wants to enter a battle, it **MUST** have an `attack()` method.

```python
from typing import Protocol

# The Job Description
class Combatable(Protocol):
    def attack(self) -> int:
        ...

# The hired employee (Matches the description!)
class KnightCard:
    def attack(self) -> int:
        return 50

# my_knight is officially "Combatable"!
```

### 3. Design Pattern: The Factory (The Vending Machine)
* **What is it?** Instead of using `__init__` to create cards all over your code, you create a central "Machine". You give the machine a string like `"Spell"`, and it builds the correct object for you.
* **Why?** It hides the complicated building process. You just press a button and get your object.

```python
class CardFactory:
    @staticmethod
    def create_card(card_type: str):
        if card_type == "Creature":
            return CreatureCard("Goblin", damage=10)
        elif card_type == "Spell":
            return SpellCard("Fireball", magic=50)
        else:
            raise ValueError("Unknown Card Type!")

# Usage: Just ask the factory!
my_card = CardFactory.create_card("Spell")
```

### 4. Design Pattern: The Strategy (The Brain Swap)
* **What is it?** Imagine a Robot Vacuum Cleaner. Sometimes you want it to be aggressive (fast but loud), and sometimes you want it to be stealthy (slow but quiet). Instead of building two different robots, you build **ONE** robot with a slot for a "Brain". You can swap the brain (the Strategy) while the robot is running!
* In our game, the `GameEngine` stays the same, but we can give it an `AggressiveStrategy` or a `DefensiveStrategy`.

```python
class AggressiveStrategy:
    def play(self):
        print("Attacking with full power!")

class Player:
    def __init__(self, strategy):
        self.brain = strategy  # Plugging in the brain
    
    def take_turn(self):
        self.brain.play()  # Using the brain

# Swap brains on the fly!
p1 = Player(AggressiveStrategy())
p1.take_turn() # Output: Attacking with full power!
```

### 5. Magic Comparison (`__lt__`, `__gt__`)
* **What is it?** How do you tell Python that a Dragon is "greater than" a Goblin? Python doesn't know math for monsters! We have to teach it what the `<` (Less Than) and `>` (Greater Than) symbols mean for our objects.

```python
class Rankable:
    def __init__(self, power):
        self.power = power
        
    # Teach Python what "Less Than" (<) means
    def __lt__(self, other):
        return self.power < other.power

card1 = Rankable(10)
card2 = Rankable(50)
print(card1 < card2) # Output: True! Python now understands!
```

---

## 🛠️ Exercises Breakdown

### 🃏 Exercise 0: Card Foundations
**Goal:** Build the basic `Card` and `CreatureCard` base classes using Inheritance, establishing the foundational properties like health and damage.

### 🎴 Exercise 1: Deck Assembly (Composition)
**Goal:** Learn Composition. We created `ArtifactCard` and `SpellCard`, and then built a `Deck` class that holds and manages a list of these cards (drawing, shuffling).

### ⚔️ Exercise 2: The Arena (Protocols/Interfaces)
**Goal:** Understand Interfaces. We created `Combatable` and `Magical` traits. Then we built an `EliteCard` that adopts both traits (Multiple Inheritance/Mixins), guaranteeing it has both physical and magical abilities.

### 🧠 Exercise 3: Game Engine (Design Patterns)
**Goal:** Implement professional Architecture.
* Built `CardFactory` and `FantasyCardFactory` to centralize object creation.
* Built a `GameEngine` that uses `GameStrategy` (like `AggressiveStrategy`) to decouple the game rules from the game logic.

### 🏆 Exercise 4: Tournament Platform (Ranking)
**Goal:** Master Object Sorting. We implemented the `Rankable` class with magic methods (`__lt__`, `__gt__`, `__eq__`) so we could easily sort a list of `TournamentCard` objects from weakest to strongest using Python's built-in `sort()` function.

---

## 🚨 Common Pitfalls (Don't do this!)

1. **Overusing Inheritance:** If a `Deck` inherits from `list`, you are saying a Deck *IS A* list. That's bad design because you expose all list methods (like `.append()` and `.clear()`) to the user. A Deck should *HAVE A* list (Composition) to protect its cards!
2. **Ignoring Protocol Rules:** If your class claims to be `Combatable` but you misspell the `attack()` method as `atk()`, the game will crash during battle because the Interface contract was broken.

---

*Summary created after completing Ex00 - Ex04.*