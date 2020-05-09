import time

secret = "drukarka"
guesses = ''
max_turns = 10
turns_played = 0
won = False

while max_turns > turns_played and not won:
    
    missing = 0
    for letter in secret:
        if letter in guesses:
            print(letter, end="")
        else:
            print("_", end="")
            missing +=1
    print()
    
    if not missing:
        print("Blip Blop ! You may have won the ballet, but not the war!")
        won = True
        break

    guess = input("Guess a character: ")
    #print(guess)

    guesses += guess
    if guess not in secret:
        turns_played +=1

if not won:
    print("Blip Blop! I won. You lost. I am the best!")
