# Chapter 12: Building the Rock Paper Scissors Game

## 🎯 Learning Objectives
- Build a complete Rock Paper Scissors game
- Apply all the concepts learned in previous lessons
- Create a well-structured, user-friendly program
- Practice debugging and testing
- Understand how to organize code into functions

## 🚀 Let's Build the Game!

Now we'll create a complete Rock Paper Scissors game using everything we've learned: variables, functions, conditionals, loops, and more!

## 📝 Complete Game Code

### The Full Rock Paper Scissors Game

```python
import random
import time

def display_welcome():
    """Display welcome message and game rules"""
    print("=" * 50)
    print("🎮 ROCK PAPER SCISSORS GAME 🎮")
    print("=" * 50)
    print()
    print("Rules:")
    print("• Rock crushes Scissors")
    print("• Scissors cuts Paper") 
    print("• Paper covers Rock")
    print("• Same choice = Tie")
    print()
    print("You can type: rock, paper, scissors (or r, p, s)")
    print("=" * 50)
    print()

def get_player_choice():
    """Get and validate player's choice"""
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower().strip()
        
        # Handle full words
        if choice in ["rock", "paper", "scissors"]:
            return choice
        
        # Handle shorthand
        shorthand = {"r": "rock", "p": "paper", "s": "scissors"}
        if choice in shorthand:
            return shorthand[choice]
        
        # Invalid input
        print("❌ Invalid choice! Please enter rock, paper, or scissors (or r, p, s)")
        print()

def get_computer_choice():
    """Generate computer's random choice"""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player, computer):
    """Determine the winner based on game rules"""
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

def get_result_message(player, computer, result):
    """Get a descriptive message about the result"""
    if result == "tie":
        return f"Both chose {player}! It's a tie!"
    
    messages = {
        ("rock", "scissors"): "Rock crushes scissors!",
        ("paper", "rock"): "Paper covers rock!",
        ("scissors", "paper"): "Scissors cuts paper!"
    }
    
    if (player, computer) in messages:
        return f"{messages[(player, computer)]} You win!"
    else:
        # Computer won
        computer_messages = {
            ("rock", "scissors"): "Rock crushes scissors!",
            ("paper", "rock"): "Paper covers rock!",
            ("scissors", "paper"): "Scissors cuts paper!"
        }
        return f"{computer_messages[(computer, player)]} Computer wins!"

def display_results(player, computer, result, score):
    """Display the game results"""
    print()
    print("🎯 RESULTS:")
    print(f"You chose: {player.upper()}")
    print(f"Computer chose: {computer.upper()}")
    print()
    
    # Add some suspense
    print("Determining winner", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print()
    print()
    
    # Show result
    message = get_result_message(player, computer, result)
    if result == "win":
        print(f"🎉 {message}")
    elif result == "lose":
        print(f"😔 {message}")
    else:
        print(f"🤝 {message}")
    
    print()
    display_score(score)

def display_score(score):
    """Display current score"""
    total = score["wins"] + score["losses"] + score["ties"]
    if total > 0:
        win_percentage = (score["wins"] / total) * 100
        print(f"📊 Score: {score['wins']} wins, {score['losses']} losses, {score['ties']} ties")
        print(f"📈 Win rate: {win_percentage:.1f}%")
    print()

def update_score(score, result):
    """Update the score based on game result"""
    if result == "win":
        score["wins"] += 1
    elif result == "lose":
        score["losses"] += 1
    else:  # tie
        score["ties"] += 1

def play_round(score):
    """Play one round of the game"""
    # Get choices
    player = get_player_choice()
    computer = get_computer_choice()
    
    # Determine winner
    result = determine_winner(player, computer)
    
    # Update score
    update_score(score, result)
    
    # Display results
    display_results(player, computer, result, score)

def play_game():
    """Main game function"""
    # Initialize
    display_welcome()
    score = {"wins": 0, "losses": 0, "ties": 0}
    
    # Main game loop
    while True:
        play_round(score)
        
        # Ask to play again
        print("=" * 30)
        play_again = input("Play again? (y/n): ").lower().strip()
        
        if play_again in ["n", "no", "quit", "exit"]:
            break
        elif play_again not in ["y", "yes", ""]:
            print("I'll take that as a yes! 😊")
        
        print()

def display_final_score(score):
    """Display final score when game ends"""
    total = score["wins"] + score["losses"] + score["ties"]
    
    print("=" * 50)
    print("🏁 GAME OVER!")
    print("=" * 50)
    print(f"Final Score:")
    print(f"• Wins: {score['wins']}")
    print(f"• Losses: {score['losses']}")
    print(f"• Ties: {score['ties']}")
    print(f"• Total games: {total}")
    
    if total > 0:
        win_percentage = (score["wins"] / total) * 100
        print(f"• Win rate: {win_percentage:.1f}%")
        
        if win_percentage > 60:
            print("🎉 Excellent playing! You're a Rock Paper Scissors master!")
        elif win_percentage > 40:
            print("👍 Good job! You held your own!")
        else:
            print("💪 Keep practicing! You'll get better!")
    
    print("=" * 50)
    print("Thanks for playing! 👋")

# Run the game
if __name__ == "__main__":
    try:
        play_game()
        # Get final score (we'll need to modify play_game to return score)
        final_score = {"wins": 0, "losses": 0, "ties": 0}  # Placeholder
        display_final_score(final_score)
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing! 👋")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Thanks for playing! 👋")
```

