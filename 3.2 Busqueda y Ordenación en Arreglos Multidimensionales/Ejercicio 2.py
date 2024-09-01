# Función para ordenar una fila usando Bubble Sort
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Función principal
def main():
    # Matriz de 3x3
    matriz = [
        [6, 1, 8],
        [0, 1, 2],
        [10, 4, 8]
    ]

    print("Matriz Original:")
    imprimir_matriz(matriz)

    # Indicar qué fila se va a ordenar (por ejemplo, la fila 1)
    fila_a_ordenar = 1

    # Ordenar la fila específica
    bubble_sort(matriz[fila_a_ordenar])

    print("\nMatriz con la fila ordenada:")
    imprimir_matriz(matriz)

# Ejecutar la función principal
if __name__ == "__main__":
    main()

