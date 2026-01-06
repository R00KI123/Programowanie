# Utwórz zmienne 'vowels' (samogłoski) i 'consonants' (spółgłoski) i przypisz każdej z nich wartość 0
vowels = 0
consonants = 0

# Utwórz pętlę i przeiteruj łańcuch znaków "Programowanie Python"
text = "Programowanie Python"

# Utwórz instrukcję warunkową IF-ELSE, która wyliczy liczbę samogłosek i spółgłosek w danym łańcuchu znaków
for char in text.lower():
    if char.isalpha():
        if char in "aeiouyąęó":
            vowels += 1
        else:
            consonants += 1

# Wydrukuj łączną liczbę samogłosek i spółgłosek w danym łańcuchu znaków
print("Liczba samogłosek:", vowels)
print("Liczba spółgłosek:", consonants)
