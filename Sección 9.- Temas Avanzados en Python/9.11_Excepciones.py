def dividir(numerador, denominador):
    try:
        resultado = numerador/denominador
        print(f"Resultado de la división {resultado}")
    except Exception as e: # Agregar este excepción es algo más generico.
        print(f"Ocurrio un error {e}")
    finally: # Este bloque siempre se ejecuta independientemente si hubo error o no
        print(f"Terminamos de procesar la excepción\n")

    # except ZeroDivisionError: # except + la excepción a capturar
    #     print("Error: No se puede dividir entre 0")
    # except TypeError:
    #     print("Error: Los operandos deben ser numericos")

# Ejemplo de uso

dividir(10,2) # Resultado: 5
dividir(10,0) # Error: ZeroDivisionError
# Una vez agregado los bloques de excepción nos imprime el mensaje 
dividir(10, "0") # Error: TypeError
# Una vez agregado los bloques de excepción nos imprime el mensaje




