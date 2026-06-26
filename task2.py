import random

def guessing_game():
    print("====================================")
    print("🎯 Welcome to the Number Guessing Game! 🎯")
    print("I'm thinking of a number between 1 and 100.")
    print("====================================")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Prompt the user for a guess
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # Compare the guess to the secret number
            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"\n🎉 Correct! You've guessed the number in {attempts} attempts!")
                break # Exit the loop since they won
                
        except ValueError:
            print("❌ Invalid input. Please enter a valid whole number.")

if __name__ == "__main__":
    guessing_game()