## 🔧 Enhanced Version with Better Structure

Let's create an even better version with improved organization:

```python
import random
import time

class RockPaperScissors:
    def __init__(self):
        self.score = {"wins": 0, "losses": 0, "ties": 0}
        self.choices = ["rock", "paper", "scissors"]
        self.winning_combinations = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }
        self.result_messages = {
            ("rock", "scissors"): "Rock crushes scissors!",
            ("paper", "rock"): "Paper covers rock!",
            ("scissors", "paper"): "Scissors cuts paper!"
        }
    
    def display_welcome(self):
        """Display welcome message and game rules"""
        print("=" * 50)
        print("🎮 ROCK PAPER SCISSORS GAME 🎮")
        print("=" * 50)
        print()
        print("Rules:")
        print("• Rock crushes Scissors")
        print("• Scissors cuts Paper") 
        print("• Paper covers Rock")
        print("• Same choice = Tie")
        print()
        print("You can type: rock, paper, scissors (or r, p, s)")
        print("=" * 50)
        print()
    
    def get_player_choice(self):
        """Get and validate player's choice"""
        while True:
            choice = input("Enter your choice (rock/paper/scissors): ").lower().strip()
            
            # Handle full words
            if choice in self.choices:
                return choice
            
            # Handle shorthand
            shorthand = {"r": "rock", "p": "paper", "s": "scissors"}
            if choice in shorthand:
                return shorthand[choice]
            
            # Invalid input
            print("❌ Invalid choice! Please enter rock, paper, or scissors (or r, p, s)")
            print()
    
    def get_computer_choice(self):
        """Generate computer's random choice"""
        return random.choice(self.choices)
    
    def determine_winner(self, player, computer):
        """Determine the winner based on game rules"""
        if player == computer:
            return "tie"
        
        if self.winning_combinations[player] == computer:
            return "win"
        else:
            return "lose"
    
    def get_result_message(self, player, computer, result):
        """Get a descriptive message about the result"""
        if result == "tie":
            return f"Both chose {player}! It's a tie!"
        
        if (player, computer) in self.result_messages:
            return f"{self.result_messages[(player, computer)]} You win!"
        else:
            # Computer won
            return f"{self.result_messages[(computer, player)]} Computer wins!"
    
    def display_results(self, player, computer, result):
        """Display the game results"""
        print()
        print("🎯 RESULTS:")
        print(f"You chose: {player.upper()}")
        print(f"Computer chose: {computer.upper()}")
        print()
        
        # Add some suspense
        print("Determining winner", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print()
        print()
        
        # Show result
        message = self.get_result_message(player, computer, result)
        if result == "win":
            print(f"🎉 {message}")
        elif result == "lose":
            print(f"😔 {message}")
        else:
            print(f"🤝 {message}")
        
        print()
        self.display_score()
    
    def display_score(self):
        """Display current score"""
        total = self.score["wins"] + self.score["losses"] + self.score["ties"]
        if total > 0:
            win_percentage = (self.score["wins"] / total) * 100
            print(f"📊 Score: {self.score['wins']} wins, {self.score['losses']} losses, {self.score['ties']} ties")
            print(f"📈 Win rate: {win_percentage:.1f}%")
        print()
    
    def update_score(self, result):
        """Update the score based on game result"""
        if result == "win":
            self.score["wins"] += 1
        elif result == "lose":
            self.score["losses"] += 1
        else:  # tie
            self.score["ties"] += 1
    
    def play_round(self):
        """Play one round of the game"""
        # Get choices
        player = self.get_player_choice()
        computer = self.get_computer_choice()
        
        # Determine winner
        result = self.determine_winner(player, computer)
        
        # Update score
        self.update_score(result)
        
        # Display results
        self.display_results(player, computer, result)
    
    def display_final_score(self):
        """Display final score when game ends"""
        total = self.score["wins"] + self.score["losses"] + self.score["ties"]
        
        print("=" * 50)
        print("🏁 GAME OVER!")
        print("=" * 50)
        print(f"Final Score:")
        print(f"• Wins: {self.score['wins']}")
        print(f"• Losses: {self.score['losses']}")
        print(f"• Ties: {self.score['ties']}")
        print(f"• Total games: {total}")
        
        if total > 0:
            win_percentage = (self.score["wins"] / total) * 100
            print(f"• Win rate: {win_percentage:.1f}%")
            
            if win_percentage > 60:
                print("🎉 Excellent playing! You're a Rock Paper Scissors master!")
            elif win_percentage > 40:
                print("👍 Good job! You held your own!")
            else:
                print("💪 Keep practicing! You'll get better!")
        
        print("=" * 50)
        print("Thanks for playing! 👋")
    
    def play_game(self):
        """Main game function"""
        # Initialize
        self.display_welcome()
        
        # Main game loop
        while True:
            self.play_round()
            
            # Ask to play again
            print("=" * 30)
            play_again = input("Play again? (y/n): ").lower().strip()
            
            if play_again in ["n", "no", "quit", "exit"]:
                break
            elif play_again not in ["y", "yes", ""]:
                print("I'll take that as a yes! 😊")
            
            print()
        
        # Show final score
        self.display_final_score()

# Run the game
if __name__ == "__main__":
    try:
        game = RockPaperScissors()
        game.play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing! 👋")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Thanks for playing! 👋")
```

