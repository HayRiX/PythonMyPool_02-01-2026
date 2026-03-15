# 🚀 Module 09: Space Station
## Strict Data Validation & Serialization (Pydantic)

## 📝 Overview
Welcome to **Day 09**! Until today, Python was very trusting. If you built a `User` class and expected an `age` (integer), but someone typed `"apple"`, Python would just accept it and crash later. Today, we learned how to become incredibly strict. We used the **Pydantic** library to build unbreakable data models for a Space Station, ensuring that bad data is destroyed before it ever enters our system.

---

## 🧠 Core Concepts (Explained with Examples)

### 1. The Passport Control (Pydantic `BaseModel`)
* **What is it?** A normal Python class is like a polite receptionist; it believes whatever you tell it. A Pydantic `BaseModel` is like a strict Passport Control Officer at the airport. It checks your data type instantly.
* You don't even need to write an `__init__` method anymore! Pydantic writes it for you behind the scenes.

```python
from pydantic import BaseModel, ValidationError

class Astronaut(BaseModel):
    name: str
    age: int

# 1. Valid Data (Passes)
hero = Astronaut(name="Alice", age=30)

# 2. Coercion (The Officer fixes your mistake)
# You gave a string "45", but Pydantic safely converts it to the integer 45!
pilot = Astronaut(name="Bob", age="45") 

# 3. Invalid Data (Arrested!)
try:
    bad_pilot = Astronaut(name="Charlie", age="apple")
except ValidationError as e:
    print("CRASH AVERTED! Age must be a valid number.")
```

### 2. The Measuring Tape (`Field` Constraints)
* **What is it?** Sometimes knowing it's an "integer" isn't enough. An age of `-500` is an integer, but it's impossible. Instead of writing custom `if` statements, we use Pydantic's `Field` to set strict limits (like a measuring tape).

```python
from pydantic import BaseModel, Field

class Engine(BaseModel):
    # Must be at least 1, and maximum 100
    power_level: int = Field(ge=1, le=100)
    # Must be exactly 3 characters long
    serial_code: str = Field(min_length=3, max_length=3)

# Engine(power_level=5000, serial_code="X") <-- ValidationError!
```

### 3. Custom Validators (The Lie Detector)
* **What is it?** What if the rules are too complex for `Field`? For example, "The astronaut's name must not contain numbers." We use the `@field_validator` decorator to build a custom Lie Detector test.

```python
from pydantic import BaseModel, field_validator

class CrewMember(BaseModel):
    name: str

    @field_validator('name')
    def name_must_be_alpha(cls, value):
        if not value.isalpha():
            raise ValueError("Names cannot contain numbers or symbols!")
        return value.title() # We can also clean the data! (alice -> Alice)
```

### 4. Serialization (The IKEA Box)
* **What is it?** You cannot send a Python Object (like our `Astronaut`) over the internet to a website. You have to pack it into a universal text format called **JSON**.
* Pydantic can instantly pack (Serialize) and unpack (Deserialize) data like an IKEA flat-pack box!

```python
# Pack into JSON (To send over the internet)
json_data = hero.model_dump_json()
print(json_data) # Output: '{"name": "Alice", "age": 30}'

# Unpack from JSON (Receiving from the internet)
new_hero = Astronaut.model_validate_json('{"name": "Eve", "age": 25}')
```

---

## 🛠️ Exercises Breakdown

### 🛰️ Exercise 0: Space Station (Basic Validation)
**Goal:** Learn the syntax of `BaseModel`.
* We created a `SpaceStation` model with strict types.
* We learned how Pydantic automatically catches missing arguments or entirely wrong data types, throwing a neat `ValidationError`.

### 👽 Exercise 1: Alien Contact (Complex Types)
**Goal:** Handle advanced data structures.
* We dealt with Lists and Dictionaries inside our models (e.g., `List[str]`).
* We created nested models (A class inside a class) to represent complex alien data.

### 👨‍🚀 Exercise 2: Space Crew (Fields & Validators)
**Goal:** Master Data Constraints.
* We used `Field` to ensure IDs and coordinates stayed within physical limits.
* We wrote custom `@field_validator` methods to enforce specific business logic (like ensuring a rank is from an approved list of titles).

---

## 🚨 Common Pitfalls (Don't do this!)

1. **Forgetting to inherit from `BaseModel`:** If you write `class Planet:`, Pydantic won't work. It **MUST** be `class Planet(BaseModel):`.
2. **Using normal `Exception` instead of `ValueError` in validators:** When writing a custom `@field_validator`, if the data is bad, you must `raise ValueError`. If you raise a normal `Exception`, Pydantic might crash instead of gracefully collecting the errors.
3. **Trusting floats with money/precise math:** Pydantic allows `float`, but for extreme precision (like space coordinates or money), professionals use the `Decimal` type to avoid rounding errors.

---

*Summary created after completing Ex00 - Ex02.*