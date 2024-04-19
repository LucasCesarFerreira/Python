import sys
import socket
from threading import Thread

SERVER_IP = ''
SERVER_PORT = 8000


def conexao():
    ip = input("Entre com o endereço de ip desejado para começar a se comunicar")
    conf = input(f"\no ip: {ip} esta correto?\n1-Sim/0-Não")
    if conf == 0:
        print("Desligando o programa...")
        sys.exit()
    return iniciar_conexao(ip)


def verifica_ip(endereco_ip):
    if len(endereco_ip) == 9 and endereco_ip is not None:
        return True
    print("Ip imcompativel, encerrando programa")
    sys.exit()


def iniciar_conexao(ip):
    print("Tentando conectar ao servidor")
    verifica_ip(ip)
    con_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        ADDR = (ip, SERVER_PORT)
        con_tcp.connect(ADDR)
    except ConnectionError as error:
        print("Conexao negada. Tente novamente!\n"
              f"tipo de erro: `{type(error)}")

    return con_tcp


def encerrar_conexao(con_tcp):
    print("Encerrando conexão TCP...")
    con_tcp.close()


def chat(con_tcp):
    print("Chat iniciado! Para sair escreva: exit ")

    while True:
        mensagem = input("voce: ")

        if mensagem is not None:
            con_tcp.send(bytes(mensagem, "utf8"))
            if mensagem == 'exit':
                break

        recv_mens = con_tcp.recv(1024).decode("utf8")

        if recv_mens is not None:
            print(f"servidor: {recv_mens}")
            if recv_mens == 'exit':
                print("Conexão encerrada do outro lado, escreva exit para sair")


if __name__ == "__main__":

    print("Bem vindo ao Chat sem nome no momento!\n")
    conexao = conexao()
    chat(conexao)

    try:
        conexao.close()
    except ConnectionError as error:
        print("A conexao TCP esta encerrada")

    receive_thread = Thread(target=chat)
    receive_thread.start()
