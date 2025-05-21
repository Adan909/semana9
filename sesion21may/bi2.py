filas = int(input("Dame el numero de filas: "))
columnas = int(input("Dame el numero de columnas: "))

matriz = []
matriz2 = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = int(input(f"Dame el valor de la posicion [{i}][{j}]: "))
        matriz[i].append(int(input(f"Dame el valor de la posicion [{i}][{j}]: ")))
        matriz[i].append(valor)
        print(matriz)
        print(f"El valor de la posicion [{i}][{j}] es: {matriz[i][j]}")
        
   
            
            
            