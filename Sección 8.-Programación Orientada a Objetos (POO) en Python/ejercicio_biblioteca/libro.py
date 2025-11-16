class Libro:

    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    @property # Metodo de solo lectura y nos devuelve el valor del atributo protegido o privado (metodo get)
    def titulo(self):
        return self._titulo
    
    @property # Metodo de solo lectura y nos devuelve el valor del atributo protegido o privado (metodo get)
    def autor(self):
        return self._autor
    @property # Metodo de solo lectura y nos devuelve el valor del atributo protegido o privado (metodo get)
    def genero(self):
        return self._genero

if __name__ == "__main__":
    libro = Libro("titulo", "autor", "genero")
    # libro.titulo = "titulo 2" Esto nos marca error (no podemos modificar el valor de titulo)
    print(f"Accedemos a la propiedad de titulo: {libro.titulo}")   

        