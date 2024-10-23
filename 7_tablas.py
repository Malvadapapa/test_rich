from rich.console import Console
from rich.table import Table
from rich.align import Align

console = Console()

# Ejemplo 1: Crear una tabla básica con alineación vertical en una columna
console.print("[bold underline]Ejemplo 1: Tabla con alineación vertical en una columna[/bold underline]")
table1 = Table(title="Star Wars Movies")

# Añadir columnas con alineación vertical
table1.add_column("Released", justify="right", style="cyan", no_wrap=True)
table1.add_column("Title", style="magenta", vertical="middle")  # Alineación vertical en la columna

# Añadir filas
table1.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker")
table1.add_row("May 25, 2018", "Solo: A Star Wars Story")
table1.add_row("Dec 15, 2017", "Star Wars Ep. VIII: The Last Jedi")
table1.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story")

# Imprimir la tabla en la consola
console.print(table1)

# Ejemplo 2: Crear una tabla con alineación vertical en una celda específica
console.print("\n[bold underline]Ejemplo 2: Tabla con alineación vertical en una celda específica[/bold underline]")
table2 = Table(title="Star Wars Movies")

# Añadir columnas
table2.add_column("Released", justify="right", style="cyan", no_wrap=True)
table2.add_column("Title", style="magenta")

# Añadir filas con alineación vertical en una celda específica
table2.add_row("Dec 20, 2019", Align("Star Wars: The Rise of Skywalker", vertical="middle"))
table2.add_row("May 25, 2018", "Solo: A Star Wars Story")
table2.add_row("Dec 15, 2017", "Star Wars Ep. VIII: The Last Jedi")
table2.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story")

# Imprimir la tabla en la consola
console.print(table2)

# Ejemplo 3: Tabla con diferentes opciones de tabla
console.print("\n[bold underline]Ejemplo 3: Tabla con diferentes opciones de tabla[/bold underline]")
table3 = Table(
    title="Star Wars Movies",  # Establece el título de la tabla
    caption="Box Office Earnings",  # Establece el pie de la tabla
    width=80,  # Establece el ancho deseado de la tabla
    min_width=60,  # Establece un ancho mínimo para la tabla
    box=None,  # No mostrar cuadrícula
    safe_box=True,  # Forzar la tabla a generar caracteres ASCII en lugar de Unicode
    padding=(0, 1),  # Relleno en las celdas
    collapse_padding=True,  # Combinar el relleno de celdas vecinas
    pad_edge=False,  # Eliminar el relleno alrededor del borde de la tabla
    expand=True,  # Expandir la tabla al tamaño máximo disponible
    show_header=True,  # Mostrar el encabezado
    show_footer=True,  # Mostrar el pie de página
    show_edge=True,  # Mostrar la línea del borde de la tabla
    show_lines=True,  # Mostrar líneas entre las filas
    leading=1,  # Espacio adicional entre las filas
    style="on blue",  # Estilo aplicado a toda la tabla
    row_styles=["dim", ""],  # Estilos para filas alternas
    header_style="bold magenta",  # Estilo del encabezado
    footer_style="bold green",  # Estilo del pie de página
    border_style="bold red",  # Estilo para los caracteres del borde
    title_style="bold yellow",  # Estilo para el título
    caption_style="bold cyan",  # Estilo para el pie de página
    title_justify="center",  # Justificación del título
    caption_justify="right",  # Justificación del pie de página
    highlight=True  # Habilitar el resaltado automático del contenido de las celdas
)

# Añadir columnas
table3.add_column("Released", justify="right", style="cyan", no_wrap=True)
table3.add_column("Title", style="magenta")
table3.add_column("Box Office", justify="right", style="green", no_wrap=True)

# Añadir filas
table3.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table3.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table3.add_row("Dec 15, 2017", "Star Wars Ep. VIII: The Last Jedi", "$1,332,539,889")
table3.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

# Imprimir la tabla en la consola
console.print(table3)

# Ejemplo 4: Tabla con diferentes opciones de columna
console.print("\n[bold underline]Ejemplo 4: Tabla con diferentes opciones de columna[/bold underline]")
table4 = Table(title="Star Wars Movies")

# Añadir columnas con diferentes opciones
table4.add_column("Released", justify="right", style="cyan", no_wrap=True)
table4.add_column("Title", style="magenta", header_style="bold magenta", footer_style="bold green", justify="left", vertical="middle", width=30, min_width=20, max_width=40, ratio=2)
table4.add_column("Box Office", justify="right", style="green", no_wrap=True)

