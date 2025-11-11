snacks = [{"id": 1, "producto": "Papas", "precio": 30},
          {"id": 2, "producto": "Refresco", "precio": 50},
          {"id": 3, "producto": "Sandwich", "precio": 120}]


def menu():
    print("*** Maquina de Snacks ***")
    print('''Menú:
            1.- Mostrar Snacks
            2.- Comprar Snack
            3.- Mostrar ticket
            4.- Salir''')
    opción = int(input("Escoge una opción: "))

def mostrar_snacks():
    print("--- Snacks Disponibles ---")
    for snack in snacks:
        print(f"ID: {snack["id"]} -> {snack["producto"]} - Precio {snack["precio"]}")

def mostrar_snack():
    selección = int(input("Que snack quieres (id)?: "))
    lista_snack = []
    for snack in snacks:
        id_snack = snack["id"]
        lista_snack.append(id_snack)
    if selección in lista_snack:
        print(f"ID: {snacks[selección-1]["id"]} -> {snacks[selección-1]["producto"]} - Precio {snacks[selección-1]["precio"]}")
    else:
        print(f"Snack no encontrado con id = {selección}")

mostrar_snack()
    

