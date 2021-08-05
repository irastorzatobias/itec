class Perro:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def saludo(self):
        return f'Hola, soy {self.name}'
        
luna = Perro("Luna",4)

print(luna.saludo())