import math

class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    def set_raio(self, raio):
        if raio <= 0:
            raise ValueError()
        else:
            self.__raio = raio
        
    def get_raio(self):
        return self.__raio
    
    def calcular_area(self):
        return math.pi * self.__raio **2

    def calcular_circunferencia(self):
        return 2 * math.pi * self.__raio
    
# teste
circulo = Circulo(4)

print(circulo.calcular_area())
print(circulo.calcular_circunferencia())

    