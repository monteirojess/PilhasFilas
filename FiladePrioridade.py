import numpy as np

class FilaPrioridade:
    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.qtd_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.qtd_elementos == 0

    def __fila_cheia(self):
        return self.qtd_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('Fila cheia')
            return

        if self.qtd_elementos == 0:
            self.valores[self.qtd_elementos] = valor
            self.qtd_elementos += 1

        else:
            num = self.qtd_elementos -1
            while num >= 0:
                if valor > self.valores[num]:
                    self.valores[num+1] = self.valores[num]
                else:
                    break
                num-=1
            self.valores[num+1]=valor
            self.qtd_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('Fila vazia')
            return
        valor=self.valores[self.qtd_elementos -1]
        self.qtd_elementos -1
        return valor

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.qtd_elementos -1]

fila = FilaPrioridade(3)
fila.enfileirar(7)
fila.primeiro()
fila.enfileirar(13)
fila.primeiro()
fila.enfileirar(58)
fila.primeiro()
print(fila.desenfileirar())
print(fila.primeiro())