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

def calcula_pontos_regra_avancada(dados):
    resultado = {
        "sequencia_baixa": calcula_pontos_sequencia_baixa(dados),
        "sequencia_alta": calcula_pontos_sequencia_alta(dados),
        "full_house": calcula_pontos_full_house(dados),
        "quadra": calcula_pontos_quadra(dados),
        "quina": calcula_pontos_quina(dados),
        "soma": calcula_pontos_soma(dados)
    }
    return resultado

def faz_jogada(dados, categoria, cartela_de_pontos):
    if categoria in ["1", "2", "3", "4", "5", "6"]:
        numero = int(categoria)
        resultado = calcula_pontos_regra_simples(dados)
        cartela_de_pontos['regra_simples'][numero] = resultado[numero]
    else:
        resultado = calcula_pontos_regra_avancada(dados)

        if categoria == "cinco_iguais":
            cartela_de_pontos['regra_avancada'][categoria] = resultado["quina"]
        elif categoria == "sem_combinacao":
            cartela_de_pontos['regra_avancada'][categoria] = resultado["soma"]
        else:
            cartela_de_pontos['regra_avancada'][categoria] = resultado[categoria]

    return cartela_de_pontos

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)