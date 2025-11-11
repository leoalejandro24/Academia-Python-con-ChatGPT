compra = 1000

compra_cliente = float(input("Ingrese el monto de la compra: "))
cliente_miembro = input("¿Es cliente miembro? (si/no): ").strip().lower()

if compra_cliente > compra and cliente_miembro == "si":
    print("Descuento del 10% aplicado")
elif compra_cliente < compra and cliente_miembro == "si":
    print("Descuento del 5% aplicado")
else:
    print("No se aplican descuentos")

