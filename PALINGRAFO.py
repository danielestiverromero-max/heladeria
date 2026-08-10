def palabra(texto):
    contador = 0
    for letra in texto:
        contador += 1
    return contador

def palingrafo(texto):
    es_palindromo = True
    longitud = palabra(texto)

    for i in range(longitud // 2):
        if texto[i] != texto[longitud - 1 - i]:
            es_palindromo = False
    return es_palindromo
    print("el texto ingresado es un palíndromo:", palingrafo(texto))
print(palingrafo("reconocer"))