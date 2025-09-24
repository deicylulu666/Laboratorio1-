# Entrada
nivel_usuario =int(input("Ingrese el nivel de acceso del usuario (0-5): "))
nivel_requerido = int(input("Ingrese el nivel de acceso requerido (1-5): "))
tarjeta_activa = input("¿La tarjeta está activa? (si/no): ").strip().lower() == "si"
dias_contrasena = int(input("Ingrese los días desde el último cambio de contraseña: "))

# Proceso y salida
if nivel_usuario < nivel_requerido:
    print("Acceso denegado: el nivel de acceso del usuario es insuficiente.")

elif not tarjeta_activa:
    print("Acceso denegado: la tarjeta no está activa.")

elif dias_contrasena > 30:
    print("Acceso denegado: la contraseña no se ha actualizado en los últimos 30 días.")

else:
    print("Acceso permitido: todas las condiciones se cumplen.")
