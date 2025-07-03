# Chapter 11: Rock Paper Scissors Game Rules

## 🎯 Learning Objectives
- Understand the rules of Rock Paper Scissors
- Learn the game logic and winning conditions
- Plan the program structure for the game
- Understand how to implement game mechanics
- Prepare for building the complete game

## 🎮 What is Rock Paper Scissors?

**Rock Paper Scissors** is a classic hand game where two players simultaneously choose one of three options: rock, paper, or scissors. The winner is determined by specific rules that create a circular relationship between the choices.

### Game Rules

1. **Rock** crushes **Scissors** (Rock wins)
2. **Scissors** cuts **Paper** (Scissors wins)
3. **Paper** covers **Rock** (Paper wins)
4. If both players choose the same option, it's a **tie**

## 🔄 Game Logic

### Winning Combinations

| Player Choice | Computer Choice | Result | Reason |
|---------------|-----------------|--------|--------|
| Rock | Scissors | Player Wins | Rock crushes Scissors |
| Rock | Paper | Computer Wins | Paper covers Rock |
| Rock | Rock | Tie | Same choice |
| Paper | Rock | Player Wins | Paper covers Rock |
| Paper | Scissors | Computer Wins | Scissors cuts Paper |
| Paper | Paper | Tie | Same choice |
| Scissors | Paper | Player Wins | Scissors cuts Paper |
| Scissors | Rock | Computer Wins | Rock crushes Scissors |
| Scissors | Scissors | Tie | Same choice |

### Visual Representation

```
    Rock
   /    \
  /      \
Paper -- Scissors
```

- Rock beats Scissors
- Scissors beats Paper  
- Paper beats Rock

## 🏗️ Program Structure

### What Our Game Will Include

1. **Welcome and Instructions**
   - Explain the game
   - Show the rules
   - Ask if player wants to play

2. **Game Loop**
   - Get player's choice
   - Generate computer's choice
   - Determine winner
   - Display results
   - Ask to play again

3. **Score Tracking**
   - Keep track of wins, losses, and ties
   - Display current score
   - Show final score when quitting

4. **Input Validation**
   - Check for valid player input
   - Handle invalid choices gracefully

## 🎯 Game Flow

### Step-by-Step Process

1. **Start Game**
   - Display welcome message
   - Show rules
   - Initialize score counters

2. **Get Player Input**
   - Ask player to choose (rock/paper/scissors)
   - Validate input
   - Convert to standardized format

3. **Generate Computer Choice**
   - Use random number generator
   - Convert number to choice (rock/paper/scissors)

4. **Determine Winner**
   - Compare player and computer choices
   - Apply game rules
   - Determine result (win/lose/tie)

5. **Display Results**
   - Show both choices
   - Announce winner
   - Update score

6. **Continue or Quit**
   - Ask if player wants to play again
   - If yes, repeat from step 2
   - If no, show final score and exit

## 🔧 Implementation Plan

### Functions We'll Need

1. **`display_welcome()`**
   - Show game title and rules
   - Explain how to play

2. **`get_player_choice()`**
   - Ask for player input
   - Validate and return choice

3. **`get_computer_choice()`**
   - Generate random choice
   - Return computer's selection

4. **`determine_winner(player, computer)`**
   - Compare choices
   - Return result (win/lose/tie)

5. **`display_results(player, computer, result)`**
   - Show both choices
   - Announce winner
   - Display current score

6. **`play_game()`**
   - Main game loop
   - Coordinate all functions

### Data Structures

1. **Choices List**
   ```python
   choices = ["rock", "paper", "scissors"]
   ```

2. **Score Dictionary**
   ```python
   score = {
       "wins": 0,
       "losses": 0,
       "ties": 0
   }
   ```

3. **Winning Combinations Dictionary**
   ```python
   winning_combinations = {
       "rock": "scissors",
       "scissors": "paper", 
       "paper": "rock"
   }
   ```

## 🎮 Game Logic Implementation

### Method 1: Using if-elif-else Statements

```python
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif player == "rock":
        if computer == "scissors":
            return "win"
        else:
            return "lose"
    elif player == "paper":
        if computer == "rock":
            return "win"
        else:
            return "lose"
    elif player == "scissors":
        if computer == "paper":
            return "win"
        else:
            return "lose"
```

### Method 2: Using Dictionary Lookup

```python
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    
    winning_combinations = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if winning_combinations[player] == computer:
        return "win"
    else:
        return "lose"
```

### Method 3: Using List Index

