class Carro:
    def __init__(self, nome):
        self.nome = nome

    def showCar(self):
        print(f'O seu carro é o {self.nome}')



c1 = Carro('Fusca')
c2 = Carro('Uno')
c1.showCar()