

number_to_guess = 2

user_number = int(input("Adivina un numero: "))


if number_to_guess == user_number:
    print("Has adivinado")
else:
    print("Incorrecto")
    user_number = int(input("Prueba otro numero: "))
    if number_to_guess == user_number:
        print("Has adivinado")
    else:
        print("Incorrecto")
        user_number = int(input("Prueba otro numero: "))
        if number_to_guess == user_number:
            print("Has adivinado")
        else:
            print("Incorrecto")
            user_number = int(input("Prueba otro numero: "))
            if number_to_guess == user_number:
                print("Has adivinado")
            else:
                print("Incorrecto")
                user_number = int(input("Prueba otro numero: "))
                if number_to_guess == user_number:
                    print("Has adivinado")
                else:
                    print("Has perdido")
