import numpy as np

class Carros:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def pilha_cheia(self):
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False

    def pilha_vazia(self):
        if self.topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.pilha_cheia():
            print("A pilha está cheia !")
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def ver_topo(self):
        if self.topo != -1:
            return self.valores
        else:
            return -1

    def remover_carro(self, valor_placa):
        carros_removidos = []
        contar_carros = 0
        desempilhar = 0
        reiniciar = True
        if self.pilha_vazia():
            return "Estacionamento vazio !"
        else:
            self.topo = 0
            for placa in self.valores:
                encontrar_placa = placa
                if(encontrar_placa == valor_placa):
                    while(reiniciar):
                       self.topo -=1
                       desempilhar = self.valores[self.topo]
                       if(desempilhar != valor_placa):
                            carros_removidos.append(desempilhar)
                            contar_carros += 1
                       else:
                            reiniciar = False
                            print(f"Deverá sair {contar_carros} carro(s), na ordem:")
                            return carros_removidos





carro = Carros(10)
carro.empilhar(1)
carro.empilhar(2)
carro.empilhar(4)
carro.empilhar(3)
carro.empilhar(8)
carro.empilhar(25)
carro.empilhar(26)
carro.empilhar(84)
carro.empilhar(13)
carro.empilhar(7)
print(carro.remover_carro(13))







