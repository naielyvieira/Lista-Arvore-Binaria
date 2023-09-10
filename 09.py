class No:
    def __init__(self, valor=None):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore_Binaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_em_nivel_recursivo(valor, self.raiz)

    def _inserir_em_nivel_recursivo(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no_atual.direita)

    def buscar(self, valor):
        return self._buscar_recursivamente(self.raiz, valor)

    def _buscar_recursivamente(self, no_atual, valor):
        if no_atual is None:
            return False

        if valor == no_atual.valor:
            return True
        elif valor < no_atual.valor:
            return self._buscar_recursivamente(no_atual.esquerda, valor)
        else:
            return self._buscar_recursivamente(no_atual.direita, valor)

    def altura(self):
        return self._calcular_altura(self.raiz)

    def _calcular_altura(self, no_atual):
        if no_atual is None:
            return 0

        altura_esquerda = self._calcular_altura(no_atual.esquerda)
        altura_direita = self._calcular_altura(no_atual.direita)

        return max(altura_esquerda, altura_direita) + 1

    def contar_nos(self):
        if self.raiz is None:
            return 0
        else:
            return self._contar_nos_recursivamente(self.raiz)

    def _contar_nos_recursivamente(self, no_atual):
        if no_atual is None:
            return 0

        # Conte o nó atual e continue contando nas subárvores esquerda e direita
        return 1 + self._contar_nos_recursivamente(no_atual.esquerda) + self._contar_nos_recursivamente(no_atual.direita)

# Exemplo de uso:
arvore = Arvore_Binaria()
arvore.inserir_em_nivel(50)
arvore.inserir_em_nivel(30)
arvore.inserir_em_nivel(70)
arvore.inserir_em_nivel(20)
arvore.inserir_em_nivel(40)
arvore.inserir_em_nivel(60)
arvore.inserir_em_nivel(80)

total_de_nos = arvore.contar_nos()
print(total_de_nos)
