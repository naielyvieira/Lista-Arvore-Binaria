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

    def encontrar_filhos_do_no(self, valor_alvo):
        no_alvo = self.encontrar_no(valor_alvo)
        if no_alvo:
            filhos = []
            if no_alvo.esquerda:
                filhos.append(no_alvo.esquerda.valor)
            if no_alvo.direita:
                filhos.append(no_alvo.direita.valor)
            return filhos
        else:
            return None

    def encontrar_no(self, valor_alvo):
        return self._encontrar_no_recursivamente(self, valor_alvo)

    def _encontrar_no_recursivamente(self, no_atual, valor_alvo):
        if no_atual is None:
            return None

        if no_atual.valor == valor_alvo:
            return no_atual

        if valor_alvo < no_atual.valor:
            return self._encontrar_no_recursivamente(no_atual.esquerda, valor_alvo)
        else:
            return self._encontrar_no_recursivamente(no_atual.direita, valor_alvo)

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

valor_alvo = 12
filhos = arvore.encontrar_filhos_do_no(valor_alvo)

print(f"Filhos do nó {valor_alvo}: {filhos}")  # Isso imprimirá os filhos do nó com o valor.
