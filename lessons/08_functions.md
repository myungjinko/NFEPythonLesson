# Chapter 8: Functions and Return Values

## 🎯 Learning Objectives
- Understand what functions are and why they're useful
- Learn how to create and call functions
- Master function parameters and arguments
- Understand return values and how to use them
- Practice creating reusable code blocks

## 🔧 What are Functions?

**Functions** are reusable blocks of code that perform specific tasks. Think of them as mini-programs within your program that you can call whenever you need them.

### Real-World Analogy: Kitchen Appliances

Think of functions like kitchen appliances:
- **Microwave**: You put food in, press a button, and get heated food out
- **Blender**: You put ingredients in, turn it on, and get a smoothie out
- **Coffee Maker**: You put coffee grounds and water in, and get coffee out

Functions work the same way:
- **Input**: You give them data (parameters)
- **Process**: They do something with that data
- **Output**: They give you back a result (return value)

## 🏗️ Creating Functions

### Basic Function Syntax

```python
def function_name():
    # Function code goes here
    print("This is inside the function")

# Calling the function
function_name()
```

### Your First Function

```python
def greet():
    print("Hello, World!")
    print("Welcome to Python functions!")

# Call the function
greet()
```

## 📥 Function Parameters

**Parameters** are like variables that hold the data you pass to a function.

### Function with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")
    print("Nice to meet you!")

# Call with different arguments
greet("Alice")
greet("Bob")
greet("Charlie")
```

### Multiple Parameters

```python
def introduce(name, age, city):
    print(f"Hi, I'm {name}")
    print(f"I'm {age} years old")
    print(f"I live in {city}")

# Call with multiple arguments
introduce("Alice", 25, "New York")
introduce("Bob", 30, "Los Angeles")
```

## 📤 Return Values

**Return values** are what functions give back to you after they finish their work.

### Function with Return Value

```python
def add_numbers(a, b):
    result = a + b
    return result

# Use the return value
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

# You can use return values in expressions
total = add_numbers(10, 20) + add_numbers(5, 5)
print(f"Total: {total}")
```

### Multiple Return Values

```python
def get_name_and_age():
    name = "Alice"
    age = 25
    return name, age

# Unpack multiple return values
person_name, person_age = get_name_and_age()
print(f"Name: {person_name}, Age: {person_age}")
```

## 🎮 Function Examples

### Example 1: Simple Calculator Functions

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"

# Use the functions
print(f"5 + 3 = {add(5, 3)}")
print(f"10 - 4 = {subtract(10, 4)}")
print(f"6 * 7 = {multiply(6, 7)}")
print(f"15 / 3 = {divide(15, 3)}")
```

### Example 2: String Processing Functions

```python
def make_uppercase(text):
    return text.upper()

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def reverse_text(text):
    return text[::-1]

# Test the functions
message = "Hello, World!"
print(f"Original: {message}")
print(f"Uppercase: {make_uppercase(message)}")
print(f"Vowel count: {count_vowels(message)}")
print(f"Reversed: {reverse_text(message)}")
```

### Example 3: Temperature Converter

```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def get_weather_advice(temperature_celsius):
    if temperature_celsius > 30:
        return "It's hot! Stay hydrated."
    elif temperature_celsius > 20:
        return "Nice weather! Enjoy the day."
    elif temperature_celsius > 10:
        return "It's cool. Wear a jacket."
    else:
        return "It's cold! Bundle up."

# Test the functions
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
advice = get_weather_advice(temp_c)

print(f"{temp_c}°C = {temp_f}°F")
print(f"Weather advice: {advice}")
```

## 🔄 Function Flow

### Understanding Function Execution

```python
def process_data(name, age):
    print("Step 1: Function starts")
    print(f"Step 2: Processing {name}, age {age}")
    
    if age >= 18:
        status = "adult"
    else:
        status = "minor"
    
    print(f"Step 3: {name} is a {status}")
    print("Step 4: Function ends")
    return status

# When you call this function:
result = process_data("Alice", 25)
print(f"Step 5: Function returned: {result}")
```

## 🎯 Default Parameters

You can give parameters default values that are used if no argument is provided.

