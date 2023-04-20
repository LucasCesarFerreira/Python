#bloco de apresentação
print("*"*6,"APP Lista de contatos","*"*6)
print("*"*44)

#bloco de entrada do dic
dict={"João":"988992355","Maria":"926765542","Jubiscleiton":"956432231","Jubiscleia":"992263637","Joelson":"999955558"}
arq=open("contatos.txt","a")

for i,j in dict.items():
    arq.writelines(i)
    arq.writelines("\n")
    arq.writelines(j)
    arq.writelines("\n")

arq.close()
#bloco de entradas
opc="S"
extra=0
y=0
x=input("(C)-Criar novo contato\n(V)-Visualizar contatos armazenados\n(E)-Excluir contato\n(L)-Limpar lista de contatos\n(B)-restaurar lista de contatos\n(S)-Sair do APP\t").upper()
while x!="C" and x!="V" and x!="E" and x!="L":
    x=input("Opção invalida!\t")


#bloco de saidas
while x!="S":
    if x=="C":
        nome=input("Insira com o nome do contato\t")
        telefone=input("Insira o numero do contato\t")
        dict[nome]=telefone
        arq = open("contatos.txt", "a")
        arq.writelines(nome)
        arq.writelines("\n")
        arq.writelines(telefone)
        arq.writelines("\n")
        arq.close()

    elif x=="V":
        if extra==0:
            for i,j in dict.items():
                print("Nome:"+i+"\n"+"Tel:"+j+"\n"+"*"*30)
        else:
            for i in dict:
                str=i[:-1]
                if y%2==0:
                    print("Nome:"+str)
                    y=y+1
                else:
                    print("Tel:" + str+"\n"+"*"*20)
                    y=y+1
    elif x=="E":
        del dict[input("Digite o contato que deseja que seja excluido\t")]
    elif x=="L" :
        dict.clear()
    elif x=="B":
        extra=1
        arq = open("contatos.txt", "r")
        dict=arq.readlines()



    x=input("(C)-Criar novo contato\n(V)-Visualizar contatos armazenados\n(E)-Excluir conta\n(L)-Limpar lista de contatos\n(B)-restaurar lista de contatos\n(S)-Sair do APP\t").upper()

print("Saindo do APP")