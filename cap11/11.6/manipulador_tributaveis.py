from tributavel import Tributavel

class ManipuladorDeTributaveis:

    def calcula_impostos(self, lista_tributaveis):
        total = 0

        for t in lista_tributaveis:
            if(isinstance(t, Tributavel)):
                total += t.get_valor_imposto()
            else:
                print(t.__repr__(), 'não é um tributável')

        return total


if __name__ == '__main__':
    from conta import ContaCorrente, SeguroDeVida

    cc = ContaCorrente('123-4', 'João', 1000.0)
    seguro = SeguroDeVida(100.0, 'José', '345-67')

    # imprime valores dos impostos
    print(cc.get_valor_imposto())
    print(seguro.get_valor_imposto())

    # cria lista de tributáveis vazia
    lista_tributaveis = []

    # registra ContaCorrente e SeguroDeVida como Tributavel
    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroDeVida)

    # adiciona objetos tributáveis na lista
    lista_tributaveis.append(cc)
    lista_tributaveis.append(seguro)

    # instância um manipulador de tributáveis
    mt = ManipuladorDeTributaveis()

    # calcula total de impostos da lista de tributáveis
    total = mt.calcula_impostos(lista_tributaveis)

    # imprime total dos impostos
    print(total)