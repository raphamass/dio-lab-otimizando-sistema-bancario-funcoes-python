# :desktop_computer: Lab Project - Otimizando o Sistema Bancário com funções Python

## Desafio - Bootcamp DIO - Python AI Backend Developer

###  *Objetivo Geral*

Criar um sistema bancário usando linguagem Python. Deixar o código mais modularizado e adicionar novas funções (Versão 2.0).

- [Versão 1.0] -  Foram implementadas 3 operações simples:

    - Depósito
    - Saque
    - Extrato

A versão 1 do programa está disponível no repositório **[raphamass/dio-lab-sistema-bancario-python](https://github.com/raphamass/dio-lab-sistema-bancario-python)**

- [Versão 2.0] - Foram feitas as seguintes implementações:

    - Criação de funções para as operações existentes:
        - Menu principal - `def menu_principal()`
        - sacar - `def sacar()`
        - depositar - `def depositar()`
        - extrato - `def exibe_extrato()`
    
    - Criação de 4 novas funções:
        - Cadastro de novo usuário - `def criar_usuário()`
        - Filtro de suário - `def filtrar_usuario()`
        - Criação de conta - `def criar_conta()`
        - Listagem de contas - `def listar_contas()`
        - Listagem de usuários - `def listar_usuarios()`

    - Criação de função para rodar o sistema `def main()` .

### *Função de Depósito*

Possibilidade de depositar valores positivos.

Na versão 1 do projeto, temos apenas um usuário. Não há necessidade de identificar número de agência e conta.

Todos os depósitos devem ser:

- Armazenados em uma variável.
- Exibidos na operação de extrato.
***

### *Função de Saque*

O sistema deve permitir:

- 3 saques diários.
- Limite de R$ 500,00 por saque

:heavy_exclamation_mark:Caso o saldo esteja insuficiente, o limite de R$500,00 seja ultrapassado, ou o número de saques supere a restrição de 3 operações, o sistema informará que a transação não pôde ser realizada.

Todos os saques devem ser:

- Armazenados em uma variável.
- Exibidos na operação de extrato.
***

### *Função de Extrato*

- Deve listar todos os depósitos/saques.
- No fim da listagem, deve exibir o saldo atual.
***

### *Função de Cadastro de Usuário*

- Cria novo usuário e armazena em lista
- Nome, data de nascimento, cpf e endereço.
- O programa não permite cadastro de 2 usuários com mesmo CPF.
***

### *Função de Criação de Conta*

- Cria e armazena contas bancárias em lista.
- Cada conta é composta por Agência(no. fixo), n. de conta, usuário.
- O número de conta é criado de forma sequencial.
- Cada usuário pode ter mais de uma conta.
- Cada conta pode ter apenas um usuário registrado.
***

### *Funções de listagem de Contas e Usuários*

- Exibem as listas de:
    - Contas criadas
    - Usuários cadastrados.
***



