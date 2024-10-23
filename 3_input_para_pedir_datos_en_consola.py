from rich.prompt import Prompt
from rich.console import Console
from rich.prompt import Confirm

# Crear una instancia de Console para imprimir en la consola
console = Console()

# Pedir al usuario que ingrese su nombre y almacenarlo en la variable 'name'
name = Prompt.ask("Enter your name")
# Imprimir el nombre ingresado por el usuario
console.print(name)

# Pedir al usuario que ingrese su nombre con un valor predeterminado "Paul Atreides"
name = Prompt.ask("Enter your name", default="Paul Atreides")
# Imprimir el nombre ingresado por el usuario o el valor predeterminado si no se ingresó nada
console.print(name)

# Preguntar al usuario si le gusta rich y almacenar la respuesta en 'is_rich_great'
is_rich_great = Confirm.ask("Do you like rich?")
# Imprimir un mensaje estilizado en verde si la respuesta es afirmativa
if is_rich_great:
    console.print('selecciono que si', style='green')
# Imprimir un mensaje estilizado en rojo si la respuesta es negativa
else:
    console.print('selecciono que no', style='red')