# Añadir filas
table4.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table4.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table4.add_row("Dec 15, 2017", "Star Wars Ep. VIII: The Last Jedi", "$1,332,539,889")
table4.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

# Imprimir la tabla en la consola
console.print(table4)

# Ejemplo 5: Crear una tabla que ocupe todo el ancho de la ventana
console.print("\n[bold underline]Ejemplo 5: Tabla que ocupa todo el ancho de la ventana[/bold underline]")
table5 = Table(
    title="Star Wars Movies",  # Establece el título de la tabla
    expand=True  # Expandir la tabla al tamaño máximo disponible
)

# Añadir columnas
table5.add_column("Released", justify="right", style="cyan", no_wrap=True)
table5.add_column("Title", style="magenta")
table5.add_column("Box Office", justify="right", style="green", no_wrap=True)

# Añadir filas
table5.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table5.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table5.add_row("Dec 15, 2017", "Star Wars Ep. VIII: The Last Jedi", "$1,332,539,889")
table5.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

# Imprimir la tabla en la consola
console.print(table5)


# Opciones de Tabla
# Existen varios argumentos de palabra clave en el constructor de la clase Table que puedes usar para definir cómo se verá una tabla.

# title: Establece el título de la tabla (texto que se muestra encima de la tabla).
# caption: Establece el pie de la tabla (texto que se muestra debajo de la tabla).
# width: Establece el ancho deseado de la tabla (desactiva el cálculo automático del ancho).
# min_width: Establece un ancho mínimo para la tabla.
# box: Define uno de los estilos de cuadrícula (Box) para la tabla, o None para no mostrar cuadrícula.
# safe_box: Establece en True para forzar la tabla a generar caracteres ASCII en lugar de Unicode.
# padding: Un entero o una tupla de 1, 2 o 4 valores para definir el relleno en las celdas.
# collapse_padding: Si es True, el relleno de celdas vecinas se combinará.
# pad_edge: Establece en False para eliminar el relleno alrededor del borde de la tabla.
# expand: Establece en True para expandir la tabla al tamaño máximo disponible.
# show_header: Establece en True para mostrar el encabezado, False para deshabilitarlo.
# show_footer: Establece en True para mostrar el pie de página, False para deshabilitarlo.
# show_edge: Establece en False para deshabilitar la línea del borde de la tabla.
# show_lines: Establece en True para mostrar líneas entre las filas, así como entre el encabezado/pie.
# leading: Espacio adicional entre las filas.
# style: Un estilo (Style) a aplicar a toda la tabla, por ejemplo, "on blue".
# row_styles: Define una lista de estilos para estilizar filas alternas, por ejemplo, ["dim", ""] para crear un efecto de franjas.
# header_style: Establece el estilo predeterminado para el encabezado.
# footer_style: Establece el estilo predeterminado para el pie de página.
# border_style: Establece un estilo para los caracteres del borde.
# title_style: Establece un estilo para el título.
# caption_style: Establece un estilo para el pie de página.
# title_justify: Establece el método de justificación del título ("left", "right", "center" o "full").
# caption_justify: Establece el método de justificación del pie de página ("left", "right", "center" o "full").
# highlight: Establece en True para habilitar el resaltado automático del contenido de las celdas.

# Opciones de Columna
# Existen varias opciones que puedes configurar en una columna para modificar su apariencia.

# header_style: Establece el estilo del encabezado, por ejemplo, "bold magenta".
# footer_style: Establece el estilo del pie de página.
# style: Define un estilo que se aplica a la columna. Podrías usar esto para resaltar una columna, por ejemplo, configurando el fondo con "on green".
# justify: Define la justificación del texto en la columna, puede ser "left", "center", "right" o "full".
# vertical: Establece la alineación vertical de las celdas en una columna, puede ser "top", "middle" o "bottom".
# width: Establece explícitamente el ancho de una fila a un número determinado de caracteres (desactiva el cálculo automático).
# min_width: Cuando se establece en un entero, impide que la columna se reduzca por debajo de este valor.
# max_width: Cuando se establece en un entero, impide que la columna crezca más allá de este valor.
# ratio: Define una proporción para establecer el ancho de la columna. Por ejemplo, si hay 3 columnas con un total de 6 de proporción, y una columna tiene ratio=2, entonces la columna ocupará un tercio del espacio disponible.
# no_wrap: Establece en True para evitar que esta columna realice saltos de línea.

# Alineación Vertical
# Puedes definir la alineación vertical de una columna configurando el parámetro vertical de la columna.
# También puedes hacer esto por celda, envolviendo tu texto o contenido con la clase Align:

# Ejemplo:
# table.add_row(Align("Título", vertical="middle"))
