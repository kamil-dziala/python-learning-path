import time


#wiek

while True:
    wiek = int(input('Wiek '))
    if wiek > 0:
        break
    else:
        print('Podaj prawdziwy wiek')


#waga
while True:
    waga = float(input('Waga '))
    if waga > 0:
        break
    else:
        print('Podaj prawdziwą waga!')


#wzrost
while True:
    wzrost = float(input('Wzrost '))
    if wzrost > 0:
        break
    else:
        print('Podaj prawdziwy wzrost!')


#płeć użytkownika
while True:
    współczynnik_płeć = input('Jaką jest twoja płeć (napisz m lub k ) ').strip().lower()
    if współczynnik_płeć in ['m', 'k']:
        break
    else:
        print('Podaj prawdziwą płeć')


#wzór na bmr
x = {'m' : 5, 'k': -161
}

bmr = 10 * waga + 6.25 * wzrost - 5 * wiek + x[współczynnik_płeć]




akt = {'1': 1.2,
           '2': 1.375,
           '3': 1.55,
           '4': 1.725,
           '5': 1.9,
    }

akt_akt = {'1': 'aktywność bardzo mała około 1000 kroków',
           '2': 'aktywność mała około 4000 kroków',
           '3': 'aktywność średnia 3 treningi w tygodniu',
           '4': 'aktyność duża, praca fizyczna i treningi',
           '5': 'aktywność bardzo duża, cięzka praca fizyczna',
           }



    #poziomy aktywnośći
time.sleep(1)
print ('Wybierz poziom aktywności ' )
time.sleep(1)
print('1 - brak aktywności')
time.sleep(1)
print("2 – lekka aktywność")
time.sleep(1)
print("3 – umiarkowana aktywność")
time.sleep(1)
print("4 – duża aktywność")
time.sleep(1)
print("5 – bardzo duża aktywność")
time.sleep(1)



while True:
    poziom_akt = input('Podaj poziom aktywnośći ').strip().lower()
    if poziom_akt in akt.keys():
        break
    else:
            print(f'Podaj poprawną aktywność, ponieważ : {poziom_akt}, jest nie poprawny')
time.sleep(1)
print(f'Wybrano poziom {poziom_akt}')
time.sleep(1)
print(f'Czyli: {akt_akt[poziom_akt]}')
time.sleep(1)










zapotrzebowanie = bmr * akt[poziom_akt]

print(f'Twoje zapotrzebowanie jest równe {zapotrzebowanie:.2f} kcal')




time.sleep(1)


#cel







cel = {'przytyć' : +250,
       'schudnąć': -250,
       'utrzymac formę' : -0,
}
while True:
    forma = input('Chcesz przytyć, schudnąć czy utrzymać formę? ')
    if forma in cel.keys():
        break
    else:
        print('Napisz jeszcze raz poprawnie')

zapotrzebowanie += cel[forma]
print(f'Więc teraz musisz jeść {zapotrzebowanie:.2f} kcal')