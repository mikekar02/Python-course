import random
import game_data
import art

game = True
score = 0
pick_a = random.choice(game_data.data)
pick_b = random.choice(game_data.data) #get a random choice from the game data and set it as a game option
while pick_a == pick_b:
        pick_b = random.choice(game_data.data) #checks if a and b are the same value if they are reroll b

while game == True:
    print(art.logo)
    print("Compare A:",pick_a["name"],",a",pick_a["description"],",from",pick_a["country"])

    print(art.vs)

    print("Compare B:",pick_b["name"],",a",pick_b["description"],",from",pick_b["country"])

    guess = input("Who has more followers? Type 'A' or 'B':").upper()

    if pick_a["follower_count"] > pick_b["follower_count"]:
        ans = "A"
    else:
        ans = "B"

    if guess == ans:
        pick_a = pick_b
        pick_b = random.choice(game_data.data)
        score += 1
        print("Correct! Your score:",score)
        while pick_a == pick_b:
            pick_b = random.choice(game_data.data)
    else:
        print("Wrong... Game over, your score:",score)
        game = False