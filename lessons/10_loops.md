# Chapter 10: Loops

## 🎯 Learning Objectives
- Understand what loops are and why they're useful
- Learn how to use for loops and while loops
- Master loop control with break and continue
- Practice iterating through different data types
- Understand nested loops and complex iteration

## 🔄 What are Loops?

**Loops** allow you to repeat code multiple times without writing it over and over. Think of them as a way to automate repetitive tasks.

### Real-World Analogy: Assembly Line

Think of loops like an assembly line:
- **For loop**: "Do this task 10 times" (you know how many times)
- **While loop**: "Keep doing this task until the condition changes" (you don't know how many times)

## 🔤 For Loops

**For loops** are used when you know how many times you want to repeat something.

### Basic For Loop

```python
for item in sequence:
    # Code to repeat
    print(item)
```

### For Loop with Range

```python
# Loop 5 times (0, 1, 2, 3, 4)
for i in range(5):
    print(f"Count: {i}")

# Loop from 1 to 5
for i in range(1, 6):
    print(f"Number: {i}")

# Loop with step (every 2 numbers)
for i in range(0, 10, 2):
    print(f"Even number: {i}")
```

### For Loop with Lists

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(f"I like {fruit}!")

# Loop with index
for i, fruit in enumerate(fruits):
    print(f"Fruit {i}: {fruit}")
```

### For Loop with Strings

```python
message = "Hello"

for letter in message:
    print(f"Letter: {letter}")

# Loop through words
words = message.split()
for word in words:
    print(f"Word: {word}")
```

## 🔁 While Loops

**While loops** continue as long as a condition is True.

### Basic While Loop

```python
while condition:
    # Code to repeat
    print("Looping...")
```

### Counter While Loop

```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
```

### User Input While Loop

```python
password = "secret"
attempts = 0

while attempts < 3:
    guess = input("Enter password: ")
    if guess == password:
        print("Correct!")
        break
    else:
        attempts += 1
        print(f"Wrong! {3 - attempts} attempts left")
```

## 🎮 Loop Examples

### Example 1: Number Patterns

```python
# Print numbers 1 to 10
print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# Print even numbers
print("Even numbers 2 to 20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# Print multiplication table
number = 5
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
```

### Example 2: List Processing

```python
# Calculate sum of numbers
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print(f"Sum: {total}")

# Find maximum number
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

print(f"Maximum: {max_num}")

# Filter even numbers
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Even numbers: {even_numbers}")
```

### Example 3: String Processing

```python
# Count vowels in a string
text = "Hello, World!"
vowels = "aeiouAEIOU"
vowel_count = 0

for letter in text:
    if letter in vowels:
        vowel_count += 1

print(f"Vowels in '{text}': {vowel_count}")

# Reverse a string
reversed_text = ""
for letter in text:
    reversed_text = letter + reversed_text

print(f"Reversed: {reversed_text}")
```

## 🔧 Loop Control

### Break Statement

**Break** exits the loop immediately.

```python
# Find first even number
numbers = [1, 3, 5, 6, 7, 8, 9]

for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
```

### Continue Statement

**Continue** skips the rest of the current iteration and continues with the next.

```python
# Print only odd numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i, end=" ")
print()
```

### Loop with Else

The **else** clause runs when the loop completes normally (not broken).

```python
# Search for a number
numbers = [1, 2, 3, 4, 5]
search_for = 6

for num in numbers:
    if num == search_for:
        print(f"Found {search_for}!")
        break
else:
    print(f"{search_for} not found!")
```

## 🏗️ Nested Loops

Loops can be nested inside other loops.

### Example: Multiplication Table

```python
# Print multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{result:2}", end=" ")
    print()  # New line after each row
```

### Example: Pattern Printing

```python
# Print triangle pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

### Example: List of Lists

```python
# Process 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

## 🎯 Advanced Loop Examples

### Example 1: Password Generator

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ""
    
    for _ in range(length):
        password += random.choice(characters)
    
    return password

# Generate passwords
for i in range(3):
    password = generate_password(8)
    print(f"Password {i+1}: {password}")
```

### Example 2: Number Guessing Game

```python
import random

def number_guessing_game():
    secret = random.randint(1, 100)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100...")
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {attempts} attempts!")
            break

# Play the game
# number_guessing_game()  # Uncomment to play
```

### Example 3: Shopping Cart

```python
def shopping_cart():
    cart = []
    
    while True:
        print("\n1. Add item")
        print("2. View cart")
        print("3. Checkout")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            item = input("Enter item name: ")
            price = float(input("Enter item price: "))
            cart.append({"item": item, "price": price})
            print(f"{item} added to cart!")
            
        elif choice == "2":
            if not cart:
                print("Cart is empty!")
            else:
                print("Shopping Cart:")
                total = 0
                for item in cart:
                    print(f"- {item['item']}: ${item['price']}")
                    total += item['price']
                print(f"Total: ${total}")
                
        elif choice == "3":
            if not cart:
                print("Cart is empty!")
            else:
                total = sum(item['price'] for item in cart)
                print(f"Total: ${total}")
                print("Thank you for shopping!")
                break
                
        elif choice == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice!")

# Run shopping cart
# shopping_cart()  # Uncomment to run
```

## 🔍 Loop Patterns

### Pattern 1: Accumulator

```python
# Sum numbers
total = 0
for i in range(1, 11):
    total += i
print(f"Sum: {total}")

# Product of numbers
product = 1
for i in range(1, 6):
    product *= i
print(f"Product: {product}")
```

### Pattern 2: Counter

```python
# Count occurrences
numbers = [1, 2, 2, 3, 2, 4, 5]
count = 0

for num in numbers:
    if num == 2:
        count += 1

print(f"Number 2 appears {count} times")
```

### Pattern 3: Filter

```python
# Filter positive numbers
numbers = [-1, 2, -3, 4, -5, 6]
positive = []

for num in numbers:
    if num > 0:
        positive.append(num)

print(f"Positive numbers: {positive}")
```

### Pattern 4: Transform

```python
# Double all numbers
numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print(f"Doubled: {doubled}")
```

## 🐛 Common Loop Mistakes

### Mistake 1: Infinite While Loop

```python
# Wrong - infinite loop
count = 0
while count < 5:
    print(count)
    # Missing count += 1

# Correct
count = 0
while count < 5:
    print(count)
    count += 1
```

### Mistake 2: Modifying List While Iterating

```python
# Wrong - can cause issues
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        numbers.remove(num)  # Modifying list while iterating

# Better - create new list
numbers = [1, 2, 3, 4, 5]
filtered = []
for num in numbers:
    if num != 3:
        filtered.append(num)
```

### Mistake 3: Wrong Range

```python
# Wrong - off-by-one error
for i in range(5):  # 0, 1, 2, 3, 4
    print(i + 1)    # 1, 2, 3, 4, 5

# Better - use correct range
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)
```

## 🎮 Practice Examples

### Example 1: Factorial Calculator

```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test factorial
for i in range(1, 6):
    print(f"{i}! = {factorial(i)}")
```

### Example 2: Prime Number Checker

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find prime numbers
primes = []
for i in range(2, 20):
    if is_prime(i):
        primes.append(i)

print(f"Prime numbers: {primes}")
```

### Example 3: Word Counter

```python
def count_words(text):
    words = text.split()
    word_count = {}
    
    for word in words:
        word = word.lower().strip(".,!?")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

# Test word counter
text = "Hello world! Hello Python! Python is awesome!"
result = count_words(text)
for word, count in result.items():
    print(f"'{word}': {count}")
```

## 📝 Key Takeaways

- **Loops** repeat code multiple times
- **For loops** are used when you know the number of iterations
- **While loops** continue until a condition becomes False
- **Break** exits a loop immediately
- **Continue** skips to the next iteration
- **Nested loops** allow complex iteration patterns
- **Range()** generates sequences for for loops
- **Enumerate()** provides both index and value
- **Loops** are essential for processing collections of data

## 🎯 Next Steps

In the next lesson, we'll learn about **Rock Paper Scissors game rules** and start building our final project!

---

**💡 Practice Exercise**: Create a program that:
1. Uses a for loop to print the first 10 Fibonacci numbers
2. Uses a while loop to find the first number divisible by both 3 and 7
3. Uses nested loops to create a pattern
4. Uses break and continue in appropriate situations

**🔍 Challenge**: Create a program that simulates a simple calculator with a menu loop that continues until the user chooses to exit! 