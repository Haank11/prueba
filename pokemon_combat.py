
pokemon_elegido = input("¿Contra que pokemon quieres luchar? (Charmander/Bulbasaur/Squirtle): ")

vida_pikachu = 100
vida_enemigo = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"

elif pokemon_elegido == "Charmander":
    vida_enemigo = 85
    nombre_pokemon = "Charmander"
    vida_pokemon = "Charmander"

elif pokemon_elegido == "Bulbasaur":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasaur"

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque quieres usar? (Chispa/Onda voltio): ")

    if ataque_elegido == "Chispa":
        print("Pikachu usa Chispa, haz provocado 10 de daño")
        vida_enemigo -= 10
    if ataque_elegido == "Onda voltio":
        print("Pikachu usa Onda voltio, haz provocado 12 de daño")
        vida_enemigo -= 12

    print("La vida de {} ahora es de {}".format(nombre_pokemon , vida_enemigo))

    if pokemon_elegido == "Squirtle":
        print("Squirtle usa Burbuja, te provoca 9 de daño")
        vida_pikachu -= 9

    if pokemon_elegido == "Bulbasaur":
        print("Bulbasaur usa Latigo Cepa, te provoca 8 de daño")
        vida_pikachu -= 8

    if pokemon_elegido == "Charmander":
        print("Charmander usa Ascuas, te provoca 7 de daño")
        vida_pikachu -= 7
    print("La vida de Pikachu ahora es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("¡Has ganado!")
if vida_pikachu <= 0:
    print("¡Has perdido!")

print("El combate ha terminado.")