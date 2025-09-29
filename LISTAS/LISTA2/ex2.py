class Viagem:
    def __init__(self, distancia, tempo):
        self.__distancia = distancia
        self.__tempo = tempo

    def set_distancia(self, distancia):
        if distancia <= 0:
            raise ValueError()
        else:
            self.__distancia = distancia

    def set_tempo(self, tempo):
        if tempo <= 0:
            raise ValueError()
        else:
            self.__tempo = tempo

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo
    
    def vel_media(self):
        return self.__distancia / self.__tempo
    
    def dados_viagem(self):
        return f"Distância: {self.__distancia}km - Tempo: {self.__tempo}h\nVelocidade média: {self.vel_media()}km/h"
    
# teste
viagem = Viagem(100, 2)
print(viagem.dados_viagem())