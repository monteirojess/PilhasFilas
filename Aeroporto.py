import numpy as np

class Aeroporto:
    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.comeco = 0
        self.fim = -1
        self. qtd_aeronaves = 0
        self.aeronaves = np.empty(self.capacidade, dtype=int)
        self.ident_letra = np.chararray(self.capacidade, itemsize=3, unicode=True)
        self.numeracao = np.chararray(self.capacidade, itemsize=4, unicode=True)

    def __fila_vazia(self):
        return self.qtd_aeronaves == 0

    def __pista_ocupada(self):
        return self.qtd_aeronaves == self.capacidade

    def fila_decolagem(self, aeronaves, ident_letra:str, numeracao):
        if self.__pista_ocupada():
            print('Aeronave na pista!')

        if self.fim == self.capacidade -1:
            self.fim = -1
        self.fim += 1
        self.aeronaves[self.fim] = aeronaves
        self.ident_letra[self.fim] = ident_letra
        self.numeracao[self.fim] = numeracao
        self.qtd_aeronaves += 1

    def pista_vazia(self):
        if self.__fila_vazia():
            print('Pista de decolagem vazia')
        else:
            temp = self.aeronaves[self.comeco]
            self.comeco += 1
            if self.comeco == self.capacidade -1:
                self.comeco = 0
            else:
                self.qtd_aeronaves -= 1
                return temp

    def num_aeronaves(self):
        if self.__fila_vazia():
           return 'Sem decolagens na sequência'
        else:
            print(f'Total de aeronaves aguardando autorização para decolagem: {self.qtd_aeronaves}')

    def proxima_decolagem(self):
        if self.__fila_vazia():
            print('Pista livre! Decolagem autorizada!')
        else:
            proxima_aeronave = self.aeronaves[self.comeco]
            ident_letra_aeronave = self.ident_letra[self.comeco]
            numeracao_aeronave = self.numeracao[self.comeco]

            print(f'Aeronave {proxima_aeronave}, COD: {ident_letra_aeronave}, de Inscrição {numeracao_aeronave}: Decolagem Autorizada!')

    def listar_aeronaves(self):
        for i in range(len(self.aeronaves)):
            print(f'Aeronaves Aguardando Decolagem:\n Aeronave: {self.aeronaves[i]}\n')

fila = Aeroporto(5)
fila.fila_decolagem(1,'GOL', '4056')
fila.fila_decolagem(2,'AZUL', '1190')
fila.fila_decolagem(3,'LATAM', '5576')
fila.fila_decolagem(4,'VASP', '2101')
fila.fila_decolagem(5,'VARIG', '7823')
fila.num_aeronaves()
fila.proxima_decolagem()
fila.listar_aeronaves()
fila.pista_vazia()
fila.num_aeronaves()
