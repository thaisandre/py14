from erros import SaldoInsuficienteError
from conta import ContaCorrente

class CaixaEletronico:

    def saca(self, conta, valor):
        try:
            conta.saca(valor)
            print('Saque de {} realizado com sucesso.'.format(valor))
        except ValueError:
            print('O valor a ser sacado deve ser um número positivo.')
        except SaldoInsuficienteError:
            print('Você não possui saldo suficiente para concluir esta operação.')

    def deposita(self, conta, valor):
        try:
            conta.deposita(valor)
            print('Depósito de {} realizado com sucesso.'.format(valor))
        except ValueError:
            print('Você tentou depositar um valor negativo.')

if __name__ == '__main__':
    caixa = CaixaEletronico()

    cc = ContaCorrente('123-5', 'José', 1000.0)

    # testes com saque
    caixa.saca(cc, 100.0) # valor ok
    caixa.saca(cc, -100.0) # valor negativo
    caixa.saca(cc, 100000000.0) # valor superior ao saldo

    # testes com depósito
    caixa.deposita(cc, 100.0) # valor ok
    caixa.deposita(cc, -100.0) # valor negativo