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

def calcula_pontos_sequencia_alta(dados):
    dados_unicos = sorted(set(dados))  
    contador = 1
    
    for i in range(1, len(dados_unicos)):
        if dados_unicos[i] == dados_unicos[i-1] + 1:
            contador += 1
            if contador >= 5:
                return 30
        else:
            contador = 1
    
    return 0

def calcula_pontos_full_house(lista_dados):
    contagem = {}
    for dado in lista_dados:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1

    valores = sorted(contagem.values())
    
    if valores == [2, 3]:
        total = 0
        for dado in lista_dados:
            total += dado
        return total
    return 0

def calcula_pontos_quadra(lista_dados):
    soma_dados = 0
    quadra = False
    for i in range(len(lista_dados)):
        contagem = 0
        for j in range(len(lista_dados)):
            if lista_dados[i] == lista_dados[j]:
                contagem += 1
        soma_dados += lista_dados[i]
        if contagem >= 4:
            quadra = True
    if quadra == True:
        return soma_dados
    else:
        return 0
    
def calcula_pontos_quina(dados):
   
    for valor in set(dados):
        if dados.count(valor) >= 5:
            return 50
    return 0

