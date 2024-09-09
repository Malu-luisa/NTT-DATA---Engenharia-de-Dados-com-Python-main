#Estrutura condicional IF
saldo = 2000.0
saque = float(input('Informe o valor do saque:'))

if saldo >= saque: 
    print('Realizando saque!')

if saldo < saque: 
    print('Saldo insuficiente')

# Estrutura condicional IF/ELSE

saldo = 2000.0
saque = float(input('Quanto voce quer sacar?'))

if saldo >= saque:
    print('Saque realizado com sucesso')
else:
    print('Saque Insuficiente!!!!')

#Estrutura condicional IF/ELIF/ELSE
import sys

opcao = int(input('Informe a opção: [1] sacar \n[2] Extrato'))

if opcao == 1:
    valor = float(input('Informe a quantidade do saque: '))
elif opcao == 2: 
    print('Exibindo Extrato')
else: 
    sys.exit('Operação Invalida')


# Estrutura condicional IF aninhado 

conta_normal = True
conta_universitaria = True

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com o cheque especial')
    else:
        print('Não foi possível realizar o saque, saldo insuficiente')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!!')
    else:
        print('Saldo insuficiente')


# Estrutura condicional If ternário

saldo = 2000
saque= 2500
status = 'sucesso' if saldo >= saque else 'falha'

print('{} ao realizar o saque!'.format(status))

