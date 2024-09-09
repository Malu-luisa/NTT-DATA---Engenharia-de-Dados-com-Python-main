# Operadores Lógicos

# AND = Para ser True tudo tem que ser verdadeiro 
# OR = Para ser True apenas um tem que ser verdadeiro 

print(True and True)     # True
print(True and False)    # False
print(False and False)   # False
print(True or True)      # True
print(True or False)     # True
print(False or False)    # False

saldo = 1000
saque = 250 
limite = 200
conta_especial = True

expre1 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expre1)  # True
	
#............................................................................

# Operador AND

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite)  # False

# Operador OR

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque or saque <= limite)  # True 

# Operador Negação

contatos_emergencia = []

print(not 1000 > 1500)  # True
print(not contatos_emergencia)  # True 
print(not 'saque 1500')  # False
print(not '')  # True

# Parênteses (importância)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

expre = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expre)  # True

# Expressão com parênteses para maior clareza
expre_certa = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expre_certa)  # True
