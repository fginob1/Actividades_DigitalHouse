# Paso 1: Solicitar al usuario que ingrese la edad del cliente
edad_cliente = int(input("Por favor, ingreses la edad del cliente: "))

# Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar
permitido = True if edad_cliente >= 18 else False

# Paso 3: Mostrar al usuario si su cliente puede ingresar o no
if permitido == True:
    print("El cliente puede ingresar a la discoteca")
else:
    print("Lo sentimos mucho pero no podes ingresar")