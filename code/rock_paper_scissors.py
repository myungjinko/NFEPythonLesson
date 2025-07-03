#!/usr/bin/env python3
"""
Rock Paper Scissors Game
A complete implementation using all Python concepts learned in the course.

This game demonstrates:
- Variables and data types
- Functions and return values
- Conditional statements (if/else)
- Loops (while)
- Input/output operations
- Error handling
- Code organization
"""

import random
import time

class RockPaperScissors:
    """A complete Rock Paper Scissors game implementation"""
    
    def __init__(self):
        """Initialize the game with default settings"""
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
        self.player_choice_history = []
    
    def display_welcome(self):
        """Display welcome message and game rules"""
        print("=" * 60)
        print("🎮 ROCK PAPER SCISSORS GAME 🎮")
        print("=" * 60)
        print()
        print("📋 Rules:")
        print("   • Rock crushes Scissors")
        print("   • Scissors cuts Paper") 
        print("   • Paper covers Rock")
        print("   • Same choice = Tie")
        print()
        print("💡 Tips:")
        print("   • You can type: rock, paper, scissors")
        print("   • Or use shorthand: r, p, s")
        print("   • Type 'quit' to exit the game")
        print("=" * 60)
        print()
    
    def get_player_choice(self):
        """Get and validate player's choice"""
        while True:
            choice = input("🎯 Enter your choice (rock/paper/scissors): ").lower().strip()
            
            # Check for quit command
            if choice in ["quit", "exit", "q"]:
                return "quit"
            
            # Handle full words
            if choice in self.choices:
                self.player_choice_history.append(choice)
                return choice
            
            # Handle shorthand
            shorthand = {"r": "rock", "p": "paper", "s": "scissors"}
            if choice in shorthand:
                full_choice = shorthand[choice]
                self.player_choice_history.append(full_choice)
                return full_choice
            
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
        """Display the game results with visual flair"""
        print()
        print("🎯 RESULTS:")
        print(f"   You chose: {player.upper()}")
        print(f"   Computer chose: {computer.upper()}")
        print()
        
        # Add some suspense
        print("   Determining winner", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print()
        print()
        
        # Show result with emojis
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
        """Display current score with statistics"""
        total = self.score["wins"] + self.score["losses"] + self.score["ties"]
        if total > 0:
            win_percentage = (self.score["wins"] / total) * 100
            print(f"📊 Current Score:")
            print(f"   Wins: {self.score['wins']} | Losses: {self.score['losses']} | Ties: {self.score['ties']}")
            print(f"   Win Rate: {win_percentage:.1f}%")
            
            # Show most common choice if we have history
            if self.player_choice_history:
                most_common = max(set(self.player_choice_history), key=self.player_choice_history.count)
                print(f"   Your favorite choice: {most_common}")
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
        
        # Check for quit
        if player == "quit":
            return False
        
        computer = self.get_computer_choice()
        
        # Determine winner
        result = self.determine_winner(player, computer)
        
        # Update score
        self.update_score(result)
        
        # Display results
        self.display_results(player, computer, result)
        
        return True
    
    def display_final_score(self):
        """Display final score when game ends"""
        total = self.score["wins"] + self.score["losses"] + self.score["ties"]
        
        print("=" * 60)
        print("🏁 GAME OVER!")
        print("=" * 60)
        print(f"📈 Final Statistics:")
        print(f"   • Total Games: {total}")
        print(f"   • Wins: {self.score['wins']}")
        print(f"   • Losses: {self.score['losses']}")
        print(f"   • Ties: {self.score['ties']}")
        
        if total > 0:
            win_percentage = (self.score["wins"] / total) * 100
            print(f"   • Win Rate: {win_percentage:.1f}%")
            
            # Performance evaluation
            if win_percentage > 60:
                print("   🎉 Excellent playing! You're a Rock Paper Scissors master!")
            elif win_percentage > 40:
                print("   👍 Good job! You held your own!")
            else:
                print("   💪 Keep practicing! You'll get better!")
            
            # Show choice statistics
            if self.player_choice_history:
                print(f"\n📊 Choice Analysis:")
                for choice in self.choices:
                    count = self.player_choice_history.count(choice)
                    percentage = (count / len(self.player_choice_history)) * 100
                    print(f"   • {choice.capitalize()}: {count} times ({percentage:.1f}%)")
        
        print("=" * 60)
        print("Thanks for playing! 👋")
        print("Come back soon for more Rock Paper Scissors fun!")
    
    def play_game(self):
        """Main game function"""
        # Initialize
        self.display_welcome()
        
        # Main game loop
        while True:
            # Play a round
            continue_playing = self.play_round()
            
            if not continue_playing:
                break
            
            # Ask to play again
            print("=" * 40)
            play_again = input("🔄 Play again? (y/n): ").lower().strip()
            
            if play_again in ["n", "no", "quit", "exit"]:
                break
            elif play_again not in ["y", "yes", ""]:
                print("I'll take that as a yes! 😊")
            
            print()
        
        # Show final score
        self.display_final_score()


def main():
    """Main function to run the game"""
    print("Starting Rock Paper Scissors Game...")
    print()
    
    try:
        # Create and play the game
        game = RockPaperScissors()
        game.play_game()
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Game interrupted by user.")
        print("Thanks for playing! 👋")
        
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try running the game again.")
        print("Thanks for playing! 👋")


# Run the game if this file is executed directly
if __name__ == "__main__":
    main() 