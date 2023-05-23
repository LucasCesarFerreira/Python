class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.numero = numero
        self.titulo = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O saldo de R${} é do titular {}".format(self.saldo, self.titulo))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor