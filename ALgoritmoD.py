# Solicitud de datos:
monto_compra = float(input("Ingrese el monto de la compra: "))
vip = input("¿Es cliente VIP? (si/no): ") == "si"
codigo = input("¿Tiene código de descuento? (si/no): ") == "si"

# Ejecucion:
total = monto_compra

# Condiciones de descuento: 
if monto_compra > 100:
    total -= total * 0.20   # Descuento del 20%

if vip:
    total -= total * 0.10   # Descuento del 10%

if codigo:
    total -= total * 0.05   # Descuento del 5%

print("El total a pagar es:", total)
