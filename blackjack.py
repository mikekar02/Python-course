import random
ans = input("Welcome to Blackjack! Want to play a hand?(y/n)")

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] #creating the cards for the game
bust1 = False
bust2 = False

if ans == "y":

    user_card1 = cards[random.randint(0, 12)]   #picking a random number from card list
    user_card2 = cards[random.randint(0, 12)]
    user_score = user_card1 + user_card2        #calculating users score
    user_hand =  [user_card1,user_card2]        #adding both cards to users hand

    cpu_card1 = cards[random.randint(0, 12)]
    cpu_score = cpu_card1
    cpu_hand = [cpu_card1] 

    print("Your cards:",user_hand, "current score:",user_score) #prints users hand and score(sum of hand)
    print("Computers first card: ",cpu_hand)#prints computer's hand and score(sum of hand)

    ans = "hit"
    while ans == "hit" and bust1 == False:
        ans = input("Do you want to hit or stay?(hit/stay)") 

        if ans == "hit":
            new_card = random.randint(0, 12) #adds a card to users hand
            user_hand.append(cards[new_card])
            user_score = user_score + cards[new_card]  #adds the new card value to the users score
            if user_score == 21:
                ans = "stop" #removes the ability to hit at 21
            if user_score <= 21: 
                print("Your cards:",user_hand, "current score:",user_score) #prints users hand and score(sum of hand)
            elif user_score >21:
                if 11 in user_hand:
                    for x in user_hand:
                        if user_hand[x] == 11:
                            user_hand[x] = 1         #if user was dealt an ace(11) in his hand and goes over 21 he can chose to play use the ace as a one
                else:
                    print("You busted...your cards:",user_hand)  
                    game = False   
                    bust1= True 

    while cpu_score < 17:
            new_card = random.randint(0, 12) #adds a card to users hand
            cpu_hand.append(cards[new_card])
            cpu_score = cpu_score + cards[new_card]  #adds the new card value to the users score

    print("Cpu cards:",cpu_hand, "current score:",cpu_score) 

    if  cpu_score > 21:
        bust2 = True

    if user_score > cpu_score and bust1 == False:
        print("User score:",user_score)
        print("Cpu score:",cpu_score)
        print("User Wins!!!")                           #user wins if he has a bigger score and hasnt busted
    elif user_score < cpu_score and bust2 == False:
        print("User score:",user_score)
        print("Cpu score:",cpu_score)
        print("Cpu Wins!!!")                    #cpu wins if he has a bigger score and hasnt busted
    else:
        print("Draw...")    #every other case is a draw