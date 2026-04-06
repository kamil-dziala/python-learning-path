import random
choosing = True
min_val = 1
challange_levels = {
    "1" : 10,
    "2" : 50,
    "3" : 100,
}

total_tries = 0
game = 0
running = True

while choosing:
    level_choosen = input("What level do you wanna choose? (1,2,3): ")
    if level_choosen not in challange_levels:
        print("Invalid input")
        continue
    else:
        max_val = challange_levels[level_choosen]
        choosing = False
        break
print(f"\nYou chose level {level_choosen}!")










total_tries = 0
game = 0
running = True




while running:
    number = random.randint(min_val, max_val)
    tries = 0
    print(f"TEST : {number}")

    while True:
        guess = int(input(f"\nEnter number between {min_val} and {max_val}: "))

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
