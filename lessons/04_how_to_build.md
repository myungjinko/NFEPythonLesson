# Chapter 4: How to Build and Run Python Code

## 🎯 Learning Objectives
- Learn how to install Python on your computer
- Understand how to write and save Python code
- Master running Python programs
- Set up a proper development environment

## 💻 Setting Up Python

### Step 1: Check if Python is Already Installed

**On Windows:**
1. Open Command Prompt (search for "cmd")
2. Type: `python --version`
3. If you see a version number, Python is installed!

**On Mac:**
1. Open Terminal (Applications → Utilities → Terminal)
2. Type: `python3 --version`
3. If you see a version number, Python is installed!

**On Linux:**
1. Open Terminal
2. Type: `python3 --version`
3. If you see a version number, Python is installed!

### Step 2: Install Python (if needed)

**Windows:**
1. Go to [python.org](https://python.org)
2. Click "Downloads"
3. Download the latest version (3.11 or higher)
4. Run the installer
5. **Important**: Check "Add Python to PATH" during installation

**Mac:**
1. Go to [python.org](https://python.org)
2. Click "Downloads"
3. Download the latest version
4. Run the installer

**Linux:**
```bash
sudo apt update
sudo apt install python3
```

## 📝 Writing Your First Python Code

### Method 1: Using a Text Editor

**Step 1: Choose a Text Editor**
- **VS Code** (recommended) - Free, powerful, great for beginners
- **PyCharm** - Professional IDE, free community version
- **Sublime Text** - Fast and lightweight
- **Notepad++** (Windows) - Simple and effective

**Step 2: Create a Python File**
1. Open your text editor
2. Create a new file
3. Save it with `.py` extension (e.g., `hello.py`)

**Step 3: Write Your Code**
```python
# This is your first Python program!
print("Hello, World!")
print("Welcome to Python programming!")
```

**Step 4: Save the File**
- Save as `hello.py` in a folder you can find easily

### Method 2: Using Python IDLE (Built-in)

**Step 1: Open IDLE**
- Windows: Search for "IDLE" in Start menu
- Mac: Applications → Python → IDLE
- Linux: Type `idle3` in terminal

**Step 2: Create New File**
- File → New File
- Write your code
- File → Save As → `hello.py`

## 🚀 Running Your Python Code

### Method 1: Command Line/Terminal

**Windows:**
1. Open Command Prompt
2. Navigate to your file: `cd C:\path\to\your\folder`
3. Run: `python hello.py`

**Mac/Linux:**
1. Open Terminal
2. Navigate to your file: `cd /path/to/your/folder`
3. Run: `python3 hello.py`

### Method 2: From Your Text Editor

**VS Code:**
1. Open your `.py` file
2. Press `F5` or click the play button
3. Select "Python" as the debugger

**PyCharm:**
1. Right-click in the editor
2. Select "Run 'filename'"

**IDLE:**
1. Press `F5` or
2. Run → Run Module

## 🔧 Setting Up a Development Environment

### Recommended: VS Code Setup

**Step 1: Install VS Code**
1. Go to [code.visualstudio.com](https://code.visualstudio.com)
2. Download and install

**Step 2: Install Python Extension**
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "Python"
4. Install the Microsoft Python extension

**Step 3: Create a Workspace**
1. File → Open Folder
2. Create a new folder for your Python projects
3. Create a new file: `hello.py`

**Step 4: Write and Run**
```python
# hello.py
print("Hello from VS Code!")
print("Python is awesome!")
```

Press `F5` to run!

## 📁 Organizing Your Code

### Best Practices for File Organization

**Create a Project Structure:**
```
MyPythonProjects/
├── lesson1/
│   ├── hello.py
│   └── variables.py
├── lesson2/
│   ├── functions.py
│   └── loops.py
└── projects/
    └── rock_paper_scissors.py
```

### File Naming Conventions

**Good Names:**
- `hello_world.py`
- `calculator.py`
- `game.py`
- `my_program.py`

**Avoid:**
- `file1.py`
- `test.py`
- `program.py`
- Names with spaces or special characters

## 🐛 Common Issues and Solutions

### Issue 1: "Python is not recognized"

**Solution:**
- Windows: Reinstall Python and check "Add to PATH"
- Mac/Linux: Use `python3` instead of `python`

### Issue 2: "Permission denied"

**Solution:**
- Mac/Linux: Use `chmod +x filename.py`
- Or run with: `python3 filename.py`

### Issue 3: "File not found"

**Solution:**
- Make sure you're in the right directory
- Use `ls` (Mac/Linux) or `dir` (Windows) to see files
- Use `cd` to change directories

## 🎮 Interactive Python (REPL)

### Using Python Interactively

**Start Python Shell:**
```bash
# Windows
python

# Mac/Linux
python3
```

**You'll see:**
```
Python 3.11.0 (main, Oct 24 2022, 18:26:48)
[GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

**Try these commands:**
```python
>>> print("Hello!")
Hello!
>>> 2 + 2
4
>>> name = "Alice"
>>> print("Hello, " + name)
Hello, Alice
>>> exit()
```

## 📋 Your First Complete Program

Let's create a simple program that demonstrates the setup:

**File: `first_program.py`**
```python
# My First Python Program
# This program introduces me to Python

# Print a welcome message
print("Welcome to Python Programming!")
print("=" * 30)

# Get user input
name = input("What's your name? ")
age = input("How old are you? ")

# Display personalized message
print(f"Hello, {name}! You are {age} years old.")
print("You're now a Python programmer!")

# Do some math
birth_year = 2024 - int(age)
print(f"You were probably born around {birth_year}")

print("=" * 30)
print("Program completed successfully!")
```

## 🎯 Running Your First Program

**Step 1: Save the code above as `first_program.py`**

**Step 2: Run it:**
```bash
# Windows
python first_program.py

# Mac/Linux
python3 first_program.py
```

**Step 3: Follow the prompts and see the output!**

## 📝 Key Takeaways

- **Python installation** is straightforward on all platforms
- **Text editors** like VS Code make coding easier
- **File organization** helps keep your projects tidy
- **Command line** is powerful for running Python programs
- **Interactive Python** is great for testing small code snippets
- **File extensions** (`.py`) are important for Python files

## 🎯 Next Steps

In the next lesson, we'll write our first real Python program and learn about the basic building blocks of programming!

---

**💡 Practice Exercise**: Create a file called `practice.py` and write a program that:
1. Asks for your favorite color
2. Asks for your favorite number
3. Prints a message using both pieces of information

**🔍 Challenge**: Try running Python interactively and experiment with different commands like `print()`, math operations, and `input()`! 