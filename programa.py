from funcoes import *

cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

def fim_de_jogo(cartela):
    for valor in cartela['regra_simples'].values():
        if valor == -1:
            return False
    for valor in cartela['regra_avancada'].values():
        if valor == -1:
            return False
    return True

while not fim_de_jogo(cartela):

    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    while True:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        opcao = input()

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            if 0 <= indice < len(dados_rolados):
                dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, indice)

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            if 0 <= indice < len(dados_guardados):
                dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, indice)

        elif opcao == "3":
            if rerrolagens < 2:
                novos = rolar_dados(5 - len(dados_guardados))
                dados_rolados = novos
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
            print("Digite a combinação desejada:")
            combinacao = input()

            if combinacao in ["1","2","3","4","5","6"]:
                chave = int(combinacao)
                if cartela['regra_simples'][chave] != -1:
                    print("Essa combinação já foi utilizada.")
                    continue
            elif combinacao in cartela['regra_avancada']:
                if cartela['regra_avancada'][combinacao] != -1:
                    print("Essa combinação já foi utilizada.")
                    continue
            else:
                print("Combinação inválida. Tente novamente.")
                continue

            todos_dados = dados_rolados + dados_guardados
            cartela = faz_jogada(todos_dados, combinacao, cartela)
            break

        else:
            print("Opção inválida. Tente novamente.")

total = 0

for valor in cartela['regra_simples'].values():
    total += valor
for valor in cartela['regra_avancada'].values():
    total += valor

soma_simples = sum(cartela['regra_simples'].values())
if soma_simples >= 63:
    total += 35

imprime_cartela(cartela)
print(f"Pontuação total: {total}")