#arreglo bidimensional

matriz = [[1, 2], [1, 2]]

for fila in matriz:
    for columna in fila:
        print(columna, end =" ")
        
suma = 0
for fila in matriz:
    for columna in fila:
        suma += columna
print(f"\nSuma total: {suma}")
    