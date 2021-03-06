from random import randint

# Variables
credit = 100
number_range = [1, 1]
number_answer = randint(number_range[0], number_range[-1])

# Just introduces the game
def introduction():
    print("Hello, and welcome to the game!")
    print("The object of the game is to reach 1000 credits\nYou earn credits by guessing what number I am thinking of")
    print(f'the number can be between {number_range[0]} and {number_range[-1]}')
    print(f"You have {credit} credits")
    print("please place your bet")
    print()


# Function that compares numbers within our specification
def get_valid_number(low, high, word):
    while True:
        try:
            entered = int(input(word))
            if low < entered < high:
                return entered
            else:
                print("Error, invalid number.\nPlease try again.")
                print()
                continue
        except ValueError:
            print("That is not a whole number, try again")
            continue


# evaluates our results and returns a positive number if we win, negative if we loose
def evaluate_results(bet, number):
    if number == number_answer:
        print("Correct, have some money!")
        return bet
    else:
        print("Wrong! I'll take those credits thank you")
        return -bet


introduction()

# Main Loop
while 0 < credit < 1000:

    print()

    # Place bet
    user_bet = get_valid_number(0, credit + 1, 'Bet: ')

    print("Now then, what number am I thinking of?")

    # Make Guess
    # The get_valid_number function checks that are number _within_ a range, but not including the high and low numbers.
    # We want to the high and low numbers to be valid, so we extend the range when calling the function by
    # adding -1 on the low order value and +1 on the high order value.
    user_number = get_valid_number(number_range[0] - 1, number_range[-1] + 1, "Enter number: ")

    # Evaluate
    credit += evaluate_results(user_bet, user_number)
    print(f"Your current credit is {credit}")

    print()

    if 0 < credit < 1000:
        print("Guess again!")

print()
if credit <= 0:
    print("You lost The whole game!\nPress enter to quit")
else:
    print("You won!\nPress enter to quit")




