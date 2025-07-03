# Exercise 1: Variables and Data Types
# Practice working with variables, data types, and basic operations

print("=" * 50)
print("EXERCISE 1: VARIABLES AND DATA TYPES")
print("=" * 50)

# ============================================================================
# TASK 1: Create Variables
# ============================================================================
print("\nTASK 1: Create Variables")
print("-" * 30)

# TODO: Create variables for your personal information
# Replace the placeholder values with your actual information

name = "Your Name"  # Replace with your name
age = 0  # Replace with your age
height = 0.0  # Replace with your height in feet
is_student = True  # Replace with True or False
favorite_colors = ["blue", "red", "green"]  # Replace with your favorite colors

# Display your information
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Student: {is_student}")
print(f"Favorite colors: {favorite_colors}")

# ============================================================================
# TASK 2: Data Type Operations
# ============================================================================
print("\nTASK 2: Data Type Operations")
print("-" * 30)

# TODO: Perform operations with your variables

# Calculate age in months
age_in_months = age * 12
print(f"Age in months: {age_in_months}")

# Calculate height in inches
height_inches = height * 12
print(f"Height in inches: {height_inches}")

# Count favorite colors
color_count = len(favorite_colors)
print(f"Number of favorite colors: {color_count}")

# ============================================================================
# TASK 3: String Operations
# ============================================================================
print("\nTASK 3: String Operations")
print("-" * 30)

# TODO: Work with string variables

# Create a full name (if you have a first and last name)
first_name = "First"  # Replace with your first name
last_name = "Last"    # Replace with your last name

# Combine first and last name
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Get the length of your name
name_length = len(full_name)
print(f"Name length: {name_length} characters")

# Convert name to uppercase
upper_name = full_name.upper()
print(f"Uppercase name: {upper_name}")

# ============================================================================
# TASK 4: Number Operations
# ============================================================================
print("\nTASK 4: Number Operations")
print("-" * 30)

# TODO: Perform mathematical operations

# Create some numbers to work with
number1 = 10
number2 = 3

# Basic operations
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
remainder = number1 % number2
power = number1 ** number2

print(f"{number1} + {number2} = {addition}")
print(f"{number1} - {number2} = {subtraction}")
print(f"{number1} * {number2} = {multiplication}")
print(f"{number1} / {number2} = {division}")
print(f"{number1} % {number2} = {remainder}")
print(f"{number1} ** {number2} = {power}")

# ============================================================================
# TASK 5: Type Conversion
# ============================================================================
print("\nTASK 5: Type Conversion")
print("-" * 30)

# TODO: Practice converting between data types

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

# ============================================================================
# TASK 6: Boolean Operations
# ============================================================================
print("\nTASK 6: Boolean Operations")
print("-" * 30)

# TODO: Work with boolean values

is_sunny = True
is_raining = False
is_warm = True

# Boolean logic
good_weather = is_sunny and is_warm
bad_weather = is_raining or not is_warm
not_sunny = not is_sunny

print(f"Is sunny: {is_sunny}")
print(f"Is raining: {is_raining}")
print(f"Is warm: {is_warm}")
print(f"Good weather: {good_weather}")
print(f"Bad weather: {bad_weather}")
print(f"Not sunny: {not_sunny}")

# ============================================================================
# TASK 7: List Operations
# ============================================================================
print("\nTASK 7: List Operations")
print("-" * 30)

# TODO: Work with lists

# Create a list of your favorite foods
favorite_foods = ["pizza", "sushi", "ice cream"]  # Replace with your favorites

print(f"Favorite foods: {favorite_foods}")
print(f"Number of foods: {len(favorite_foods)}")
print(f"First food: {favorite_foods[0]}")
print(f"Last food: {favorite_foods[-1]}")

# Add a new food
favorite_foods.append("chocolate")
print(f"After adding chocolate: {favorite_foods}")

# ============================================================================
# TASK 8: Interactive Variables
# ============================================================================
print("\nTASK 8: Interactive Variables")
print("-" * 30)

# TODO: Get user input and create variables

print("Let's create some variables with your input!")

# Get user information
user_name = input("What's your favorite animal? ")
user_number = input("What's your lucky number? ")
user_city = input("What city would you like to visit? ")

# Convert number to integer
user_number_int = int(user_number)

# Display the information
print(f"\nGreat! Here's what you told me:")
print(f"Favorite animal: {user_name}")
print(f"Lucky number: {user_number_int}")
print(f"City to visit: {user_city}")

# Do some calculations
number_squared = user_number_int ** 2
print(f"Your lucky number squared: {number_squared}")

print("\n" + "=" * 50)
print("EXERCISE 1 COMPLETE!")
print("=" * 50)

# ============================================================================
# BONUS CHALLENGE
# ============================================================================
print("\nBONUS CHALLENGE:")
print("Create a program that calculates the area and perimeter of a rectangle")
print("using variables for length and width.")

# TODO: Complete the bonus challenge
length = 5
width = 3

area = length * width
perimeter = 2 * (length + width)

print(f"Rectangle with length {length} and width {width}:")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}") 