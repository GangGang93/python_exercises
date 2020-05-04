# Import the modules here
import sys
import random

ans = True

while ans:
    question = input("ask the magic 8 ball a question: (press enter to quit)")

    answers = random.randint(1,8)

    if question == "":
        sys.exit()

    elif answers == 1:
        print("You're Valid")

    elif answers == 2:
        print("You're a dub")

    elif answers == 3:
        print("You lookin Shaky")

    elif answers == 4:
        print("Are You Dumb")

    elif answers == 5:
        print("You got 5 on it")

    elif answers == 6:
        print("Ya mama")

    elif answers == 7:
        print("Is you serious")

    elif answers == 8:
        print("I'm out")
