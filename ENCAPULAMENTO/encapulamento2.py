class Triangulo:
    def __init__(self):
        self.__base = 0
        self.__altura = 0

    def calcular_area(self):
        return self.__base * self.__altura / 2

    # GETTERS E SETTERS
    def set_base(self, base):
        if base <= 0:
            raise ValueError()
        else:
            self.__base = base
    def set_altura(self, altura):
        if altura <= 0:
            raise ValueError()
        else:
            self.__altura = altura

    def get_base(self):
        return self.__base
    def get_altura(self):
        return self.__altura
    
# User Interface    
class TrianguloUI:
    @staticmethod
    def main():
        triangulo1 = Triangulo()
        triangulo2 = Triangulo()

        print(id(triangulo1))
        print(id(triangulo2))
    
TrianguloUI.main()