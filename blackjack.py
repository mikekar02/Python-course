import random
ans = input("Welcome to Blackjack! Want to play a hand?(y/n)")

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] #creating the cards for the game

if ans == "y":

    user_card1 = cards[random.randint(0, 12)]   #picking a random number from card list
    user_card2 = cards[random.randint(0, 12)]
    user_hand =  [user_card1,user_card2]        #adding both cards to users hand

    cpu_card1 = cards[random.randint(0, 12)]
    cpu_hand = [cpu_card1,"--"] 

    print("Your cards:",user_hand, "current score:",(user_card1+user_card2)) #prints users hand and score(sum of hand)
    print("Computers first card: ",cpu_hand)#prints computer's hand and score(sum of hand)

    