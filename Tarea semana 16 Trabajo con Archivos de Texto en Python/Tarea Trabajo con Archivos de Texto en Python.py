# Nombre del archivo
file_name = "my_notes.txt"

# Escritura de Archivo de Texto
# Crear un nuevo archivo y escribir notas personales en él
with open(file_name, 'w') as file:  # Abrir el archivo en modo escritura
    # Escribir notas en el archivo
    file.write("Nota 1: Estudiar para el examen.\n")  # Primera nota
    file.write("Nota 2: Aprender programación.\n")       # Segunda nota
    file.write("Nota 3: Hacer ejercicio.\n")         # Tercera nota

# Lectura de Archivo de Texto
# Abrir el archivo para leer su contenido
with open(file_name, 'r') as file:  # Abrir el archivo en modo lectura
    # Leer línea por línea utilizando readline()
    line = file.readline()  # Leer la primera línea
    while line:  # Continuar hasta que no haya más líneas
        print(line.strip())  # Mostrar la línea leída, eliminando espacios en blanco
        line = file.readline()  # Leer la siguiente línea

# Cierre de Archivos
# El archivo se cierra automáticamente al salir del bloque with
