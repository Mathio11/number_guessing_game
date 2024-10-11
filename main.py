import random
import art
print(art.logo)


def easy(num):
    attempts = 10
    for i in range(attempts):
        print(f"Number of attempts: {attempts}")
        guess = int(input("Make a guess:\n"))
        if num == guess:
            return "You are correct, You have the won the game, congrats"
        elif num < guess:
            attempts -= 1
            print("Too High")
        elif num > guess:
            attempts -= 1
            print("Too Low")
    if attempts == 0:
        return "You ran out of attempts, better luck next time"

def hard(num):
    attempts = 5
    for i in range(attempts):
        print(f"Number of attempts: {attempts}")
        guess = int(input("Make a guess:\n"))
        if num == guess:
            return "You are correct, You have the won the game, congrats"
        elif num < guess:
            attempts -= 1
            print("Too High")
        elif num > guess:
            attempts -= 1
            print("Too Low")
    if attempts == 0:
        return "You ran out of attempts, better luck next time"



def number_guessing():
    print("Welcome to the number guessing game")
    difficulty = input("Which difficulty do you want to play: easy or hard\n").lower()
    num = random.randint(0, 100)

    if difficulty == 'easy':
        print(easy(num))
    elif difficulty == 'hard':
        print(hard(num))
    else:
        print("Invalid choice, please choose 'easy' or 'hard'.")
        return number_guessing()

    play_again = input("Do you want to play again? yes or no\n").lower()
    if play_again == 'yes':
        number_guessing()
    else:
        print("Thanks for playing!")




number_guessing()






