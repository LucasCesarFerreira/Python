print("*"*6+"Programa de maquina de vendas"+"*"*6)
#declarando as portas
porta1='vazio'
porta2=0.00

#imprimindo as opções bebidas e seus valores
print("Valores das bebidas: ")
print("1-Coca Cola (R$3.75)\n2-Mata Leão (R$2.45)\n3-Guaraná Antártica (R$3.55)\n4-Citrus Schweppes (R$3.15)\n5-Garrafa de Água (R$1.35)\n6-Long neck Spaten (R$5.75)\n7-Long neck Stella (R$5.85)\n8-Long neck Heineken (R$6.50)")
#entrando com a opção de bebida desejada
Opc=int(input("escolha o numero da bebida desejada:\n"))
if Opc==1:
    print("Valor a ser pago: R&3.75")
    deve=3.75
    bebida='Coca Cola'
else:
    if Opc==2:
        print("Valor a ser pago: R&2.45")
        deve=2.45
        bebida='Mata Leão'
    else:
        if Opc==3:
            print("Valor a ser pago: R&3.55")
            deve=3.55
            bebida='Guaraná Antártica'
        else:
            if Opc==4:
                print("Valor a ser pago: R&3.15")
                deve=3.15
                bebida='Citrus Schweppes'
            else:
                if Opc==5:
                    print("Valor a ser pago: R&1.35")
                    deve=1.35
                    bebida='Garrafa de Água'
                else:
                    if Opc==6:
                        print("Valor a ser pago: R&5.75")
                        deve=5.75
                        bebida='Long neck Spaten'
                    else:
                        if Opc==7:
                            print("Valor a ser pago: R&5.85")
                            deve=5.85
                            bebida='Long neck Stella'
                        else:
                            if Opc==8:
                                print("Valor a ser pago: R&6.50")
                                deve=6.50
                                bebida='Long neck Heineken'

#gaveta para a entrada do dinheiro
gaveta=float(input("Entre com o dinheiro: \n"))

#casos dos possiveis dinheiros creditados
if gaveta==deve:
    #exato dinheiro da bebida
    porta1=bebida
    porta2=0.00
else:
    if gaveta<deve:
        #menos dinheiro do que deve
        porta2=gaveta
    else:
        #mais dinheiro que deve
        porta1=bebida
        porta2=gaveta-deve

print("Porta1: "+porta1+'\nPorta2: R$',porta2)
