# Chapter 6: Variables and Data Types

## 🎯 Learning Objectives
- Understand what variables are and how to use them
- Learn about different data types in Python
- Master creating and modifying variables
- Practice working with numbers, text, and other data

## 📦 What are Variables?

**Variables** are like containers that store information in your computer's memory. Think of them as labeled boxes where you can put different types of data.

### Real-World Analogy: Storage Boxes

Imagine you have storage boxes in your room:
- A box labeled "name" contains "Alice"
- A box labeled "age" contains 25
- A box labeled "favorite_color" contains "blue"

In Python, these would be:
```python
name = "Alice"
age = 25
favorite_color = "blue"
```

## 🔤 Creating Variables

### Basic Variable Creation

**Syntax:** `variable_name = value`

```python
# Creating variables
name = "Alice"
age = 25
height = 5.6
is_student = True

# Using variables
print(name)
print(age)
print(height)
print(is_student)
```

### Variable Naming Rules

**Good Names:**
```python
first_name = "Alice"
last_name = "Smith"
user_age = 25
favorite_color = "blue"
is_active = True
```

**Bad Names:**
```python
# Don't use spaces
first name = "Alice"  # Error!

# Don't start with numbers
1name = "Alice"       # Error!

# Don't use special characters (except _)
user-name = "Alice"   # Error!

# Don't use Python keywords
if = "something"      # Error!
```

## 📊 Data Types in Python

Python has several built-in data types. Let's explore them:

### 1. **Strings (str)**
Strings are text enclosed in quotes.

```python
# String examples
name = "Alice"
message = 'Hello, World!'
address = """123 Main Street
New York, NY 10001"""

# String operations
print(name + " " + "Smith")  # Concatenation
print(name * 3)              # Repetition
print(len(name))             # Length
```

### 2. **Integers (int)**
Whole numbers (positive, negative, or zero).

```python
# Integer examples
age = 25
temperature = -5
year = 2024
count = 0

# Integer operations
print(age + 5)      # Addition
print(age - 3)      # Subtraction
print(age * 2)      # Multiplication
print(age / 2)      # Division (gives float)
print(age // 2)     # Integer division
print(age % 3)      # Modulo (remainder)
print(age ** 2)     # Exponentiation
```

### 3. **Floats (float)**
Decimal numbers.

```python
# Float examples
height = 5.6
weight = 150.5
pi = 3.14159
temperature = 98.6

# Float operations
print(height + 0.5)
print(weight * 2.2)  # Convert to kg
print(pi * 2)
```

### 4. **Booleans (bool)**
True or False values.

```python
# Boolean examples
is_student = True
is_working = False
is_sunny = True

# Boolean operations
print(is_student and is_sunny)  # True and True = True
print(is_student or is_working) # True or False = True
print(not is_working)           # not False = True
```

### 5. **Lists (list)**
Collections of items in square brackets.

```python
# List examples
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]

# List operations
print(fruits[0])        # First item
print(len(fruits))      # Number of items
fruits.append("grape")  # Add item
print(fruits)
```

## 🔍 Checking Data Types

Use the `type()` function to see what type a variable is:

```python
name = "Alice"
age = 25
height = 5.6
is_student = True

print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student)) # <class 'bool'>
```

## 🔄 Converting Between Data Types

Sometimes you need to convert one data type to another:

### String Conversions
```python
# Convert to string
age = 25
age_string = str(age)
print(age_string)  # "25"
print(type(age_string))  # <class 'str'>

# Convert from string
age_text = "25"
age_number = int(age_text)
print(age_number)  # 25
print(type(age_number))  # <class 'int'>
```

### Number Conversions
```python
# Integer to float
whole_number = 5
decimal_number = float(whole_number)
print(decimal_number)  # 5.0

# Float to integer
decimal = 5.7
whole = int(decimal)
print(whole)  # 5 (truncates decimal part)
```

## 🎮 Working with Variables

