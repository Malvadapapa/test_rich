#importamos la libreria
from rich import print
#Necesario para usar la consola de rich
from rich.console import Console
 
#Necesario para usar los paneles de rich
from rich.panel import Panel

# Crear una instancia de Console 
console = Console()

# Usar Panel con la función print de rich
console.print(Panel("Hello, [red]World!")) # ejemplo de panel básico
console.print("Ejemplo de panel básico: console.print(Panel('Hello, [red]World!'))\n")

console.print(Panel.fit("Hello, [red]World!")) # ejemplo de panel ajustado
console.print("Ejemplo de panel ajustado: console.print(Panel.fit('Hello, [red]World!'))\n")

console.print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you")) # ejemplo de panel con título y subtítulo
console.print("Ejemplo de panel con título y subtítulo: console.print(Panel('Hello, [red]World!', title='Welcome', subtitle='Thank you'))\n")



