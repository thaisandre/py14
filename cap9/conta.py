class Conta:

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
        self._saldo += valor

    def saca(self, valor):
        if self._saldo < valor:
            return False
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

if __name__ == '__main__':
    conta1 = Conta('123-4', 'João', 1000.0)
    conta2 = Conta('123-5', 'Maria', 2000.0)

    # imprime o saldo das contas
    print(conta1.saldo)
    print(conta2.saldo)

    # deposita 100.0 na conta1
    conta1.deposita(100.0)

    # saca 100.0 na conta2
    conta2.saca(100.0)

    # transfere 50.0 da conta1 para conta2
    conta1.transfere_para(conta2, 50.0)

    # imprime extrato das contas
    conta1.extrato()
    conta2.extrato()


    