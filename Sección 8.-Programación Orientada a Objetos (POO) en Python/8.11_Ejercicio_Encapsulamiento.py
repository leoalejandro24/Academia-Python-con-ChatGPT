class Aritmetica:

    def __init__(self, operando1, operando2):
        self._operando1 = operando1
        self._operando2 = operando2

    def get_operando1(self):
        return self._operando1
    
    def set_operando1(self, operando1):
        self._operando1 = operando1

    def get_operando2(self):
        return self._operando2
    
    def set_operando2(self, operando2):
        self._operando2 = operando2

    def sumar(self):
        print(f"La suma de los dos operando es {self._operando1 + self._operando2}")

    def resta(self):
        print(f"La resta de los dos operando es {self._operando1 - self._operando2}")

# Get es para obtener los valores.
# Set es para modificar

aritmetica1 = Aritmetica(5,5)
aritmetica1.sumar()

aritmetica1.set_operando1(2)
aritmetica1.set_operando2(5)
aritmetica1.sumar()

aritmetica2 = Aritmetica(3,2)
aritmetica2.resta()

aritmetica2.set_operando1(2)
aritmetica2.set_operando2(5)
aritmetica2.resta()






# aritmetica1.set_operando1(2)
# aritmetica1.set_operando2(5)
# aritmetica1.sumar()

# aritmetica2 = Aritmetica(12,16)
# aritmetica2.sumar()    