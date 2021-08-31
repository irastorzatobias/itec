class Asignatura:
    def __init__(self,materia:str,nota:int):
        self.materia = materia
        self.nota = nota

    def setNota(self, newNota):
        """ cambia la nota """
        self.nota = newNota

    def getNota(self):
        """ Retorna materia y nota"""
        return self.nota
    
    def aprobadoDesaprobado(self):
        if self.nota >= 4:
            return f'Asignatura aprobada'
        else:
            return f'Asignatura desaprobada'

    def getAsignatura(self):
        return self.materia

class Alumno:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.asignaturas = []

    def setNombre(self, newName):
        self.nombre = newName
    
    def getNombre(self):
        return self.nombre
    
    def setEdad(self, newAge):
        self.edad = newAge

    def getEdad(self):
        return self.edad
    
    def checkCourse(self,course):
        """ Metodo que chequea si una asignatura ya está en self asignatura"""
        for a in self.asignaturas:
            if course.lower() in a.getAsignatura().lower(): # si coincide el nombre con la asignatura, devuelve true
                return True
    
    def setAsignatura(self,asignatura:str,nota:str):
        if self.checkCourse(asignatura.lower()):
            print('La asignatura ya existe')
        else:
            self.asignaturas.append(Asignatura(asignatura, nota))
    
    def getPromedio(self):
        """ Retorna el promedio de todas las asignaturas de un alumno"""
        cantAsignaturas = len(self.asignaturas)
        result = 0
        for a in self.asignaturas:
            result += a.getNota()
        result = result / cantAsignaturas
        return result
    
    def getAsignaturas(self):
        """ Printea todas las asignaturas y la nota del alumno"""
        if len(self.asignaturas) >= 1:            
            for e in self.asignaturas:
                print(f'Asignatura: {e.getAsignatura()}, nota: {e.getNota()}')
                print(e.aprobadoDesaprobado())
        else:
            print('No hay asignaturas agregadas')


class Aplicacion:
    """ Supongo que simula ser el controller."""
    def __init__(self):
        self.alumnos = [Alumno('Tobias',22),Alumno('Pepito',25),Alumno('Lautaro',26)]
        self.alumnos[0].setAsignatura('Matematica',10)
        self.alumnos[0].setAsignatura('Matematica II',7)
        self.alumnos[0].setAsignatura('Matematica III',6)
        # Segundo alumno
        self.alumnos[1].setAsignatura('Ingles I',9)
        self.alumnos[1].setAsignatura('Ingles II',2)
        self.alumnos[1].setAsignatura('Ingles III',9)
        # Tercer alumno
        self.alumnos[2].setAsignatura('Logica I',8)
        self.alumnos[2].setAsignatura('Logica II',8)
        self.alumnos[2].setAsignatura('Logica III',8)

    def getAlumnos(self):
        i = 1
        for a in self.alumnos:
            print(f'Alumno {1}: ')
            print(a.getNombre(), a.getEdad())
            a.getAsignaturas()
            print(f'Promedio: {a.getPromedio()}')
            print('\n')
            
if __name__ == '__main__':
    clase1 = Aplicacion()
    clase1.getAlumnos()
    
    
    
    
    