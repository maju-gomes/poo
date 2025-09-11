class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calc_area(self):
        return self.base * self.altura
    
    def calc_diagonal(self):
        return (self.base ** 2 + self.altura ** 2) ** 0.5
    
    def __str__(self):
        return f"Base: {self.base}\nAltura: {self.altura}\nÁrea: {self.calc_area()}\nDiagonal: {self.calc_diagonal()}"