# Programa que permite crear empresa de informatica
from dataclasses import dataclass
from validacion_entero import validacionEntero as vInt

@dataclass
class Persona:
    nombre: str
    
    def getName(self):
        """ Getter para el nombre """
        return self.nombre  
    
    def setName(self,newName:str):
        """ Setter para el nombre """
        self.nombre = newName
        
        
@dataclass
class Empleado(Persona):
    # No se emplea constructor de sueldo ya que no lo pide la consigna
    def setSalario(self, salario:int):
        """ Setter para el salario"""
        self.salario = salario
        
    def getSalario(self):
        """ Getter para el salario"""
        try:
            return self.salario
        except:
            return f'No se establecio sueldo para el empleado indicado'
    
@dataclass
class Programador(Empleado):
    """ Constructor que recibe nombre, heredado de persona y lenguaje."""
    lenguaje:str
    def setProyecto(self, proyecto:str):
        """" Define proyecto para el programador"""
        self.proyecto = proyecto

    def getProgramador(self):
        """ Devuelve el lenguaje y el proyecto del programador"""
        try:
            return f'Lenguaje: {self.lenguaje.title()}\nProyecto: {self.proyecto.title()}'
        except:
            return 'Faltan asignación de proyecto para devolver los datos del programador'

@dataclass
class Empresa:
    # Al colocarlos asi en dataclass ya los declara como atributos de la clase
    listaProyectos = ["Web Pollitos", "Sistema Gallina SRL"]
    listaLenguajes = ["Python", "JavaScript", "C#", "HTML & CSS"]
    listaProgramadores = []
    nombreEmpresa:str
    rubro:str
    
    # fin constructor
    
    def getNombreEmpresa(self):
        """ Getter nombre empresa"""
        return self.nombreEmpresa

    def setNombreEmpresa(self, newName:str):
        """ Setter nombre empresa """
        self.nombreEmpresa = newName
        
    def getRubro(self):
        """ Getter nombre rubro"""
        return self.rubro
    
    def setRubro(self, newRubro):
        """ Setter nombre rubro"""
        self.rubro = newRubro
    
            
    def getProyectos(self):
        """ Getter para los proyectos"""
        return self.listaProyectos

    
    def agEmp(self):    
        """ Agrega empleado a la empresa """
        while True:
            # Establecer lenguaje del programador
            lenguajeManejado = input('Que lenguaje maneja el programador?: ')
            if lenguajeManejado not in self.listaLenguajes:
                print('No cumple con los lenguajes de la empresa, los solicitados son los siguientes: ')
                for l in self.listaLenguajes:
                    print(l)
                break
            else:
                # Establecer nombre del programador
                nombreEmpleado = input('Ingrese el nombre del empleado: ')
                newProgramador = Programador(nombreEmpleado, lenguajeManejado)
                if lenguajeManejado.lower() == 'python':
                    newProgramador.setSalario(175000)
                else:
                    newProgramador.setSalario(110000)
                # Printea proyectos disponibles
                for i,p in enumerate(self.getProyectos()):
                    print(f'{i} - {p}')
                proyecto = vInt('Ingrese el proyecto al que desea incorporar al programador: ',0,len(self.listaProyectos) - 1)
                newProgramador.setProyecto(self.listaProyectos[proyecto])
                self.listaProgramadores.append(newProgramador)
                break                

    
    def mostrarTodo(self):
        """Devuelve nombre de la firma, rubro y cada uno de los empleados"""
        print(f'Bienvenido a {self.getNombreEmpresa()}')
        print(f'Nuestro rubro: {self.getRubro()}')
        if len(self.listaProgramadores) >= 1:
            for i,e in enumerate(self.listaProgramadores):
                print(f'Programador {i}:')
                print(e.getName())
                print(e.getSalario())
                print(e.getProgramador())
        else:
            print('No hay empleados cargados en la empresa todavia')
    
                        
                     

if __name__ == '__main__':
    techcess = Empresa('Techcess','Informatica')
    # techcess.agEmp()
    techcess.mostrarTodo()
        