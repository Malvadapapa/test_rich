import os
import sys

from rich import print
from rich.columns import Columns

# Crear una lista de elementos para mostrar en columnas
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]

# Crear columnas con los elementos de la lista
columns = Columns(items, equal=True, expand=True)

# Imprimir las columnas en la consola
print(columns)

from rich import print
from rich.console import Group
from rich.panel import Panel

# Crear un grupo de paneles
panel_group = Group(
    Panel("Hello", style="on blue"),  # Panel con texto "Hello" y fondo azul
    Panel("World", style="on red"),   # Panel con texto "World" y fondo rojo
)

# Imprimir el grupo de paneles dentro de un panel
print(Panel(panel_group))

from rich import print
from rich.console import group
from rich.panel import Panel

# Definir una función generadora que crea paneles
@group()
def get_panels():
    yield Panel("Hello", style="on blue")  # Generar un panel con texto "Hello" y fondo azul
    yield Panel("World", style="on red")   # Generar un panel con texto "World" y fondo rojo

# Imprimir los paneles generados dentro de un panel
print(Panel(get_panels()))