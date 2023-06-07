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
        return f'Nome : {self._nome}\nData de lançamento: {self.ano}\nTemporadas: {self.temporadas}\nLikes: {self._like}'


filmes_e_series = []


def registra_programa(tipo):
    nome = input("Entre com o nome do programa: ")
    ano = input("Entre com o ano de lançamento: ")

    if tipo == 1:
        duracao = input("Entre com a duração em minutos: ")
        filmes_e_series.append(Filme(nome, ano, duracao))

    else:
        temporadas = input("Entre com o numero de temporadas: ")
        filmes_e_series.append(Serie(nome, ano, temporadas))


def like():
    for i in filmes_e_series:
        opt = input(f'Deseja dar like em {i.nome}?(Y \ N)')
        if opt.upper() == 'Y':
            i.dar_like()


def mostra_programa():
    for i in filmes_e_series:
        print(i, "\n")
    time.sleep(4)
