#bloco de apresentação
print("*"*6+"Programa de login app"+"*"*6)
print("*"*44)
#bloco de entradas
usuario=input("Entre com o usuario a ser cadastrado\t")
while not (usuario.isalnum()) or usuario[0].isnumeric():
    usuario=input("Usuario invalido! tente novamente\t")
print("Usuario cadastrado com sucesso!")
senha=input("crie uma senha\t")
while len(senha)<8 or senha.isalnum():
    senha=input("senha invalida! tente novamente\t")
print("Senha cadastrada com sucesso!")
#bloco de processamento
usuariolis=list(usuario)
senhalis=list(senha)
login=list(input("Entre com o usuario:\t"))
print("*"*len(senha))
password=list(input("Entre com a senha:\t"))
#bloco de saidas
if login!=usuariolis:
    print("Usuario não cadastrado!")
elif password!=senhalis:
    print("Senha incorreta!")
else:
    print("bem vindo ao APP")