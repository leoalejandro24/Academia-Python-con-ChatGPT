# Función para saber si un numero es par o no

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    

# Llamamos a la función
if __name__ == "__main__":
    numero = int(input("Propociona nu valor númerico: "))
    print(f"Número par? {es_par(numero)}")