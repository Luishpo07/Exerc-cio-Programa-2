import random

def rolar_dados(numero):
    dados = []
    for i in range(numero):
        valor = random.randint(1, 6)
        dados.append(valor)
    return dados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados[dado_para_guardar]
    dados_no_estoque.append(dado)
    dados_rolados.pop(dado_para_guardar)
    return [dados_rolados, dados_no_estoque]