```python
def greet(name="World"):
    print(f"Hello, {name}!")

# Call with argument
greet("Alice")  # Prints: Hello, Alice!

# Call without argument (uses default)
greet()         # Prints: Hello, World!

def create_profile(name, age=18, city="Unknown"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

# Different ways to call
create_profile("Alice")                    # Uses defaults for age and city
create_profile("Bob", 25)                  # Uses default for city
create_profile("Charlie", 30, "Boston")    # Uses all provided values
```

## 🔍 Local vs Global Variables

### Understanding Variable Scope

```python
# Global variable
global_name = "Alice"

def test_function():
    # Local variable
    local_name = "Bob"
    print(f"Inside function: {local_name}")
    print(f"Global variable: {global_name}")

# Call function
test_function()

# This works - global variable
print(f"Outside function: {global_name}")

# This would cause an error - local variable not accessible
# print(local_name)  # Error!
```

## 🎮 Advanced Function Examples

### Example 1: Grade Calculator

```python
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_grade_message(grade):
    messages = {
        "A": "Excellent work!",
        "B": "Good job!",
        "C": "Satisfactory",
        "D": "Needs improvement",
        "F": "Failed"
    }
    return messages.get(grade, "Unknown grade")

# Use the functions
score = 85
grade = calculate_grade(score)
message = get_grade_message(grade)

print(f"Score: {score}")
print(f"Grade: {grade}")
print(f"Message: {message}")
```

### Example 2: Shopping Cart

```python
def add_item(cart, item, price):
    cart.append({"item": item, "price": price})
    return cart

def remove_item(cart, item_name):
    for i, item in enumerate(cart):
        if item["item"] == item_name:
            del cart[i]
            break
    return cart

def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["price"]
    return total

def display_cart(cart):
    if not cart:
        print("Cart is empty")
        return
    
    print("Shopping Cart:")
    for item in cart:
        print(f"- {item['item']}: ${item['price']}")
    
    total = calculate_total(cart)
    print(f"Total: ${total}")

# Test the shopping cart
my_cart = []
my_cart = add_item(my_cart, "Apple", 0.50)
my_cart = add_item(my_cart, "Banana", 0.30)
my_cart = add_item(my_cart, "Orange", 0.75)

display_cart(my_cart)

my_cart = remove_item(my_cart, "Banana")
display_cart(my_cart)
```

### Example 3: Number Game

```python
import random

def generate_number(min_val=1, max_val=100):
    return random.randint(min_val, max_val)

def check_guess(secret, guess):
    if guess < secret:
        return "Too low!"
    elif guess > secret:
        return "Too high!"
    else:
        return "Correct!"

def play_number_game():
    secret_number = generate_number()
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100...")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        result = check_guess(secret_number, guess)
        print(result)
        
        if result == "Correct!":
            print(f"You got it in {attempts} attempts!")
            break

# Play the game
# play_number_game()  # Uncomment to play
```

## 🐛 Common Function Mistakes

### Mistake 1: Forgetting Return Statement

```python
# Wrong - function doesn't return anything
def add_numbers(a, b):
    result = a + b
    # Missing return statement

# Correct
def add_numbers(a, b):
    result = a + b
    return result
```

### Mistake 2: Wrong Parameter Names

```python
# Wrong - parameter name doesn't match usage
def greet(name):
    print(f"Hello, {user_name}!")  # user_name is not defined

# Correct
def greet(name):
    print(f"Hello, {name}!")
```

### Mistake 3: Not Using Return Values

```python
# Wrong - ignoring return value
def get_full_name(first, last):
    return f"{first} {last}"

get_full_name("Alice", "Smith")  # Return value is ignored

# Correct - use the return value
full_name = get_full_name("Alice", "Smith")
print(full_name)
```

## 📝 Key Takeaways

- **Functions** are reusable blocks of code
- **Parameters** are inputs to functions
- **Return values** are outputs from functions
- **Default parameters** provide fallback values
- **Local variables** are only accessible inside functions
- **Functions** help organize and reuse code
- **Always use return** when you want to get data back from a function

## 🎯 Next Steps

In the next lesson, we'll learn about **conditional statements (if/else)** - how to make decisions in your code!

---

**💡 Practice Exercise**: Create a function that:
1. Takes a person's name and age as parameters
2. Returns a personalized message based on their age
3. Uses default parameters for some values
4. Calls the function with different arguments

**🔍 Challenge**: Create a function that takes a list of numbers and returns both the sum and average of those numbers! 