# bloco d apresentacao
print("*" * 4, "Fat recursivo", "*" * 4)
print("*" * 44)


# bloco d entrada
def fat(a,b):
    if a>1:
        b=b*a
        return fat(a-1,b)
    return b

x = int(input("Entre com um numero para fazer o fatorial\t"))
# bloco d saida
print(fat(x,1))
