# Operadores Lógicos

# AND: Para a expressão ser True, todas as condições devem ser verdadeiras
# OR: Para a expressão ser True, pelo menos uma das condições deve ser verdadeira

print(True and True)     # True: ambas as condições são verdadeiras
print(True and False)    # False: uma condição é falsa
print(False and False)   # False: ambas as condições são falsas
print(True or True)      # True: ambas as condições são verdadeiras
print(True or False)     # True: pelo menos uma condição é verdadeira
print(False or False)    # False: ambas as condições são falsas

# Exemplo com variáveis
saldo = 1000  # Definindo o saldo da conta
saque = 250   # Definindo o valor do saque
limite = 200  # Definindo o limite de saque
conta_especial = True  # Definindo se a conta é especial

# Expressão lógica combinada usando AND e OR
expre1 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expre1)  # True: A conta é especial e o saldo é suficiente para o saque

#............................................................................

# Operador AND
saldo = 1000
saque = 200
limite = 100

# Verifica se o saldo é suficiente e o saque está dentro do limite
print(saldo >= saque and saque <= limite)  # False: o saque está fora do limite

# Operador OR
saldo = 1000
saque = 200
limite = 100

# Verifica se o saldo é suficiente ou se o saque está dentro do limite
print(saldo >= saque or saque <= limite)  # True: o saldo é suficiente

# Operador Negação (NOT)
contatos_emergencia = []  # Lista vazia

print(not 1000 > 1500)  # True: a negação de uma expressão falsa resulta em True
print(not contatos_emergencia)  # True: a lista está vazia, que é considerada False, então not resulta em True
print(not 'saque 1500')  # False: a string não está vazia, então not resulta em False
print(not '')  # True: a string está vazia, que é considerada False, então not resulta em True

# Parênteses (importância para clareza e precedência)
saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Expressão lógica sem parênteses
expre = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expre)  # True: a expressão é avaliada com base na precedência dos operadores

# Expressão lógica com parênteses para maior clareza
expre_certa = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expre_certa)  # True: a expressão é avaliada de acordo com a lógica correta definida pelos parênteses
