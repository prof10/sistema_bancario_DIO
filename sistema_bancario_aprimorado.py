# Inicialização de variáveis
usuarios = []
contas = []
numero_conta_sequencial = 1

# Função para criar um usuário
def criar_usuario(nome, data_nascimento, cpf, endereco):
    # Remove qualquer caractere que não seja número do CPF
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se o CPF já existe
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado.")
            return None
    
    # Cria e adiciona o novo usuário à lista
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} criado com sucesso!")
    return usuario

# Função para criar uma conta corrente
def criar_conta(cpf_usuario):
    global numero_conta_sequencial

    # Remove qualquer caractere que não seja número do CPF
    cpf_usuario = ''.join(filter(str.isdigit, cpf_usuario))

    # Busca o usuário pelo CPF
    usuario = next((u for u in usuarios if u['cpf'] == cpf_usuario), None)
    if usuario is None:
        print("Usuário não encontrado.")
        return None

    # Cria a conta corrente para o usuário
    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta_sequencial,
        'usuario': usuario
    }
    numero_conta_sequencial += 1
    contas.append(conta)
    print(f"Conta {conta['numero_conta']} criada com sucesso para {usuario['nome']}!")
    return conta

# Função para realizar depósito (positional only)
def depositar(valor, /):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        return saldo, extrato
    else:
        print("Valor de depósito inválido. Tente novamente.")

# Função para realizar saque (keyword only)
def sacar(*, valor):
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
        return saldo, extrato
    else:
        print("Valor de saque inválido. Tente novamente.")

# Função para exibir o extrato (positional only e keyword only)
def exibir_extrato(saldo, /, *, extrato):
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print("\nExtrato:")
        for movimento in extrato:
            print(movimento)
        print(f"\nSaldo atual: R$ {saldo:.2f}\n")

# Função de menu para criar usuários e contas
def menu_banco():
    while True:
        print("\n==== Menu ====")
        print("1. Criar Usuário")
        print("2. Criar Conta Corrente")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Extrato")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
            cpf = input("Digite o CPF: ")
            endereco = input("Digite o endereço (logradouro, nro-bairro-cidade/sigla estado): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)
        
        elif opcao == "2":
            cpf = input("Digite o CPF do usuário para criar a conta: ")
            criar_conta(cpf)

        elif opcao == "3":
            valor = float(input("Digite o valor do depósito: R$ "))
            depositar(valor)
        
        elif opcao == "4":
            valor = float(input("Digite o valor do saque: R$ "))
            sacar(valor=valor)
        
        elif opcao == "5":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "6":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Variáveis globais para o saldo, limite de saque e extrato
saldo = 0.0
limite_saque = 500.0
saques_realizados = 0
limite_saques_diarios = 3
extrato = []

# Iniciar o sistema
menu_banco()
