import random

def set_lives(dif):
    if dif == "easy":
        return 10
    elif dif == "hard":
        return 5            #chooses amount of lives based on difficulty
    
def compare(user_guess):
    global lives
    
    if user_guess < rand_num:
        print("Higher")
    elif user_guess > rand_num:
        print("Lower")
    else:
        print("You got it! The answer was ",rand_num)
        lives = 0
        return True

global rand_num
rand_num = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
dif = input("Choose a difficulty. Type 'easy' or 'hard'.").lower() #set the difficulty

global lives
lives = set_lives(dif)

while lives > 0:
    print("You have",lives,"attempts to guess the number")
    guess = int(input("Make a guess:"))  
    lives = lives -1    #receives users guess and takes a life away

    compare(guess)

