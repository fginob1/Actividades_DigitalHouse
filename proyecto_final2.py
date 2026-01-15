# Paso 1: Solicitar al usuario las medidas del mueble en centimetros
medida_cms = float(input("Por favor ingresas medidas de la pieza del mueble en cms: "))

# Paso 2: Convertir las medidas de centimetros a pulgadas
medida_pulgadas = medida_cms / 2.54

# Paso 3: Mostrar las  medidas convertidas en pulgadas al usuario
print("La medida en pulgadas seria ", medida_pulgadas)