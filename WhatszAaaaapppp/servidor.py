import socket
from threading import Thread

SERVER_PORT = 8001


def accept_conexoes():
    while True:
        client, client_address = SERVER.accept()
        enderecos[client] = client_address
        Thread(target=trata_client, args=(client,)).start()


def trata_client(client):
    name = client.recv(1024).decode("utf8")
    client.send(bytes(name + " está online!", "utf8"))
    msg = "%s entrou no chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        # loop infinito de comunicacao
        msg = client.recv(1024)  # recebendo uma mensagem do cliente
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name + "")
        else:   # mensagem com instrucao de saída
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s saiu do chat" % name, "utf8"))
            break


def broadcast(msg, prefix=""):

    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)


clients = {}
enderecos = {}

HOST = "127.0.0.1"


ADDR = (HOST, SERVER_PORT)

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(1)
    print("Aguardando conexão...")
    ACCEPT_THREAD = Thread(target=accept_conexoes)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
SERVER.close()


"""
SERVER_IP = ''
SERVER_PORT = 8000


def bind_to_server():

    con_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server = (SERVER_IP, SERVER_PORT)
    con_tcp.bind(socket_server)
    con_tcp.listen(1)

    return con_tcp


def confirma_cliente(con_tcp):
    conexao, ip_client = con_tcp.accept()
    print(f"\nO cliente com  o ip {ip_client[0]} se conectou!")
    return conexao, ip_client


def fecha_conexao(con_tcp):
    print("Encerrando conexão e fechando o programa...")
    con_tcp.close()


def listening(con_tcp, ip_client):
    print("Iniciando o chat. Aguardando mensagem...\n")

    while True:
        recv_mens = con_tcp.recv(1024).decode("ascii")

        if recv_mens is not None:
            print(f"Cliente:{ip_client[0]} :{recv_mens}")
            if recv_mens == 'exit':
                print("Conexão encerrada do outro lado, escreva exit para sair")

        enviando_msg = input("Você: ")

        if enviando_msg is not None:
            con_tcp.send(bytes(enviando_msg ,"utf8"))
            if enviando_msg == 'exit':
                break

    fecha_conexao(con_tcp)


if __name__ == "__main__":

    conexao_atual = bind_to_server()
    accept_connection, cliente = confirma_cliente(conexao_atual)
    listening(accept_connection, cliente)

    sys.exit()
"""
