# Estrutura condicional IF
saldo = 2000.0  # Define o saldo da conta
saque = float(input('Informe o valor do saque:'))  # Solicita o valor do saque ao usuário e converte para float

if saldo >= saque: 
    print('Realizando saque!')  # Executado se o saldo for suficiente para o saque

if saldo < saque: 
    print('Saldo insuficiente')  # Executado se o saldo for insuficiente para o saque

# Estrutura condicional IF/ELSE
saldo = 2000.0  # Define o saldo da conta
saque = float(input('Quanto você quer sacar?'))  # Solicita o valor do saque ao usuário e converte para float

if saldo >= saque:
    print('Saque realizado com sucesso')  # Executado se o saldo for suficiente para o saque
else:
    print('Saque Insuficiente!!!!')  # Executado se o saldo for insuficiente para o saque

# Estrutura condicional IF/ELIF/ELSE
import sys  # Importa o módulo sys para usar sys.exit

opcao = int(input('Informe a opção: [1] sacar \n[2] Extrato'))  # Solicita a opção ao usuário e converte para int

if opcao == 1:
    valor = float(input('Informe a quantidade do saque: '))  # Solicita o valor do saque ao usuário e converte para float
elif opcao == 2: 
    print('Exibindo Extrato')  # Executado se a opção for 2
else: 
    sys.exit('Operação Inválida')  # Encerra o programa com uma mensagem de erro se a opção não for 1 ou 2

# Estrutura condicional IF aninhado
conta_normal = True  # Define se a conta é normal
conta_universitaria = True  # Define se a conta é universitária

saldo = 2000  # Define o saldo da conta
saque = 2500  # Define o valor do saque
cheque_especial = 450  # Define o valor do cheque especial

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')  # Executado se a conta for normal e o saldo for suficiente para o saque
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com o cheque especial')  # Executado se a conta for normal e o saque está dentro do limite do cheque especial
    else:
        print('Não foi possível realizar o saque, saldo insuficiente')  # Executado se a conta for normal e o saldo mais o cheque especial não forem suficientes
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!!')  # Executado se a conta for universitária e o saldo for suficiente para o saque
    else:
        print('Saldo insuficiente')  # Executado se a conta for universitária e o saldo for insuficiente

# Estrutura condicional IF ternário
saldo = 2000  # Define o saldo da conta
saque = 2500  # Define o valor do saque

# Atribui 'sucesso' se o saldo for suficiente para o saque, caso contrário, atribui 'falha'
status = 'sucesso' if saldo >= saque else 'falha'

print('{} ao realizar o saque!'.format(status))  # Exibe o status da operação de saque