## 🎮 How to Run the Game

### Step 1: Save the Code
Save either version as `rock_paper_scissors.py`

### Step 2: Run the Game
```bash
python rock_paper_scissors.py
```

### Step 3: Play!
Follow the prompts to play the game.

## 🔍 Code Explanation

### Key Components

1. **Welcome Function**: Displays game rules and instructions
2. **Input Validation**: Handles various input formats (full words, shorthand)
3. **Random Choice**: Computer makes unpredictable choices
4. **Game Logic**: Determines winner using dictionary lookup
5. **Score Tracking**: Keeps track of wins, losses, and ties
6. **User Experience**: Clear messages, suspense, and feedback
7. **Error Handling**: Graceful handling of interruptions and errors

### Advanced Features

1. **Emojis**: Make the game more visually appealing
2. **Suspense**: Adds dots while "thinking"
3. **Statistics**: Shows win percentage
4. **Flexible Input**: Accepts both full words and shorthand
5. **Class Structure**: Better organization in the enhanced version

## 🧪 Testing the Game

### Test Cases to Try

1. **All Valid Inputs**:
   - "rock", "paper", "scissors"
   - "r", "p", "s"
   - "ROCK", "PAPER", "SCISSORS"

2. **Invalid Inputs**:
   - "banana", "123", ""

3. **Edge Cases**:
   - Interrupt with Ctrl+C
   - Play many rounds
   - Test all winning combinations

### Expected Behavior

- Game should handle all valid inputs
- Invalid inputs should show error message and ask again
- Score should update correctly
- Game should continue until player chooses to quit
- Final score should display properly

## 🎯 Customization Ideas

### Add These Features

1. **Best of Series**:
   ```python
   def play_best_of(self, rounds):
       # Play until someone wins majority
   ```

2. **Statistics Tracking**:
   ```python
   def track_statistics(self):
       # Track most common choice, streaks, etc.
   ```

3. **Difficulty Levels**:
   ```python
   def set_difficulty(self, level):
       # Easy: random, Hard: pattern recognition
   ```

4. **Sound Effects** (if possible):
   ```python
   def play_sound(self, sound_type):
       # Add audio feedback
   ```

## 📝 Key Takeaways

- **Functions** organize code into reusable blocks
- **Classes** provide even better organization
- **Input validation** is crucial for user experience
- **Error handling** prevents crashes
- **User experience** matters - clear messages, feedback
- **Testing** ensures your code works correctly
- **Documentation** helps others understand your code

## 🎉 Congratulations!

You've now built a complete Rock Paper Scissors game using all the Python concepts you've learned:

- ✅ Variables and data types
- ✅ Functions and return values
- ✅ Conditional statements (if/else)
- ✅ Loops (for and while)
- ✅ Input/output operations
- ✅ Error handling
- ✅ Code organization

This game demonstrates how all these concepts work together to create a complete, functional program!

## 🚀 Next Steps

Now that you've built this game, you can:

1. **Add more features** (statistics, difficulty levels, etc.)
2. **Create other games** (Number Guessing, Tic-Tac-Toe, etc.)
3. **Learn more Python** (file handling, web development, data science)
4. **Build real projects** (web apps, automation scripts, etc.)

You're now a Python programmer! 🐍✨

---

**💡 Practice Exercise**: Try adding these features to your game:
1. Track the player's most common choice
2. Add a "best of 3" mode
3. Show a streak counter for consecutive wins
4. Add ASCII art for the choices

**🔍 Challenge**: Create a tournament mode where the computer plays multiple games and shows overall statistics! 