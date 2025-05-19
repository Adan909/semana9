estudiantes = ['Jorge Picado', 'Franklin Callejas', 'Jose Espinoza', 'Joshua Saenz', ]
tamaño = len(estudiantes)
print(f"Cantidad de estudiantes {tamaño}")

#recorrer los elementos del arreglo

for estudiante in estudiantes:
    print(f"{estudiante} tiene {len(estudiante)} letras")
    vocales = "aeiou"
    sumavoc = 0
    for letra in estudiante:
        if letra in vocales:
            sumavoc += 1
        print(f"{letra.upper()}" * 2)
    print(f"{estudiante} tiene {sumavoc} vocales")    
        