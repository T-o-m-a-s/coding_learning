def lineal():
    metodo=1
    while metodo != 0:
        print('Funcion Lineal')
        print('1) A partir de su pendiente y ordenada al origen')
        print('2) A partir de 2 puntos de esta')
        print('3) Ingrese 0 para volver al menu de funciones')
        continuar=0
        metodo=int(input('Seleccione la manera de dar los detalles de la funcion lineal:'))
        while metodo not in {0,1,2}:
            print('Por favor ingresar un numero valido')
            metodo=int(input('Seleccione la manera de dar los detalles de la funcion lineal:'))
        if metodo == 1:
            M=float(input('Ingrese el valor de su pendiente:'))
            B=float(input('Ingrese el valor de su ordenada al origen:'))
            if M == 0:
                if B == 0:
                    print('Su funcion es F(X)=0')
                else:
                    print('Su funcion es F(X)=',B)
            else:
                print('Su funcion es F(X)=',M,'X','+',B)
                continuar=1
        elif metodo == 2:
            X1=float(input('Ingrese el valor en X del primer punto:')) 
            X2=float(input('Ingrese el valor en X del segundo punto:'))
            Y1=float(input('Ingrese el valor en Y del primer punto:'))
            Y2=float(input('Ingrese el valor en Y del segundo punto:'))
            if X1!=X2 and Y1!=Y2:
                M=float((Y2-Y1)/(X2-X1))
                B=float(Y1-M*X1)
                print('Su funcion es F(X)=',M,'X','+',B)
                continuar=1
            elif X1==X2:
                print('No es una funcion bien definida para el formato F(X)=X')
            elif Y1==Y2:
                B=Y1
                print('Su funcion es F(X)=',B)
        elif metodo == 0:
            break
        if continuar == 1 and M != 0:
            ev=int(input('Si desea evaluar la funcion obtenida en algun valor de X ingrese 1, sino ingrese 0 para volver al menu de funcion lineal:'))
            while ev != 0:
                if ev == 1:
                    resev=evlineal(M,B)
                    if resev==0:
                        ev=0
                else:
                    print('Por favor ingresar solo los comandos disponibles')
                    ev=int(input('Si desea evaluar la funcion obtenida en algun valor de X ingrese 1, sino ingrese 0 para volver al menu de funcion lineal:'))
    return -1

def evlineal(M,B):
    continuar=1
    while continuar !=0:
        if continuar == 1:
            X=float(input('Ingrese el numero en el que desea evaluar la funcion:'))
            Y=M*X+B
            print('El resultado de evaluar en ese valor es:',Y)
        else:
            print('Por favor ingresar solo los comandos disponibles')
        continuar=float(input('Ingrese 0 para volver al menu de funcion lineal o ingrese 1 para volver a evaluar en la misma funcion:'))
    return 0

