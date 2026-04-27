import random

def rolar_dados(numero):
    dados = []
    for i in range(numero):
        valor = random.randint(1, 6)
        dados.append(valor)
    return dados

