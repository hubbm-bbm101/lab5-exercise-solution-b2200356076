import random
number = random.randint(1,100)
while True:
    user_input = int(input("guess your number:"))
    if user_input == number:
        print("You Won.")
        break
    elif user_input > number:
        print("decrease your number")
    else:
        print("increase your number")
