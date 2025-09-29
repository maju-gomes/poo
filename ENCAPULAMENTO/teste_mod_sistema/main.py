class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura / 2
    
class TrianguloUI:
    @staticmethod
    def main():
        obj_triangulo = Triangulo(20, 10)
        print(obj_triangulo.calcular_area())
    
TrianguloUI.main()