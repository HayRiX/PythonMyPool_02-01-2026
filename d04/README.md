# Module 04: Cyber Archives
## File Input/Output & Context Managers

## 📝 Overview
Welcome to **Day 04**! Until today, everything we stored in variables or lists disappeared the moment our program finished running. It was like drawing in the sand. Today, we learned how to carve our data into stone: **File Handling (I/O)**. We learned how to read from files, write to them, and manage them safely.

---

## 🧠 Core Concepts (Explained with Examples)

Imagine your hard drive is a giant **Library**, and files are the **Books**.

### 1. Opening and Closing (The Golden Rule)
To read a book, you must first take it off the shelf (`open`), and when you are done, you **must** put it back (`close`). If you don't close the file, it gets locked, and other programs can't use it, which causes memory leaks.

```python
# The Dangerous Way (If an error happens before close(), it stays open forever)
my_file = open("secret.txt", "r")
print(my_file.read())
my_file.close() 
```

### 2. The Smart Librarian (`with` statement)
Because programmers often forget to close files, Python gives us the `with` statement (called a **Context Manager**). Think of it as a smart librarian: you read the book, and the librarian automatically puts it back for you the moment you are done, **even if the program crashes!**

```python
# The Pythonic & Safe Way:
with open("secret.txt", "r") as my_file:
    content = my_file.read()
    print(content)
# <-- The file is automatically closed right here!
```

### 3. File Modes (The Magic Pen)
When you open a file, you must tell Python what you intend to do with it:
* 👓 **`"r"` (Read):** You can only look. No pens allowed. (Throws an error if the file doesn't exist).
* ✍️ **`"w"` (Write):** You take a giant eraser, **destroy** everything in the file, and write a brand new story. (Creates a new file if it doesn't exist).
* ➕ **`"a"` (Append):** You go to the very last page and add a new chapter. The old story is safe.

```python
# Writing (Will erase old content)
with open("diary.txt", "w") as f:
    f.write("Today I learned Python!\n")

# Appending (Adds to the end)
with open("diary.txt", "a") as f:
    f.write("And it was super fun!\n")
```

### 4. Reading Line by Line (Stream Management)
If you try to read a 10 Gigabyte file using `.read()`, your computer will try to load all 10GB into RAM at once... and your PC will crash 💥.
Instead, we read it line by line (Streaming), just like drinking water sip by sip instead of swallowing the whole bottle at once.

```python
with open("huge_book.txt", "r") as f:
    for line in f:
        print(line.strip()) # .strip() removes the invisible '\n' at the end
```

---

## 🛠️ Exercises Breakdown

### 📜 Exercise 0: Ancient Text (Reading Files)
**Goal:** Learn the absolute basics of opening a file safely using `with` and reading its contents without crashing. We handled the `FileNotFoundError` gracefully using a `try/except` block.

### 🗄️ Exercise 1: Archive Creation (Writing Files)
**Goal:** Create a new file from scratch. We learned how to use the `"w"` mode to create a file and write specific text into it.

### 🌊 Exercise 2: Stream Management (Line by Line)
**Goal:** Handle large files efficiently. We opened a file and used a