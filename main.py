#bloco de apresentação
print("*"*6+"Programa de cadastro de clientes"+"*"*6)
print("*"*44)
#bloco de entradas
nome=input("Entre com o nome do usuario\t")
CPF=input("Entre com o CPF do usuario\t")
while CPF.isnumeric()==False:
    CPF=input("CPF invalido! Digite novamente\n")
RG=input("Entre com o RG do usuario\t")
while RG.isnumeric()==False:
    RG=input("RG invalido! Digite novamente\n")
sexo=input("Entre como o sexo(M/F) do usuario\t").upper()
while sexo!='M' and sexo!='F':
    sexo=input("opção invalida! Entre corretamento como o sexo(M/F)\t")
idade=int(input("Entre com a idade do usuario\t"))

#bloco de processamento
if sexo=='M':
    ano_aposenta=idade+65
else:
    ano_aposenta=idade+60
#bloco de saidas
print("*"*6+"Dados recebidos"+"*"*6)
print("Nome do Usuario: ",nome)
print("CPF do Usuario: ",CPF[0:3]+"."+CPF[3:6]+"."+CPF[6:9]+"-"+CPF[9: ])
print("RG do Usuario: ",RG[0:2]+"."+RG[2:5]+"."+RG[5:8]+"-"+RG[8])
print("Sexo do Usuario: ",sexo)
print("Idade do Usuario: ",idade)
print("Idade de aposentadoria do Usuario: ",ano_aposenta)