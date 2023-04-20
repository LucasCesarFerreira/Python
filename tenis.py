#bloco de apresentação
print("*"*10,"Jogo de tenis","*"*10)
print("*"*40)

#bloco de função
def JogF():
    Print("Rodada de empate!")
    e1=0
    e2=0
    while e1<2 or e2<2:
        x = int(input("Quem marcou ponto? Jogador 1 ou 2\t"))
        if x==1:
            e1=e1+1
            e2=0
        else:
            e2 = e2 + 1
            e1 = 0
    if e1==2:
        return 1
    else:
        return 2

#bloco de entradas
jog1=input("Entre com o nome do jogador 1\t")
jog2=input("Entre com o nome do jogador 2\t")
j1=0
j2=0

vit1=False
vit2=False
res=0


while vit1==False or vit2==False:
    if j1==45 or j2==45:
        if j1==45 and j2<=30:
            x = int(input("Quem marcou ponto? Jogador 1 ou 2\t"))
            if x==1:
                vit1=True
            else:
                res=JogF()
        elif j2==45 and j1<=30:
            x = int(input("Quem marcou ponto? Jogador 1 ou 2\t"))
            if x==2:
                vit2=True
            else:
                res=JogF()
        else:
            res=JogF()

        if res==1:
            vit1==True
        else:
            vit2==True

    else:
        x = int(input("Quem marcou ponto? Jogador 1 ou 2\t"))
        if x==1:
            j1=j1+15
            print(jog1+"marcou um ponto!\nPontuação:"+jog1+":",j1,"---"+jog2+":",j2)
        else:
            j2 = j2 + 15
            print(jog2 + "marcou um ponto!\nPontuação:" + jog1 + ":", j1 , "---" + jog2 + ":" , j2)


if vit1==True:
    Print("Jogador1 Venceu!!!")
else:
    Print("Jogador2 Venceu!!!")



