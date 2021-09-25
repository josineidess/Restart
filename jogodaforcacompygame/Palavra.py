"""Classe que serve de modelo para as palavras"""


class Palavra:
    __palavras = []  # Atributo estático para consulta das palavras

    def __init__(self, nome, categoria, dificuldade):
        self.__nome = nome
        self.__categoria = categoria
        self.__dificuldade = dificuldade

    @property
    def nome(self):
        return self.__nome

    @property
    def categoria(self):
        return self.__categoria

    @property
    def dificuldade(self):
        return self.__dificuldade

    @nome.setter
    def nome(self, novo):
        self.__nome = novo
        return True

    @categoria.setter
    def categoria(self, nova):
        self.__categoria = nova
        return True

    @dificuldade.setter
    def dificuldade(self, nova):
        self.__dificuldade = nova
        return True
    @staticmethod
    def add_palavra(palavra):  # Atributo que adiciona palavras a lista estática
        Palavra.__palavras.append(palavra)
        return True

    @staticmethod
    def get_palavras():  # Função que passa as palavras da lista estática
        return Palavra.__palavras

