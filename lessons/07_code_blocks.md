# Chapter 7: Code Blocks and Indentation

## 🎯 Learning Objectives
- Understand what code blocks are and why they're important
- Learn how Python uses indentation to organize code
- Master proper indentation techniques
- Understand scope and code organization

## 📦 What are Code Blocks?

**Code blocks** are groups of related code statements that work together. Think of them as paragraphs in a book - they group related ideas together.

### Real-World Analogy: Building Blocks

Imagine you're building with LEGO blocks:
- Each block is a line of code
- Groups of blocks form structures (code blocks)
- The way you arrange blocks matters (indentation)

## 🔤 Indentation in Python

Python uses **indentation** (spaces or tabs) to show which code belongs together. This is different from many other programming languages that use curly braces `{}`.

### Basic Indentation Rules

**Rule 1: Use consistent indentation**
```python
# Good - using 4 spaces
if condition:
    print("This is indented")
    print("This is also indented")
print("This is not indented")

# Bad - mixing spaces and tabs
if condition:
    print("This uses spaces")
	print("This uses tabs")  # Error!
```

**Rule 2: Indent after colons `:`**
```python
# After if statements
if age >= 18:
    print("You are an adult")

# After for loops
for i in range(5):
    print(i)

# After function definitions
def greet():
    print("Hello!")
```

## 🏗️ Types of Code Blocks

### 1. **Conditional Blocks (if/else)**

```python
# Simple if block
if temperature > 30:
    print("It's hot!")
    print("Wear light clothes")
    print("Stay hydrated")

# If-else block
if score >= 80:
    print("Great job!")
    print("You passed!")
else:
    print("Keep trying!")
    print("Study more next time")

# If-elif-else block
if grade >= 90:
    print("A - Excellent!")
elif grade >= 80:
    print("B - Good job!")
elif grade >= 70:
    print("C - Satisfactory")
else:
    print("F - Needs improvement")
```

### 2. **Loop Blocks (for/while)**

```python
# For loop block
for i in range(3):
    print(f"Count: {i}")
    print("Still in the loop")
print("Loop finished")

# While loop block
count = 0
while count < 3:
    print(f"Count is: {count}")
    count += 1
    print("Still counting...")
print("Counting finished")
```

### 3. **Function Blocks**

```python
def greet(name):
    print(f"Hello, {name}!")
    print("Welcome to Python!")
    return "Greeting sent"

def calculate_area(length, width):
    area = length * width
    print(f"Area: {area}")
    return area
```

## 🎯 Understanding Scope

**Scope** refers to where variables can be accessed in your code.

### Global vs Local Scope

```python
# Global variable (accessible everywhere)
global_name = "Alice"

def greet():
    # Local variable (only accessible inside function)
    local_message = "Hello!"
    print(f"{local_message} {global_name}")

# This works - global_name is accessible
print(global_name)

# This would cause an error - local_message is not accessible here
# print(local_message)  # Error!
```

## 🔍 Indentation Examples

### Example 1: Nested Conditions

```python
age = 25
has_license = True

if age >= 18:
    print("You are an adult")
    if has_license:
        print("You can drive")
        print("Be careful on the road")
    else:
        print("You need to get a license")
else:
    print("You are a minor")
    if age >= 16:
        print("You can get a learner's permit")
    else:
        print("You're too young to drive")
```

### Example 2: Loops with Conditions

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
        print("Even numbers are cool!")
    else:
        print(f"{i} is odd")
        print("Odd numbers are interesting!")
    print("Still in the loop")
print("Loop finished")
```

### Example 3: Functions with Multiple Blocks

```python
def analyze_number(number):
    if number > 0:
        print("Positive number")
        if number > 100:
            print("That's a big number!")
        else:
            print("That's a reasonable size")
    elif number < 0:
        print("Negative number")
        print("Don't be so negative!")
    else:
        print("Zero")
        print("The neutral number")
    
    # This runs regardless of the condition
    print("Analysis complete")
```

## 🐛 Common Indentation Mistakes

### Mistake 1: Inconsistent Indentation

```python
# Wrong - mixing spaces and tabs
if condition:
    print("This uses spaces")
	print("This uses tabs")  # Error!

