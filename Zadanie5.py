# Utwórz słownik filmów. Niech kluczem będzie nazwa filmu, a parą wartości dwie liczby:
# kryteria wiekowe oraz liczba dostępnych biletów
movies = {
    "Finding Nemo": [5, 2],
    "Moana": [6, 3],
    "Batman": [18, 5],
    "The Lion King": [10, 4]
}

# Utwórz pętlę, która będzie działać w nieskończoność
while True:

    # Pobierz tytuł filmu od użytkownika, usuń spacje z początku i końca
    # a następnie zamień frazę na format tytułowy
    movie = input("Podaj tytuł filmu (lub 'koniec' aby zakończyć): ").strip().title()

    if movie == "Koniec":
        print("Dziękujemy za skorzystanie z systemu rezerwacji")
        break

    # Stwórz instrukcję warunkową if. Jeśli wybrany film jest dostępny w słowniku, kontynuuj
    if movie in movies:

        # Zapytaj użytkownika o wiek
        age = int(input("Podaj swój wiek: "))

        # Sprawdź użytkownika pod kątem kwalifikowalności
        if age >= movies[movie][0]:

            # Jeśli użytkownik znajduje się w grupie docelowej, sprawdź dostępność miejsc
            if movies[movie][1] > 0:

                # Jeśli liczba dostępnych miejsc jest wartością dodatnią, zmniejsz pulę dostępnych miejsc o 1
                movies[movie][1] -= 1
                print("Rezerwacja udana")

            else:
                print("Brak dostępnych miejsc na ten film.")

        else:
            print("Nie spełniasz kryterium wiekowego")

    else:
        print("Nie mamy takiego filmu w repertuarze")
