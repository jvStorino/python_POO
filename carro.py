class Carro:
    def __init__(self, nome):
        self.nome = nome 
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self.fabricante
    
    fabricante.setter
    def fabricante(self, valor):
        self.fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

mustang = Carro('Mustang')
coyote_50 = Motor('Coyote 5.0')
ford = Fabricante('Ford')
mustang.motor = coyote_50
mustang.fabricante = ford

print(mustang.nome, mustang.motor.nome, mustang.fabricante.nome, sep='\n')