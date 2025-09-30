from nicegui import ui
from random import uniform
from alumnos import Alumno
from administrador import Administrador

# Instancias
administrador = Administrador(nombre='CUCEI')
alumno=Alumno()

# Configuraciones de estilos
classes = 'w-full items-center justify-center'

#----------------------------------------------------------------------------------------------------------
# Funciones para la interfaz gráfica
def mostrar_tabla():
    """Actualiza la tabla con los datos de los alumnos en la lista."""
    tabla.rows = [alumno.to_dict() for alumno in administrador.alumnos]

def agregar_alumno():
    """Agrega un alumno a la lista usando los valores ingresados en los campos de entrada."""
    codigo = codigo_input.value
    semestre = int(semestre_input.value)
    promedio = float(promedio_input.value)
    alumno = Alumno(codigo=codigo, semestre=semestre, promedio=promedio)
    administrador.insertar_final(alumno)
    mostrar_tabla()  # Actualiza la tabla después de agregar el alumno

def generar_promedio():
    """Genera un promedio aleatorio y lo muestra en el campo de entrada de promedio."""
    promedio = round(uniform(0.0, 100.0), 2)  # Promedio aleatorio con 2 decimales
    promedio_input.value = promedio  # Muestra el promedio generado en el campo de entrada

def ordenar_por_codigo():
    """Ordena la lista de alumnos por código según el orden especificado."""
    administrador.ordenar_codigo(reverse=not orden_ascendente.value)
    mostrar_tabla()

def ordenar_por_semestre():
    """Ordena la lista de alumnos por semestre según el orden especificado."""
    administrador.ordenar_semestre(reverse=not orden_ascendente.value)
    mostrar_tabla()

def ordenar_por_promedio():
    """Ordena la lista de alumnos por promedio según el orden especificado."""
    administrador.ordenar_promedio(reverse=not orden_ascendente.value)
    mostrar_tabla()

#----------------------------------------------------------------------------------------------------------
# Interfaz gráfica con NiceGUI
with ui.row().classes(classes):
    # Entradas para código, semestre y promedio
    codigo_input = ui.input(label='Código').props('maxlength=5')  # Código de 5 dígitos
    semestre_input = ui.input(label='Semestre').props('type=number')
    promedio_input = ui.input(label='Promedio').props('type=number')

# Botones para agregar y generar promedios
with ui.row().classes(classes):
    ui.button('Generar Promedio Aleatorio', on_click=generar_promedio)
    ui.button('Agregar Alumno', on_click=agregar_alumno)

# Checkbox para seleccionar el orden de la tabla
with ui.row().classes(classes):
    orden_ascendente = ui.checkbox('Orden Ascendente', value=True)

# Botones para ordenar los datos en la tabla
with ui.row().classes(classes):
    ui.button('Ordenar por Código', on_click=ordenar_por_codigo)
    ui.button('Ordenar por Semestre', on_click=ordenar_por_semestre)
    ui.button('Ordenar por Promedio', on_click=ordenar_por_promedio)

# Tabla para mostrar los datos
with ui.row().classes(classes):
    tabla = ui.table(
        columns=[
            {'name': 'CODIGO', 'label': 'CODIGO', 'field': 'codigo'},
            {'name': 'SEMESTRE', 'label': 'SEMESTRE', 'field': 'semestre'},
            {'name': 'PROMEDIO', 'label': 'PROMEDIO', 'field': 'promedio'}
        ],
        rows=[]
    )

ui.run()
