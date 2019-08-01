class ManipuladorDeTributaveis:

    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()

        return total


if __name__ == '__main__':
    from conta import ContaCorrente, SeguroDeVida, TributavelMixIn

    #cria duas contas correntes
    cc1 = ContaCorrente('123-4', 'João', 1000.0)
    cc2 = ContaCorrente('123-5', 'João', 1000.0)

    # cria dois seguros de vida
    seguro1 = SeguroDeVida(100.0, 'Carlos', '345-77')
    seguro2 = SeguroDeVida(200.0, 'Maria', '237-98')

    # cria lista de tributaveis
    lista_tributaveis = []

    # adiciona objetos tributaveis na lista
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)

    # instância um ManipuladorDeTributaveis
    manipulador = ManipuladorDeTributaveis()

    # chama o metodo calcula_impostos do manipulador passando a lista de tributáveis
    total = manipulador.calcula_impostos(lista_tributaveis)

    # imprime o total de impostos calculado pelo manipulador
    print(total)