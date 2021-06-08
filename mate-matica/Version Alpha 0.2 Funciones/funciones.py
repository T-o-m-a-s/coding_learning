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
            if M != 0:
                continuar=1
            impresoradepolinomios(0,0,0,0,0,0,0,0,0,M,B)
        elif metodo == 2:
            X1=float(input('Ingrese el valor en X del primer punto:')) 
            X2=float(input('Ingrese el valor en X del segundo punto:'))
            Y1=float(input('Ingrese el valor en Y del primer punto:'))
            Y2=float(input('Ingrese el valor en Y del segundo punto:'))
            if X1!=X2 and Y1!=Y2:
                M=float((Y2-Y1)/(X2-X1))
                B=float(Y1-M*X1)
                impresoradepolinomios(0,0,0,0,0,0,0,0,0,M,B)
                continuar=1
            elif X1==X2:
                print('No es una funcion bien definida para el formato F(X)=X')
            elif Y1==Y2:
                B=Y1
                impresoradepolinomios(0,0,0,0,0,0,0,0,0,0,B)
        elif metodo == 0:
            break
        if continuar == 1 and M != 0:
            ev=int(input('Si desea evaluar la funcion obtenida en algun valor de X ingrese 1, sino ingrese 0 para volver al menu de funcion lineal:'))
            while ev != 0:
                if ev == 1:
                    resev=evaluadorapolinomios(0,0,0,0,0,0,0,0,0,M,B)
                    if resev==0:
                        ev=0
                else:
                    print('Por favor ingresar solo los comandos disponibles')
                    ev=int(input('Si desea evaluar la funcion obtenida en algun valor de X ingrese 1, sino ingrese 0 para volver al menu de funcion lineal:'))
    return -1
def Cuadratica():
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
                impresoradepolinomios(0,0,0,0,0,0,0,0,A,B,C)                  
                if B != 0:    
                    XV=-(B/(2*A))
                elif B == 0:
                    XV=0
                YV=A*(XV)**2+B*XV+C
                Bhaskara(XV,A,B,C)
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
                    impresoradepolinomios(0,0,0,0,0,0,0,0,A,B,C)
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
                    impresoradepolinomios(0,0,0,0,0,0,0,0,A,B,C)
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
                    impresoradepolinomios(0,0,0,0,0,0,0,0,A,B,C)
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
            Bhaskara(XV,A,B,C)
            impresoradepolinomios(0,0,0,0,0,0,0,0,A,B,C)
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
                if A == 0:
                    print('Los valores de los puntos no permiten crear una funcion cuadratica,intente con otros.')
                    continuar=0
                elif A != 0:
                    if B != 0:    
                        XV=-(B/(2*A))
                    elif B == 0:
                        XV=0
                    YV=A*(XV)**2+B*XV+C
                    Bhaskara(XV,A,B,C)
                    XRV=round(XV,2)
                    YRV=round(YV,2)
                    print('Las coordenadas de su vertice son',XRV,'en X y',YRV,'en Y')
                    impresoradepolinomios(0,0,0,0,0,0,0,0,A,B,C)                  
            if valido == 0:
                print('Los valores de los puntos no permiten crear una funcion cuadratica,intente con otros.')
        if metodo == 0:
            break
        if continuar == 1:
            ev=int(input('Si desea evaluar la funcion obtenida en algun valor de X ingrese 1, sino ingrese 0 para volver al menu de funcion cuadratica:'))
            while ev != 0:
                if ev == 1:
                    resev=evaluadorapolinomios(0,0,0,0,0,0,0,0,A,B,C)
                    if resev==0:
                        ev=0
                else:
                    print('Por favor ingresar solo los comandos disponibles')
                    ev=int(input('Si desea evaluar la funcion obtenida en algun valor de X ingrese 1, sino ingrese 0 para volver al menu de funcion cuadratica:'))      
    return -1
def Bhaskara(XV,A,B,C):
    disc=B**2-4*A*C
    if disc == 0:
        X1=XV
        X2=X1
        XRV=round(XV,2)
        print('Tiene raiz doble en el',XRV)
    elif disc > 0:
        X1=XV+(disc)**(1/2)/(2*A)
        X2=XV-(disc)**(1/2)/(2*A)
        XR1=round(X1,2)
        XR2=round(X2,2)
        print('Sus raices son',XR1,'y',XR2)
    elif disc < 0:
        X1=complex(round(XV,2),round((+(-disc)**(1/2)/(2*A)),2))
        X2=complex(round(XV,2),round((-(-disc)**(1/2)/(2*A)),2))
        print('Sus raices complejas son',X1,'y',X2)
        print('Con j=i')                    
def polinomica():
    metodo=1
    while metodo != 0:
        print('Funcion Polinomica')
        print('1) A partir de sus coeficientes')
        print('2) A partir de puntos de esta')
        print('3) Ingrese 0 para volver al menu de funciones')
        metodo=int(input('Elija su opcion:'))
        while metodo not in {0,1,2}:
            print('Por favor ingresar un numero valido')
            metodo=int(input('Elija su opcion:'))
        if metodo == 1:
            polinomiocoeficiente()
        if metodo == 2:
            polinomiointerpolar()
    return -1
