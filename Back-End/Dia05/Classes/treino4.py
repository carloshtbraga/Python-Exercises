class Camera:
    def __init__(self,nome, filmando = False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if (self.filmando):
           return print(f'A camera da {self.nome} já está filmando')           
        self.filmando = True
        print(f'A sua camera da {self.nome} está filmando a partir de agora')

c1 = Camera('Sony')
c1.filmar()
c1.filmar()
