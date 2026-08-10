
def vocal(texto):
    contador = 0
    vocales = "aeiouAEIOU"
    for letra in texto:
        for vocal in vocales:
            if letra == vocal:
                contador += 1

    return contador
print(vocal("elefante"))
