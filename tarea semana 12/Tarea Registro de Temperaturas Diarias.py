# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [  # Ciudad 1 Quito
        [  # Semana 1
            {"day": "Lunes", "temp": 87},
            {"day": "Martes", "temp": 40},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 68},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 90}
        ],
        [  # Semana 2 Guayaquil
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 61},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 46}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 74},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 93},
            {"day": "Domingo", "temp": 95}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 76},
            {"day": "Viernes", "temp": 64},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 91}
        ]
    ],
    [  # Ciudad 2 Manabi
        [  # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 79}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 62},
            {"day": "Miércoles", "temp": 54},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 82}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 80},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 91},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 80}
        ]
    ]
]


# Calcular el promedio de temperaturas para cada ciudad y semana
def calcular_promedio_temperaturas(temperaturas):
    promedios = []
    for ciudad_index, ciudad in enumerate(temperaturas):
        print(f"\nPromedios de temperaturas para Ciudad {ciudad_index + 1}:")
        ciudad_promedios = []
        for semana_index, semana in enumerate(ciudad):
            suma = 0
            for dia in semana:
                suma += dia['temp']
            promedio = suma / len(semana)
            ciudad_promedios.append(promedio)
            print(f"Semana {semana_index + 1}: {promedio:.2f}°C")
        promedios.append(ciudad_promedios)
    return promedios


# Función para seleccionar ciudad y mostrar datos
def seleccionar_ciudad(temperaturas):
    while True:
        print("\nSeleccione una ciudad:")
        print("1. Ciudad 1 Quito")
        print("2. Ciudad 2 Guayaquil")
        print("3. Ciudad 3 Manabi")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            ciudad_index = 0
        elif opcion == "2":
            ciudad_index = 1
        elif opcion == "3":
            ciudad_index = 2
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
            continue

        print(f"\nDatos para Ciudad {ciudad_index + 1}:")
        for semana_index, semana in enumerate(temperaturas[ciudad_index]):
            print(f"\nSemana {semana_index + 1}:")
            for dia in semana:
                print(f"{dia['day']}: {dia['temp']}°C")


# Ejecutar funciones
calcular_promedio_temperaturas(temperaturas)
seleccionar_ciudad(temperaturas)
