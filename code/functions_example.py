# Functions and Return Values Example
# This file demonstrates all the concepts from Chapter 8

print("=" * 50)
print("FUNCTIONS AND RETURN VALUES DEMONSTRATION")
print("=" * 50)

# ============================================================================
# 1. BASIC FUNCTIONS
# ============================================================================
print("\n1. BASIC FUNCTIONS")
print("-" * 30)

def greet():
    print("Hello, World!")
    print("Welcome to Python functions!")

def say_goodbye():
    print("Goodbye!")
    print("See you later!")

# Call the functions
greet()
say_goodbye()

# ============================================================================
# 2. FUNCTIONS WITH PARAMETERS
# ============================================================================
print("\n2. FUNCTIONS WITH PARAMETERS")
print("-" * 30)

def greet_person(name):
    print(f"Hello, {name}!")
    print("Nice to meet you!")

def introduce(name, age, city):
    print(f"Hi, I'm {name}")
    print(f"I'm {age} years old")
    print(f"I live in {city}")

# Call with different arguments
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")

introduce("Alice", 25, "New York")
introduce("Bob", 30, "Los Angeles")

# ============================================================================
# 3. FUNCTIONS WITH RETURN VALUES
# ============================================================================
print("\n3. FUNCTIONS WITH RETURN VALUES")
print("-" * 30)

def add_numbers(a, b):
    result = a + b
    return result

def multiply_numbers(a, b):
    return a * b

def get_full_name(first, last):
    return f"{first} {last}"

# Use return values
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

product = multiply_numbers(6, 7)
print(f"6 * 7 = {product}")

full_name = get_full_name("Alice", "Smith")
print(f"Full name: {full_name}")

# Use return values in expressions
total = add_numbers(10, 20) + add_numbers(5, 5)
print(f"Total: {total}")

# ============================================================================
# 4. MULTIPLE RETURN VALUES
# ============================================================================
print("\n4. MULTIPLE RETURN VALUES")
print("-" * 30)

def get_person_info():
    name = "Alice"
    age = 25
    city = "New York"
    return name, age, city

def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

# Unpack multiple return values
person_name, person_age, person_city = get_person_info()
print(f"Name: {person_name}, Age: {person_age}, City: {person_city}")

numbers_list = [1, 2, 3, 4, 5]
total_sum, avg = calculate_stats(numbers_list)
print(f"Numbers: {numbers_list}")
print(f"Sum: {total_sum}, Average: {avg}")

# ============================================================================
# 5. DEFAULT PARAMETERS
# ============================================================================
print("\n5. DEFAULT PARAMETERS")
print("-" * 30)

def greet_with_default(name="World"):
    print(f"Hello, {name}!")

def create_profile(name, age=18, city="Unknown"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

# Call with different numbers of arguments
greet_with_default("Alice")  # Uses provided argument
greet_with_default()         # Uses default

create_profile("Alice")                    # Uses defaults for age and city
create_profile("Bob", 25)                  # Uses default for city
create_profile("Charlie", 30, "Boston")    # Uses all provided values

# ============================================================================
# 6. CALCULATOR FUNCTIONS
# ============================================================================
print("\n6. CALCULATOR FUNCTIONS")
print("-" * 30)

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

# Test calculator functions
print(f"5 + 3 = {add(5, 3)}")
print(f"10 - 4 = {subtract(10, 4)}")
print(f"6 * 7 = {multiply(6, 7)}")
print(f"15 / 3 = {divide(15, 3)}")
print(f"10 / 0 = {divide(10, 0)}")

# ============================================================================
# 7. STRING PROCESSING FUNCTIONS
# ============================================================================
print("\n7. STRING PROCESSING FUNCTIONS")
print("-" * 30)

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

def count_words(text):
    return len(text.split())

# Test string functions
message = "Hello, World!"
print(f"Original: {message}")
print(f"Uppercase: {make_uppercase(message)}")
print(f"Vowel count: {count_vowels(message)}")
print(f"Reversed: {reverse_text(message)}")
print(f"Word count: {count_words(message)}")

# ============================================================================
# 8. TEMPERATURE CONVERTER FUNCTIONS
# ============================================================================
print("\n8. TEMPERATURE CONVERTER FUNCTIONS")
print("-" * 30)

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

# Test temperature functions
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
advice = get_weather_advice(temp_c)

print(f"{temp_c}°C = {temp_f}°F")
print(f"Weather advice: {advice}")

# Convert back
temp_c_back = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c_back}°C")

