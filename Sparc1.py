import random

#Take care of each turn of a game.
def round(people_list):

    coins_taken = 0
    current_players_index = []

    #Everyone who contributed - 1 coin.
    #Randomly choose a person from the list of current players.
    #Give that person coins.
    for i in range(len(people_list)):
        if people_list[i] >= 1:
            people_list[i] -= 1
            coins_taken += 1
            current_players_index.append(i)

    lucky_person = random.choice(current_players_index)

    people_list[lucky_person] += coins_taken

    coins_taken = 0
    current_players_index = []

    for people in people_list:
        if people == 0:
            people_list.remove(people)

    return None


#Run one game at a time.
def game(number_of_players, number_of_coins):

    rounds = 0
    people_list = []

    #Generate a list of people's coins for the game.
    for i in range(number_of_players) :
        people_list.append(number_of_coins)

    while len(people_list) > 1:
        round(people_list)
        rounds += 1

    people_list = []

    return rounds

#Loop through the game.
number_of_players = 2
for number_of_coins in range (2,11):
    print ("\n")
    total_rounds = 0

    for i in range (3) :

        for t in range(10000):
            total_rounds += game(number_of_players,number_of_coins)

        print(total_rounds/10000, end=",")

        total_rounds = 0
