#### Prosty program kalkulatora

# Utwórz funkcję dodawania dwóch liczb
def add(a, b):
    return a + b

# Utwórz funkcję odejmowania dwóch liczb
def subtract(a, b):
    return a - b

# Utwórz funkcję mnożenia dwóch liczb
def multiply(a, b):
    return a * b

# Utwórz funkcję dzielenia dwóch liczb
def divide(a, b):
    if b == 0:
        return "You can't divide by zero!"
    return a / b

# Wyświetl listę operacji
print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

# Pozwól użytkownikowi wybrać żądane działanie na podstawie wyświetlonej listy poleceń
op = input("Please enter choice (a/ b/ c/ d): ")

# Przechwyć 2 liczby wprowadzone przez użytkownika i przekonwertuj je na format liczby całkowitych
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Logika do wykonywania określonej operacji za pomocą instrukcji IF -ELIF -ELSE.
if op == "a":
    print("Result:", add(num1, num2))
elif op == "b":
    print("Result:", subtract(num1, num2))
elif op == "c":
    print("Result:", multiply(num1, num2))
elif op == "d":
    print("Result:", divide(num1, num2))
else:
    # Jeśli użytkownik wybierze operację, która nie jest dostępna, wyświetl komunikat o błędzie
    print("Invalid operation selected.")
