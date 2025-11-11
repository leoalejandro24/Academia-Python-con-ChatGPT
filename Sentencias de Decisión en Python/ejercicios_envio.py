costo_nacional = 10
costo_internacional = 20

destino = input("Ingrese el destino del paquete (nacional/internacional)").lower().strip()
# lower nos ayuda a dejar el texto en minuscula y strip a eliminar los espacios en blanco
# del inicio y final del texto

peso_paquete = float(input("Ingrese el peso del paquete (KG)"))

if destino == "nacional":
    print(f"El costo del envio del paquete es: {peso_paquete*costo_nacional}")

elif destino == "internacional":
    print(f"El costo del envio del paquete es: {peso_paquete*costo_internacional}")

else:
    print("Ingrese valores correctos.")