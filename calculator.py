import math

while True:
    symbols = {"+", "-", "*" , "/" , "**","sqrt","!"}


    while True:
        symbol = input("\nEnter symbol: (+,-,*,/,**,sqrt,!) lub stop (aby zatrzymać kalkulator): ").lower().strip()
        if symbol == "stop" or symbol in symbols:
            break
        else:
            print("Invalid input try again")

    if symbol == "stop":
        print("Okej do zobacznia")
        break




    try:
#SILNIA
        if symbol == "!":
            first_number = float(input("Enter number: "))
            first_number = int(first_number)
            while first_number < 0:
                print("Cant make it")
                first_number = int(input("Enter number again: "))

            print(f"{math.factorial(first_number)}")


#PIERWIASTEK
        elif symbol == "sqrt":
            first_number = float(input("Enter number: "))

            while first_number < 0:
                print("Cant make it")
                first_number = float(input("Enter number again: "))

            print(f"{math.sqrt(first_number):.2f}")




#ZADAWANIE PYTAŃ O LICZBY
        else:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))




#DODAWANIE
            if symbol == "+":
                print(f"{first_number + second_number:.2f}")
#ODJEMOWANIE
            elif symbol == "-":
                print(f"{first_number - second_number:.2f}")
#MNOŻENIE
            elif symbol == "*":
                print(f"{first_number * second_number:.2f}")



#DZIELENIE
            elif symbol == "/":
                while second_number == 0:
                    print("Division by zero")
                    second_number = float(input("Enter second numbe again: "))

                print(f"{first_number / second_number:.2f}")













#POTĘGA
            elif symbol == "**":
                print(pow(first_number, second_number))

    except ValueError:
        print("Błąd: Musisz podać liczbę, a nie tekst!")