def impresoradepolinomios(A,B,C,D,E,F,G,H,I,J,K):
    polinomio=[]
    mas='+'
    menos='-'
    A=round(A,2)
    B=round(B,2)
    C=round(C,2)
    D=round(D,2)
    E=round(E,2)
    F=round(F,2)
    G=round(G,2)
    H=round(H,2)
    I=round(I,2)
    J=round(J,2)
    K=round(K,2)
    A=str(A)
    B=str(B)
    C=str(C)
    D=str(D)
    E=str(E)
    F=str(F)
    G=str(G)
    H=str(H)
    I=str(I)
    J=str(J)
    K=str(K)   
    if float(A) != 0:
        X10='X^10'
        if float(A) < 0:
            A=float(A)
            A=abs(A)
            A=str(A)
            if polinomio == []:
                polinomio.append(menos)
            elif polinomio != []:
                polinomio.pop()
                polinomio.append(menos)
        if float(A) == 1:
            polinomio.append(X10)
        else:
            polinomio.append(A+X10)
        polinomio.append(mas)
    if float(B) != 0:
        X9='X^9'
        if float(B) < 0:
            B=float(B)
            B=abs(B)
            B=str(B)
            if polinomio == []:
                polinomio.append(menos)
            elif polinomio != []:
                polinomio.pop()
                polinomio.append(menos)
        if float(B) == 1:
            polinomio.append(X9)
        else:
            polinomio.append(B+X9)
        polinomio.append(mas)
    if float(C) != 0:
        X8='X^8'
        if float(C) < 0:
            C=float(C)
            C=abs(C)
            C=str(C)
            if polinomio == []:
                polinomio.append(menos)
            elif polinomio != []:
                polinomio.pop()
                polinomio.append(menos)
        if float (C) == 1:
            polinomio.append(X8)
        else:
            polinomio.append(C+X8)
        polinomio.append(mas)
    if float(D) != 0:
        X7='X^7'
        if float(D) < 0:
            D=float(D)
            D=abs(D)
            D=str(D)
            if polinomio == []:
                polinomio.append(menos)
            elif polinomio != []:
                polinomio.pop()
                polinomio.append(menos)
        if float(D) == 1:
            polinomio.append(X7)
        else:
            polinomio.append(D+X7)
        polinomio.append(mas)
    if float(E) != 0:
        X6='X^6'
        if float(E) < 0:
            E=float(E)
            E=abs(E)
            E=str(E)
            if polinomio == []:
                polinomio.append(menos)
            elif polinomio != []:
                polinomio.pop()
                polinomio.append(menos)
        if float(E) == 1:
            polinomio.append(X6)
        else:
            polinomio.append(E+X6)
        polinomio.append(mas)
    if float(F) != 0:
        X5='X^5'
        if float(F) < 0:
            F=float(F)
            F=abs(F)
            F=str(F)
            if polinomio == []:
                polinomio.append(menos)
            elif polinomio != []:
                polinomio.pop()
                polinomio.append(menos)
        if float(F) == 1:
            polinomio.append(X5)
        else:    
            polinomio.append(F+X5)
        polinomio.append(mas)
    if float(G) != 0:
        X4='X^4'
        if float(G) < 0:
            G=float(G)
            G=abs(G)
            G=str(G)
            if polinomio == []:
                polinomio.append(menos)
            elif polinomio != []:
                polinomio.pop()
                polinomio.append(menos)
        if float(G) == 1:
            polinomio.append(X4)
        else:
            polinomio.append(G+X4)
        polinomio.append(mas)
    if float(H) != 0:
        X3='X^3'
        if float(H) < 0:
            H=float(H)
            H=abs(H)
            H=str(H)
            if polinomio == []:
                polinomio.append(menos)
            elif polinomio != []:
                polinomio.pop()
                polinomio.append(menos)
        if float(H) == 1:
            polinomio.append(X3)
        else:
            polinomio.append(H+X3)
        polinomio.append(mas)
    if float(I) != 0:
        X2='X^2'
        if float(I) < 0:
            I=float(I)
            I=abs(I)
            I=str(I)
            if polinomio == []:
                polinomio.append(menos)
            elif polinomio != []:
                polinomio.pop()
                polinomio.append(menos)
        if float(I) == 1:
            polinomio.append(X2)
        else:
            polinomio.append(I+X2)
        polinomio.append(mas)
    if float(J) != 0:
        X1='X'
        if float(J) < 0:
            J=float(J)
            J=abs(J)
            J=str(J)
            if polinomio == []:
                polinomio.append(menos)
            elif polinomio != []:
                polinomio.pop()
                polinomio.append(menos)
        if float(J) == 1:
            polinomio.append(X1)
        else:
            polinomio.append(J+X1)
        polinomio.append(mas)
    if float(K) != 0:
        if float(K) < 0:
            K=float(K)
            K=abs(K)
            K=str(K)
            if polinomio == []:
                polinomio.append(menos)
            elif polinomio != []:
                polinomio.pop()
                polinomio.append(menos)
        polinomio.append(K)
        polinomio.append(mas)
    if polinomio != []:
        polinomio.pop()
        print('F(X)=',' '.join(polinomio))
    if polinomio == []:
        print('F(X)=0')
