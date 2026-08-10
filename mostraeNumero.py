def mostrarN(numero):
    posicion= 0
    for posicion in range (1,numero):
        
        if posicion % 3 ==0:
            print(fizz)
        elif posicion % 5 ==0:
            print(buzz)
        elif posicion % 3 ==0 and posicion % 5 ==0:
            print(fizzbuzz)
        else:
            return posicion
    posicion += 1 
x = mostrarN(3)
print(x)