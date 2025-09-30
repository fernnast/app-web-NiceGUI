from random import randint

class Alumno:
    def __init__(self, codigo=0, semestre=1, promedio=0.0) -> None:
        self.codigo = codigo
        self.semestre = semestre
        self.promedio = promedio
        
    def __repr__(self) -> str:
        return 'codigo: ' + str(self.codigo), 'semestre: ' + str(self.semestre), 'promedio: ' + str(self.promedio)
    
    def to_dict(self):
        return{
            'codigo': self.codigo,
            'semestre': self.semestre,
            'promedio': self.promedio
        }