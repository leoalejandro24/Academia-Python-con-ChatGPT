mensaje = input("Ingresa un mensaje: ")
repeticiones = int(input("Cantidad de veces a repetir el mensaje: "))

for _ in range(repeticiones): # Usamos el guion bajo (_) para ignorar el número que se genera pero seguimos con
                              # sintaxis correcta.
    print(mensaje)