from Palavra import Palavra
import random

"""Classe que contém as funções de interação do jogo"""


class Jogo:
    def __init__(self, jogador, tema, dificuldade):
        self.__tema = tema
        self.__dificuldade = dificuldade
        self.__jogadas = []
        self.__palavras_selecionadas = (
            []
        )  # Palavras que se encaixam nas especificações do jogador
        self.__pontuacao = 0
        self.__palavra_atual = []  # Palavra a ser descoberta
        self.__tentativa = []  # Progresso da palavra a ser descoberta
        self.__letras_tentadas = []
        self.__jogador = jogador
        self.__palpites = 0

    @property
    def tema(self):
        return self.__tema

    @property
    def dificuldade(self):
        return self.__dificuldade

    @property
    def pontuacao(self):
        return self.__pontuacao

    @property
    def palavra_selecionadas(self):
        return self.__palavras_selecionadas

    @property
    def jogagor(self):
        return self.__jogador

    @property
    def palpites(self):
        return self.__palpites

    @property
    def tentativa(self):
        return self.__tentativa

    @property
    def palavra_atual(self):
        return self.__palavra_atual

    def rodando(self):
        if " " not in self.__tentativa or self.palpites == 5:
            return True
        else:
            return False

    def ganhou(self):
        if self.palpites < 5:
            return True
        else:
            return False

    def selecionar(self):
        for palavra in Palavra.get_palavras():
            if (
                palavra.categoria == self.__tema
                and palavra.dificuldade == self.__dificuldade
            ):
                self.__palavras_selecionadas.append(palavra)

    def pegar_palavra(self):
        sorteado = random.randint(0, len(self.__palavras_selecionadas) - 1)
        if sorteado not in self.__jogadas:
            self.__palavra_atual = list(self.__palavras_selecionadas[sorteado].nome)
            self.__tentativa = list(" " * len(self.__palavra_atual))
            self.__jogadas.append(sorteado)
        else:
            self.pegar_palavra()

    def tentar(self, letra):
        if letra not in self.__letras_tentadas and letra in self.__palavra_atual:
            for l in range(len(self.__palavra_atual)):
                if self.__palavra_atual[l] == letra:
                    self.__tentativa[l] = letra
                    self.__letras_tentadas.append(letra)
            return True
        else:
            if letra not in self.__palavra_atual:
                print("Não tem essa letra...")
            if letra in self.__letras_tentadas:
                print("Essa letra já foi...")
        self.__letras_tentadas.append(letra)
        self.__palpites += 1
        return False

