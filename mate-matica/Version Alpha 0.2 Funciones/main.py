
from funciones import lineal, Cuadratica, polinomica

print('Maquina de funciones')
print()
funcion=-1
while funcion != 0:
    while funcion == -1:
        print('0)Ingrese 0 para terminar el programa')
        print('1)Funcion Lineal')
        print('2)Funcion Cuadratica')
        print('3)Funcion Polinomica')
        funcion=int(input('Elija su funcion:'))
        if funcion==0:
            break
        if funcion==1:
            funcion=lineal()
        if funcion==2:
            funcion=Cuadratica()
        if funcion==3:
            funcion=polinomica()
        elif funcion not in {-1,0,1,2,3}:
            print('Por favor ingrese un numero valido')
            funcion=-1