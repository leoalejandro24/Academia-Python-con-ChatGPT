from ejercicio_biblioteca.libro import Libro

class Biblioteca:

    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []

    def agregar_libro(self, libro):
        self._libros.append(libro)

    def buscar_libro_por_autor(self, autor):
        for libro in self._libros:
            if libro.autor == autor:
                # print(libro)  De esta forma imprime la dirección en memoria
                self.mostrar_libro(libro) # De esta forma usamos la función de abajo para mostrar el libro

    def mostrar_libro(self, libro):
        print(f"Libro -> Titulo: {libro.titulo}, Autor: {libro.autor}, Genero: {libro.genero}")
        
    def buscar_libros_por_genero(self, genero):
        for libro in self._libros:
            if libro.genero == genero:
                self.mostrar_libro(libro)

    def mostrar_todos_los_libros(self):
        print(f"Todos los libros de la biblioteca {self._nombre}:")
        for libro in self._libros:
            self.mostrar_libro(libro)
