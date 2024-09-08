# Crear la matriz 3D de temperaturas
ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

temperaturas = [[[0 for dia in range(len(dias_semana))] for semana in range(semanas)] for ciudad in range(len(ciudades))]

# Llenar la matriz con datos de ejemplo
for ciudad in range(len(ciudades)):
    for semana in range(semanas):
        for dia in range(len(dias_semana)):
            temperaturas[ciudad][semana][dia] = 30 + ciudad + semana + dia

# Calcular el promedio de temperaturas por ciudad y semana
for ciudad in range(len(ciudades)):
    print(f"Promedios de temperaturas para {ciudades[ciudad]}:")
    for semana in range(semanas):
        total = 0
        for dia in range(len(dias_semana)):
            total += temperaturas[ciudad][semana][dia]
        promedio = total / len(dias_semana)
        print(f"Semana {semana+1}: {promedio:.2f}°C")
