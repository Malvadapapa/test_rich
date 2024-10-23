#importamos la libreria
from rich import print
#Necesario para usar la consola de rich
from rich.console import Console
#Necesario para usar temas personalizados
from rich.theme import Theme
 

# Crear un tema personalizado
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})

# Crear una instancia de Console con el tema personalizado
console = Console(theme=custom_theme)

# Ejemplos de uso de tema personalizado
console.print("This is information", style="info") # ejemplo de información usando tema personalizado
console.print("Ejemplo de información usando tema personalizado: console.print('This is information', style='info')\n")

console.print("[warning]The pod bay doors are locked[/warning]") # ejemplo de advertencia usando tema personalizado
console.print("Ejemplo de advertencia usando tema personalizado: console.print('[warning]The pod bay doors are locked[/warning]')\n")

console.print("Something terrible happened!", style="danger") # ejemplo de peligro usando tema personalizado
console.print("Ejemplo de peligro usando tema personalizado: console.print('Something terrible happened!', style='danger')\n")



# Estilos
console.print("Hello", style="magenta") # ejemplo de color
console.print("Ejemplo de color: console.print('Hello', style='magenta')\n")

console.print("DANGER!", style="red on white") # ejemplo de advertencia usar el on para poner fondo
console.print("Ejemplo de advertencia usar el on para poner fondo: console.print('DANGER!', style='red on white')\n")
# Estilos
console.print("Hello", style="magenta") # ejemplo de color
console.print("Ejemplo de color: console.print('Hello', style='magenta')\n")

console.print("DANGER!", style="red on white") # ejemplo de advertencia usar el on para poner fondo
console.print("Ejemplo de advertencia usar el on para poner fondo: console.print('DANGER!', style='red on white')\n")

# Ejemplo de texto en negrita
console.print("Texto en negrita", style="bold") # ejemplo de texto en negrita
console.print("Ejemplo de texto en negrita: console.print('Texto en negrita', style='bold')\n")

# Ejemplo de texto oculto
console.print("Texto oculto", style="conceal") # ejemplo de texto oculto usar conceal para ocultar
console.print("Ejemplo de texto oculto: console.print('Texto oculto', style='conceal')\n")

# Ejemplo de texto en cursiva
console.print("Texto en cursiva", style="italic") # ejemplo de texto en cursiva usar italic para cursiva
console.print("Ejemplo de texto en cursiva: console.print('Texto en cursiva', style='italic')\n")

# Ejemplo de texto con colores invertidos
console.print("Texto con colores invertidos", style="reverse") # ejemplo de texto con colores invertidos usar reverse para invertir colores
console.print("Ejemplo de texto con colores invertidos: console.print('Texto con colores invertidos', style='reverse')\n")

# Ejemplo de texto tachado
console.print("Texto tachado", style="strike") # ejemplo de texto tachado usar strike para tachar
console.print("Ejemplo de texto tachado: console.print('Texto tachado', style='strike')\n")

# Ejemplo de texto subrayado
console.print("Texto subrayado", style="underline") # ejemplo de texto subrayado usar underline para subrayar
console.print("Ejemplo de texto subrayado: console.print('Texto subrayado', style='underline')\n")

# Ejemplo de texto doblemente subrayado
console.print("Texto doblemente subrayado", style="underline2") # ejemplo de texto doblemente subrayado usar underline2 para doble subrayado
console.print("Ejemplo de texto doblemente subrayado: console.print('Texto doblemente subrayado', style='underline2')\n")

# Ejemplo de texto con línea superior
console.print("Texto con línea superior", style="overline") # ejemplo de texto con línea superior usar overline para línea superior
console.print("Ejemplo de texto con línea superior: console.print('Texto con línea superior', style='overline')\n")

# Imprime un enlace en la consola
console.print("Este es un ejemplo de cómo imprimir un enlace en la consola usando rich.")

print("Visit my [link=https://www.willmcgugan.com]blog[/link]!")