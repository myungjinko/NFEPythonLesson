# Chapter 9: Conditional Statements (if/else)

## 🎯 Learning Objectives
- Understand what conditional statements are and why they're important
- Learn how to use if, elif, and else statements
- Master comparison operators and logical operators
- Practice making decisions in your code
- Understand nested conditions and complex logic

## 🤔 What are Conditional Statements?

**Conditional statements** allow your program to make decisions based on certain conditions. Think of them as the "if-then" logic that helps your program choose different paths.

### Real-World Analogy: Traffic Lights

Think of conditional statements like traffic lights:
- **If** the light is green → **then** go
- **If** the light is red → **then** stop
- **If** the light is yellow → **then** slow down

In programming, we use similar logic to make decisions.

## 🔤 Basic if Statement

### Simple if Statement

```python
if condition:
    # Code to run if condition is True
    print("Condition is True!")
```

### Your First if Statement

```python
age = 18

if age >= 18:
    print("You are an adult!")
    print("You can vote!")
    print("You can drive!")

print("This always runs")
```

## 🔍 Comparison Operators

These operators help you compare values:

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `age == 18` |
| `!=` | Not equal to | `age != 18` |
| `>` | Greater than | `age > 18` |
| `<` | Less than | `age < 18` |
| `>=` | Greater than or equal to | `age >= 18` |
| `<=` | Less than or equal to | `age <= 18` |

### Examples with Comparison Operators

```python
# Equal to
if age == 18:
    print("You are exactly 18!")

# Not equal to
if age != 18:
    print("You are not 18!")

# Greater than
if age > 18:
    print("You are older than 18!")

# Less than
if age < 18:
    print("You are younger than 18!")

# Greater than or equal to
if age >= 18:
    print("You are 18 or older!")

# Less than or equal to
if age <= 18:
    print("You are 18 or younger!")
```

## 🔄 if-else Statements

**else** provides an alternative when the condition is False.

```python
if condition:
    # Code to run if condition is True
    print("Condition is True!")
else:
    # Code to run if condition is False
    print("Condition is False!")
```

### Example: Age Checker

```python
age = 16

if age >= 18:
    print("You are an adult!")
    print("You can vote and drive!")
else:
    print("You are a minor!")
    print("You need to wait a few more years!")
```

## 🔀 if-elif-else Statements

**elif** (else if) allows you to check multiple conditions in order.

```python
if condition1:
    # Code for condition1
    print("Condition 1 is True!")
elif condition2:
    # Code for condition2
    print("Condition 2 is True!")
elif condition3:
    # Code for condition3
    print("Condition 3 is True!")
else:
    # Code if no conditions are True
    print("None of the conditions are True!")
```

### Example: Grade Calculator

```python
score = 85

if score >= 90:
    print("Grade: A")
    print("Excellent work!")
elif score >= 80:
    print("Grade: B")
    print("Good job!")
elif score >= 70:
    print("Grade: C")
    print("Satisfactory")
elif score >= 60:
    print("Grade: D")
    print("Needs improvement")
else:
    print("Grade: F")
    print("Failed")
```

## 🔗 Logical Operators

These operators help you combine conditions:

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both conditions must be True | `age >= 18 and has_license` |
| `or` | At least one condition must be True | `age >= 18 or has_parent` |
| `not` | Reverses the condition | `not is_minor` |

### Examples with Logical Operators

```python
age = 20
has_license = True
has_money = False

# AND operator - both must be True
if age >= 18 and has_license:
    print("You can drive alone!")

# OR operator - at least one must be True
if age >= 18 or has_license:
    print("You have some driving privileges!")

# NOT operator - reverses the condition
if not has_money:
    print("You need to get some money!")

# Complex conditions
if age >= 18 and has_license and not has_money:
    print("You can drive but you're broke!")
```

## 🎮 Conditional Statement Examples

### Example 1: Weather Advisor

```python
temperature = 25
is_raining = False
is_sunny = True

if temperature > 30:
    print("It's hot! Stay hydrated!")
elif temperature > 20:
    if is_sunny:
        print("Nice weather! Perfect for a walk!")
    else:
        print("It's cool but not sunny.")
elif temperature > 10:
    print("It's cool. Wear a jacket!")
else:
    print("It's cold! Bundle up!")

if is_raining:
    print("Don't forget your umbrella!")
```

### Example 2: Shopping Discount

```python
purchase_amount = 150
is_member = True
is_holiday = False

# Calculate discount
discount = 0

if purchase_amount >= 100:
    discount += 10  # 10% off for purchases over $100

if is_member:
    discount += 5   # 5% off for members

if is_holiday:
    discount += 15  # 15% off for holiday sales

final_price = purchase_amount * (1 - discount / 100)

print(f"Original price: ${purchase_amount}")
print(f"Discount: {discount}%")
print(f"Final price: ${final_price:.2f}")
```

### Example 3: Password Checker

```python
def check_password(password):
    has_letter = False
    has_number = False
    has_special = False
    
    # Check each character
    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True
        else:
            has_special = True
    
    # Evaluate password strength
    if len(password) < 8:
        return "Too short! Password must be at least 8 characters."
    elif not has_letter:
        return "Weak! Password must contain letters."
    elif not has_number:
        return "Weak! Password must contain numbers."
    elif not has_special:
        return "Good! But could be stronger with special characters."
    else:
        return "Strong password!"

# Test passwords
passwords = ["abc", "password123", "MyP@ssw0rd!"]
for pwd in passwords:
    result = check_password(pwd)
    print(f"Password '{pwd}': {result}")
```

