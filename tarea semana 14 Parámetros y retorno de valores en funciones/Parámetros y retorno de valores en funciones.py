#Crea una función llamada calcular_descuento que tome dos parámetros: el monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).
def calcular_descuento(monto_total, porcentaje=10):
    # Calcula el monto del descuento
    descuento = monto_total * porcentaje / 100
    return round(descuento, 2)

# Ejemplo 1
monto_total = 4000
descuento = calcular_descuento(monto_total)
print(f"Monto total de $ {monto_total}: {descuento:.2f}")

# Ejemplo 2
monto_total2 = 8000
descuento = 30
descuento2 = calcular_descuento(monto_total2, descuento)
print(f"Monto total de $ {monto_total2}: {descuento2:.2f}")

# Solicitar monto total al usuario
monto_total = float(input("Ingrese el monto total de la compra: "))
descuento = calcular_descuento(monto_total)
print(f"Descuento para un monto total de $ {monto_total}: {descuento:.2f}")