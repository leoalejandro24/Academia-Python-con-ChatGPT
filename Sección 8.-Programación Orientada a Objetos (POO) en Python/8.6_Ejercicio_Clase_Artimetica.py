class Aritmetica:

    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        print(f"La suma de los dos operando es {self.operando1 + self.operando2}")

    def resta(self):
        print(f"La resta de los dos operando es {self.operando1 - self.operando2}")


aritmetica1 = Aritmetica(5,7)
aritmetica1.sumar()

aritmetica2 = Aritmetica(12,16)
aritmetica2.sumar()    
