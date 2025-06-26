import textwrap

print( ''' 
----------------------
BEM VINDO AO SEU BANCO
---------------------- 

[!] SELECIONE A OPÇÃO QUE DESEJA REALIZAR:''')

def menu():
    menu = """
    =============== MENU ===============
    [1]\tDEPOSITAR
    [2]\tSACAR
    [3]\tEXTRATO
    [4]\tNOVA CONTA
    [5]\tLISTAR CONTAS
    [6]\tNOVO USUÁRIO
    [7]\tSAIR
    ==>  """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor_depositar,extrato,/):
    if valor_depositar > 0:
            saldo += valor_depositar
            extrato += f'Depósito\tR$ {valor_depositar:.2f}\n'
            print("Seu depósito foi realizado com sucesso!")
    else:
            print("Valor inválido. Tente novamente!")
    return saldo,extrato

def sacar(*,saldo, valor_sacar, extrato,limite_saque,numero_de_saques,limite_saques):
    excedeu_saldo = valor_sacar > saldo
    excedeu_limite = valor_sacar > limite_saque
    excedeu_saques = numero_de_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou!Você não tem saldo suficiente.")

    elif excedeu_limite: 
        print("\nOperação falhou!O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou!Número máximo de saques excedido.")

    elif valor_sacar > 0:
        saldo -= valor_sacar
        extrato += f'Saque\t\tR$ {valor_sacar:.2f}\n'
        numero_de_saques += 1 
        print("Saque realizado com sucesso!")
    else:
        print("A operação falhou!O valor informado é inválido.")

    return saldo,extrato,numero_de_saques

def exibir_extrato(saldo,/,*,extrato):
    print("\n=========== EXTRATO ===========")
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo Atual:    R$ {saldo:.2f}")
    print("================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF(Somente números):")
    usuario = filtrar_usuarios(cpf,usuarios)

    if usuario:
        print('Já existe usuário com esse CPF!')
        return
    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe sua data de nascimento (dd - mm - aaaa): ")
    endereco = input("Informe o endereço (Logradouro,nmr - bairro - cidade/siga estado): ")
    
    usuarios.append({"nome":nome, "data de nascimento": data_nascimento,"cpf": cpf,"endereço": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuarios(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]  
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return{"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}  
    
    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f''' \
            Agência:\t{conta['agencia']}   
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3 
    AGENCIA = "0001"  

    saldo = 0
    extrato = ''
    limite_saque = 500
    numero_de_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()  

        if opcao == "1":
            valor_depositar = float(input('''Insira o valor do depósito: R$ '''))
            saldo, extrato = depositar(saldo,valor_depositar,extrato)

        elif opcao == "2":
            valor_sacar = float(input('Informe o valor que deseja sacar: R$'))

            saldo,extrato,numero_de_saques = sacar(
                saldo=saldo,
                valor_sacar=valor_sacar,
                extrato=extrato,
                limite_saque=limite_saque,
                numero_de_saques=numero_de_saques,
                limite_saques=LIMITE_SAQUES
            )
            
            
        elif opcao == "3":
            exibir_extrato(saldo,extrato=extrato)
        
        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)    

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "7":
            print("Obrigado por usar nossos serviços!")
            break
        
        else:
            print("Opção inválida. Por favor, selecione novamente a opção desejada. ")

main()