# Correct - use only spaces (recommended)
if condition:
    print("This uses spaces")
    print("This also uses spaces")
```

### Mistake 2: Missing Indentation

```python
# Wrong - missing indentation
if age >= 18:
print("You are an adult")  # Error!

# Correct - proper indentation
if age >= 18:
    print("You are an adult")
```

### Mistake 3: Extra Indentation

```python
# Wrong - extra indentation
    print("This is over-indented")  # Error!

# Correct - proper indentation
print("This is correctly indented")
```

### Mistake 4: Wrong Indentation Level

```python
# Wrong - inconsistent indentation levels
if condition:
    print("Level 1")
  print("Level 2")  # Error!

# Correct - consistent indentation
if condition:
    print("Level 1")
    print("Level 1")
```

## 🎮 Practice Examples

### Example 1: Grade Calculator

```python
def calculate_grade(score):
    if score >= 90:
        grade = "A"
        message = "Excellent work!"
    elif score >= 80:
        grade = "B"
        message = "Good job!"
    elif score >= 70:
        grade = "C"
        message = "Satisfactory"
    elif score >= 60:
        grade = "D"
        message = "Needs improvement"
    else:
        grade = "F"
        message = "Failed"
    
    print(f"Grade: {grade}")
    print(f"Message: {message}")
    return grade

# Test the function
calculate_grade(85)
```

### Example 2: Number Analyzer

```python
def analyze_numbers():
    for i in range(1, 6):
        print(f"Analyzing number: {i}")
        
        if i == 1:
            print("First number")
        elif i == 5:
            print("Last number")
        else:
            print("Middle number")
        
        if i % 2 == 0:
            print("Even number")
        else:
            print("Odd number")
        
        print("-" * 20)

analyze_numbers()
```

### Example 3: Shopping List Processor

```python
def process_shopping_list(items):
    total_items = len(items)
    print(f"Processing {total_items} items...")
    
    for item in items:
        print(f"Processing: {item}")
        
        if len(item) > 5:
            print("That's a long item name!")
        else:
            print("Short and sweet!")
        
        if "milk" in item.lower():
            print("Don't forget to refrigerate!")
        elif "bread" in item.lower():
            print("Keep it fresh!")
        else:
            print("Regular item")
        
        print()

# Test the function
shopping_list = ["Milk", "Bread", "Apples", "Chocolate"]
process_shopping_list(shopping_list)
```

## 🔧 Best Practices

### 1. **Use 4 Spaces (Not Tabs)**
```python
# Good - 4 spaces
if condition:
    print("Indented with 4 spaces")

# Avoid tabs - they can cause issues
```

### 2. **Be Consistent**
```python
# Good - consistent indentation
def function1():
    if condition:
        print("Level 1")
        print("Level 1")
    print("Level 0")

def function2():
    if condition:
        print("Level 1")
        print("Level 1")
    print("Level 0")
```

### 3. **Use Clear Block Structure**
```python
# Good - clear structure
if user_age >= 18:
    if has_id:
        print("Welcome!")
        print("You can enter")
    else:
        print("Need ID")
        print("Please get your ID")
else:
    print("Too young")
    print("Come back when older")
```

## 📝 Key Takeaways

- **Code blocks** group related code statements together
- **Indentation** is how Python shows which code belongs together
- **Use 4 spaces** for indentation (not tabs)
- **Indent after colons** (`:`)
- **Be consistent** with your indentation
- **Scope** determines where variables can be accessed
- **Proper indentation** is essential for Python to work correctly

## 🎯 Next Steps

In the next lesson, we'll learn about **functions and return values** - how to create reusable blocks of code!

---

**💡 Practice Exercise**: Create a program with multiple code blocks that:
1. Asks for a number
2. Uses if/elif/else to categorize it (small, medium, large)
3. Uses a for loop to count from 1 to that number
4. Uses proper indentation throughout

**🔍 Challenge**: Create a function that has nested if statements and loops, demonstrating different levels of indentation! 