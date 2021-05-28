import random
import playsound
print("Welcome to snake, water and Gun game, Made by ELDERNY")
tries = 10
user_wins = 0
pc_wins = 0
user_loss = 0
pc_loss = 0
draw = 0
lost = "You lost this match"
win = "You won this match"
def decide(tries):
    """FUNCTION FOR PLAYING ANOTHER GAME"""
    if user_wins > pc_wins:
        print("\nYou've WON with score: ", "Your Wins: ", str(user_wins), ", Pc Wins: ", str(pc_wins), ", Draw: ", str(draw), "You lost: ", str(user_loss), "matches, Pc lost: ", str(pc_loss), " times")
        get = int(input("Please 1 to restart or 2 to close\n"))
        if get == 1:
            tries = 10
            return tries
        elif get == 2:
            tries = 0
            return tries
    elif user_wins < pc_wins:
        print("\nYou've LOST with score: ", "Your Wins: ", str(user_wins), ", Pc Wins: ", str(pc_wins), ", Draw: ", str(draw), "You lost: ", str(user_loss), "matches, Pc lost: ", str(pc_loss), " times")
        get = int(input("Please 1 to restart or 2 to close\n"))
        if get == 1:
            tries = 10
            return tries
        elif get == 2:
            tries = 0
            return tries
    elif user_wins == pc_wins:
        print("HUH, lucky man, TRY AGAIN")
    else:
        print("BUG, either you skilled or game crashed")
while (tries>=1):
    ask = input("\nType 's' for snake, 'g' for gun and 'w' for water \nType here: ")
    random_pc = ['snake', 'gun', 'water']
    pc = random.choice(random_pc)
    tries = tries - 1
    if ask == "s":
        print("You've selected: snake")
        print("Pc has selected: ", pc)
        if ask == "s" and pc == "water":
            print("You won, you drank the water", win)
            user_wins = user_wins + 1
            pc_loss = pc_loss + 1
            data1 = "Tries Left: " + str(tries) + " and Points: \n" + "Draw: " + str(draw) + " Times, "
            data2 = "Your Wins: " + str(user_wins) + ", " + "Computer Wins: " + str(pc_wins)
            data = data1 + data2
            print(data)
        elif ask == "s" and pc == "snake":
            print("AA, both got same, NOONE wins")
            draw = draw + 1
            data1 = "Tries Left: " + str(tries) + " and Points: \n" + "Draw: " + str(draw) + " Times, "
            data2 = "Your Wins: " + str(user_wins) + ", " + "Computer Wins: " + str(pc_wins)
            data = data1 + data2
            print(data)
        elif ask == "s" and pc == "gun":
            print("You, lost computer shot you", lost)
            pc_wins = pc_wins + 1
            user_loss = user_loss + 1
            data1 = "Tries Left: " + str(tries) + " and Points: \n" + "Draw: " + str(draw) + " Times, "
            data2 = "Your Wins: " + str(user_wins) + ", " + "Computer Wins: " + str(pc_wins)
            data = data1 + data2
            print(data)
    elif ask == "g":
        print("You've selected: gun")
        print("Pc has selected: ", pc)
        if ask == "g" and pc == "water":
            print("Gun doesn't affects water,", lost)
            pc_wins = pc_wins + 1
            user_loss = user_loss + 1
            data1 = "Tries Left: " + str(tries) + " and Points: \n" + "Draw: " + str(draw) + " Times, "
            data2 = "Your Wins: " + str(user_wins) + ", " + "Computer Wins: " + str(pc_wins)
            data = data1 + data2
            print(data)
        elif ask == "g" and pc == "snake":
            print("Headshot, you killed him,", win)
            user_wins = user_wins + 1
            pc_loss = pc_loss + 1
            data1 = "Tries Left: " + str(tries) + " and Points: \n" + "Draw: " + str(draw) + " Times, "
            data2 = "Your Wins: " + str(user_wins) + ", " + "Computer Wins: " + str(pc_wins)
            data = data1 + data2
            print(data)
        elif ask == "g" and pc == "gun":
            print("Both selected gun, Draw")
            draw = draw + 1
            data1 = "Tries Left: " + str(tries) + " and Points: \n" + "Draw: " + str(draw) + " Times, "
            data2 = "Your Wins: " + str(user_wins) + ", " + "Computer Wins: " + str(pc_wins)
            data = data1 + data2
            print(data)
    elif ask == "w":
        print("You've selected: water")
        print("Pc has selected: ", pc)
        if ask == "w" and pc == "water":
            print("Water Water gives nothing, XD")
            draw = draw + 1
            data1 = "Tries Left: " + str(tries) + " and Points: \n" + "Draw: " + str(draw) + " Times, "
            data2 = "Your Wins: " + str(user_wins) + ", " + "Computer Wins: " + str(pc_wins)
            data = data1 + data2
            print(data)
        elif ask == "w" and pc == "snake":
            print("Computer drank you", lost)
            user_loss = user_loss + 1
            pc_wins = pc_wins + 1
            data1 = "Tries Left: " + str(tries) + " and Points: \n" + "Draw: " + str(draw) + " Times, "
            data2 = "Your Wins: " + str(user_wins) + ", " + "Computer Wins: " + str(pc_wins)
            data = data1 + data2
            print(data)
        elif ask == "w" and pc == "gun":
            print("Gun, doesn't affects you", win)
            user_wins = user_wins + 1
            pc_loss = pc_loss + 1
            data1 = "Tries Left: " + str(tries) + " and Points: \n" + "Draw: " + str(draw) + " Times, "
            data2 = "Your Wins: " + str(user_wins) + ", " + "Computer Wins: " + str(pc_wins)
            data = data1 + data2
            print(data)
    else:
        print("Wrong Input!!")
        data = "Tries Left: " + str(tries)
        print(data)
else:
    decide(tries)