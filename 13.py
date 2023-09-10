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

    def encontrar_nos_no_nivel(self, nivel_desejado):
        return self._encontrar_nos_no_nivel_recursivamente(self, nivel_desejado)

    def _encontrar_nos_no_nivel_recursivamente(self, no_atual, nivel_atual):
        if no_atual is None:
            return []

        if nivel_atual == 0:
            return [no_atual.valor]

        nos_no_nivel_esquerdo = self._encontrar_nos_no_nivel_recursivamente(no_atual.esquerda, nivel_atual - 1)
        nos_no_nivel_direito = self._encontrar_nos_no_nivel_recursivamente(no_atual.direita, nivel_atual - 1)

        return nos_no_nivel_esquerdo + nos_no_nivel_direito

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

nivel_desejado = 0# Nível desejado (a raiz está no nível 0)
nos_no_nivel = arvore.encontrar_nos_no_nivel(nivel_desejado)

print(f"Nós no nível {nivel_desejado}: {nos_no_nivel}")
