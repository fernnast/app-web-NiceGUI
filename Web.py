
from nicegui import ui
from random import randint
from alumnos import Alumno
from administrador import Administrador

alumno = Alumno()
administrador = Administrador(nombre='CUCEI')

classes = 'w-full items-center justify-center'
style = 'aling-items:center; justify-content:center; border: 1px solid black; border-radius: 8px'
tail = 'w-full ml-5 mr-5'

#----------------------------------------------------------------------------------------------------------
def mostrar_tabla():
    administrador.mostrar_tabla()
    tabla.rows = [alumno.to_dict() for alumno in administrador.alumnos]

#----------------------------------------------------------------------------------------------------------

with ui.row().classes(classes):
    ui.button('Mostrar datos', on_click=lambda: mostrar_tabla())


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

      
    # self.codigo = codigo
    # self.semestre = semestre
    # self.promedio = promedio