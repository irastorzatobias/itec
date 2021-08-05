def repiteLetra(letra, palabra):
    contador = 0
    for e in palabra:
        if e == letra:
            contador = contador + 1
    return contador

word = 'Quiero comer manzanas, solamente manzanas'
char = input('Ingrese una letra: ')


print(f"{char} se repite {repiteLetra(char, word)} veces")

