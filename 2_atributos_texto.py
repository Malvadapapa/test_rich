from rich.console import Console
from rich.text import Text

#INVESTIGAR POR QUE LOS ALINEADOS NO ANDAN 



console = Console()

# Crear un objeto Text con el contenido "Hello, World!"
console.print("Creando un objeto Text con el contenido 'Hello, World!'\n")
text = Text("Hello, World!")

# Aplicar el estilo "bold magenta" desde el inicio hasta el sexto carácter
console.print("Aplicando el estilo 'bold magenta' desde el inicio hasta el sexto carácter\n")
text.stylize("bold magenta", 0, 6)

# Imprimir el texto estilizado en la consola
console.print("Imprimiendo el texto estilizado en la consola\n")
console.print(text)


# Crear un objeto Text vacío
console.print("Creando un objeto Text vacío\n")
text = Text()

# Añadir "Hello" con el estilo "bold magenta"
console.print("Añadiendo 'Hello' con el estilo 'bold magenta'\n")
text.append("Hello", style="bold magenta")

# Añadir " World!" sin estilo adicional
console.print("Añadiendo ' World!' sin estilo adicional\n")
text.append(" World!")

# Imprimir el texto estilizado en la consola
console.print("Imprimiendo el texto estilizado en la consola\n")
console.print(text)


# Crear un objeto Text con justificación a la izquierda
console.print("Creando un objeto Text con justificación a la izquierda\n")
text_left = Text("Este texto está justificado a la izquierda.", justify="left")
console.print(text_left)

# Crear un objeto Text con justificación centrada
console.print("Creando un objeto Text con justificación centrada\n")
text_centered = Text("Este texto está centrado.", justify="center")
console.print(text_centered)

# Crear un objeto Text con justificación a la derecha
console.print("Creando un objeto Text con justificación a la derecha\n")
text_right = Text("Este texto está justificado a la derecha.", justify="right")
console.print(text_right, width=50)

# Crear un objeto Text con justificación completa
console.print("Creando un objeto Text con justificación completa\n")
text_full = Text("Este texto está justificado completamente.", justify="full")
console.print(text_full)

# Crear un objeto Text con overflow de tipo "ellipsis"
console.print("Creando un objeto Text con overflow de tipo 'ellipsis'\n")
text_overflow = Text("Este texto es demasiado largo para caber en una línea.", overflow="ellipsis")
console.print(text_overflow)

# Crear un objeto Text sin ajuste de línea
console.print("Creando un objeto Text sin ajuste de línea\n")
text_no_wrap = Text("Este texto no se ajustará a la línea y continuará en una sola línea larga.", no_wrap=True)
console.print(text_no_wrap)

# Crear un objeto Text con tamaño de tabulación personalizado
console.print("Creando un objeto Text con tamaño de tabulación personalizado\n")
text_tab_size = Text("Texto con\ttabulaciones.", tab_size=4)
console.print(text_tab_size)