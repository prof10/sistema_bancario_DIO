# Inicialização de variáveis
saldo = 0.0
limite_saque = 500.0
saques_realizados = 0
limite_saques_diarios = 3
extrato = []

# Função para realizar depósito
def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido. Tente novamente.")

# Função para realizar saque
def sacar(valor):
    global saldo, saques_realizados, extrato
    if valor > saldo:
        print("Saldo insuficiente para saque.")
    elif valor > limite_saque:
        print(f"O valor máximo para saque é R$ {limite_saque:.2f}.")
    elif saques_realizados >= limite_saques_diarios:
        print("Limite de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        saques_realizados += 1
        extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de saque inválido. Tente novamente.")

# Função para exibir o extrato
def exibir_extrato():
    global saldo, extrato
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print("\nExtrato:")
        for movimento in extrato:
            print(movimento)
        print(f"\nSaldo atual: R$ {saldo:.2f}\n")

# Menu de operações
def menu():
    while True:
        print("\n==== Menu ====")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: R$ "))
            depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: R$ "))
            sacar(valor)
        elif opcao == "3":
            exibir_extrato()
        elif opcao == "4":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o sistema
menu()
