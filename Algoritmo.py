# Datos solicitados:
tA= int(input("Ingrese el tiempo asignado a la tarea (en días): "))
tC = int(input("Ingrese el tiempo real utilizado en la tarea (en días): "))

# Proceso para calcular:
if tC > tA:
    retraso = tC- tA
    porcentaje = (retraso / tA) * 100
    print(f"La tarea tiene un retraso de {retraso} días.")
    print(f"Porcentaje de retraso: {porcentaje:}%")
else:
    print("La tarea se completó a tiempo o antes del plazo.")
