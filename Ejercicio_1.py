matrizA = []
matrizB = []
matrizR = []

filasA = int(input("Ingresa el número de filas de la mariz A: ")) #Valor de N
columnasA = int(input("Ingresa el número de columnas de la mariz A: ")) #Valor de M
filasB = int(input("Ingresa el número de filas de la mariz B: ")) #Valor de N
columnasB = int(input("Ingresa el número de columnas de la mariz B: ")) #Valor de P

if columnasA != filasB:
    print ('Esta multiplicaión de matrices no tiene solución')
else:
    print ("_______Matriz A _______")
    for i in range(filasA):    
        matrizA.append([0]*columnasA)
    for f in range(filasA):
        for c in range(columnasA):
            matrizA[f][c] = int(input("Elemento en la posición (%d,%d): "%(f,c)))

    print ("_______Matriz B _______")
    for i in range(filasB):    
        matrizB.append([0]*columnasB)
    for f in range(filasB):
        for c in range(columnasB):
            matrizB[f][c] = int(input("Elemento en la posición (%d,%d): "%(f,c)))        
    
    print("__Matrices__")
    print ('Matriz A\n')
    print(matrizA)
    print('MatrizB\n')
    print(matrizB)

    print("-----Multiplicar Matrices-----")

    for k in range(filasA):
        matrizR.append([0]*columnasB)
        for i in range(columnasB):
            matrizR[k][i] = 0

    for i in range(filasA):
        for j in range(columnasA):
            for k in range(columnasB):
                matrizR[i][k] = matrizR[i][k] + (matrizA[i][j] * matrizB[j][k])
    print(matrizR)                 