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


    def mostrar_pos_ordem(self):
        valores = []
        if self.raiz is None:
            print('A árvore está vazia!')
        else:
            self._mostrar_pos_ordem_recursiva(self.raiz, valores)
        return valores

    def _mostrar_pos_ordem_recursiva(self, no, valores):
        if no is not None:
            self._mostrar_pos_ordem_recursiva(no.esquerda, valores)
            self._mostrar_pos_ordem_recursiva(no.direita, valores)
            valores.append(no.valor)

# Exemplo de uso:
arvore = Arvore_Binaria()
arvore.inserir_em_nivel(50)
arvore.inserir_em_nivel(30)
arvore.inserir_em_nivel(70)
arvore.inserir_em_nivel(20)
arvore.inserir_em_nivel(40)
arvore.inserir_em_nivel(60)
arvore.inserir_em_nivel(80)

valores_pos_ordem = arvore.mostrar_pos_ordem()
print("\nValores Pós-Ordem")
print(valores_pos_ordem)
    

