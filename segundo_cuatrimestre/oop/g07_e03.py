class Operacion:
    def __init__(self, *args):
        self.operandos = []
        for e in args:
            self.operandos.append(e)
    
    def getOperandos(self):
        return self.operandos

    def opera(self):
        pass


class Suma(Operacion):
    def __init__(self, *args):
        super().__init__(*args)

    def opera(self):
        result = 0
        for e in self.operandos: # hereda operandos de Operacion
            result += e
        return result

class Promedio(Suma):
    def __init__(self, *args):
        super().__init__(*args)
        self.suma = self.opera() # realiza la suma de los operandos
    
    def getPromedio(self):
        return self.suma / len(self.operandos) # operandos los heredo de operacion, que a su vez los heredo de suma
        
    


if __name__ == '__main__':
    p = Promedio(1,2,3,4,55)
    print(p.getPromedio())
        