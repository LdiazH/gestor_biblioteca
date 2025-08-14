# 📚 Gestor de Biblioteca en Python

Este proyecto es una aplicación de consola para gestionar una biblioteca, permitiendo agregar, eliminar, buscar y prestar libros. Está desarrollado en Python utilizando principios de programación orientada a objetos, persistencia de datos en archivos CSV y buenas prácticas de validación.

## 🚀 Características

- Agregar libros con título, autor y año de publicación
- Eliminar libros por título
- Listar todos los libros o solo los disponibles
- Buscar libros por título
- Marcar libros como prestados o devueltos
- Persistencia automática en archivo `biblioteca.txt`
- Manejo de errores y validaciones robustas

## 🧠 Clases Principales

### `Libro`
Representa un libro físico con atributos privados y propiedades para validación:
- `titulo`, `autor`, `year`, `prestado`

### `Libro_digital`
Hereda de `Libro` y añade el atributo `formato` (ePub, PDF, etc.)

### `Biblioteca`
Gestiona una colección de libros:
- Métodos para agregar, eliminar, buscar, listar, prestar y devolver libros
- Guarda y carga datos desde `biblioteca.txt`

## 🖥️ Cómo Ejecutar

1. Clona el repositorio o copia los archivos en tu entorno local.
2. Asegúrate de tener Python 3 instalado.
3. Ejecuta el programa desde la terminal:

```bash
python main.py

👨‍💻 Autor
Luis Enrique Díaz Huenulef



