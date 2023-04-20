#bloco de apresentação
print("*"*6,"Media de provas","*"*6)
print("*"*42)
#bloco de entradas
nome=input("Entre com o seu nome:\t")
list=[float(input("entre com a nota de uma prova:\t"))]
opc=input("deseja continuar? S/N:\t").upper()
while opc=='S':
    list.append(float(input("nota da prova:\t")))
    opc=input("Deseja continuar? S/N:\t").upper()
#bloco de processamento
media=sum(list)/len(list)
#bloco de saidas
print("Aluno:",nome)
print("Notas do aluno:",list)
list.sort()
print("Notas em ordem crescente:",list)
list.reverse()
print("Notas em ordem decrescente:",list)
print(f"A media das provas é:{media:.2f}")