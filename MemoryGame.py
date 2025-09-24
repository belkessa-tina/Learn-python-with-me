import time
import random
import os

# Clears the terminal screen (Windows or Unix)
def clear_screen():
    if os.name == 'posix':
        os.system('clear')  # For Linux/macOS
    else:
        os.system('cls')    # For Windows

# Generate the initial number (1 digit) to be memorized
sequence = random.randint(0, 9)
score = 0  # Tracks the number of correct attempts

# Function to display a number, let user memorize it, then ask for input
def memorize_sequence(sequence):
    print("Memorize this sequence of number:")
    time.sleep(1)
    print(sequence)
    time.sleep(3)
    clear_screen()
    # Ask the user to input the number they just saw
    user_input = int(input("Enter the sequence you have memorized: "))
    clear_screen()
    return user_input

# First memory check
user_value = memorize_sequence(sequence)

# Loop continues as long as the user remembers the correct sequence
while user_value == sequence:
    print("✅ Correct! Good job!")
    score += 1
    print(f"Your current score is: {score}")
    
    # Extend the sequence by adding another random digit at the end
    sequence_str = str(sequence) + str(random.randint(0, 9))
    sequence = int(sequence_str)  # Convert back to int

    # Ask the user to memorize and recall the new sequence
    user_value = memorize_sequence(sequence)

# Game ends if the user gets the sequence wrong
print("❌ Incorrect. Game over.")
print(f"🎯 Your final score is: {score}")




#this is just an alternayive very beginner program
"""
print(f"Memorize this sequence of number: ")
time.sleep(1)
print(f"{sequence}")
time.sleep(3)
clear_screen()
memorize = int(input("enter the sequence you have memorised "))



while(memorize == sequence):
    print(f"Correct: Good Job!")
    cont = cont + 1
    #sequence = random.randint(0,9)
    print(f"Your acutal s score is: {cont}")
    sstr = str(sequence) + str(random.randint(0,9))
    sequence = int(sstr)
    print(f"Memorize this sequence of number: ")
    time.sleep(1)
    print(f"{sequence}")
    time.sleep(3)
    clear_screen()
    memorize = int(input("enter the sequence you have memorised "))
print("False: You didn't get the right answer")
print(f"Your final score is: {cont}")
"""
