from random import randint
player_2 = randint(1, 100)
guess = 5
while guess > 0:
    player_1 = int(input("player_1 Enter your guess (1-100) : "))
    if player_1 == player_2:
        print("Wow you Win!")
        break
    elif player_1 != player_2 and player_1 > player_2:
        guess = guess-1
        print("choice some lower number ,gusses left", guess)
    elif player_1 != player_2 and player_1 < player_2:
        guess = guess-1
        print("choice some higher number , gusses left", guess)
    if guess == 0:
        print("Player 1 lost. The number was ", player_2)
    else:
        pass
