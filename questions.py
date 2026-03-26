import random

categorias = {
    "Programacion": ["python", "variable", "funcion", "bucle", "lista", "cadena"],
    "Utiles": ["cartuchera", "lapiz", "goma", "regla", "compas", "tijera"],
    "Comidas": ["manzana", "fideos", "sushi", "milanesa", "guiso", "pure"]
}

print("¡Bienvenido al Ahorcado!")
print()

print("categorias disponibles:")

nombres_categorias = list(categorias.keys())
for cat in nombres_categorias:
    print(f'{cat}')
    
while True:    
    while True:
        num_categoria = input("elija el numero de la categoria: ")
        
        if num_categoria.isdigit():
            categ_bien = int(num_categoria) 
        
            if 1 <= categ_bien <= len(nombres_categorias):
                categoria_elegida = nombres_categorias[categ_bien - 1]
                break
            else:
                print(f"elija entre 1 y {len(nombres_categorias)}.")
        else:
            print("Entrada no valida. ingrese un número entero.")
            
    palabras_disponibles = categorias[categoria_elegida]

    fila_de_palabras = random.sample(palabras_disponibles, len(palabras_disponibles))

    while len(fila_de_palabras) > 0:
        word = fila_de_palabras.pop()
        guessed = []
        attempts = 6
        puntaje_total = 0

        print(f'categoria elegida: {categoria_elegida}, empezamos')
        print()

        print('nueva ronda')
        print(f'Palabras restantes en la categoría: {len(fila_de_palabras)+1}')

        while attempts > 0:
            # Mostrar progreso: letras adivinadas y guiones para las que faltan
            progress = ""
            for letter in word:
                if letter in guessed:
                    progress += letter + " "
                else:
                    progress += "_ "
            print(progress)
            # Verificar si el jugador ya adivinó la palabra completa
            if "_" not in progress:
                puntaje_total += 6
                print("¡Ganaste!")
                break
            
            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")
            
            letter = input("Ingresá una letra: ")

            if len(letter)!= 1 or not letter.isalpha():
                print('Entrada no valida')
                continue

            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                puntaje_total -= 1
                print("Esa letra no está en la palabra.")
            
            print()

        else:
            puntaje_total = 0
            print(f"¡Perdiste! La palabra era: {word}")

        print(f'puntaje de la ronda {puntaje_total}')

        if len(fila_de_palabras) == 0:
            print('no hay mas palabras en la categoria')
            break

        if len(fila_de_palabras) > 0:
                jugar_otra = input('para jugar otra ronda de la misma categoria presiona 1, si no presiona cualquier otra tecla ')
                if jugar_otra != '1':
                    break

    nueva_cat = input('si queres volver a jugar con las mismas palabras o cambiar la categoria presiona 1, si no presiona cualquier otra tecla ')    
    if nueva_cat != '1':
        break

