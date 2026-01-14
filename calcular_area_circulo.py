import math

# Paso 1: Solicitar al usuario el radio del circulo cuya area quiere calcular
radio circulo = float(input("Por favor, ingrese el radio del circulo"))

# Paso 2: Calcular el area del circulo usando la conocida formula
area_circulo = math.pi * (radio_circulo**2)

# Paso 3: Mostrar al usuario el area calculada
print(f"El area del circulo es {area_circulo}")