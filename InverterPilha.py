import numpy as np

class InverterPilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __pilha_cheia(self):
      if self.__topo == self.__capacidade -1:
          return True
      else:
          return False

    def __pilha_vazia(self):
      if self.__topo == -1:
          return True
      else:
          return False

    def empilhar(self,valor):
      if self.__pilha_cheia():
          print('A pilha está cheia')
      else:
          self.__topo += 1
          self.__valores[self.__topo] = valor

    def desempilhar(self):
      if self.__pilha_vazia():
          print('A pilha está vazia')
      else:
          self.__topo -= 1

    def ver_topo(self):
      if self.__topo != -1:
          return self.__valores[self.__topo]
      else:
          return -1

    def inverso(self):
        for i in self.__valores:
            if self.__topo == -1:
                print('Pilha vazia')
            else:
                pilha_invertida = self.__valores[::-1]
        return pilha_invertida


pilha = InverterPilha(5)
pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(55)
pilha.empilhar(45)
pilha.empilhar(52)
print(pilha.inverso())