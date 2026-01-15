# Paso 1: Definir el valor actual del euro y dolar con respecto al peso mexicano
tipo_cambio_euro_mxn = 23.70
tipo_cambio_usd_mxn = 20.75

# Paso 2: Solicitar al usuario el tipo de conversion (Euro a Mex o Dolar a Mex)
tipo_conversion = input("Ingrese la moneda de origen para la conversion (EUR/USD): ").upper()

# Paso 3: Solicitar al usuario el monto a convertir
monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# Paso 4: Realizar la conversion utilizando el tipo de cambio correspondiente
if tipo_conversion == "EUR":
    resultado = monto_a_convertir * tipo_cambio_euro_mxn
    print("El resultado de la conversion de EUR a MXN es: ", resultado)
elif tipo_conversion == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_mxn
    print("El resultado de la conversion de USD a MXN es: ", resultado)
else:
    print("No esta disponible la conversion de este tipo de conversion actualmente")