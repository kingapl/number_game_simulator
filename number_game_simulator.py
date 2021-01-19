import random, time


def pick_numbers():
    print("+++++\nPodaj kolejno 5 liczb z zakresu 1-30.")

    quantity = 0
    numbers = []

    while quantity < 5:
        try:
            number = int(input("Wybrano: "))
            if number <= 0 or number > 30:
                print("Nie można wybrać liczby spoza zakresu.")
            elif number not in numbers:
                numbers.append(number)
                quantity += 1
            else:
                print("Liczba została już wybrana, podaj inną.")
        except ValueError:
            print("Nie wybrano liczby. Podaj liczbę.")

    print(f"\nWybrane liczby: {sorted(numbers)}.") 

    return numbers


def draw():
    print("\nLosowanie pięciu liczb z zakresu 1-30.\n**********\n")
    time.sleep(1)

    quantity = 0
    drawn_numbers = []

    print("Wylosowane liczby to:")
    time.sleep(1)

    while quantity < 5:
        drawn_number = random.randint(1, 30)
        if drawn_number not in drawn_numbers:
            drawn_numbers.append(drawn_number)
            print(drawn_number)
            quantity += 1
            time.sleep(1)
        else:
            continue
    
    return drawn_numbers
    

def verify_matching_numbers(numbers, drawn_numbers):
    matching = 0
    matching_numbers = []

    for number in numbers:
        for drawn_number in drawn_numbers:
            if number == drawn_number:
                matching += 1
                matching_numbers.append(number)
            else:
                continue
                
    return matching, matching_numbers


numbers = pick_numbers()
drawn_numbers = draw()
matching, matching_numbers = verify_matching_numbers(numbers, drawn_numbers)

print(f"\nIlość trafień: {matching}")
if matching_numbers != []:
    print(f"Trafione liczby: {matching_numbers}")
print(f"Wygrana: {matching*100} zł\n+++++")