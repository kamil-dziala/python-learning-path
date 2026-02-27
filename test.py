wiek_str = input("Ile masz lat? ")
# Musimy zamienić tekst na liczbę (integer), żeby móc ją porównać
wiek = int(wiek_str)

if wiek >= 18:
    print("Jesteś pełnoletni! Możesz wejść.")
    print("Zapraszamy!")
else:
    print("Jesteś niepełnoletni.")
    brakuje = 18 - wiek
    print("Wróć do nas za " + str(brakuje) + " lat(a)")
print('Hello world')