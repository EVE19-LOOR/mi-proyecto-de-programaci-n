# Matriz de 3 x 3
matriz = [
    [6, 1, 8],
    [0, 1, 2],
    [10, 4, 8]
]

print("Matriz:")
for fila in matriz:
    print(fila)

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return i, j


# Buscar un valor específico
valor_buscado = 2
resultado = buscar_valor(matriz, valor_buscado)

if valor_buscado == valor_buscado:
    print(f"El valor {valor_buscado} se encuentra en la posición: {resultado}")
else:
    print("Valor incorrecto")

