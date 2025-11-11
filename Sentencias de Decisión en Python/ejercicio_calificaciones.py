nota = int(input("Ingrese una nota (0 al 10): "))

if nota >= 9 and nota <= 10:
    print("Su nota es un A")
elif nota >= 8 and nota < 9:
    print("Su nota es un B")
elif nota >= 7 and nota < 8:
    print("Su nota es un C")
elif nota >= 6 and nota < 7:
    print("Su nota es un D")
elif nota >= 0 and nota < 6:
    print("Su nota es un F")
else:
    print("Valor desconocido")



