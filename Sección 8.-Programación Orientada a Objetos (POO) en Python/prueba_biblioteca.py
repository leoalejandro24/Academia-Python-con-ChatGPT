from ejercicio_biblioteca.biblioteca import Biblioteca
from ejercicio_biblioteca.libro import Libro

# Creamos un objeto de tipo biblioteca

bibliotecaChile = Biblioteca("Biblioteca Chile")

# Agregar algunos libros 
libro1 = Libro("El Alquimista", "Paulo Cohelo", "Ficción")
libro2 = Libro("1984", "George Orwell", "Ficción")
libro3 = Libro("El código Da Vinci", "Dan Brown", "Misterio")
libro4 = Libro("Rayuela", "Julio Cortázar", "Novela")
libro5 = Libro("Veronica decide morir", "Paulo Cohelo", "Ficción")

# Agregar los libros a la biblioteca

bibliotecaChile.agregar_libro(libro1)
bibliotecaChile.agregar_libro(libro2)
bibliotecaChile.agregar_libro(libro3)
bibliotecaChile.agregar_libro(libro4)
bibliotecaChile.agregar_libro(libro5)

# Nombre de la biblioteca

print(f"*** Bienvenidos a la {bibliotecaChile._nombre} ***")

# Buscar libros por autor

print(f"Libros de Paulo Cohelo")
bibliotecaChile.buscar_libro_por_autor("Paulo Cohelo")

# Buscar libros por genero

print("Libros del Genero Ficción")
bibliotecaChile.buscar_libros_por_genero("Ficción")

# Mostrar todos los libros de la biblioteca

bibliotecaChile.mostrar_todos_los_libros()