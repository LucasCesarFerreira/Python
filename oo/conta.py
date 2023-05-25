class Conta:

    def __init__(self, numero, titular, saldo, limite):#Construtor
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titulo = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):#Mostrar o saldo de determinado cliente
        print("O saldo de R${} é do titular {}".format(self.__saldo, self.__titulo))

    def deposita(self, valor): #colocar dinheiro na conta
        self.__saldo += valor

    def __pode_sacar(self, valor):#verifica se o cliente pode sacar a quantia desejada
        valor_disponivel = (self.__saldo + self.__limite)
        return valor <= valor_disponivel

    def saca(self, valor): #saca o valor desejado
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino): # transferencia de dinheiro entre clientes
        if (self.__pode_sacar(valor)):
            self.saca(valor)
            destino.deposita(valor)
        else:
            print("Saldo insuficiente para transferencia")

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titulo

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
