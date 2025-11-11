filas = int(input("Ingrese la cantidad de filas del triangulo: "))
n_astericos = 1
espacios_en_blanco = filas

for fila in range(1,(filas+1)):
    en_blanco = " "*(espacios_en_blanco - 1)
    print(en_blanco, end="")
    print("*"*n_astericos)
    n_astericos += 2
    espacios_en_blanco -= 1






#    *     1
#   ***    2 
#  *****   3
# *******  4
#********* 5