import abc
from tributavel import Tributavel
from erros import SaldoInsuficienteError

class Conta(abc.ABC):

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def titular(self):
        return self._titular.capitalize()

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    def deposita(self, valor):
        if(valor < 0):
            raise ValueError('Você tentou depositar um valor negativo')
        else:
            self._saldo += valor

    def saca(self, valor):
        if valor < 0:
            raise ValueError('Você tentou sacar um valor negativo')
        if self._saldo < valor:
            raise SaldoInsuficienteError('Saldo insuficiente')
        else:
            self._saldo -= valor

    def extrato(self):
        print('número: {}\nsaldo: {}'.format(self._numero, self._saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if(retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True

    @abc.abstractmethod
    def atualiza(self, taxa):
        pass

    def __str__(self):
        return 'Conta[{}, {}, {}, {}]'.format(self._numero, self._titular, self._saldo, self._limite)


class ContaCorrente(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def get_valor_imposto(self):
        return self._saldo * 0.01


class ContaPoupanca(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3

    def deposita(self, valor):
        if(valor < 0):
            raise ValueError('Você tentou depositar um valor negativo')
        else:
            self._saldo += valor - 0.10


class ContaInvestimento(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5

class SeguroDeVida():

    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 42 + self._valor * 0.05


if __name__ == '__main__':
    cc = ContaCorrente('123-5', 'José', 1000.0)

    valor = -1000.0
    #valor = 5000.0

    try:
        cc.saca(valor)
        print('Saque de {} realizado com sucesso'.format(valor))
    except ValueError:
        print('O valor a ser sacado deve ser um número positivo')
    except SaldoInsuficienteError:
        print('Você não possui saldo suficiente para concluir esta operação.')