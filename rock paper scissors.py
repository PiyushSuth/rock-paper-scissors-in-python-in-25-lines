import random

moves = "Rock", "Paper", "Scissors"

player_moves = int(input("Chose Rock as 1, Paper as 2 and Scissors as 3:"))
comp_moves = random.choice(moves)
print(f"Computer has chosen {comp_moves}")
# if player_moves == 1:
#     print("You have chosen rock")
# elif player_moves == 2:
#     print("You have chosen paper")
# elif player_moves == 3:
#     print("You have chosen rock")

if player_moves == comp_moves:
    print("Its a tie")
elif player_moves == 1:
    if comp_moves == "Paper":
        print("You Won!")
    elif comp_moves == "Scissors":
        print("You Lost")
elif player_moves == 2:
    if comp_moves == "Rock":
        print("You Won!")
    elif comp_moves == "Scissors":
        print("You Lost")
elif player_moves == 3:
    if comp_moves == "Rock":
        print("You Lost")
    elif comp_moves == "Paper":
        print("You Won!")