import time


class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome

    @property
    def like(self):
        return self._like

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._like += 1

    def __str__(self):
        return f'Nome : {self._nome}\nData de lançamento: {self.ano}\nLikes: {self._like}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome : {self._nome}\nData de lançamento: {self.ano}\nDuração: {self.duracao}min\nLikes: {self._like}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome}\nData de lançamento: {self.ano}\nTemporadas: {self.temporadas}\nLikes: {self._like}'


class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)


filmes_e_series = []
playlist_fds = Playlist("Fim de Semana", filmes_e_series)


def registra_programa(tipo):
    nome = input("Entre com o nome do programa: ")
    ano = input("Entre com o ano de lançamento: ")

    if tipo == 1:
        duracao = input("Entre com a duração em minutos: ")
        playlist_fds.append(Filme(nome, ano, duracao))

    else:
        temporadas = input("Entre com o numero de temporadas: ")
        playlist_fds.append(Serie(nome, ano, temporadas))


def like():
    #nome = input("Entre com o nome do filme que deseja dar like").title()
    #if(nome in playlist_fds):

    for i in playlist_fds:
        opt = input(f'Deseja dar like em {i.nome}?(Y/N)')
        if opt.upper() == 'Y':
            i.dar_like()


def mostra_programa():
    print(f'Tamanho da playlist: {len(playlist_fds)}')
    for i in playlist_fds:
        print(i, "\n")
    time.sleep(4)
