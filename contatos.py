#bloco de apresentação
print("*"*6,"APP Lista de contatos","*"*6)
print("*"*44)

#bloco de entrada do dic
dict={"João":"988992355","Maria":"926765542","Jubiscleiton":"956432231","Jubiscleia":"992263637","Joelson":"999955558"}

#bloco de entradas
opc="S"

x=input("(C)-Criar novo contato\n(V)-Visualizar contatos armazenados\n(E)-Excluir contato\n(L)-Limpar lista de contatos\n(S)-Sair do APP\t").upper()
while x!="C" and x!="V" and x!="E" and x!="L":
    x=input("Opção invalida!\t")
#bloco de saidas
while x!="S":
    if x=="C":
        nome=input("Insira com o nome do contato\t")
        telefone=input("Insira o numero do contato\t")
        dict[nome]=telefone
    elif x=="V":
        for i,j in dict.items():
            print("Nome:"+i+"---Tel:"+j)
    elif x=="E":
        del dict[input("Digite o contato que deseja que seja excluido\t")]
    else :#esse aqui é a função L
        dict.clear()

    x=input("(C)-Criar novo contato\n(V)-Visualizar contatos armazenados\n(E)-Excluir conta\n(L)-Limpar lista de contatos\n(S)-Sair do APP\t").upper()

print("Saindo do APP")