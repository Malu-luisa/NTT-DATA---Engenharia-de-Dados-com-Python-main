# Operadores de identidade
# São utilizados para comparar se dois objetos ocupam a mesma posição na memória

saldo = 1000  # Definindo a variável 'saldo' com o valor 1000
limite = 500  # Definindo a variável 'limite' com o valor 500

# Verifica se 'saldo' e 'limite' são o mesmo objeto na memória
print(saldo is limite)  # False: 'saldo' e 'limite' não ocupam a mesma posição na memória
print(saldo is not limite)  # True: 'saldo' e 'limite' são objetos diferentes na memória

# Exemplo

curso = 'Curso de python'  # Definindo a variável 'curso' com a string 'Curso de python'
nome_curso = curso  # Atribuindo a mesma referência de 'curso' a 'nome_curso'
saldo, limite = 200, 200  # Definindo 'saldo' e 'limite' com o valor 200

# Verifica se 'curso' e 'nome_curso' são o mesmo objeto na memória
print(curso is nome_curso)  # True: 'curso' e 'nome_curso' referenciam o mesmo objeto na memória

# Verifica se 'curso' e 'nome_curso' não são o mesmo objeto na memória
print(curso is not nome_curso)  # False: 'curso' e 'nome_curso' são o mesmo objeto na memória

# Verifica se 'saldo' e 'limite' são o mesmo objeto na memória
print(saldo is limite)  # True: em alguns casos, o Python pode otimizar o armazenamento de inteiros pequenos (como 200) e reutilizar o mesmo objeto
