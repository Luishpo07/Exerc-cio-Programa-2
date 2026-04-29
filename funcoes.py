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

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    valor = dados_no_estoque.pop(dado_para_remover)
    dados_rolados.append(valor)
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados):
    resultado = {}
    for face in range(1, 7):
        soma = 0
        for d in dados:
            if d == face:
                soma += d
        resultado[face] = soma
    return resultado

def calcula_pontos_soma(dados):
    total = 0
    for valor in dados:
        total += valor
    return total

def calcula_pontos_sequencia_baixa(dados):
    unicos = sorted(set(dados))
    
    for i in range(len(unicos) - 3):
        if (unicos[i] + 1 == unicos[i + 1] and
            unicos[i] + 2 == unicos[i + 2] and
            unicos[i] + 3 == unicos[i + 3]):
            return 15
    
    return 0