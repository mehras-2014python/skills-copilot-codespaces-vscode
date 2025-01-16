import random
class NumberGuessingGame:
    def __init__(self):
        self.number = random.randint(1,50)
        self.guesses_left = 100
        print("Welcome to the Number Guessing Game !")
        print("i have piked a number between 1 and 50.can you guess it ?")
        print("you have 100 attempts.Good luck!")
    def play (self):
        while self.guesses_left > 0:
            try:

                guess = int(input())
                if guess > self.number:
                    print("Say a smaller number")
                    self.guesses_left -=1
                if guess < self.number:
                    print("Say a bigger number")
                    self.guesses_left -=1
                if guess ==self.number:
                    print ("you win!!!")
                if self.guesses_left == 0:
                    print ("loser")
                



            except ValueError:
                print("invalid input.Please enter a number between 1 and 50")
game = NumberGuessingGame ()
game.play()




