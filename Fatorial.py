print('*'*6,'Programa de calculo de fatorial','*'*6)

f=int(input("entre com um numero inteiro: "))
if f>=2:
    for x in range(f+1):
        if x==0:
            t=1
        else:
            t=t*x
else:
    t=1

print("O fatorial de ",f,"é: ",t)