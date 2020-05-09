import time
from dictionary import get_random_word


class Hangman():
    def __init__(self):
        self.secret = get_random_word()
        self.guesses = ''
        self.max_turns = 15
        self.turns_played = 0
        self.won = False

    def play(self):
        while self.didnt_loose():
            self.show_game_status()
            self.get_a_guess()
            self.check_if_won()
        self.announce_the_result()

    def didnt_loose(self):
        return self.max_turns > self.turns_played and not self.won

    def show_game_status(self):
        self.show_remaining_turns()
        self.show_guesses()
        self.show_remaining_turns()
        self.show_word()

    def show_word(self):
        for letter in self.secret:
            if letter in self.guesses:
                print(letter, end="")
            else:
                print("_", end="")
        print()

    def show_remaining_turns(self): 
        #TODO
        pass

    def show_guesses(self): 
        #TODO
        pass

    def show_remaining_turns(self): 
        #TODO
        pass

    def get_a_guess(self):
        guess = input("Guess a character: ")
        self.guesses += guess
        if guess not in self.secret:
            self.turns_played +=1
        
    def check_if_won(self):
        for letter in self.secret:
            if letter not in self.guesses:
                self.won = False
                break
        else:
            self.won = True

    def announce_the_result(self):
        if self.won:
            print("Blip Blop ! You may have won the battle, but not the war!")
        else:
            print("Blip Blop! I won. You lost. I am the best!")
        print("The word was: ",self.secret)

