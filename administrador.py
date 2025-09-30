from typing import List
from alumnos import Alumno
from random import randint

class Administrador:
    def __init__(self, nombre:str) -> None:
         self.nombre = nombre
         self.alumnos: List[Alumno] = []
         
    def insertar_final(self, alumno:Alumno):
           self.alumnos.append(alumno)
           
    def mostrar(self):
        print('agencia: ' + self.nombre)
        for alumno in self.alumnos:
            print(alumno)
            
    def mostrar_tabla(self):
        headers = 'CODIGO'.ljust(6) + 'SEMESTRE'.ljust(3) + 'PROMEDIO'.ljust(6)
        print('_'*len(headers))
        for alumno in self.alumnos:
            codigo = str(alumno.codigo).ljust(6)
            semestre = str(alumno.semestre).ljust(3)
            promedio = str(alumno.promedio).ljust(6)
            print(codigo+semestre+promedio)
            
    def guardar(self):
        with open('./csv/alumnos.csv', 'w') as archivo:
            for alumno in self.alumnos:
                archivo.write(str(alumno.codigo) + ',')
                archivo.write(str(alumno.semestre) + ',')
                archivo.write(str(alumno.promedio) + '\n')
    
    def recuperar(self, nombre:str):
        with open(nombre, 'r') as archivo:
            for line in archivo:
                atributos = line.strip().split(',')
                alumno = Alumno(codigo=atributos[0], semestre=atributos[1], promedio=atributos[2])
                self.alumnos.append(alumno)
        
    def limpiar(self):
        self.alumnos.clear()
        
    def generar_promedio(self, cantidad)-> Alumno:
        for alumno in range(cantidad):
               promedio = float(randint(0, 100))
               self.insertar_final(Alumno(promedio=promedio))
    
    def ordenar_codigo(self, reverse=False):
        self.alumnos.sort(key= lambda alumno: alumno.codigo, reverse=reverse)
        
    def ordenar_semestre(self, reverse=False):
        self.alumnos.sort(key= lambda alumno: alumno.semestre, reverse=reverse)
        
    def ordenar_promedio(self, reverse=False):
        self.alumnos.sort(key= lambda alumno: alumno.promedio, reverse=reverse)
                
        
        
    # self.codigo = codigo
    # self.semestre = semestre
    # self.promedio = promedio