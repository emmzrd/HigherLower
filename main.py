from art import logo, vs
from game_data import data
from replit import clear
import random

score = 0
D = random.choice(data)

should_continue = True
while should_continue:

    C = D
    D = random.choice(data)

    A_followers = [value for value in C.values()][1]
    B_followers = [value for value in D.values()][1]

    print(logo)
    print(A_followers)
    print(B_followers)


    def compare_C():
        print("Compare A:", [value for value in C.values()][0], ', a', [value for value in C.values()][2], ", from",
              [value for value in C.values()][3])


    compare_C()

    print(vs)


    def compare_D():
        print("Against B:", [value for value in D.values()][0], ', a', [value for value in D.values()][2], ", from",
              [value for value in D.values()][3])


    compare_D()

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    clear()
    if guess == "A":
        if A_followers > B_followers:
            score += 1
            print(f"You're right! Current score is {score}")

        elif A_followers < B_followers:
            print(logo)
            print(f"Sorry, that's wrong. Final score is {score}")
            should_continue = False

    elif guess == "B":
        if A_followers > B_followers:
            print(logo)
            print(f"Sorry, that's wrong. Final score is {score}")
            should_continue = False

        elif A_followers < B_followers:
            score += 1
            print(f"You're right! Current score is {score}")
