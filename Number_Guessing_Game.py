def set_lives(dif):
    if dif == "easy":
        return 10
    elif dif == "hard":
        return 5


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
dif = input("Choose a difficulty. Type 'easy' or 'hard'.").lower() #set the difficulty

lives = set_lives(dif)