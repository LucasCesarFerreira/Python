#bloco de apresentação
print("*"*6,"Jogo da forca","*"*6)
print("*"*44)
#bloco de entradas
cont=0
sword="jogo divertido"
letras=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
forca=('o','-','|','-','-','<')
sword2=sword.replace(" ","#")
for i in range (25):
    sword2=sword2.replace(letras[i],"_")

print("["+sword2+"]","["+" "*len(forca)+"]")
tent=0
#bloco de processamento
swordl=list(sword2)
while tent!=6:
    x=input("Chute uma letra\t").lower()
    for i in range (len(sword)):
        if sword[i]==x:
            swordl[i]=x
            print(swordl, forca[:tent])

            tent = tent + 1
            print(swordl, forca[:tent])

if tent!=0:
    print(swordl, forca[:tent], "LOST")
else:
    print(swordl, forca[:tent], "WIN!!!!!")

#bloco de saidas