## 🏗️ Nested Conditions

You can put conditions inside other conditions.

### Example: Driving License Check

```python
age = 20
has_license = True
has_car = False
has_money = True

if age >= 18:
    print("You are old enough to drive!")
    
    if has_license:
        print("You have a license!")
        
        if has_car:
            print("You have a car!")
            
            if has_money:
                print("You can drive anywhere!")
            else:
                print("You need money for gas!")
        else:
            print("You need to borrow or rent a car!")
    else:
        print("You need to get a license first!")
else:
    print("You are too young to drive!")
    if age >= 16:
        print("But you can get a learner's permit!")
```

## 🔍 Complex Conditions

### Example: Movie Ticket System

```python
age = 25
is_student = True
is_matinee = False
is_3d = True

# Calculate ticket price
base_price = 12

if age < 3:
    price = 0
    print("Free ticket for babies!")
elif age < 12:
    price = base_price * 0.5
    print("Child discount applied!")
elif age >= 65:
    price = base_price * 0.7
    print("Senior discount applied!")
else:
    price = base_price

# Student discount
if is_student and age >= 12:
    price *= 0.8
    print("Student discount applied!")

# Matinee discount
if is_matinee:
    price *= 0.8
    print("Matinee discount applied!")

# 3D surcharge
if is_3d:
    price += 3
    print("3D surcharge added!")

print(f"Final ticket price: ${price:.2f}")
```

## 🎯 Conditional Expressions (Ternary Operator)

A shorter way to write simple if-else statements.

### Traditional if-else
```python
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"
```

### Conditional Expression
```python
age = 20
status = "adult" if age >= 18 else "minor"
```

### More Examples
```python
# Find the larger number
a, b = 5, 10
larger = a if a > b else b

# Check if number is even or odd
number = 7
result = "even" if number % 2 == 0 else "odd"

# Grade check
score = 85
grade = "pass" if score >= 60 else "fail"
```

## 🐛 Common Conditional Mistakes

### Mistake 1: Using = instead of ==
```python
# Wrong
if age = 18:  # This assigns, doesn't compare
    print("You are 18!")

# Correct
if age == 18:  # This compares
    print("You are 18!")
```

### Mistake 2: Missing Colon
```python
# Wrong
if age >= 18
    print("Adult!")

# Correct
if age >= 18:
    print("Adult!")
```

### Mistake 3: Wrong Indentation
```python
# Wrong
if age >= 18:
print("Adult!")  # Missing indentation

# Correct
if age >= 18:
    print("Adult!")  # Proper indentation
```

### Mistake 4: Unnecessary Conditions
```python
# Wrong
if age >= 18:
    if age < 65:
        print("Working age")

# Better
if 18 <= age < 65:
    print("Working age")
```

## 🎮 Practice Examples

### Example 1: Number Analyzer

```python
def analyze_number(number):
    print(f"Analyzing number: {number}")
    
    if number == 0:
        print("This is zero!")
    elif number > 0:
        print("This is a positive number!")
        if number % 2 == 0:
            print("It's also even!")
        else:
            print("It's also odd!")
    else:
        print("This is a negative number!")
        if number % 2 == 0:
            print("It's also even!")
        else:
            print("It's also odd!")

# Test the function
analyze_number(0)
analyze_number(7)
analyze_number(-4)
```

### Example 2: Rock Paper Scissors Logic

```python
def determine_winner(player, computer):
    if player == computer:
        return "Tie!"
    elif player == "rock":
        if computer == "scissors":
            return "You win!"
        else:
            return "Computer wins!"
    elif player == "paper":
        if computer == "rock":
            return "You win!"
        else:
            return "Computer wins!"
    elif player == "scissors":
        if computer == "paper":
            return "You win!"
        else:
            return "Computer wins!"
    else:
        return "Invalid choice!"

# Test the function
print(determine_winner("rock", "scissors"))  # You win!
print(determine_winner("paper", "rock"))     # You win!
print(determine_winner("scissors", "rock"))  # Computer wins!
```

### Example 3: Time Greeter

```python
import datetime

def greet_by_time():
    current_hour = datetime.datetime.now().hour
    
    if 5 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 17:
        return "Good afternoon!"
    elif 17 <= current_hour < 21:
        return "Good evening!"
    else:
        return "Good night!"

# Get current greeting
greeting = greet_by_time()
print(greeting)
```

## 📝 Key Takeaways

- **Conditional statements** help your program make decisions
- **if** runs code when a condition is True
- **else** provides an alternative when the condition is False
- **elif** checks additional conditions
- **Comparison operators** (`==`, `!=`, `>`, `<`, `>=`, `<=`) compare values
- **Logical operators** (`and`, `or`, `not`) combine conditions
- **Nested conditions** allow complex decision-making
- **Conditional expressions** provide a shorter syntax for simple if-else
- **Proper indentation** is crucial for conditional statements

## 🎯 Next Steps

In the next lesson, we'll learn about **loops** - how to repeat code multiple times!

---

**💡 Practice Exercise**: Create a program that:
1. Asks for a person's age and income
2. Uses if/elif/else to determine their tax bracket
3. Uses logical operators to check multiple conditions
4. Provides different advice based on the results

**🔍 Challenge**: Create a program that simulates a simple ATM with conditions for checking balance, withdrawal limits, and account status! 