import random
min_val = 1
max_val = 10

total_tries = 0
game = 0
running = True




while running:
    number = random.randint(min_val, max_val)
    tries = 0
    print(number)

    while True:
        guess = int(input("\nEnter number between 1 and 10: "))

        if not (min_val <= guess <= max_val):
            print("Invalid input")
            continue

        tries += 1

        if guess == number:
            game += 1
            total_tries += tries
            print(f"You win in {tries} tries!")

            while True:
                again = input("\nWould you like to play again? (y/n) or type 'game' to chcek your wins: ")
                if again == "game":
                    print(f"You have won {game} games!")
                    continue
                elif again == "y":
                    break
                elif again == "n":
                    running = False
                    print(f"Thank you for playing, you won {game} games!Hope you enjoy your game!")
                    break

                else:
                    print("Invalid input")
            break
        elif guess > number:
            print("LOWWER")
        else:
            print("UPPER")


if game > 0:
    avarage_guesses_per_game = total_tries / game
    avarage_guesses_per_game = int(avarage_guesses_per_game)
    print(f"\nYour avarage guesses per game is {avarage_guesses_per_game} guesses!")