```python
def determine_winner(player, computer):
    choices = ["rock", "paper", "scissors"]
    
    if player == computer:
        return "tie"
    
    player_index = choices.index(player)
    computer_index = choices.index(computer)
    
    # Check if player wins (next choice beats current)
    if (player_index + 1) % 3 == computer_index:
        return "win"
    else:
        return "lose"
```

## 🎯 Input Handling

### Getting Player Choice

```python
def get_player_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        
        if choice in ["rock", "paper", "scissors"]:
            return choice
        elif choice in ["r", "p", "s"]:
            # Convert shorthand to full word
            shorthand = {"r": "rock", "p": "paper", "s": "scissors"}
            return shorthand[choice]
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")
```

### Getting Computer Choice

```python
import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
```

## 📊 Score Tracking

### Score Management

```python
def initialize_score():
    return {"wins": 0, "losses": 0, "ties": 0}

def update_score(score, result):
    if result == "win":
        score["wins"] += 1
    elif result == "lose":
        score["losses"] += 1
    else:  # tie
        score["ties"] += 1

def display_score(score):
    print(f"Score - Wins: {score['wins']}, Losses: {score['losses']}, Ties: {score['ties']}")
```

## 🎮 Game Flow Example

### Sample Game Session

```
Welcome to Rock Paper Scissors!
Rules: Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock

Enter your choice (rock/paper/scissors): rock
You chose: rock
Computer chose: scissors
Rock crushes scissors! You win!

Score - Wins: 1, Losses: 0, Ties: 0

Play again? (y/n): y

Enter your choice (rock/paper/scissors): paper
You chose: paper
Computer chose: rock
Paper covers rock! You win!

Score - Wins: 2, Losses: 0, Ties: 0

Play again? (y/n): n

Final Score - Wins: 2, Losses: 0, Ties: 0
Thanks for playing!
```

## 🔍 Advanced Features

### Optional Enhancements

1. **Statistics**
   - Win percentage
   - Most common choice
   - Streak tracking

2. **Computer Strategy**
   - Pattern recognition
   - Adaptive AI
   - Difficulty levels

3. **Visual Elements**
   - ASCII art for choices
   - Color coding
   - Animations

4. **Game Modes**
   - Best of 3/5/7
   - Tournament mode
   - Two-player mode

## 🐛 Common Issues and Solutions

### Issue 1: Case Sensitivity
```python
# Problem: "Rock" vs "rock"
# Solution: Convert to lowercase
choice = input("Enter choice: ").lower()
```

### Issue 2: Invalid Input
```python
# Problem: Player enters "banana"
# Solution: Input validation
while choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice!")
    choice = input("Enter choice: ").lower()
```

### Issue 3: Random Seed
```python
# Problem: Same sequence every time
# Solution: Use current time as seed
import random
import time
random.seed(time.time())
```

## 🎯 Testing the Game Logic

### Test Cases

```python
def test_game_logic():
    test_cases = [
        ("rock", "scissors", "win"),
        ("rock", "paper", "lose"),
        ("rock", "rock", "tie"),
        ("paper", "rock", "win"),
        ("paper", "scissors", "lose"),
        ("paper", "paper", "tie"),
        ("scissors", "paper", "win"),
        ("scissors", "rock", "lose"),
        ("scissors", "scissors", "tie")
    ]
    
    for player, computer, expected in test_cases:
        result = determine_winner(player, computer)
        if result == expected:
            print(f"✓ {player} vs {computer}: {result}")
        else:
            print(f"✗ {player} vs {computer}: expected {expected}, got {result}")

# Run tests
test_game_logic()
```

## 📝 Key Takeaways

- **Rock Paper Scissors** has simple but important rules
- **Game logic** can be implemented in multiple ways
- **Input validation** is crucial for user experience
- **Score tracking** adds engagement to the game
- **Random choice generation** makes the computer unpredictable
- **Clear game flow** ensures smooth gameplay
- **Error handling** prevents crashes from invalid input

## 🎯 Next Steps

In the next lesson, we'll **build the complete Rock Paper Scissors game** using all the concepts we've learned!

---

**💡 Practice Exercise**: Before building the game, try to:
1. Write the `determine_winner()` function using your preferred method
2. Create a simple test to verify your logic works correctly
3. Plan how you'll handle user input and validation
4. Think about how you'll structure the main game loop

**🔍 Challenge**: Try implementing a simple version of the game with just the core logic, then we'll build the complete version in the next lesson! 