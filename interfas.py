import tkinter as tk
def sumar(n):
    if n <= 1: return 1
    return n + sumar(n-1)

def ejecutar():
    numero = int(entrada.get())
    resultado = sumar(numero)
    resp.config(text=f"El resultado es :{resultado}")

Windows = tk.Tk()
Windows.title("Aplicacion de Suma")
Windows.geometry("340x240")
Windows.minsize(320,220)
Windows.maxsize(500,350)

tk.Label(Windows,text="ingresa un numero n :").pack()
entrada = tk.Entry(Windows)
entrada.pack()

tk.Button(Windows, text="calcular", command=ejecutar).pack()
resp = tk.Label(Windows, text="Resultado = 0")
resp.pack()

Windows.mainloop()


#para crear un ejecutable
#pyintaller --noconsole --onefile INTERFAS.PY