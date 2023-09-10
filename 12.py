class No:
    def __init__(self, valor=None):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
class Arvore_Binaria:
    def __init__(self, valor=None):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def inserir_em_nivel(self, valor):
        if self.valor is None:
            self.valor = valor
        else:
            self._inserir_em_nivel_recursivo(valor, self)

    def _inserir_em_nivel_recursivo(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = Arvore_Binaria(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = Arvore_Binaria(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no_atual.direita)

    def remover_no(self, valor):
        self, _ = self._remover_no_recursivamente(self, valor)

    def _remover_no_recursivamente(self, no_atual, valor):
        if no_atual is None:
            return no_atual, None

        if valor < no_atual.valor:
            no_atual.esquerda, _ = self._remover_no_recursivamente(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita, _ = self._remover_no_recursivamente(no_atual.direita, valor)
        else:
            if no_atual.esquerda is None and no_atual.direita is None:
                no_atual = None
            elif no_atual.esquerda is None:
                no_atual = no_atual.direita
            elif no_atual.direita is None:
                no_atual = no_atual.esquerda
            else:
                sucessor, _ = self._encontrar_minimo_recursivamente(no_atual.direita)
                no_atual.valor = sucessor.valor
                no_atual.direita, _ = self._remover_no_recursivamente(no_atual.direita, sucessor.valor)

        return no_atual, None

    def _encontrar_minimo_recursivamente(self, no_atual):
        while no_atual.esquerda:
            no_atual = no_atual.esquerda
        return no_atual, None

    def mostrar_em_ordem(self):
        valores = []
        self._mostrar_em_ordem_recursiva(self, valores)
        return valores

    def _mostrar_em_ordem_recursiva(self, no_atual, valores):
        if no_atual:
            self._mostrar_em_ordem_recursiva(no_atual.esquerda, valores)
            valores.append(no_atual.valor)
            self._mostrar_em_ordem_recursiva(no_atual.direita, valores)

# Exemplo de uso:
arvore = Arvore_Binaria()
arvore.inserir_em_nivel(10)
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(15)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(12)
arvore.inserir_em_nivel(20)
arvore.inserir_em_nivel(14)

print("Árvore antes da remoção:")
print(arvore.mostrar_em_ordem())

arvore.remover_no(10)

print("Árvore após a remoção:")
print(arvore.mostrar_em_ordem())
