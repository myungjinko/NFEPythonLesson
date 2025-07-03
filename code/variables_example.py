# Variables and Data Types Example
# This file demonstrates all the concepts from Chapter 6

print("=" * 50)
print("VARIABLES AND DATA TYPES DEMONSTRATION")
print("=" * 50)

# ============================================================================
# 1. BASIC VARIABLE CREATION
# ============================================================================
print("\n1. BASIC VARIABLE CREATION")
print("-" * 30)

# Creating different types of variables
name = "Alice"
age = 25
height = 5.6
is_student = True
favorite_colors = ["blue", "green", "purple"]

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")
print(f"Favorite Colors: {favorite_colors}")

# ============================================================================
# 2. DATA TYPES
# ============================================================================
print("\n2. DATA TYPES")
print("-" * 30)

# Check data types
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")
print(f"Type of is_student: {type(is_student)}")
print(f"Type of favorite_colors: {type(favorite_colors)}")

# ============================================================================
# 3. STRING OPERATIONS
# ============================================================================
print("\n3. STRING OPERATIONS")
print("-" * 30)

first_name = "Alice"
last_name = "Smith"

# Concatenation
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# String repetition
stars = "*" * 10
print(f"Stars: {stars}")

# String length
print(f"Length of first_name: {len(first_name)}")

# ============================================================================
# 4. NUMBER OPERATIONS
# ============================================================================
print("\n4. NUMBER OPERATIONS")
print("-" * 30)

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Integer Division: {a} // {b} = {a // b}")
print(f"Modulo: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# ============================================================================
# 5. FLOAT OPERATIONS
# ============================================================================
print("\n5. FLOAT OPERATIONS")
print("-" * 30)

pi = 3.14159
radius = 5.0

area = pi * radius ** 2
circumference = 2 * pi * radius

print(f"Pi: {pi}")
print(f"Radius: {radius}")
print(f"Area: {area}")
print(f"Circumference: {circumference}")

# ============================================================================
# 6. BOOLEAN OPERATIONS
# ============================================================================
print("\n6. BOOLEAN OPERATIONS")
print("-" * 30)

is_sunny = True
is_raining = False
is_warm = True

print(f"Is sunny: {is_sunny}")
print(f"Is raining: {is_raining}")
print(f"Is warm: {is_warm}")

# Boolean logic
print(f"Good weather: {is_sunny and is_warm}")
print(f"Bad weather: {is_raining or not is_warm}")
print(f"Not sunny: {not is_sunny}")

# ============================================================================
# 7. LIST OPERATIONS
# ============================================================================
print("\n7. LIST OPERATIONS")
print("-" * 30)

fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")

# Accessing list items
print(f"First fruit: {fruits[0]}")
print(f"Last number: {numbers[-1]}")

# List length
print(f"Number of fruits: {len(fruits)}")

# Adding items
fruits.append("grape")
print(f"After adding grape: {fruits}")

# ============================================================================
# 8. TYPE CONVERSION
# ============================================================================
print("\n8. TYPE CONVERSION")
print("-" * 30)

# String to number
age_string = "25"
age_number = int(age_string)
print(f"Age string: '{age_string}' -> Age number: {age_number}")

# Number to string
score = 100
score_string = str(score)
print(f"Score number: {score} -> Score string: '{score_string}'")

# Integer to float
whole = 5
decimal = float(whole)
print(f"Whole number: {whole} -> Decimal: {decimal}")

# Float to integer
decimal_num = 5.7
whole_num = int(decimal_num)
print(f"Decimal: {decimal_num} -> Whole: {whole_num}")

# ============================================================================
# 9. UPDATING VARIABLES
# ============================================================================
print("\n9. UPDATING VARIABLES")
print("-" * 30)

score = 0
print(f"Initial score: {score}")

score = score + 10
print(f"After adding 10: {score}")

score += 5
print(f"After += 5: {score}")

score -= 3
print(f"After -= 3: {score}")

score *= 2
print(f"After *= 2: {score}")

# ============================================================================
# 10. MULTIPLE ASSIGNMENT
# ============================================================================
print("\n10. MULTIPLE ASSIGNMENT")
print("-" * 30)

# Assign multiple variables at once
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")

# Assign same value to multiple variables
a = b = c = 0
print(f"a = {a}, b = {b}, c = {c}")

# ============================================================================
# 11. STRING FORMATTING
# ============================================================================
print("\n11. STRING FORMATTING")
print("-" * 30)

name = "Alice"
age = 25
city = "New York"

# F-strings (recommended)
message1 = f"Hello, {name}! You are {age} years old and live in {city}."
print(f"F-string: {message1}")

# With expressions
message2 = f"In 5 years, {name} will be {age + 5} years old."
print(f"F-string with expression: {message2}")

# Using .format()
message3 = "Hello, {}! You are {} years old and live in {}.".format(name, age, city)
print(f".format(): {message3}")

# ============================================================================
# 12. PRACTICAL EXAMPLE: PERSONAL INFO
# ============================================================================
print("\n12. PRACTICAL EXAMPLE: PERSONAL INFO")
print("-" * 30)

# Store personal information
first_name = "Alice"
last_name = "Smith"
age = 25
height = 5.6
is_student = True
favorite_subjects = ["Math", "Science", "Art"]

# Display information
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Student: {is_student}")
print(f"Favorite subjects: {favorite_subjects}")

# Calculate age in months
age_in_months = age * 12
print(f"Age in months: {age_in_months}")

# Calculate height in inches
height_inches = height * 12
print(f"Height in inches: {height_inches}")

# ============================================================================
# 13. PRACTICAL EXAMPLE: SHOPPING CALCULATOR
# ============================================================================
print("\n13. PRACTICAL EXAMPLE: SHOPPING CALCULATOR")
print("-" * 30)

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

# ============================================================================
# 14. INTERACTIVE EXAMPLE
# ============================================================================
print("\n14. INTERACTIVE EXAMPLE")
print("-" * 30)

# Get user input and demonstrate variables
print("Let's create some variables with your input!")

user_name = input("What's your name? ")
user_age = input("How old are you? ")
user_favorite_number = input("What's your favorite number? ")

# Convert age to integer and favorite number to integer
user_age_int = int(user_age)
user_favorite_int = int(user_favorite_number)

# Calculate some things
age_in_10_years = user_age_int + 10
favorite_squared = user_favorite_int ** 2

# Display results
print(f"\nGreat! Here's what I learned about you:")
print(f"Name: {user_name}")
print(f"Age: {user_age_int}")
print(f"Favorite number: {user_favorite_int}")
print(f"In 10 years, you'll be {age_in_10_years} years old!")
print(f"Your favorite number squared is {favorite_squared}!")

print("\n" + "=" * 50)
print("VARIABLES DEMONSTRATION COMPLETE!")
print("=" * 50) 