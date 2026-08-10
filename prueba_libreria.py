import sys 
sys.path.append(r'C:\Users\USER\proyecto1\libreria_personal') 
import misFunciones 
print('La libreria se importo correctamente') 
print(dir(misFunciones))

from misFunciones.recursividad import sumarn
print(sumarn(5))