"""Classe que serve como modelo para Jogador"""


class Jogador:
    def __init__(self, nome):
        self.__nome = nome
        self.__pontos = 0


@property
def nome(self):
    return self.__nome


@property
def pontos(self):
    return self.__pontos


@nome.setter
def nome(self, novo):
    self.__nome = novo
    return True
