# Crear un diccionario con información ficticia
persona = {
    "nombre": "Damian villamar",
    "edad": 24,
    "ciudad": "Manabi",
    "profesion": "Ingeniero"
}
print(persona)  # Imprime el diccionario completo
print(persona["nombre"])   # Imprime el nombre
print(persona["edad"])     # Imprime la edad
print(persona["ciudad"])   # Imprime la ciudad (corrige "cuidad" a "ciudad")
print(persona["profesion"]) # Imprime la profesión


# Acceder y modificar el valor de "ciudad"
persona["ciudad"] = "Quito"

# Agregar una nueva clave-valor para "telefono" si no existe
persona.setdefault("telefono", "0956527182")

# Eliminar la clave "edad"
persona.pop("edad", None)  # Usa pop con un valor por defecto para evitar errores

# Imprimir el diccionario final
print(persona)

