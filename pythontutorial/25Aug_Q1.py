"""Q. In this game, there is a list of words present, out of which our interpreter will
choose 1 random word. The user first has to input their names and then, will be asked
to guess any alphabet. If the random word contains that alphabet, it will be shown as
the output(with correct placement) else the program will ask you to guess another alphabet.
The user will be given 12 turns(which can be changed accordingly) to guess the complete word."""
import random

words = ['math', 'computer', 'science', 'programming',
         'python', 'biology', 'physics', 'chemistry']

word = random.choice(words)
print(word)

name = input("What is your name?? ")

print(f"Hello {name}, Time to play hangman!")
print("Start guessing...")

guesses = []
win = False
for i in range(12):
    char1 = input("Guess a character: ")
    if len(char1) == 1:
        if char1 in word:
            print("Correct Input")
            guesses.append(char1)
            print(guesses)
        else:
            print("Wrong Input")
    else:
        print("Wrong Input")
    count = 0
    for j in word:
        if j in guesses:
            print(j,end="")
        else:
            print("_",end="")
            count += 1
    if count == 0:
        print("\nWinner")
        win = True
        break
    else:
        print("\nTry again")
if not win:
    print("Game lost")