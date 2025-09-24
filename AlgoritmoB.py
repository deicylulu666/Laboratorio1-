#se importa la libreria
import math
# Solicitamos el radio de la pelota : 
radio = float(input("Ingrese el radio de la pelota: "))
# Validamos que el dato ingresado positivo 
#se cacula el valumen 
if radio > 0:
    volumen = (4/3) * math.pi * (radio**3)
    print(f"El volumen de la pelota es: {volumen:} unidades cúbicas")
else:
    print("El radio debe ser un valor positivo.")
