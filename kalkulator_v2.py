print("--- Prosty Kalkulator (wpisz 'exit' aby zakończyć) ---")

while True:
    # Pobieramy pierwszą liczbę (z obsługą wyjścia)
    wejscie = input("\nWpisz pierwszą liczbę (lub 'exit'): ")
    if wejscie.lower() == 'exit':
        print("Do widzenia!")
        break

    try:
        num1 = float(wejscie)
        op = input("Wpisz operator (+, -, *, /, ^): ") # Dodałem ^ jako symbol potęgi
        num2 = float(input("Wpisz drugą liczbę: "))

        if op == "+":
            print(f"Wynik: {num1 + num2}")
        elif op == "-":
            print(f"Wynik: {num1 - num2}")
        elif op == "*":
            print(f"Wynik: {num1 * num2}")
        elif op == "/":
            if num2 == 0:
                print("Błąd: Nie można dzielić przez zero!")
            else:
                print(f"Wynik: {num1 / num2}")
        elif op == "^":
            # To jest nowa funkcja potęgowania
            # W Pythonie używamy ** do potęgowania
            print(f"Wynik: {num1 ** num2}") 
        else:
            print("Błąd: Nieznany operator")
            
    except ValueError:
        print("Błąd: Proszę wpisywać tylko liczby")

# Komentarz zostawiony przez Macieja Jakubowskiego.