def cuadratica():
    metodo=1
    while metodo !=0:
        print('Funcion Cuadratica')
        print('1) A partir de sus coeficientes B y C')
        print('2) A partir de sus raices')
        print('3) A partir de las coordenadas de su vertice')
        print('4) A partir de 3 puntos')
        print('5) Ingrese 0 para volver al menu de funciones')
        print()
        print('Tener en cuenta que en metodos 1, 2 y 3 se necesita el valor del coeficiente A')
        print()
        continuar=1
        metodo=int(input('Seleccione la manera de dar los detalles de la funcion cuadratica:'))
        while metodo not in {0,1,2,3,4}:
            print('Por favor ingresar un numero valido')
            metodo=int(input('Seleccione la manera de dar los detalles de la funcion cuadratica:'))
        if metodo == 1:
                A=float(input('Ingrese el valor del coeficiente A:')) 
                B=float(input('Ingrese el valor del coeficiente B:'))
                C=float(input('Ingrese el valor del coeficiente C:'))
                while A == 0:
                    A=float(input('Por favor ingrese un valor distinto de 0 para A:'))                
                if B == 0:
                    if C == 0:
                        print('Su funcion es F(X)=',A,'X^2')
                    else:
                        print('Su funcion es F(X)=',A,'X^2','+',C)   
                else:
                    if C == 0:
                        print('Su funcion es F(X)=',A,'X^2','+',B,'X')
                    else:
                        print('Su funcion es F(X)=',A,'X^2','+',B,'X','+',C)                  
                if B != 0:    
                    XV=-(B/2*A)
                elif B == 0:
                    XV=0
                YV=A*(XV)**2+B*XV+C
                disc=B**2-4*A*C
                if disc == 0:
                    print('Tiene raiz doble en el',XV)
                    X1=XV
                    X2=X1
                elif disc > 0:
                    X1=XV+(disc)**(1/2)/2*A
                    X2=XV-(disc)**(1/2)/2*A
                    print('Sus raices son',X1,'y',X2)
                elif disc < 0:
                    X1=complex(XV,+(-disc)**(1/2)/2*A)
                    X2=complex(XV,-(-disc)**(1/2)/2*A)
                    print('Sus raices complejas son',X1,'y',X2)
                    print('Con j=i')
                print('Las coordenadas de su vertice son',XV,'en X y',YV,'en Y')
        if metodo == 2:
            print('1)Ingrese 1 si tiene una sola raiz doble real')
            print('2)Ingrese 2 si tiene dos raices reales')
            print('3)Ingrese 3 si tiene dos raices complejas')
            metodoraiz=int(input('Elija su opcion:'))
            if metodoraiz not in {1,2,3}:
                print('Por favor ingrese un numero valido')
                metodoraiz=int(input('Elija su opcion:'))
            if metodoraiz in {1,2,3}:
                A=float(input('Ingrese el valor del coeficiente A:'))
                while A == 0:
                    A=float(input('Por favor ingrese un valor distinto de 0 para A:'))
                if metodoraiz == 1:
                    X0=float(input('Ingrese el valor de su raiz doble:'))
                    B=-2*A*X0
                    C=A*(X0)**2
                    if B == 0:
                        if C == 0:
                            print('Su funcion es F(X)=',A,'X^2')
                        else:
                            print('Su funcion es F(X)=',A,'X^2','+',C)   
                    else:
                        if C == 0:
                            print('Su funcion es F(X)=',A,'X^2','+',B,'X')
                        else:
                            print('Su funcion es F(X)=',A,'X^2','+',B,'X','+',C)
                    print('Las coordenadas de su vertice son',X0,'en X y 0 en Y')
                elif metodoraiz == 2:
                    X1=float(input('Ingrese el valor de su primera raiz real:'))
                    X2=float(input('Ingrese el valor de su segunda raiz real:'))
                    while X1 == X2:
                        X2=float(input('Ingrese un valor que sea distinto del de la primera raiz:'))
                    B=-2*A*(X1+X2)
                    C=A*X1*X2
                    XV=(X1+X2)/2
                    YV=A*(XV)**2+B*XV+C
                    if B == 0:
                        if C == 0:
                            print('Su funcion es F(X)=',A,'X^2')
                        else:
                            print('Su funcion es F(X)=',A,'X^2','+',C)   
                    else:
                        if C == 0:
                            print('Su funcion es F(X)=',A,'X^2','+',B,'X')
                        else:
                            print('Su funcion es F(X)=',A,'X^2','+',B,'X','+',C)
                    print('Las coordenadas de su vertice son',XV,'en X y',YV,'en Y')
                elif metodoraiz == 3:
                    print('Recordar: En estos casos siempre se cumple que las raices son Z1 y su conjugado,por lo que sus partes reales deben ser iguales')
                    real=float(input('Ingrese el valor de la parte real:'))
                    imaginario=float(input('Ingrese el valor de la parte imaginaria:'))
                    while imaginario == 0:
                        float(input('Por favor ingresar una parte imaginaria distinta de 0:'))
                    imaginario=abs(imaginario)
                    B=-2*A*real
                    C=A*(real**2+imaginario**2)
                    if B == 0:
                        if C == 0:
                            print('Su funcion es F(X)=',A,'X^2')
                        else:
                            print('Su funcion es F(X)=',A,'X^2','+',C)   
                    else:
                        if C == 0:
                            print('Su funcion es F(X)=',A,'X^2','+',B,'X')
                        else:
                            print('Su funcion es F(X)=',A,'X^2','+',B,'X','+',C)
                    if real == 0:
                        print('Las coordenadas de su vertice son 0 en X y',C,'en Y')
                    else:
                        YV=A*real**2+B*real+C
                        print('Las coordenadas de su vertice son',real,'en X y',YV,'en Y')
        if metodo == 3:
            A=float(input('Ingrese el valor del coeficiente A:'))
            while A == 0:
                A=float(input('Por favor ingrese un valor distinto de 0 para A:'))
            XV=float(input('Ingrese el valor en el eje X del vertice:'))
            YV=float(input('Ingrese el valor en el eje Y del vertice:'))
            B=-2*A*XV
            C=A*(XV)**2+YV
            disc=B**2-4*A*C
            if disc == 0:
                print('Tiene raiz doble en el',XV)
                X1=XV
                X2=X1
            elif disc > 0:
                X1=XV+(disc)**(1/2)/2*A
                X2=XV-(disc)**(1/2)/2*A
                print('Sus raices son',X1,'y',X2)
            elif disc < 0:
                X1=complex(XV,+(-disc)**(1/2)/2*A)
                X2=complex(XV,-(-disc)**(1/2)/2*A)
                print('Sus raices complejas son',X1,'y',X2)
                print('Con j=i')
            if B == 0:
                if C == 0:
                    print('Su funcion es F(X)=',A,'X^2')
                else:
                    print('Su funcion es F(X)=',A,'X^2','+',C)   
            else:
                if C == 0:
                    print('Su funcion es F(X)=',A,'X^2','+',B,'X')
                else:
                    print('Su funcion es F(X)=',A,'X^2','+',B,'X','+',C) 
        if metodo == 4:
            valido=0
            X1=float(input('Ingrese el valor en X del primer punto:')) 
            Y1=float(input('Ingrese el valor en Y del primer punto:'))
            X2=float(input('Ingrese el valor en X del segundo punto:'))
            Y2=float(input('Ingrese el valor en Y del segundo punto:'))
            X3=float(input('Ingrese el valor en X del tercer punto:'))
            Y3=float(input('Ingrese el valor en Y del tercer punto:'))
            if Y1 != Y2 != Y3 and X1 != X2 != X3:
                valido=1
            elif Y1 == Y2 and Y3 != Y1 and Y3 != Y2 and X1 != X2 != X3:
                valido=1
            elif Y1 == Y3 and Y2 != Y1 and Y2 != Y3 and X1 != X2 != X3:
                valido=1
            elif Y2 == Y3 and Y1 != Y2 and Y1 != Y3 and X1 != X2 != X3:
                valido=1
            if valido == 1:
                CTE1=(X1-X2)*(X1-X3)
                CTE2=(X2-X1)*(X2-X3)
                CTE3=(X3-X1)*(X3-X2)
                A=Y1/CTE1+Y2/CTE2+Y3/CTE3
                B=-(Y1*(X3+X2))/CTE1-(Y2*(X3+X1))/CTE2-(Y3*(X2+X1))/CTE3
                C=(Y1*X2*X3)/CTE1+(Y2*X1*X3)/CTE2+(Y3*X2*X1)/CTE3
                A1=round(A,2)
                B1=round(B,2)
                C1=round(C,2)
                if A == 0:
                    print('Los valores de los puntos no permiten crear una funcion cuadratica,intente con otros.')
                    continuar=0
                elif A != 0:
                    if B != 0:    
                        XV=-(B/2*A)
                    elif B == 0:
                        XV=0
                    YV=A*(XV)**2+B*XV+C
                    disc=B**2-4*A*C
                    if disc == 0:
                        X1=XV
                        X2=X1
                        XRV=round(XV,2)
                        print('Tiene raiz doble en el',XRV)
                    elif disc > 0:
                        X1=XV+(disc)**(1/2)/2*A
                        X2=XV-(disc)**(1/2)/2*A
                        XR1=round(X1,2)
                        XR2=round(X2,2)
                        print('Sus raices son',XR1,'y',XR2)
                    elif disc < 0:
                        X1=complex(round(XV,2),round((+(-disc)**(1/2)/2*A),2))
                        X2=complex(round(XV,2),round((-(-disc)**(1/2)/2*A),2))
                        print('Sus raices complejas son',X1,'y',X2)
                        print('Con j=i')
                    XRV=round(XV,2)
                    YRV=round(YV,2)
                    print('Las coordenadas de su vertice son',XRV,'en X y',YRV,'en Y')
                    if B == 0:
                        if C == 0:
                            print('Su funcion es F(X)=',A1,'X^2')
                        else:
                            print('Su funcion es F(X)=',A1,'X^2','+',C1)   
                    else:
                        if C == 0:
                            print('Su funcion es F(X)=',A1,'X^2','+',B1,'X')
                        else:
                            print('Su funcion es F(X)=',A1,'X^2','+',B1,'X','+',C1)                  
            if valido == 0:
                print('Los valores de los puntos no permiten crear una funcion cuadratica,intente con otros.')
        if metodo == 0:
            break
        if continuar == 1:
            ev=int(input('Si desea evaluar la funcion obtenida en algun valor de X ingrese 1, sino ingrese 0 para volver al menu de funcion cuadratica:'))
            while ev != 0:
                if ev == 1:
                    resev=evcuadratica(A,B,C)
                    if resev==0:
                        ev=0
                else:
                    print('Por favor ingresar solo los comandos disponibles')
                    ev=int(input('Si desea evaluar la funcion obtenida en algun valor de X ingrese 1, sino ingrese 0 para volver al menu de funcion cuadratica:'))      
    return -1

def evcuadratica(A,B,C):
    continuar=1
    while continuar !=0:
        if continuar == 1:
            X=float(input('Ingrese el numero en el que desea evaluar la funcion:'))
            Y=A*(X)**2+B*X+C
            print('El resultado de evaluar en ese valor es:',Y)
        else:
            print('Por favor ingresar solo los comandos disponibles')
        continuar=float(input('Ingrese 0 para volver al menu de funcion cuadratica o ingrese 1 para volver a evaluar en la misma funcion:'))
    return 0