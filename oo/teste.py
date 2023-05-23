
def cria_conta(numero ,titular ,saldo ,limite):
    conta ={"Número" :numero ,"Titular" :titular ,"Saldo" :saldo, "Limite" : limite }
    return conta


def deposita(conta,valor):
    conta["Saldo"] += valor
    return conta


def saca(conta,valor):
    conta["Saldo"] -= valor
    return conta


def extrato(conta):
    print("O saldo é {}".format(conta["Saldo"]))
"""
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatdata(self):
        print("{}/{}/{}".format(self.dia,self.mes,self.ano))
        
"""