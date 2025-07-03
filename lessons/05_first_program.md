# Chapter 5: Your First Python Program

## 🎯 Learning Objectives
- Write and understand your first complete Python program
- Learn about comments, print statements, and input
- Understand basic program structure
- Practice running and testing your code

## 🚀 Writing Your First Program

Let's start with the classic "Hello, World!" program and then build something more interesting!

### Program 1: Hello, World!

**File: `hello_world.py`**
```python
# This is my first Python program
print("Hello, World!")
```

**Let's break it down:**
- `#` - This is a **comment**. Comments are notes for humans, not code for computers
- `print()` - This is a **function** that displays text on the screen
- `"Hello, World!"` - This is a **string** (text enclosed in quotes)

### Program 2: Interactive Greeting

**File: `greeting.py`**
```python
# Interactive Greeting Program
# This program asks for your name and greets you

# Print a welcome message
print("Welcome to my first Python program!")

# Ask for the user's name and store it
name = input("What's your name? ")

# Print a personalized greeting
print("Hello, " + name + "!")
print("Nice to meet you!")
```

**Let's break it down:**
- `name = input("What's your name? ")` - This line:
  - Shows the message "What's your name? "
  - Waits for you to type something and press Enter
  - Stores what you typed in a **variable** called `name`
- `print("Hello, " + name + "!")` - This combines text with the name you entered

## 📝 Understanding Program Structure

### 1. **Comments**
Comments explain what your code does:

```python
# This is a single-line comment
print("This is code")

# You can have multiple comments
# to explain complex parts
print("More code")

"""
This is a multi-line comment.
You can write several lines
to explain your program.
"""
```

### 2. **Print Statements**
`print()` displays information:

```python
print("Simple text")
print(42)                    # Numbers
print("Text" + " " + "more") # Combining text
print("Line 1")
print("Line 2")              # Each print is on a new line
```

### 3. **Input Statements**
`input()` gets information from the user:

```python
# Basic input
name = input("Enter your name: ")

# Input with explanation
age = input("How old are you? ")

# Input for numbers (but still comes as text)
favorite_number = input("What's your favorite number? ")
```

## 🎮 Your First Interactive Program

Let's create a fun program that asks questions and responds!

**File: `conversation.py`**
```python
# Conversation Program
# This program has a conversation with the user

print("=" * 40)
print("Welcome to the Python Conversation Bot!")
print("=" * 40)

# Get user information
name = input("What's your name? ")
age = input("How old are you? ")
favorite_color = input("What's your favorite color? ")

# Have a conversation
print(f"\nNice to meet you, {name}!")
print(f"You're {age} years old - that's a great age!")
print(f"I love the color {favorite_color} too!")

# Do some fun calculations
birth_year = 2024 - int(age)
print(f"You were probably born around {birth_year}")

# Ask more questions
hobby = input("What's your favorite hobby? ")
print(f"That's awesome! {hobby} sounds like fun!")

# Say goodbye
print(f"\nThanks for chatting with me, {name}!")
print("Have a great day!")
print("=" * 40)
```

## 🔧 Understanding the Code

### String Formatting
There are several ways to combine text and variables:

**Method 1: Using + (concatenation)**
```python
name = "Alice"
print("Hello, " + name + "!")
```

**Method 2: Using f-strings (recommended)**
```python
name = "Alice"
print(f"Hello, {name}!")
```

**Method 3: Using .format()**
```python
name = "Alice"
print("Hello, {}!".format(name))
```

### Converting Data Types
Sometimes you need to convert between different types of data:

```python
# Input always gives you a string
age_text = input("How old are you? ")  # "25" (string)

# Convert string to integer for math
age_number = int(age_text)             # 25 (integer)

# Now you can do math
birth_year = 2024 - age_number
```

## 🎯 Practice Programs

### Program 3: Simple Calculator

**File: `calculator.py`**
```python
# Simple Calculator
# This program adds two numbers

print("Simple Calculator")
print("-" * 20)

# Get two numbers from the user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert to integers and add
result = int(num1) + int(num2)

# Show the result
print(f"{num1} + {num2} = {result}")
```

### Program 4: Story Generator

**File: `story.py`**
```python
# Story Generator
# This program creates a fun story using user input

print("Story Generator")
print("=" * 30)

# Get story elements from user
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")

# Create the story
print(f"\nOnce upon a time, {name} went to {place}.")
print(f"While there, {name} saw a {animal} eating {food}.")
print(f"The {animal} was very happy to share the {food} with {name}.")
print("They became best friends and lived happily ever after!")
print("\nThe End!")
```

## 🐛 Common Mistakes and How to Fix Them

### Mistake 1: Forgetting Quotes
```python
# Wrong
print(Hello, World!)

# Correct
print("Hello, World!")
```

### Mistake 2: Wrong Indentation
```python
# Wrong (extra spaces)
    print("Hello")

# Correct
print("Hello")
```

### Mistake 3: Forgetting to Convert Input
```python
# Wrong (will give error)
age = input("How old are you? ")
result = age + 5  # Can't add string and number

# Correct
age = input("How old are you? ")
result = int(age) + 5  # Convert to integer first
```

## 🎮 Interactive Practice

Try running Python interactively and experiment:

```python
>>> print("Hello!")
>>> name = input("What's your name? ")
>>> print("Hello, " + name)
>>> age = input("How old are you? ")
>>> print("You are " + age + " years old")
>>> int(age) + 5
```

## 📋 Complete Program Example

Here's a complete program that demonstrates everything we've learned:

**File: `complete_program.py`**
```python
# Complete Python Program Example
# This program demonstrates all the basic concepts

print("=" * 50)
print("Welcome to the Complete Python Program!")
print("=" * 50)

# Get user information
print("\nLet's get to know each other!")
name = input("What's your name? ")
age = input("How old are you? ")
city = input("What city do you live in? ")

# Process the information
age_number = int(age)
birth_year = 2024 - age_number

# Display results
print(f"\nGreat! Here's what I learned about you:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Birth year: approximately {birth_year}")

# Do some fun calculations
print(f"\nFun facts:")
print(f"You've been alive for about {age_number * 365} days!")
print(f"In 10 years, you'll be {age_number + 10} years old!")

# Ask for a number and do math
favorite_number = input(f"\nWhat's your favorite number, {name}? ")
number = int(favorite_number)
print(f"Your number squared is: {number * number}")
print(f"Your number plus 10 is: {number + 10}")

# Say goodbye
print(f"\nThanks for using my program, {name}!")
print("Come back soon!")
print("=" * 50)
```

## 📝 Key Takeaways

- **Comments** (`#`) help explain your code
- **print()** displays information on the screen
- **input()** gets information from the user
- **Variables** store information for later use
- **f-strings** make it easy to combine text and variables
- **int()** converts text to numbers for math
- **Programs** are made up of instructions that run in order

## 🎯 Next Steps

In the next lesson, we'll learn about **variables and data types** - the building blocks for storing and working with information!

---

**💡 Practice Exercise**: Create a program called `my_info.py` that:
1. Asks for your name, age, and favorite movie
2. Calculates how old you'll be in 5 years
3. Prints a message about your favorite movie
4. Uses f-strings for all the output

**🔍 Challenge**: Try creating a program that asks for 3 numbers and calculates their average! 