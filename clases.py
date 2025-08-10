class Libro:
    def __init__(self, titulo, autor, year):
        self._titulo = titulo
        self._autor = autor
        self._year = year
        self._prestado = False

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, nuevo_titulo):
        if nuevo_titulo:
            self._titulo = nuevo_titulo
        else:
            print("Error: El título no puede estar vacío.")

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, nuevo_autor):
        if nuevo_autor:
            self._autor = nuevo_autor
        else:
            print("Error: El autor no puede estar vacío.")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, nuevo_year):
        if isinstance(nuevo_year, int) and nuevo_year > 0:
            self._year = nuevo_year
        else:
            print("Error: El año debe ser un número entero positivo.")
            
    @property
    def prestado(self):
        return self._prestado

    @prestado.setter
    def prestado(self, estado):
        if isinstance(estado, bool):
            self._prestado = estado
        else:
            print("Error: El estado de préstamo debe ser un valor booleano (True/False).")
            
    # Metodo str
    def __str__(self):
        estado = "Prestado" if self._prestado else "Disponible"
        return f"Título: {self._titulo}, Autor: {self._autor}, Año: {self._year}, Estado: {estado}"


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.cargar_libros()

    def guardar_libros(self):
        """Guarda la lista de libros en un archivo de texto (CSV)."""
        try:
            with open("biblioteca.txt", "w") as f:
                for libro in self.libros:
                    f.write(f"{libro.titulo},{libro.autor},{libro.year},{libro.prestado}\n")
            print("Datos de la biblioteca guardados correctamente.")
        except FileNotFoundError:
            print("No se encontró el archivo 'biblioteca.txt'. Se creará uno nuevo al guardar.")
            self.libros = []
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            self.libros = []

    def cargar_libros(self):
        """Carga la lista de libros desde un archivo de texto (CSV)."""
        try:
            with open("biblioteca.txt", "r") as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) == 4:
                        titulo, autor, year_str, prestado_str = partes
                        year = int(year_str)
                        prestado = prestado_str.lower() == 'true'
                        nuevo_libro = Libro(titulo, autor, year)
                        nuevo_libro.prestado = prestado
                        self.libros.append(nuevo_libro)
            print("Datos de la biblioteca cargados exitosamente.")
        except FileNotFoundError:
            print("No se encontró el archivo 'biblioteca.txt'. Se creará uno nuevo al guardar.")
            self.libros = []
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            self.libros = []

    def agregar_libro(self, libro):
        if self.buscar_libro_por_titulo(libro.titulo):
            print(f"El libro '{libro.titulo}' ya existe en la biblioteca.")
        else:
            self.libros.append(libro)
            self.guardar_libros()

    def eliminar_libro_por_titulo(self, titulo):
        try:
            libro_encontrado = self.buscar_libro_por_titulo(titulo)
            if libro_encontrado:
                self.libros.remove(libro_encontrado)
                self.guardar_libros()
                return True
            return False
        except FileNotFoundError:
            print("No se encontró el archivo 'biblioteca.txt'. Se creará uno nuevo al guardar.")
            self.libros = []
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            self.libros = []
            
    def buscar_libro_por_titulo(self, titulo):
        try: 
            for libro in self.libros:
                if libro.titulo.lower() == titulo.lower():
                    return libro
            return None
        except FileNotFoundError:
            print("No se encontró el archivo 'biblioteca.txt'. Se creará uno nuevo al guardar.")
            self.libros = []
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            self.libros = []

    def listar_libros(self):
        return self.libros

    def listar_libros_disponibles(self):
        return [libro for libro in self.libros if not libro.prestado]

    def marcar_como_prestado(self, titulo):
        try: 
            libro = self.buscar_libro_por_titulo(titulo)
            if libro and not libro.prestado:
                libro.prestado = True
                self.guardar_libros()
                return True
            return False
        except FileNotFoundError:
            print("No se encontró el archivo 'biblioteca.txt'. Se creará uno nuevo al guardar.")
            self.libros = []
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            self.libros = []

    def devolver_libro(self, titulo):
        try:
            libro = self.buscar_libro_por_titulo(titulo)
            if libro and libro.prestado:
                libro.prestado = False
                self.guardar_libros()
                return True
            return False
        except FileNotFoundError:
            print("No se encontró el archivo 'biblioteca.txt'. Se creará uno nuevo al guardar.")
            self.libros = []
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            self.libros = []


class Libro_digital(Libro):
    def __init__(self, titulo, autor, year, formato):
        super().__init__(titulo, autor, year)
        self.formato = formato        
        
        
            
"""
metodos
Agregar un libro

Eliminar un libro por su título

Listar todos los libros disponibles

Buscar un libro por su título

Marcar un libro como prestado

Devolver un libro prestado
"""       