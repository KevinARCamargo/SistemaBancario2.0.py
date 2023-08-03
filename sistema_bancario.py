#Variáveis
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar Cliente
[5] Abrir nova Conta
[6] Listar usuários
[7] Listar contas
[0] Sair

=> """

#Variáveis
usuarios = []
contas = []
AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


#Funções
#A função depósito deve receber os argumentos apenas por posição
def gerar_deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato
    

#A função saque possuí o requerimento de ser keyword only
def gerar_saque(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    #Verificações
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    #Operação
    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return numero_saques, saldo, extrato

#A função extrato deve receber o saldo como argumento posicional e extrato como keyword only
def gerar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

#Cadastrar Usuários
def cadastrar_usuario(usuarios):
    print("\n========== Cadastro de Usuários ==========\n")
    cpf = input("Cpf (Somente números): ")
    verificacao = verifica_cpf(usuarios=usuarios, cpf=cpf)
    if verificacao == True:
        nome = input("Nome: ")
        data_de_nascimento = input("Data de Nascimento(dd/mm/aaaa): ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla do estado): ")
        usuarios.append({"cpf": cpf, "nome": nome, "data_de_nascimento": data_de_nascimento, "endereco": endereco})
        print("Cliente cadastrado com sucesso!")
    else:
        print("Erro! Este Cpf ja foi cadastrado anteriormente")

#Criar conta
def criar_conta(contas, numero_conta, agencia):
    print("\n========== Contas ==========\n")
    cpf = input("Cpf (Somente números): ")
    verificacao = verifica_cpf(usuarios=usuarios, cpf=cpf)
    if verificacao == False:
        
        contas.append({"cpf": cpf, "numero_conta": numero_conta, "agencia": agencia})
        print("Conta criada com sucesso!")
    else:
        print("Erro! Este Cpf não consta em nosso sistema")

#Verifica se o cpf ja foi cadastrado no sistema
def verifica_cpf(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return False
    return True

#Listar usuários
def listar_usuarios(usuarios):
    print("\n========== Usuários ===========\n")
    for usuario in usuarios:
        cpf = usuario["cpf"]
        nome = usuario["nome"]
        print(f"Cpf: {cpf} - Nome: {nome}")
       

#Listar Contas
def listar_contas(contas):
    print("\n========== Contas ===========\n")
    for conta in contas:
        cpf = conta["cpf"]
        agencia = conta["agencia"]
        numero_conta = conta["numero_conta"]
        print(f"Número Conta: {numero_conta} - Cpf: {cpf} - Agência: {agencia}")

#Menu
while True:

    opcao = input(menu)
    opcao = int(opcao)

    #Depósito
    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = gerar_deposito(saldo,valor,extrato)

    #Saque
    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))
        numero_saques, saldo, extrato = gerar_saque(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)

    #Extrato  
    elif opcao == 3:
        gerar_extrato(saldo, extrato = extrato)

    #Adicionar novo Usuário
    elif opcao == 4:
        cadastrar_usuario(usuarios)
    
    elif opcao == 5:
        numero_conta = len(contas) + 1 
        criar_conta(contas, numero_conta, AGENCIA)
    
    elif opcao == 6:
        listar_usuarios(usuarios)
    
    elif opcao == 7:
        listar_contas(contas)

    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")