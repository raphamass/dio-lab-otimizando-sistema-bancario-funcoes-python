""" 
Bootcamp DIO - Python AI Backend Developer.
Lab Project - Otimizando o Sistema Bancário com Funções Python.

Objetivo geral: separar as operações existentes em funções dedicadas.
Criar duas novas funções: criar usuário(cliente) e criar conta bancária.
"""
def menu_principal():
    """Exibe menu principal."""
    menu = """\n
    *********** MENU ***********
    [1]Depósito
    [2]Saque
    [3]Extrato
    [4]Criar novo usuário
    [5]Criar nova conta
    [6]Listar contas
    [7]Listar usuários
    [8]Sair
    ****************************
    Selecione uma opção:
    => """
    return int(input(menu))

def depositar(saldo, valor, extrato,/):
    """Realiza depósito em uma conta.

    Args:
        saldo (float): Saldo atual da conta.
        valor (float): Valor a ser depositado.
        extrato (float): Extrato atual da conta.

    Retorna:
        saldo: Saldo atualizado após o depósito.
        extrato: extrato atualizado c/ registro do depósito.
    
    Se o valor do depósito for maior que zero, o saldo é incrementado
    pelo valor do depósito e o extrato é atualizado. Caso contrário, 
    uma mensagem de erro é exibida.
    """

    if valor > 0:
        saldo += valor
        extrato += f"Depósito no valor de: R$ {valor:.2f}\n"
        print("\n<<< Depósito realizado!! >>>")
    else:
        print("\n### Depósito não realizado! Valor informado é inválido. ###")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Realiza saque em uma conta.

    Args:
        saldo (float): Saldo atual da conta.
        valor (float): Valor a ser sacado.
        extrato (str): Extrato atual da conta.
        limite (float): Limite máximo de saque permitido.
        numero_saques (list): Lista contendo o número atual de saques.
        limite_saques (int): Número máximo de saques permitidos.

    Retorna:
        saldo: saldo atualizado após saque.
        extrato: extrato atualizado com o registro do saque.
    """

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques[0] >= limite_saques

    if excedeu_saldo:
        print("\n### Saque não realizado! Saldo em conta insuficiente. ###")
    elif excedeu_limite:
        print("### Saque não realizado! Limite máximo de saque: R$ 500,00. ###")
    elif excedeu_saques:
        print("### Saque não realizado! Número máximo de saques "\
              "excedido (3)! ###")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque realizado no valor de: R$ {valor:.2f}\n"
        numero_saques[0] += 1
        print("\n<<< Saque realizado com sucesso!! >>>")
    else:
        print("### Saque não realizado! Valor informado inválido. ###")
    
    return saldo, extrato

def exibe_extrato(saldo, /, *, extrato):
    """Exibe o extrato de uma conta.

    Args:
        saldo (float): Saldo atual da conta.
        extrato (str): extrato atual da conta.
    
    A função imprime o extrato da conta. Se não houver movimentações, 
    uma mensagem indicando que não houve movimentações é exibida. 
    Em seguida, o saldo atual é impresso.
    """
   
    print("\n============== EXTRATO ==============")
    print("Nenhuma movimentação realizada." if not extrato else extrato)
    print(f"\nSalto atual:\tR$ {saldo:.2f}")
    print("=====================================")

def criar_usuario(usuarios):
    """Cria um novo usuário.

    Args:
        usuarios (list): Lista de usuários existentes.
    A função solicita ao usuário que insira o CPF, o nome completo, 
    a data de nascimento e o endereço. Se o CPF já estiver em uso, uma 
    mensagem de erro é exibida e a função retorna. Caso contrário, um 
    novo usuário é criado e adicionado à lista de usuários.
    """
    
    cpf = input("Por favor, informe o CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n### O CPF informado já está em uso! ###")
        return
    
    nome = input("Por favor, informe o nome completo: ")
    data_nascimento = input("Por favor, informe a data de nascimento " \
                            "(dd-mm-aaaa): ")
    endereco = input("Informe o endereço " \
                     " (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })

    print("<<< Usuário criado com sucesso!! >>>")

def filtrar_usuario(cpf, usuarios):
    """Filtra um usuário com base no CPF.

    Args:
        cpf (str): CPF do Usuário a ser filtrado.
        usuarios (list): LIsta de usuários existentes.

    Retorna:
        usuario(dict): Usuário filtrado se encontrado, caso contrário,
        retorna None.
        A função percorre a lista de usuários e retorna o primeiro 
        usuário que tem o mesmo CPF que o fornecido. Se nenhum usuário 
        for encontrado com o CPF fornecido, a função retorna None.
    """

    usuarios_filtrados = [
        usuario for usuario in usuarios 
        if usuario['cpf'] == cpf
    ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    """Cria uma conta nova para um usuário.

    Args:
        agencia (str): Número da agência.
        numero_conta (str): Número da conta criada.
        usuarios (list): Lista de usuários existentes.

    Retorna:
        conta(dict): Dicionário contendo detalhes da conta se o usuário
        for encontrado, caso contrário, retorna None.
    
    A função solicita ao usuário que insira o CPF. Se o usuário com o 
    CPF fornecido for encontrado na lista de usuários, uma nova conta é 
    criada e um dicionário contendo detalhes da conta é retornado. Se o 
    usuário não for encontrado, uma mensagem de erro é exibida e a 
    função retorna None.
    """

    cpf = input("Por favor, informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n<<< Conta criada com sucesso!! >>>")
        return {
            'agencia': agencia,
            'numero_conta': numero_conta,
            'usuario': usuario
        }
    
    print("\n### Usuário não encontrado, não foi possível criar conta! ###")

def listar_contas(contas):
    """Lista todas as contas existentes.

    Args:
        contas(list): Uma lista de contas existentes.

    A função percorre a lista de contas e imprime os detalhes de cada 
    conta, incluindo a agência, o número da conta e o nome do titular. 
    Se a lista de contas estiver vazia, uma mensagem indicando que 
    nenhuma conta foi criada é exibida.
    """

    if not contas:
        print("\n### Nenhuma conta foi criada. ###")
        return
    
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def listar_usuarios(usuarios):
    """Lista todos os usuários cadastrados.
    
    Args:
        usuarios(list): Uma lista de usuários existentes.

    A função percorre a lista de usuários e imprime os detalhes de cada 
    usuário, incluindo o nome, a data de nascimento, o CPF e o endereço. 
    Se a lista de usuários estiver vazia, uma mensagem indicando que 
    nenhum usuário foi cadastrado é exibida.
    """

    if not usuarios:
        print("\n### Nenhum usuário cadastrado. ###")
        return
    
    for usuario in usuarios:
        linha = f"""
            Nome:\t\t{usuario['nome']}
            Nascimento:\t\t{usuario['data_nascimento']}
            CPF:\t\t{usuario['cpf']}
            Endereço:\t\t{usuario['endereco']}
        """
        print("-" * 100)
        print(linha)

def main():
    """Executa o programa principal.

       A função inicializa as variáveis necessárias e entra em um loop 
       infinito onde apresenta um menu de opções para o usuário. 
       Dependendo da opção escolhida pelo usuário, a função realiza 
       diferentes operações, como depositar, sacar, exibir extrato, 
       criar usuário, criar conta, listar contas, listar usuários e 
       sair do programa. Se a opção escolhida pelo usuário não for 
       válida, uma mensagem de erro é exibida. 
    """

    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = [0]
    usuarios = []
    contas = []

    while True:
        opcao = menu_principal()

        if opcao == 1:
            valor = float(input("Por favor, informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 2:
            valor = float(input("Por favor, informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
            
        elif opcao == 3:
           exibe_extrato(saldo, extrato=extrato)
        
        elif opcao == 4:
            criar_usuario(usuarios)
        
        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 7:
            listar_usuarios(usuarios)

        elif opcao == 8:
            print("Operação finalizada! Obrigado por utilizar nosso sistema!\n")
            break
         
        else:
            print("Operação inválida, por favor selecione a opção desejada.")

main()