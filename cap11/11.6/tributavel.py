import abc

class Tributavel(abc.ABC):
    """Classe que contém operações de um objeto tributável

    As subclasses concretas devem sobrescrever o método get_valor_imposto
    """

    @abc.abstractmethod
    def get_valor_imposto(self):
        """
        aplica taxa de imposto sobre um determinado valor do objeto
        :return valor do imposto (float)
        """
        pass


if __name__ == '__main__':
    help(Tributavel)