### Updating Variables
```python
# Start with a value
score = 0
print(f"Score: {score}")

# Update the value
score = score + 10
print(f"Score: {score}")

# Shortcut for adding
score += 5
print(f"Score: {score}")

# Other shortcuts
score -= 3    # score = score - 3
score *= 2    # score = score * 2
score /= 4    # score = score / 4
```

### Multiple Assignment
```python
# Assign multiple variables at once
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3

# Assign same value to multiple variables
a = b = c = 0
print(a, b, c)  # 0 0 0
```

## 📝 String Formatting with Variables

### F-strings (Recommended)
```python
name = "Alice"
age = 25
city = "New York"

# F-string formatting
message = f"Hello, {name}! You are {age} years old and live in {city}."
print(message)

# With expressions
print(f"In 5 years, {name} will be {age + 5} years old.")
```

### Other String Formatting Methods
```python
name = "Alice"
age = 25

# Using .format()
message = "Hello, {}! You are {} years old.".format(name, age)

# Using % (older method)
message = "Hello, %s! You are %d years old." % (name, age)
```

## 🎯 Practice Examples

### Example 1: Personal Information
```python
# Store personal information
first_name = "Alice"
last_name = "Smith"
age = 25
height = 5.6
is_student = True

# Display information
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Student: {is_student}")

# Calculate age in months
age_in_months = age * 12
print(f"Age in months: {age_in_months}")
```

### Example 2: Shopping Calculator
```python
# Store item prices
apple_price = 0.50
banana_price = 0.30
orange_price = 0.75

# Store quantities
apple_count = 3
banana_count = 5
orange_count = 2

# Calculate totals
apple_total = apple_price * apple_count
banana_total = banana_price * banana_count
orange_total = orange_price * orange_count

# Calculate grand total
total = apple_total + banana_total + orange_total

# Display results
print("Shopping Receipt:")
print(f"Apples: {apple_count} x ${apple_price} = ${apple_total}")
print(f"Bananas: {banana_count} x ${banana_price} = ${banana_total}")
print(f"Oranges: {orange_count} x ${orange_price} = ${orange_total}")
print(f"Total: ${total}")
```

### Example 3: Temperature Converter
```python
# Get temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display result
print(f"{celsius}°C is equal to {fahrenheit}°F")

# Check if it's hot or cold
if fahrenheit > 80:
    print("It's hot!")
elif fahrenheit < 50:
    print("It's cold!")
else:
    print("It's nice weather!")
```

## 🐛 Common Variable Mistakes

### Mistake 1: Using Undefined Variables
```python
# Wrong
print(name)  # Error: name is not defined

# Correct
name = "Alice"
print(name)
```

### Mistake 2: Wrong Data Type for Operations
```python
# Wrong
age = "25"
result = age + 5  # Error: can't add string and integer

# Correct
age = "25"
result = int(age) + 5
```

### Mistake 3: Forgetting to Convert Input
```python
# Wrong
number = input("Enter a number: ")
result = number * 2  # This repeats the string, doesn't multiply

# Correct
number = input("Enter a number: ")
result = int(number) * 2
```

## 📝 Key Takeaways

- **Variables** are containers that store data in memory
- **Data types** include strings, integers, floats, booleans, and lists
- **Variable names** should be descriptive and follow naming rules
- **Type conversion** is important when working with different data types
- **F-strings** are the best way to format strings with variables
- **Variables can be updated** and modified throughout your program

## 🎯 Next Steps

In the next lesson, we'll learn about **code blocks and indentation** - how Python organizes code into logical groups!

---

**💡 Practice Exercise**: Create a program that:
1. Stores your name, age, and favorite number in variables
2. Calculates how old you'll be in 10 years
3. Calculates your favorite number squared
4. Prints all the information using f-strings

**🔍 Challenge**: Create a program that converts between different units (like meters to feet, or Celsius to Fahrenheit) using variables! 