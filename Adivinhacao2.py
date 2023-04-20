print("*"*6,"Jogo de adivinhação","*"*6)

x=57

i=int(input("tente acertar o valor do numero secreto entre 1 e 100"))
while i!=x:
    if i<x:
        print("maior")
    else:
        print("menor")
    i=int(input("entre com um novo valor"))

print("Acertou!")