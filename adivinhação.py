#bloco de apresentação
print("*"*6,"Jogo de adivinhação","*"*6)

x=69
t=0
#bloco de recebimento de dados
i=int(input("tente acertar o valor do numero secreto entre 1 e 100:\t"))
while i<1 or i>100:
    i=int(input("VALOR INVALIDO! Entre com um novo valor:\t"))
#bloco de processamento
while i!=x:
    t+=1
    if t>0 and t!=3:
        print(t,"de 3 tentativas usadas! restam",3-t,"tentativas")
    if t==3:
        print("Todas as tentativas foram usadas! você perdeu")
        break
    if i<x:
        print("maior")
    else:
        print("menor")
    i=int(input("entre com um novo valor"))

#bloco de saida de dados
if i==x:
    print("Acertou!")