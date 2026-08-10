def menu():
    print("Bienvenido a su heladeria de confianza")
    print("Que desea ordenar hoy?")
    print("MENU PRINCIPAL")
    print("1. Helado sabor vainilla.")
    print("2. Helado sabor chocolate.")
    print("3. Salir. ")

def tomarPedido(totalPedido):
    menu()
    opcion = input("Elija un opcion del menu:")
    print()
    if opcion == "1":
        print("Elegiste un helado de vainilla y tiene un valor de $2")
        return tomarPedido(totalPedido + 2)
    elif opcion == "2":
        print("Elegiste un helado de chocolate y tiene un valor de $3")
        return tomarPedido(totalPedido + 3)
    elif opcion == "3":
        return totalPedido 

    else:
        print("Opción no válida. Intente de nuevo.")
        return tomarPedido(totalPedido)

           
def main():
    pagoTotal = tomarPedido(0)
    print("El total a pagar es:", pagoTotal,"gracias por su compra , vuelva pronto." )

main()