import time
from rich.progress import track, Progress, BarColumn, TextColumn, TimeElapsedColumn, TimeRemainingColumn, MofNCompleteColumn, FileSizeColumn, TotalFileSizeColumn, DownloadColumn, TransferSpeedColumn, SpinnerColumn, ProgressColumn

# Usar track para crear una barra de progreso mientras se itera sobre un rango de 5
for i in track(range(5), description="Processing..."):
    # Simular trabajo en progreso con una pausa de 1 segundo
    time.sleep(1)

# Simular el procesamiento de una compra
def process_purchase():
    # Usar track para crear una barra de progreso mientras se itera sobre un rango de 3 (3 segundos)
    for i in track(range(3), description="Procesando su compra..."):
        # Simular trabajo en progreso con una pausa de 1 segundo
        time.sleep(1)

# Llamar a la función para procesar la compra
process_purchase()

import time
from rich.progress import Progress

# Crear un objeto Progress para gestionar múltiples barras de progreso
with Progress() as progress:

    # Añadir tareas con descripciones y totales
    task1 = progress.add_task("[red]Downloading...", total=100)
    task2 = progress.add_task("[green]Processing...", total=100)
    task3 = progress.add_task("[cyan]Cooking...", total=100)

    # Actualizar las tareas hasta que todas estén completas
    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.9)
        time.sleep(0.02)

# BarColumn: Muestra la barra de progreso.
# TextColumn: Muestra texto.
# TimeElapsedColumn: Muestra el tiempo transcurrido.
# TimeRemainingColumn: Muestra el tiempo estimado restante.
# MofNCompleteColumn: Muestra el progreso de finalización como "{task.completed}/{task.total}" (funciona mejor si completed y total son enteros).
# FileSizeColumn: Muestra el progreso como tamaño de archivo (asume que los pasos son bytes).
# TotalFileSizeColumn: Muestra el tamaño total del archivo (asume que los pasos son bytes).
# DownloadColumn: Muestra el progreso de la descarga (asume que los pasos son bytes).
# TransferSpeedColumn: Muestra la velocidad de transferencia (asume que los pasos son bytes).
# SpinnerColumn: Muestra una animación de "spinner".
# RenderableColumn: Muestra un renderizable arbitrario de Rich en la columna.

# Crear un objeto Progress con varias columnas para mostrar información detallada
with Progress(
    TextColumn("[progress.description]{task.description}"),  # Columna de texto para la descripción de la tarea
    BarColumn(),  # Columna de barra de progreso
    TimeElapsedColumn(),  # Columna de tiempo transcurrido
    TimeRemainingColumn(),  # Columna de tiempo restante estimado
    MofNCompleteColumn(),  # Columna de progreso de finalización
    FileSizeColumn(),  # Columna de tamaño de archivo
    TotalFileSizeColumn(),  # Columna de tamaño total de archivo
    DownloadColumn(),  # Columna de progreso de descarga
    TransferSpeedColumn(),  # Columna de velocidad de transferencia
    SpinnerColumn()  # Columna de animación de "spinner"
) as progress:

    # Añadir tareas con descripciones y totales
    task1 = progress.add_task("[red]Downloading...", total=100)
    task2 = progress.add_task("[green]Processing...", total=100)
    task3 = progress.add_task("[cyan]Cooking...", total=100)

    # Actualizar las tareas hasta que todas estén completas
    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.9)
        time.sleep(0.02)

# Crear una barra de progreso con un spinner al final
with Progress(
    TextColumn("[progress.description]{task.description}"),  # Columna de texto para la descripción de la tarea
    BarColumn(),  # Columna de barra de progreso
    SpinnerColumn(),  # Columna de animación de "spinner"
    expand=True  # Extender la barra de progreso al ancho completo disponible
) as progress:

    # Añadir una tarea con la descripción "Guardando los cambios en la base de datos"
    task = progress.add_task("[green]Guardando los cambios en la base de datos...", total=100)

    # Simular el progreso de la tarea
    while not progress.finished:
        progress.update(task, advance=1)  # Avanzar la barra de progreso
        time.sleep(0.03)  # Simular trabajo en progreso con una pausa