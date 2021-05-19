from random import randint

credit = 100
print("Welcome\nWhat number from 1 - 1000000000 am I thinking of?")
print(f"You have {credit} credits")
print("please place your bet")

number = randint(1, 1000000000)

while True:
    bet = int(input("Bet: "))
    print("What number am I thinking?")
    user_number = (int(input("Enter number: ")))

    if user_number == number:
        print("Correct, have some money!")
        credit = credit + bet
        print("Guess again!")

    else:
        print("Wrong! I'll take those credits thank you")
        credit = credit - bet
        print("Guess again!")

    if credit > 1000:
        break


print("YOU WON")
print("How did you do that?")
input()


