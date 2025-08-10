from clases import Libro, Biblioteca



"""
--- Gestor de Biblioteca ---
1. Agregar libro
2. Eliminar libro
3. Ver todos los libros
4. Buscar libro
5. Marcar libro como prestado
6. Devolver libro
7. Salir
Elige una opción:
"""
#funcione menu principal
def menu_principal():
    """Muestra el menú principal del sistema"""
    biblioteca = Biblioteca()
    try:
        while True:
            print("\n--- Gestor de Biblioteca ---")
            print("1. Agregar libro")
            print("2. Eliminar libro")
            print("3. Ver todos los libros")
            print("4. Ver libros disponibles")
            print("5. Buscar libro por título")
            print("6. Marcar libro como prestado")
            print("7. Devolver libro")
            print("8. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                titulo = input("Ingrese el título: ")
                autor = input("Ingrese el autor: ")
                
                # Manejo de errores para la entrada del año
                try:
                    year = int(input("Ingrese el año de publicación: "))
                    nuevo_libro = Libro(titulo, autor, year)
                    biblioteca.agregar_libro(nuevo_libro)
                    print(f"El libro '{titulo}' ha sido agregado correctamente.")
                except ValueError:
                    print("Error: El año debe ser un número entero. El libro no ha sido agregado.")
            
            elif opcion == "2":
                titulo = input("Ingrese el título del libro a eliminar: ")
                if biblioteca.eliminar_libro_por_titulo(titulo):
                    print(f"El libro '{titulo}' ha sido eliminado correctamente.")
                else:
                    print(f"Error: El libro '{titulo}' no se encontró en la biblioteca.")

            elif opcion == "3":
                libros = biblioteca.listar_libros()
                if libros:
                    print("\n--- Todos los Libros ---")
                    for libro in libros:
                        print(libro)
                else:
                    print("No hay libros en la biblioteca.")

            elif opcion == "4":
                libros_disponibles = biblioteca.listar_libros_disponibles()
                if libros_disponibles:
                    print("\n--- Libros Disponibles ---")
                    for libro in libros_disponibles:
                        print(libro)
                else:
                    print("No hay libros disponibles en este momento.")

            elif opcion == "5":
                titulo = input("Ingrese el título del libro a buscar: ")
                libro_encontrado = biblioteca.buscar_libro_por_titulo(titulo)
                if libro_encontrado:
                    print("\n--- Libro Encontrado ---")
                    print(libro_encontrado)
                else:
                    print(f"Error: El libro '{titulo}' no se encontró en la biblioteca.")
            
            elif opcion == "6":
                titulo = input("Ingrese el título del libro a prestar: ")
                if biblioteca.marcar_como_prestado(titulo):
                    print(f"El libro '{titulo}' ha sido marcado como prestado.")
                else:
                    print(f"Error: No se pudo prestar el libro '{titulo}'. Puede que ya esté prestado o no exista.")

            elif opcion == "7":
                titulo = input("Ingrese el título del libro a devolver: ")
                if biblioteca.devolver_libro(titulo):
                    print(f"El libro '{titulo}' ha sido devuelto correctamente.")
                else:
                    print(f"Error: No se pudo devolver el libro '{titulo}'. Puede que no estuviera prestado o no exista.")

            elif opcion == "8":
                print("Gracias por usar el gestor de biblioteca. ¡Hasta pronto!")
                break
            
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
    except KeyboardInterrupt:
        print("\n\nProceso interrumpido por el usuario (Ctrl+C).")
        # Asegurar los datos guardados antes de salir
        biblioteca.guardar_libros() 
        print("Datos guardados antes de salir. ¡Hasta pronto!")
# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()


#libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)

#bliblioteca = Biblioteca()

#bliblioteca.agregar_libro(libro1)

