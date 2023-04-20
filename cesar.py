#blco de apresentação
print("*"*4,"Cifra de cesar","*"*4)
print("*"*44)

#bloco de entradas
alfabeto=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

pal=input("Entre com uma palavra com apenas letras do alfabeto\t")
while not pal.isalpha():
    pal=input("Erro, caracteres não permitidos detectado, entre com uma nova frase\t")

key=int(input("entre com uma chave\t"))
x=0
frase=""
frse=""
for i in pal:
    while i != alfabeto[x]:
        x=x+1
    i=alfabeto[x+key]
    frase=frase+i
    x=0


for i in frase:
    while i != alfabeto[x]:
        x=x+1
    i=alfabeto[x-key]
    frse=frse+i
    x=0

#bloco de saidas
print(pal)
print(frase)
print(frse)