# ============================================================================
# 9. GRADE CALCULATOR FUNCTIONS
# ============================================================================
print("\n9. GRADE CALCULATOR FUNCTIONS")
print("-" * 30)

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

def calculate_gpa(grades):
    grade_points = {
        "A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0
    }
    total_points = 0
    for grade in grades:
        total_points += grade_points.get(grade, 0)
    return total_points / len(grades)

# Test grade functions
scores = [85, 92, 78, 95, 88]
grades = []

for score in scores:
    grade = calculate_grade(score)
    grades.append(grade)
    message = get_grade_message(grade)
    print(f"Score: {score} -> Grade: {grade} - {message}")

gpa = calculate_gpa(grades)
print(f"Overall GPA: {gpa:.2f}")

# ============================================================================
# 10. SHOPPING CART FUNCTIONS
# ============================================================================
print("\n10. SHOPPING CART FUNCTIONS")
print("-" * 30)

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

# Test shopping cart
my_cart = []
my_cart = add_item(my_cart, "Apple", 0.50)
my_cart = add_item(my_cart, "Banana", 0.30)
my_cart = add_item(my_cart, "Orange", 0.75)
my_cart = add_item(my_cart, "Milk", 2.50)

display_cart(my_cart)

my_cart = remove_item(my_cart, "Banana")
display_cart(my_cart)

# ============================================================================
# 11. NUMBER GAME FUNCTIONS
# ============================================================================
print("\n11. NUMBER GAME FUNCTIONS")
print("-" * 30)

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

def get_hint(secret, guess):
    difference = abs(secret - guess)
    if difference <= 5:
        return "Very close!"
    elif difference <= 15:
        return "Getting warmer!"
    else:
        return "Still far away!"

# Test number game functions
secret_number = generate_number(1, 50)
print(f"Secret number: {secret_number}")  # Normally you wouldn't show this!

test_guesses = [10, 25, 35, 42]
for guess in test_guesses:
    result = check_guess(secret_number, guess)
    hint = get_hint(secret_number, guess)
    print(f"Guess: {guess} -> {result} ({hint})")

# ============================================================================
# 12. UTILITY FUNCTIONS
# ============================================================================
print("\n12. UTILITY FUNCTIONS")
print("-" * 30)

def is_even(number):
    return number % 2 == 0

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test utility functions
test_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in test_numbers:
    even_status = "even" if is_even(num) else "odd"
    prime_status = "prime" if is_prime(num) else "not prime"
    print(f"{num}: {even_status}, {prime_status}")

print(f"Factorial of 5: {factorial(5)}")
print(f"Fibonacci(7): {fibonacci(7)}")

# ============================================================================
# 13. INTERACTIVE FUNCTION DEMO
# ============================================================================
print("\n13. INTERACTIVE FUNCTION DEMO")
print("-" * 30)

def get_user_info():
    name = input("What's your name? ")
    age = int(input("How old are you? "))
    favorite_number = int(input("What's your favorite number? "))
    return name, age, favorite_number

def create_personalized_message(name, age, favorite_number):
    if age < 18:
        status = "young"
    elif age < 65:
        status = "adult"
    else:
        status = "senior"
    
    if favorite_number % 2 == 0:
        number_type = "even"
    else:
        number_type = "odd"
    
    message = f"Hello {name}! As a {status} person, you chose the {number_type} number {favorite_number}."
    return message

# Uncomment the lines below to run the interactive demo
# print("Let's create a personalized message!")
# user_name, user_age, user_fav_num = get_user_info()
# personalized_msg = create_personalized_message(user_name, user_age, user_fav_num)
# print(f"\n{personalized_msg}")

print("Interactive demo skipped (uncomment code to run)")

# ============================================================================
# 14. FUNCTION COMPOSITION
# ============================================================================
print("\n14. FUNCTION COMPOSITION")
print("-" * 30)

def double(x):
    return x * 2

def add_five(x):
    return x + 5

def square(x):
    return x ** 2

# Compose functions
def double_then_add_five(x):
    return add_five(double(x))

def square_then_double(x):
    return double(square(x))

def complex_operation(x):
    return add_five(double(square(x)))

# Test function composition
test_value = 3
print(f"Original value: {test_value}")
print(f"Double then add 5: {double_then_add_five(test_value)}")
print(f"Square then double: {square_then_double(test_value)}")
print(f"Square, double, then add 5: {complex_operation(test_value)}")

print("\n" + "=" * 50)
print("FUNCTIONS DEMONSTRATION COMPLETE!")
print("=" * 50) 