# import os
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

from funciones import lineal, cuadratica

if __name__ == "__main__":

    print()
    print('Maquina de funciones')
    
    funcion=-1
    while funcion != 0:
        while funcion == -1:

            print()
            print('1) Funcion Lineal')
            print('2) Funcion Cuadratica')
            print('0) Terminar el programa')
            
            funcion=int(input('Elija su funcion:'))

            if funcion == 0:
                break
            elif funcion == 1:
                funcion = lineal()
            elif funcion == 2:
                funcion = cuadratica()
            elif funcion not in {-1,0,1,2}:
                print('Por favor ingrese un numero valido')
                funcion=-1

