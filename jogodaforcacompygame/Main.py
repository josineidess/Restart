from Jogador import Jogador
from Jogo import Jogo
from Palavra import Palavra

"""Adicionando jogadores padrões"""

josi = Jogador("Josi")

"""Adicionando palavras"""

# Frutas
abacate = Palavra("abacate", "frutas", 2)
ameixa = Palavra("ameixa", "frutas", 2)
banana = Palavra("banana", "frutas", 2)
carambola = Palavra("carambola", "frutas", 2)
damasco = Palavra("damasco", "frutas", 3)

# Objetos
celular = Palavra("celular", "objetos", 1)
carregador = Palavra("carregador", "objetos", 2)
cadeira = Palavra("cadeira", "objetos", 1)
lata = Palavra("lata", "objetos", 1)

# Profissoes
medico = Palavra("medico", "profissoes", 2)
ginecologista = Palavra("ginecologista", "profissoes", 3)
pediatra = Palavra("pediatra", "profissoes", 2)
mergulhador = Palavra("mergulhador", "profissoes", 2)

"""Adicionando palavras"""
Palavra.add_palavra(abacate)
Palavra.add_palavra(ameixa)
Palavra.add_palavra(banana)
Palavra.add_palavra(carambola)
Palavra.add_palavra(damasco)
Palavra.add_palavra(celular)
Palavra.add_palavra(carregador)
Palavra.add_palavra(cadeira)
Palavra.add_palavra(lata)
Palavra.add_palavra(medico)
Palavra.add_palavra(ginecologista)
Palavra.add_palavra(pediatra)
Palavra.add_palavra(mergulhador)


"""Testando esquema de jogo pelo terminal"""

play = Jogo(josi, "frutas", 2)
play.selecionar()
play.pegar_palavra()

while not play.rodando():
    print("erros: %d" % play.palpites)
    print(play.tentativa)
    play.tentar(input("letra: "))

print(play.tentativa)
print(play.palpites)
if play.ganhou():
    print("Você ganhou!")
else:
    print("Você perdeu...")

