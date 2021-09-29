class Persona:
    def __init__(self,nombre,apellido):
        self.sexo = 'No binario'
        self.nombre = nombre
        self.apellido = apellido
    
    def getSexo(self):
        return self.sexo    

def main():
    tobias = Persona('Tobias', 'Irastorza')
    print(tobias.getSexo())


if __name__ == '__main__':
    main()