print("*"*6,"Programa de Juros Simples","*"*6)
#entrando com o capital
C=float(input("Entre com o capital"))
#entrando com o numero de meses para pagamento
print("escolha a quantia de meses para pagamento:")
#mostrando as opções de meses para o usuario
print("2 meses\n6 meses\n12 meses\n24 meses\n")
t=int(input())
#fazendo o calculo do juros para o respectivo mês
if t==2:
#caso 2 meses
J=C*0.069*t
elif t==6:
    # caso 6 meses
    J=C*0.0714*t
elif t==12:
    # caso 12 meses
    J=C*0.0921*t
else:
    # caso 24 meses
    J=C*0.1246*t

print("O Valor a ser pago é: ",J+C)

#resultado de usar palavras reservadas como variavel: erro
#resultado se tirar a identação de if: erro