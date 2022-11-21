import numpy as np

class VetorPilha:
    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype =int)

    def adicionar(self,vetor):
        self.vetor = vetor
        print(self.vetor )

    def criar_pilha(self):
        tamanho_vetor = self.capacidade
        tamanho_pilha = 0
        continuar = True
        while (continuar):
            for i in self.vetor:
                self.topo += 1
                tamanho_pilha += 1
                temporaria = i
                self.valores[self.topo] = temporaria
                if (tamanho_pilha == tamanho_vetor):
                    continuar = False
            return self.valores






array = VetorPilha(4)
array.adicionar([1,2,3,4])
print(array.criar_pilha())



