#inicio do programa
print("*"*6,"Programa de juros compostos","*"*6)

#entrada de variaveis
C=float(input("Entre com o capital"))
t=int(input("entre com o tempo"))
tot=1
#calculos do programa
if t==2:
    #caso 2 meses
    for i in range(t):
        tot=tot*(1+0.069)
    M = C * tot
elif t==6:
    # caso 6 meses
    for i in range(t):
        tot=tot*(1+0.0714)
    M = C * tot
elif t==12:
    # caso 12 meses
    for i in range(t):
        tot=tot*(1+0.0921)
    M=C*tot
else:
    # caso 24 meses
    for i in range(t):
        tot=tot*(1+0.1246)
    M = C * tot

print("Valor a ser pago: R$",M)