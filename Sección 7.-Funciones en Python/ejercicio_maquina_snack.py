snacks = [{"id": 1, "producto": "Papas", "precio": 30},
          {"id": 2, "producto": "Refresco", "precio": 50},
          {"id": 3, "producto": "Sandwich", "precio": 120}]

carrito = []


def menu():
    print("*** Maquina de Snacks ***")
    print('''Menú:
            1.- Mostrar Snacks
            2.- Comprar Snack
            3.- Mostrar ticket
            4.- Salir''')
    opción = int(input("Escoge una opción: "))
    if opción == 1:
        mostrar_snacks()
    elif opción == 2:
        comprar_snack()
    elif opción == 3:
        ticket_de_venta()
    elif opción == 4:
        print("Regresa pronto!")
    else:
        print("Opción invalida. seleccciona otra opción...")
        menu()

def mostrar_snacks():
    print("--- Snacks Disponibles ---")
    for snack in snacks:
        print(f"ID: {snack["id"]} -> {snack["producto"]} - Precio {snack["precio"]}")
    menu()


def comprar_snack():
    id_disponibles = []
    for s in snacks:
        agregar = s["id"]
        id_disponibles.append(agregar)
    snack = int(input("Que snack quieres?(id): "))
    if snack not in id_disponibles:
        print(f"Snack no encontrado con id = {snack}")
    else:
        añadir = snacks[snack-1]
        print(f"OK. snack agregado : {añadir}")
        carrito.append(añadir)
    menu()

def ticket_de_venta():
    print("*** Ticket de Venta ***")
    total = 0
    for productos in carrito:
        print(f"- {productos["producto"]} - ${productos["precio"]}")
        total += productos["precio"]
    print(f"TOTAL -> {total}")
    menu()


menu()