def polinomiointerpolar():
    print('Si grado=1, se necesitan 2 puntos')
    print('Si grado=2, se necesitan 3 puntos')
    print('Si grado=3, se necesitan 4 puntos')
    print('Si grado=4, se necesitan 5 puntos')
    print('Si grado=5, se necesitan 6 puntos')
    print('Si grado=6, se necesitan 7 puntos')
    print('Si grado=7, se necesitan 8 puntos (No disponible aun)')
    print('Si grado=8, se necesitan 9 puntos (No disponible aun)')
    print('Si grado=9, se necesitan 10 puntos (No disponible aun)')
    print('Si grado=10, se necesitan 11 puntos (No disponible aun)')
    print('Ingrese 0 para volver al menu de funcion polinomica')
    metodo=int(input('Ingrese el grado del polinomio que quiere obtener:'))
    while metodo not in {0,1,2,3,4,5,6,7,8,9,10}:
        print('Por favor solo ingresar grados disponibles')
        metodo=int(input('Ingrese el grado del polinomio que quiere obtener:'))
    while metodo in {7,8,9,10}:
        print('Metodo aun no disponible')
        metodo=int(input('Ingrese el grado del polinomio que quiere obtener:'))
    if metodo == 1:
        A=0
        B=0
        C=0
        D=0
        E=0
        F=0
        G=0
        H=0
        I=0
        X1=float(input('Ingrese el valor en X del primer punto:')) 
        X2=float(input('Ingrese el valor en X del segundo punto:'))
        Y1=float(input('Ingrese el valor en Y del primer punto:'))
        Y2=float(input('Ingrese el valor en Y del segundo punto:'))
        if X1!=X2 and Y1!=Y2:
            J=float((Y2-Y1)/(X2-X1))
            K=float(Y1-J*X1)
            impresoradepolinomios(A,B,C,D,E,F,G,H,I,J,K)
        elif X1==X2:
            print('No es una funcion bien definida para el formato F(X)=X')
        elif Y1==Y2:
            J=0
            K=Y1
            impresoradepolinomios(A,B,C,D,E,F,G,H,I,J,K)
    if metodo == 2:
        A=0
        B=0
        C=0
        D=0
        E=0
        F=0
        G=0
        H=0
        X1=float(input('Ingrese el valor en X del primer punto:')) 
        Y1=float(input('Ingrese el valor en Y del primer punto:'))
        X2=float(input('Ingrese el valor en X del segundo punto:'))
        Y2=float(input('Ingrese el valor en Y del segundo punto:'))
        X3=float(input('Ingrese el valor en X del tercer punto:'))
        Y3=float(input('Ingrese el valor en Y del tercer punto:'))
        if X1 != X2 != X3:
            CTE1=(X1-X2)*(X1-X3)
            CTE2=(X2-X1)*(X2-X3)
            CTE3=(X3-X1)*(X3-X2)
            I=Y1/CTE1+Y2/CTE2+Y3/CTE3
            J=-(Y1*(X3+X2))/CTE1-(Y2*(X3+X1))/CTE2-(Y3*(X2+X1))/CTE3
            K=(Y1*X2*X3)/CTE1+(Y2*X1*X3)/CTE2+(Y3*X2*X1)/CTE3
            impresoradepolinomios(A,B,C,D,E,F,G,H,I,J,K)        
        else:
            print('No es una funcion bien definida para el formato F(X)=X')
    if metodo == 3:
        A=0
        B=0
        C=0
        D=0
        E=0
        F=0
        G=0
        X1=float(input('Ingrese el valor en X del primer punto:')) 
        Y1=float(input('Ingrese el valor en Y del primer punto:'))
        X2=float(input('Ingrese el valor en X del segundo punto:'))
        Y2=float(input('Ingrese el valor en Y del segundo punto:'))
        X3=float(input('Ingrese el valor en X del tercer punto:'))
        Y3=float(input('Ingrese el valor en Y del tercer punto:'))
        X4=float(input('Ingrese el valor en X del cuarto punto:'))
        Y4=float(input('Ingrese el valor en Y del cuarto punto:'))
        if X1 != X2 != X3 != X4:
            CTE1=(X1-X2)*(X1-X3)*(X1-X4)
            CTE2=(X2-X1)*(X2-X3)*(X2-X4)
            CTE3=(X3-X1)*(X3-X2)*(X3-X4)
            CTE4=(X4-X1)*(X4-X2)*(X4-X3)
            H=Y1/CTE1+Y2/CTE2+Y3/CTE3+Y4/CTE4
            I=-(Y1*(X2+X3+X4))/CTE1-(Y2*(X1+X3+X4))/CTE2-(Y3*(X1+X2+X4))/CTE3-(Y4*(X1+X2+X3))/CTE4
            J=(Y1*(X2*X3+X2*X4+X3*X4))/CTE1+(Y2*(X1*X3+X1*X4+X3*X4))/CTE2+(Y3*(X1*X2+X1*X4+X2*X4))/CTE3+(Y4*(X1*X2+X1*X3+X2*X3))/CTE4
            K=-(Y1*X2*X3*X4)/CTE1-(Y2*X1*X3*X4)/CTE2-(Y3*X1*X2*X4)/CTE3-(Y4*X1*X2*X3)/CTE4
            impresoradepolinomios(A,B,C,D,E,F,G,H,I,J,K)
        else:
            print('No es una funcion bien definida para el formato F(X)=X')
    if metodo == 4:
        A=0
        B=0
        C=0
        D=0
        E=0
        F=0
        X1=float(input('Ingrese el valor en X del primer punto:')) 
        Y1=float(input('Ingrese el valor en Y del primer punto:'))
        X2=float(input('Ingrese el valor en X del segundo punto:'))
        Y2=float(input('Ingrese el valor en Y del segundo punto:'))
        X3=float(input('Ingrese el valor en X del tercer punto:'))
        Y3=float(input('Ingrese el valor en Y del tercer punto:'))
        X4=float(input('Ingrese el valor en X del cuarto punto:'))
        Y4=float(input('Ingrese el valor en Y del cuarto punto:'))
        X5=float(input('Ingrese el valor en X del quinto punto:'))
        Y5=float(input('Ingrese el valor en Y del quinto punto:'))
        if X1 != X2 != X3 != X4 != X5:
            CTE1=(X1-X2)*(X1-X3)*(X1-X4)*(X1-X5)
            CTE2=(X2-X1)*(X2-X3)*(X2-X4)*(X2-X5)
            CTE3=(X3-X1)*(X3-X2)*(X3-X4)*(X3-X5)
            CTE4=(X4-X1)*(X4-X2)*(X4-X3)*(X4-X5)
            CTE5=(X5-X1)*(X5-X2)*(X5-X3)*(X5-X4)
            K1=Y1/CTE1
            K2=Y2/CTE2
            K3=Y3/CTE3
            K4=Y4/CTE4
            K5=Y5/CTE5
            G=K1+K2+K3+K4+K5
            H=-(K1*(X2+X3+X4+X5))-(K2*(X1+X3+X4+X5))-(K3*(X1+X2+X4+X5))-(K4*(X1+X2+X3+X5))-(K5*(X1+X2+X3+X4))
            I=(K1*(X2*X3+X2*X4+X2*X5+X3*X4+X3*X5+X4*X5))+(K2*(X1*X3+X1*X4+X1*X5+X3*X4+X3*X5+X4*X5))+(K3*(X1*X2+X1*X4+X1*X5+X2*X4+X2*X5+X4*X5))+(K4*(X1*X2+X1*X3+X1*X5+X2*X3+X2*X5+X3*X5))+(K5*(X1*X2+X1*X3+X1*X4+X2*X3+X2*X4+X3*X4))
            J=-(K1*(X2*X3*X4+X3*X4*X5+X4*X5*X2+X5*X2*X3))-(K2*(X1*X3*X4+X3*X4*X5+X4*X5*X1+X5*X1*X3))-(K3*(X1*X2*X4+X2*X4*X5+X4*X5*X1+X5*X1*X2))-(K4*(X1*X2*X3+X2*X3*X5+X3*X5*X1+X5*X1*X2))-(K5*(X1*X2*X3+X2*X3*X4+X3*X4*X1+X4*X1*X2))
            K=(K1*(X2*X3*X4*X5))+(K2*(X1*X3*X4*X5))+(K3*(X1*X2*X4*X5))+(K4*(X1*X2*X3*X5))+(K5*(X1*X2*X3*X4))
            impresoradepolinomios(A,B,C,D,E,F,G,H,I,J,K)
        else:
            print('No es una funcion bien definida para el formato F(X)=X')
    if metodo == 5:
        A=0
        B=0
        C=0
        D=0
        E=0
        X1=float(input('Ingrese el valor en X del primer punto:')) 
        Y1=float(input('Ingrese el valor en Y del primer punto:'))
        X2=float(input('Ingrese el valor en X del segundo punto:'))
        Y2=float(input('Ingrese el valor en Y del segundo punto:'))
        X3=float(input('Ingrese el valor en X del tercer punto:'))
        Y3=float(input('Ingrese el valor en Y del tercer punto:'))
        X4=float(input('Ingrese el valor en X del cuarto punto:'))
        Y4=float(input('Ingrese el valor en Y del cuarto punto:'))
        X5=float(input('Ingrese el valor en X del quinto punto:'))
        Y5=float(input('Ingrese el valor en Y del quinto punto:'))
        X6=float(input('Ingrese el valor en X del sexto punto:'))
        Y6=float(input('Ingrese el valor en Y del sexto punto:'))
        if X1 != X2 != X3 != X4 != X5 != X6:
            CTE1=(X1-X2)*(X1-X3)*(X1-X4)*(X1-X5)*(X1-X6)
            CTE2=(X2-X1)*(X2-X3)*(X2-X4)*(X2-X5)*(X2-X6)
            CTE3=(X3-X1)*(X3-X2)*(X3-X4)*(X3-X5)*(X3-X6)
            CTE4=(X4-X1)*(X4-X2)*(X4-X3)*(X4-X5)*(X4-X6)
            CTE5=(X5-X1)*(X5-X2)*(X5-X3)*(X5-X4)*(X5-X6)
            CTE6=(X6-X1)*(X6-X2)*(X6-X3)*(X6-X4)*(X6-X5)
            K1=Y1/CTE1
            K2=Y2/CTE2
            K3=Y3/CTE3
            K4=Y4/CTE4
            K5=Y5/CTE5
            K6=Y6/CTE6
            F=K1+K2+K3+K4+K5+K6
            G=-(K1*(X2+X3+X4+X5+X6))-(K2*(X1+X3+X4+X5+X6))-(K3*(X1+X2+X4+X5+X6))-(K4*(X1+X2+X3+X5+X6))-(K5*(X1+X2+X3+X4+X6))-(K6*(X1+X2+X3+X4+X5))
            H1=(K1*(X2*X3+X2*X4+X2*X5+X2*X6+X3*X4+X3*X5+X3*X6+X4*X5+X4*X6+X5*X6))
            H2=(K2*(X1*X3+X1*X4+X1*X5+X1*X6+X3*X4+X3*X5+X3*X6+X4*X5+X4*X6+X5*X6))
            H3=(K3*(X1*X2+X1*X4+X1*X5+X1*X6+X2*X4+X2*X5+X2*X6+X4*X5+X4*X6+X5*X6))
            H4=(K4*(X1*X2+X1*X3+X1*X5+X1*X6+X2*X3+X2*X5+X2*X6+X3*X5+X3*X6+X5*X6))
            H5=(K5*(X1*X2+X1*X3+X1*X4+X1*X6+X2*X3+X2*X4+X2*X6+X3*X4+X3*X6+X4*X6))
            H6=(K6*(X1*X2+X1*X3+X1*X4+X1*X5+X2*X3+X2*X4+X2*X5+X3*X4+X3*X5+X4*X5))
            H=H1+H2+H3+H4+H5+H6
            I1=-(K1*(X2*X3*X4+X2*X3*X5+X2*X3*X6+X2*X4*X5+X2*X4*X6+X2*X5*X6+X3*X4*X5+X3*X4*X6+X3*X5*X6+X4*X5*X6))
            I2=-(K2*(X1*X3*X4+X1*X3*X5+X1*X3*X6+X1*X4*X5+X1*X4*X6+X1*X5*X6+X3*X4*X5+X3*X4*X6+X3*X5*X6+X4*X5*X6))
            I3=-(K3*(X1*X2*X4+X1*X2*X5+X1*X2*X6+X1*X4*X5+X1*X4*X6+X1*X5*X6+X2*X4*X5+X2*X4*X6+X2*X5*X6+X4*X5*X6))
            I4=-(K4*(X1*X2*X3+X1*X2*X5+X1*X2*X6+X1*X3*X5+X1*X3*X6+X1*X5*X6+X2*X3*X5+X2*X3*X6+X2*X5*X6+X3*X5*X6))
            I5=-(K5*(X1*X2*X3+X1*X2*X4+X1*X2*X6+X1*X3*X4+X1*X3*X6+X1*X4*X6+X2*X3*X4+X2*X3*X6+X2*X4*X6+X3*X4*X6))
            I6=-(K6*(X1*X2*X3+X1*X2*X4+X1*X2*X5+X1*X3*X4+X1*X3*X5+X1*X4*X5+X2*X3*X4+X2*X3*X5+X2*X4*X5+X3*X4*X5))
            I=I1+I2+I3+I4+I5+I6
            J1=(K1*(X2*X3*X4*X5+X2*X3*X4*X6+X2*X3*X5*X6+X2*X4*X5*X6+X3*X4*X5*X6))
            J2=(K2*(X1*X3*X4*X5+X1*X3*X4*X6+X1*X3*X5*X6+X1*X4*X5*X6+X3*X4*X5*X6))
            J3=(K3*(X1*X2*X4*X5+X1*X2*X4*X6+X1*X2*X5*X6+X1*X4*X5*X6+X2*X4*X5*X6))
            J4=(K4*(X1*X2*X3*X5+X1*X2*X3*X6+X1*X2*X5*X6+X1*X3*X5*X6+X2*X3*X5*X6))
            J5=(K5*(X1*X2*X3*X4+X1*X2*X3*X6+X1*X2*X4*X6+X1*X3*X4*X6+X2*X3*X4*X6))
            J6=(K6*(X1*X2*X3*X4+X1*X2*X3*X5+X1*X2*X4*X5+X1*X3*X4*X5+X2*X3*X4*X5))
            J=J1+J2+J3+J4+J5+J6
            K=-(K1*(X2*X3*X4*X5*X6))-(K2*(X1*X3*X4*X5*X6))-(K3*(X1*X2*X4*X5*X6))-(K4*(X1*X2*X3*X5*X6))-(K5*(X1*X2*X3*X4*X6))-(K6*(X1*X2*X3*X4*X5))
            impresoradepolinomios(A,B,C,D,E,F,G,H,I,J,K)
        else:
            print('No es una funcion bien definida para el formato F(X)=X')
    if metodo == 6:
        A=0
        B=0
        C=0
        D=0
        X1=float(input('Ingrese el valor en X del primer punto:')) 
        Y1=float(input('Ingrese el valor en Y del primer punto:'))
        X2=float(input('Ingrese el valor en X del segundo punto:'))
        Y2=float(input('Ingrese el valor en Y del segundo punto:'))
        X3=float(input('Ingrese el valor en X del tercer punto:'))
        Y3=float(input('Ingrese el valor en Y del tercer punto:'))
        X4=float(input('Ingrese el valor en X del cuarto punto:'))
        Y4=float(input('Ingrese el valor en Y del cuarto punto:'))
        X5=float(input('Ingrese el valor en X del quinto punto:'))
        Y5=float(input('Ingrese el valor en Y del quinto punto:'))
        X6=float(input('Ingrese el valor en X del sexto punto:'))
        Y6=float(input('Ingrese el valor en Y del sexto punto:'))
        X7=float(input('Ingrese el valor en X del septimo punto:'))
        Y7=float(input('Ingrese el valor en Y del septimo punto:'))
        if X1 != X2 != X3 != X4 != X5 != X6 != X7:
            CTE1=(X1-X2)*(X1-X3)*(X1-X4)*(X1-X5)*(X1-X6)*(X1-X7)
            CTE2=(X2-X1)*(X2-X3)*(X2-X4)*(X2-X5)*(X2-X6)*(X2-X7)
            CTE3=(X3-X1)*(X3-X2)*(X3-X4)*(X3-X5)*(X3-X6)*(X3-X7)
            CTE4=(X4-X1)*(X4-X2)*(X4-X3)*(X4-X5)*(X4-X6)*(X4-X7)
            CTE5=(X5-X1)*(X5-X2)*(X5-X3)*(X5-X4)*(X5-X6)*(X5-X7)
            CTE6=(X6-X1)*(X6-X2)*(X6-X3)*(X6-X4)*(X6-X5)*(X6-X7)
            CTE7=(X7-X1)*(X7-X2)*(X7-X3)*(X7-X4)*(X7-X5)*(X7-X6)
            K1=Y1/CTE1
            K2=Y2/CTE2
            K3=Y3/CTE3
            K4=Y4/CTE4
            K5=Y5/CTE5
            K6=Y6/CTE6
            K7=Y7/CTE7
            E=K1+K2+K3+K4+K5+K6+K7
            F=-(K1*(X2+X3+X4+X5+X6+X7))-(K2*(X1+X3+X4+X5+X6+X7))-(K3*(X1+X2+X4+X5+X6+X7))-(K4*(X1+X2+X3+X5+X6+X7))-(K5*(X1+X2+X3+X4+X6+X7))-(K6*(X1+X2+X3+X4+X5+X7))-(K7*(X1+X2+X3+X4+X5+X6))
            G1=(K1*(X2*X3+X2*X4+X2*X5+X2*X6+X2*X7+X3*X4+X3*X5+X3*X6+X3*X7+X4*X5+X4*X6+X4*X7+X5*X6+X5*X7+X6*X7))
            G2=(K2*(X1*X3+X1*X4+X1*X5+X1*X6+X1*X7+X3*X4+X3*X5+X3*X6+X3*X7+X4*X5+X4*X6+X4*X7+X5*X6+X5*X7+X6*X7))
            G3=(K3*(X1*X2+X1*X4+X1*X5+X1*X6+X1*X7+X2*X4+X2*X5+X2*X6+X2*X7+X4*X5+X4*X6+X4*X7+X5*X6+X5*X7+X6*X7))
            G4=(K4*(X1*X2+X1*X3+X1*X5+X1*X6+X1*X7+X2*X3+X2*X5+X2*X6+X2*X7+X3*X5+X3*X6+X3*X7+X5*X6+X5*X7+X6*X7))
            G5=(K5*(X1*X2+X1*X3+X1*X4+X1*X6+X1*X7+X2*X3+X2*X4+X2*X6+X2*X7+X3*X4+X3*X6+X3*X7+X4*X6+X4*X7+X6*X7))
            G6=(K6*(X1*X2+X1*X3+X1*X4+X1*X5+X1*X7+X2*X3+X2*X4+X2*X5+X2*X7+X3*X4+X3*X5+X3*X7+X4*X5+X4*X7+X5*X7))
            G7=(K7*(X1*X2+X1*X3+X1*X4+X1*X5+X1*X6+X2*X3+X2*X4+X2*X5+X2*X6+X3*X4+X3*X5+X3*X6+X4*X5+X4*X6+X5*X6))
            G=G1+G2+G3+G4+G5+G6+G7
            H1=-(K1*(X2*X3*X4+X2*X3*X5+X2*X3*X6+X2*X3*X7+X2*X4*X5+X2*X4*X6+X2*X4*X7+X2*X5*X6+X2*X5*X7+X2*X6*X7+X3*X4*X5+X3*X4*X6+X3*X4*X7+X3*X5*X6+X3*X5*X7+X3*X6*X7+X4*X5*X6+X4*X5*X7+X4*X6*X7+X5*X6*X7))
            H2=-(K2*(X1*X3*X4+X1*X3*X5+X1*X3*X6+X1*X3*X7+X1*X4*X5+X1*X4*X6+X1*X4*X7+X1*X5*X6+X1*X5*X7+X1*X6*X7+X3*X4*X5+X3*X4*X6+X3*X4*X7+X3*X5*X6+X3*X5*X7+X3*X6*X7+X4*X5*X6+X4*X5*X7+X4*X6*X7+X5*X6*X7))
            H3=-(K3*(X1*X2*X4+X1*X2*X5+X1*X2*X6+X1*X2*X7+X1*X4*X5+X1*X4*X6+X1*X4*X7+X1*X5*X6+X1*X5*X7+X1*X6*X7+X2*X4*X5+X2*X4*X6+X2*X4*X7+X2*X5*X6+X2*X5*X7+X2*X6*X7+X4*X5*X6+X4*X5*X7+X4*X6*X7+X5*X6*X7))
            H4=-(K4*(X1*X2*X3+X1*X2*X5+X1*X2*X6+X1*X2*X7+X1*X3*X5+X1*X3*X6+X1*X3*X7+X1*X5*X6+X1*X5*X7+X1*X6*X7+X2*X3*X5+X2*X3*X6+X2*X3*X7+X2*X5*X6+X2*X5*X7+X2*X6*X7+X3*X5*X6+X3*X5*X7+X3*X6*X7+X5*X6*X7))
            H5=-(K5*(X1*X2*X3+X1*X2*X4+X1*X2*X6+X1*X2*X7+X1*X3*X4+X1*X3*X6+X1*X3*X7+X1*X4*X6+X1*X4*X7+X1*X6*X7+X2*X3*X4+X2*X3*X6+X2*X3*X7+X2*X4*X6+X2*X4*X7+X2*X6*X7+X3*X4*X6+X3*X4*X7+X3*X6*X7+X4*X6*X7))
            H6=-(K6*(X1*X2*X3+X1*X2*X4+X1*X2*X5+X1*X2*X7+X1*X3*X4+X1*X3*X5+X1*X3*X7+X1*X4*X5+X1*X4*X7+X1*X5*X7+X2*X3*X4+X2*X3*X5+X2*X3*X7+X2*X4*X5+X2*X4*X7+X2*X5*X7+X3*X4*X5+X3*X4*X7+X3*X5*X7+X4*X5*X7))
            H7=-(K7*(X1*X2*X3+X1*X2*X4+X1*X2*X5+X1*X2*X6+X1*X3*X4+X1*X3*X5+X1*X3*X6+X1*X4*X5+X1*X4*X6+X1*X5*X6+X2*X3*X4+X2*X3*X5+X2*X3*X6+X2*X4*X5+X2*X4*X6+X2*X5*X6+X3*X4*X5+X3*X4*X6+X3*X5*X6+X4*X5*X6))
            H=H1+H2+H3+H4+H5+H6+H7
            I1=(K1*(X2*X3*X4*X5+X2*X3*X4*X6+X2*X3*X4*X7+X2*X3*X5*X6+X2*X3*X5*X7+X2*X3*X6*X7+X2*X4*X5*X6+X2*X4*X5*X7+X2*X4*X6*X7+X2*X5*X6*X7+X3*X4*X5*X6+X3*X4*X5*X7+X3*X4*X6*X7+X3*X5*X6*X7+X4*X5*X6*X7))
            I2=(K2*(X1*X3*X4*X5+X1*X3*X4*X6+X1*X3*X4*X7+X1*X3*X5*X6+X1*X3*X5*X7+X1*X3*X6*X7+X1*X4*X5*X6+X1*X4*X5*X7+X1*X4*X6*X7+X1*X5*X6*X7+X3*X4*X5*X6+X3*X4*X5*X7+X3*X4*X6*X7+X3*X5*X6*X7+X4*X5*X6*X7))
            I3=(K3*(X1*X2*X4*X5+X1*X2*X4*X6+X1*X2*X4*X7+X1*X2*X5*X6+X1*X2*X5*X7+X1*X2*X6*X7+X1*X4*X5*X6+X1*X4*X5*X7+X1*X4*X6*X7+X1*X5*X6*X7+X2*X4*X5*X6+X2*X4*X5*X7+X2*X4*X6*X7+X2*X5*X6*X7+X4*X5*X6*X7))
            I4=(K4*(X1*X2*X3*X5+X1*X2*X3*X6+X1*X2*X3*X7+X1*X2*X5*X6+X1*X2*X5*X7+X1*X2*X6*X7+X1*X3*X5*X6+X1*X3*X5*X7+X1*X3*X6*X7+X1*X5*X6*X7+X2*X3*X5*X6+X2*X3*X5*X7+X2*X3*X6*X7+X2*X5*X6*X7+X3*X5*X6*X7))
            I5=(K5*(X1*X2*X3*X4+X1*X2*X3*X6+X1*X2*X3*X7+X1*X2*X4*X6+X1*X2*X4*X7+X1*X2*X6*X7+X1*X3*X4*X6+X1*X3*X4*X7+X1*X3*X6*X7+X1*X4*X6*X7+X2*X3*X4*X6+X2*X3*X4*X7+X2*X3*X6*X7+X2*X4*X6*X7+X3*X4*X6*X7))
            I6=(K6*(X1*X2*X3*X4+X1*X2*X3*X5+X1*X2*X3*X7+X1*X2*X4*X5+X1*X2*X4*X7+X1*X2*X5*X7+X1*X3*X4*X5+X1*X3*X4*X7+X1*X3*X5*X7+X1*X4*X5*X7+X2*X3*X4*X5+X2*X3*X4*X7+X2*X3*X5*X7+X2*X4*X5*X7+X3*X4*X5*X7))
            I7=(K7*(X1*X2*X3*X4+X1*X2*X3*X5+X1*X2*X3*X6+X1*X2*X4*X5+X1*X2*X4*X6+X1*X2*X5*X6+X1*X3*X4*X5+X1*X3*X4*X6+X1*X3*X5*X6+X1*X4*X5*X6+X2*X3*X4*X5+X2*X3*X4*X6+X2*X3*X5*X6+X2*X4*X5*X6+X3*X4*X5*X6))
            I=I1+I2+I3+I4+I5+I6+I7
            J1=-(K1*(X2*X3*X4*X5*X6+X2*X3*X4*X5*X7+X2*X3*X4*X6*X7+X2*X3*X5*X6*X7+X2*X4*X5*X6*X7+X3*X4*X5*X6*X7))
            J2=-(K2*(X1*X3*X4*X5*X6+X1*X3*X4*X5*X7+X1*X3*X4*X6*X7+X1*X3*X5*X6*X7+X1*X4*X5*X6*X7+X3*X4*X5*X6*X7))
            J3=-(K3*(X1*X2*X4*X5*X6+X1*X2*X4*X5*X7+X1*X2*X4*X6*X7+X1*X2*X5*X6*X7+X1*X4*X5*X6*X7+X2*X4*X5*X6*X7))
            J4=-(K4*(X1*X2*X3*X5*X6+X1*X2*X3*X5*X7+X1*X2*X3*X6*X7+X1*X2*X5*X6*X7+X1*X3*X5*X6*X7+X2*X3*X5*X6*X7))
            J5=-(K5*(X1*X2*X3*X4*X6+X1*X2*X3*X4*X7+X1*X2*X3*X6*X7+X1*X2*X4*X6*X7+X1*X3*X4*X6*X7+X2*X3*X4*X6*X7))
            J6=-(K6*(X1*X2*X3*X4*X5+X1*X2*X3*X4*X7+X1*X2*X3*X5*X7+X1*X2*X4*X5*X7+X1*X3*X4*X5*X7+X2*X3*X4*X5*X7))
            J7=-(K7*(X1*X2*X3*X4*X5+X1*X2*X3*X4*X6+X1*X2*X3*X5*X6+X1*X2*X4*X5*X6+X1*X3*X4*X5*X6+X2*X3*X4*X5*X6))
            J=J1+J2+J3+J4+J5+J6+J7
            K=(K1*(X2*X3*X4*X5*X6*X7))+(K2*(X1*X3*X4*X5*X6*X7))+(K3*(X1*X2*X4*X5*X6*X7))+(K4*(X1*X2*X3*X5*X6*X7))+(K5*(X1*X2*X3*X4*X6*X7))+(K6*(X1*X2*X3*X4*X5*X7))+(K7*(X1*X2*X3*X4*X5*X6))
            impresoradepolinomios(A,B,C,D,E,F,G,H,I,J,K)
        else:
            print('No es una funcion bien definida para el formato F(X)=X')
