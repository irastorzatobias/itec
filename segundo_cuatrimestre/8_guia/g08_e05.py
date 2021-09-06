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
        """ Agrega asignatura al alumno"""
        if self.checkCourse(asignatura.lower()):
            print('La asignatura ya existe')
        else:
            self.asignaturas.append(Asignatura(asignatura, nota))
    
    def getPromedio(self):
        """ Retorna el promedio de todas las asignaturas de un alumno"""
        cantAsignaturas = len(self.asignaturas)
        result = 0
        if cantAsignaturas >= 1:
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
    """ Supongo que simula ser el controller, creado a lo bestia sin inputs."""
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

    def getFullAlumnos(self):
        """" Retorna la informacion de todos los alumnos"""
        i = 1
        for a in self.alumnos:
            print(f'Alumno {i}: ')
            print(a.getNombre(), a.getEdad())
            a.getAsignaturas()
            print(f'Promedio: {a.getPromedio()}')
            i = i + 1
            print('\n')

    def getAlumnosName(self):
        """" Devuelve el nombre de los alumnos """
        for a in self.alumnos:
            print(a.getNombre())

    def setAlumno(self, nombre:str, edad:int):
        """ Agregar nuevo alumno"""
        i = 0
        while True:
            alumnoNombre = self.alumnos[i].getNombre()
            if alumnoNombre.lower() == nombre.lower():
                print('El alumno ya existe, no se agrego a la lista')
                break
            else:
                print(f'Se agrego con exito {nombre} a la lista de alumnos')
                self.alumnos.append(Alumno(nombre,edad))
                break

    def getAlumnoData(self, nombre):
        """ Tras pasarle un nombre como parametro, devuelve los datos de ese alumno en particular"""
        i = 0
        while True:
            if nombre.lower() == self.alumnos[i].getNombre().lower():
                print(f'Nombre: {nombre}')
                self.alumnos[i].getAsignaturas()
                print(f'Promedio: {self.alumnos[i].getPromedio()}')
                break
            elif i == len(self.alumnos) - 1:
                print(f'No se encontro el alumno {nombre}')
                break  
            else:
                i += 1

    def getAlumnoNumber(self, nombre):
        """" Retorna el numero del alumno correspondiente en el la lista"""
        i = 0
        while True:
            if nombre.lower() == self.alumnos[i].getNombre().lower():
                return i
            elif i == len(self.alumnos):
                return (f'No se encontro el alumno {nombre}')  
            else:
                i += 1

    def setAlumnoData(self,nombre:str, asignatura:str, nota:int):
        """ Agregarle asignatura a alumno especifico """
        numeroAlumno = self.getAlumnoNumber(nombre)
        if type(numeroAlumno) == str:
            print(numeroAlumno)
        else:
            self.alumnos[numeroAlumno].setAsignatura(asignatura, nota)
        


              
if __name__ == '__main__':
    """ La mayoria de las clases fueron hechas en base de prints"""
    clase1 = Aplicacion()
    # Todos los alumnos 
    print('Datos de todos los alumnos')
    clase1.getFullAlumnos()
    # Nombre de los alumnos
    print('Nombres de los alumnos')
    clase1.getAlumnosName()
    # Un alumno en particular, devuelve error en caso que no exista el alumno
    print('\nDatos de alumno en particular')
    clase1.getAlumnoData('Pepito') 
    # Agrega un alumno con nombre y apellido
    clase1.setAlumno('Marcelo',29)

    # Agrega una asignatura a algun alumno, en caso de que no exista, lo informa.
    print('\nAgregando asignatura a alumno nuevo')
    clase1.setAlumnoData('Marcelo','Sistemas',8)
    
    
    # clase1.getFullAlumnos()
    
    

    
    
    
    