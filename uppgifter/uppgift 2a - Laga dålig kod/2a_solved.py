from random import randint

# Variables
credit = 100
number_range = [1, 50]
number_answer = randint(number_range[0], number_range[-1])

print("Hello, and welcome to the game!")
print("The object of the game is to reach 1000 credits\nYou earn credits by guessing what number I am thinking of")
print(f'the number can be between {number_range[0]} and {number_range[-1]}')
print(f"You have {credit} credits")
print("please place your bet")
print()

# Main Loop
while 0 < credit < 1000:
    # Bet Loop
    while True:
        try:
            temp_bet = int(input("Bet: "))
            if 0 < temp_bet <= credit:
                bet = temp_bet
                break
            else:
                print('not a valid bet, try again')
                continue
        except ValueError:
            print("That is not a whole number, try again")
            continue

    print("Now then, what number am I thinking of?")

    # Guess Loop
    while True:
        # The try-statement is not something we've used yet. It "tries" to run the code, in this case it tries to
        # convert the input() to an integer. Normally, if we would enter something that can't be converted to an
        # integer here, the program would crash. With a try statement, we instead raise an exception, and execute
        # the code under the except. We could also solve this with if-statements but the code would be harder to read.
        try:
            user_number = (int(input("Enter number: ")))
            if number_range[0] <= user_number <= number_range[-1]:
                break
            else:
                print(f"not within scope, remember your guess must be between {number_range[0]} and {number_range[-1]}.")
                continue
        except ValueError:
            print("Not a whole number, please try again")
            continue

    # Evaluate Loop
    if user_number == number_answer:
        print("Correct, have some money!")
        credit = credit + bet
        print(f"Your current credit is {credit}")

    else:
        print("Wrong! I'll take those credits thank you")
        credit = credit - bet
        print(f"Your current credit is {credit}")

    print()

    if credit > 0:
        print("Guess again!")

print()
if credit <= 0:
    print("You lost The whole game!\nPress enter to quit")
else:
    print("You won!\nPress enter to quit")




