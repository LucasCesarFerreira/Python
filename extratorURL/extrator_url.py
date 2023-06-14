import main
# https://bytebank.com/cambio?moedaOrigem=Real&quantidade=100&moedaDestino=Dolar
url = input("Entre com a url desejada: ")
extrator = main.ExtratorURL(url)
param = input("Entre com o parametro que deseja o valor: ")
valor_quant = extrator.get_parametro(param)
print(valor_quant)
