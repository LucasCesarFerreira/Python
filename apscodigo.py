#Bloco de apresentação
print("*"*10,"Programa de Criptografia","*"*10)
print("*"*46)
#Bloco de funções
def matriz (a):
    b = a.replace(" ","")
    b = b.replace(",", "")
    b = b.replace("[", "")
    b = b.replace("]", "")
    b = b.replace("'", "")
    lmsg = list(b)
    if (len(lmsg)%8)==0:
        linha = len(lmsg)//8
    else:
        linha = 1+(len(lmsg)//8)
    k = 0
    cmsg = []
    for m in range(linha):
        cmsg.append([0]*8)
    for i in range(linha):
        for j in range(8):
            if k < (len(lmsg)):
                cmsg[i][j] = lmsg[k]
            else:
                cmsg[i][j] = "*"
            k = k + 1
    return cmsg

def cripto(a):
    linha = len(a)
    c = []
    for m in range(linha):
        c.append([0] * 8)
   #origin - 0,1,2,3,4,5,6,7
    chavec = 1,0,2,7,3,6,4,5
    for i in range(linha):
        for j in range(8):
            k = chavec[j]
            c[i][j] = a[i][k]
    return c

def descripto(a):
    #msg: roaetoor aurd oaupr oeoird eam*****
    linha = len(a)
    c = []
    for m in range(linha):
        c.append([0] * 8)
   #origin - 0,1,2,3,4,5,6,7
   #chavec = 1,0,2,7,3,6,4,5
    chaved = 1,0,2,4,6,7,5,3
    for i in range(linha):
        for j in range(8):
            k = chaved[j]
            c[i][j] = a[i][k]
    return c

def limpar(a):
    lmsg = str(a)
    lmsg = lmsg.replace("[", "")
    lmsg = lmsg.replace("]", "")
    lmsg = lmsg.replace(",", "")
    lmsg = lmsg.replace("'", "")
    lmsg = lmsg.replace(" ", "")
    lmsg = lmsg.replace("*", "")
    b = str(lmsg)
    return b

#Bloco de processamento
op = 'm'
while op!="e":
    op=input("Escolha uma opção:\nC-Criptografe uma mensagem\nD-Descriptografe uma mensagem\nE-Sair\n"+"*"*46+"\n").lower()
    if op == "c":
        msg=input("*"*46+"\nDigite a mensagem a ser criptografada:\n").lower()
        while len(msg) > 128:
            print("\n!!!Mensagem excedeu 128 caracteres!!!\n")
            msg = input("*"*46+"\nDigite a mensagem a ser criptografada:\n").lower()
        saida = cripto(matriz(msg))
        print("*"*46+"\nMensagem criptografada:")
        print(limpar(saida)+"\n"+"*"*46)
    elif op == "d":
        dmsg = input("*"*46+"\nEntre com uma mensagem para descriptografar:\n").lower()
        while len(dmsg) > 128:
            print("\n!!!Mensagem excedeu 128 caracteres!!!\n")
            dmsg = input("*"*46+"\nEntre com uma mensagem para descriptografar:\n").lower()
        saida = descripto(matriz(dmsg))
        print("*"*46+"\nMensagem descriptografada:")
        print(limpar(saida)+"\n"+"*"*46)
    elif op == "e":
        print("Encerrando o programa...")
    else:
        print("Opção invalida, selecione uma opção abaixo:\t")