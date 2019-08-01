from conta import Conta, ContaCorrente, ContaPoupanca

class AtualizadorDeContas:

    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    @property
    def saldo_total(self):
        return self._saldo_total   

    def roda(self, conta):
        #imprime o saldo atual
        print('saldo anterior: {}'.format(conta.saldo))
        
        #atualiza a conta com taxa selic
        conta.atualiza(self._selic)

        # imprime o saldo final
        print('saldo atualizado: {}'.format(conta.saldo))

        #soma o saldo final ao atributo saldo_total
        self._saldo_total += conta.saldo
        

if __name__ == '__main__':
    #c = Conta('123-4', 'Joao', 1000.0)
    cc = ContaCorrente('123-5', 'José', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)

    adc = AtualizadorDeContas(0.01)

    #adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)

    print('Saldo total: {}'.format(adc.saldo_total))