def polinomiocoeficiente():
    print('Si grado=1, 2 coeficientes')
    print('Si grado=2, 3 coeficientes')
    print('Si grado=3, 4 coeficientes')
    print('Si grado=4, 5 coeficientes')
    print('Si grado=5, 6 coeficientes')
    print('Si grado=6, 7 coeficientes')
    print('Si grado=7, 8 coeficientes')
    print('Si grado=8, 9 coeficientes')
    print('Si grado=9, 10 coeficientes')
    print('Si grado=10, 11 coeficientes')
    metodo=int(input('Ingrese el grado del polinomio que quiere obtener:'))
    while metodo not in {0,1,2,3,4,5,6,7,8,9,10}:
        print('Por favor solo ingresar grados disponibles')
        metodo=int(input('Ingrese el grado del polinomio que quiere obtener:'))
    if metodo == 1:
        J=float(input('Ingrese el valor del coeficiente de X:'))
        K=float(input('Ingrese el valor del termino independiente:'))
        impresoradepolinomios(0,0,0,0,0,0,0,0,0,J,K)
    if metodo == 2:
        I=float(input('Ingrese el valor del coeficiente de X^2:'))
        J=float(input('Ingrese el valor del coeficiente de X:'))
        K=float(input('Ingrese el valor del termino independiente:'))
        impresoradepolinomios(0,0,0,0,0,0,0,0,I,J,K)
    if metodo == 3:
        H=float(input('Ingrese el valor del coeficiente de X^3:'))
        I=float(input('Ingrese el valor del coeficiente de X^2:'))
        J=float(input('Ingrese el valor del coeficiente de X:'))
        K=float(input('Ingrese el valor del termino independiente:'))
        impresoradepolinomios(0,0,0,0,0,0,0,H,I,J,K)
    if metodo == 4:
        G=float(input('Ingrese el valor del coeficiente de X^4:'))
        H=float(input('Ingrese el valor del coeficiente de X^3:'))
        I=float(input('Ingrese el valor del coeficiente de X^2:'))
        J=float(input('Ingrese el valor del coeficiente de X:'))
        K=float(input('Ingrese el valor del termino independiente:'))
        impresoradepolinomios(0,0,0,0,0,0,G,H,I,J,K)
    if metodo == 5:
        F=float(input('Ingrese el valor del coeficiente de X^5:'))
        G=float(input('Ingrese el valor del coeficiente de X^4:'))
        H=float(input('Ingrese el valor del coeficiente de X^3:'))
        I=float(input('Ingrese el valor del coeficiente de X^2:'))
        J=float(input('Ingrese el valor del coeficiente de X:'))
        K=float(input('Ingrese el valor del termino independiente:'))
        impresoradepolinomios(0,0,0,0,0,F,G,H,I,J,K)
    if metodo == 6:
        E=float(input('Ingrese el valor del coeficiente de X^6:'))
        F=float(input('Ingrese el valor del coeficiente de X^5:'))
        G=float(input('Ingrese el valor del coeficiente de X^4:'))
        H=float(input('Ingrese el valor del coeficiente de X^3:'))
        I=float(input('Ingrese el valor del coeficiente de X^2:'))
        J=float(input('Ingrese el valor del coeficiente de X:'))
        K=float(input('Ingrese el valor del termino independiente:'))
        impresoradepolinomios(0,0,0,0,E,F,G,H,I,J,K)
    if metodo == 7:
        D=float(input('Ingrese el valor del coeficiente de X^7:'))
        E=float(input('Ingrese el valor del coeficiente de X^6:'))
        F=float(input('Ingrese el valor del coeficiente de X^5:'))
        G=float(input('Ingrese el valor del coeficiente de X^4:'))
        H=float(input('Ingrese el valor del coeficiente de X^3:'))
        I=float(input('Ingrese el valor del coeficiente de X^2:'))
        J=float(input('Ingrese el valor del coeficiente de X:'))
        K=float(input('Ingrese el valor del termino independiente:'))
        impresoradepolinomios(0,0,0,D,E,F,G,H,I,J,K)
    if metodo == 8:
        C=float(input('Ingrese el valor del coeficiente de X^8:'))
        D=float(input('Ingrese el valor del coeficiente de X^7:'))
        E=float(input('Ingrese el valor del coeficiente de X^6:'))
        F=float(input('Ingrese el valor del coeficiente de X^5:'))
        G=float(input('Ingrese el valor del coeficiente de X^4:'))
        H=float(input('Ingrese el valor del coeficiente de X^3:'))
        I=float(input('Ingrese el valor del coeficiente de X^2:'))
        J=float(input('Ingrese el valor del coeficiente de X:'))
        K=float(input('Ingrese el valor del termino independiente:'))
        impresoradepolinomios(0,0,C,D,E,F,G,H,I,J,K)
    if metodo == 9:
        B=float(input('Ingrese el valor del coeficiente de X^9:'))
        C=float(input('Ingrese el valor del coeficiente de X^8:'))
        D=float(input('Ingrese el valor del coeficiente de X^7:'))
        E=float(input('Ingrese el valor del coeficiente de X^6:'))
        F=float(input('Ingrese el valor del coeficiente de X^5:'))
        G=float(input('Ingrese el valor del coeficiente de X^4:'))
        H=float(input('Ingrese el valor del coeficiente de X^3:'))
        I=float(input('Ingrese el valor del coeficiente de X^2:'))
        J=float(input('Ingrese el valor del coeficiente de X:'))
        K=float(input('Ingrese el valor del termino independiente:'))
        impresoradepolinomios(0,B,C,D,E,F,G,H,I,J,K) 
    if metodo == 10:
        A=float(input('Ingrese el valor del coeficiente de X^10:'))
        B=float(input('Ingrese el valor del coeficiente de X^9:'))
        C=float(input('Ingrese el valor del coeficiente de X^8:'))
        D=float(input('Ingrese el valor del coeficiente de X^7:'))
        E=float(input('Ingrese el valor del coeficiente de X^6:'))
        F=float(input('Ingrese el valor del coeficiente de X^5:'))
        G=float(input('Ingrese el valor del coeficiente de X^4:'))
        H=float(input('Ingrese el valor del coeficiente de X^3:'))
        I=float(input('Ingrese el valor del coeficiente de X^2:'))
        J=float(input('Ingrese el valor del coeficiente de X:'))
        K=float(input('Ingrese el valor del termino independiente:'))
        impresoradepolinomios(A,B,C,D,E,F,G,H,I,J,K)
def evaluadorapolinomios(A,B,C,D,E,F,G,H,I,J,K):
    continuar=1
    while continuar !=0:
        if continuar == 1:
            X=float(input('Ingrese el numero en el que desea evaluar la funcion:'))
            Y=A*(X)**10+B*(X)**9+C*(X)**8+D*(X)**7+E*(X)**6+F*(X)**5+G*(X)**4+H*(X)**3+I*(X)**2+J*(X)**1+K
            print('El resultado de evaluar en ese valor es:',Y)
        else:
            print('Por favor ingresar solo los comandos disponibles')
        continuar=float(input('Ingrese 0 para volver al menu de funcion o ingrese 1 para volver a evaluar en la misma funcion:'))
    return 0    
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