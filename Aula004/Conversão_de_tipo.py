# Inteiro
preco = 10  # Definindo a variável 'preco' como um número inteiro
print(preco)  # Exibe o valor de 'preco'
# >>> 10

# Conversão de inteiro para float
preco = float(preco)  # Convertendo o valor de 'preco' para float
print(preco)  # Exibe o valor de 'preco' agora como um float
# >>> 10.0

# Outra forma de obter um float usando divisão
preco = 10 / 2  # Divisão de inteiros resulta em um float
print(preco)  # Exibe o resultado da divisão
# >>> 5.0

# Float
preco = 10.30  # Definindo a variável 'preco' como um número float
print(preco)  # Exibe o valor de 'preco'
# >>> 10.3

# Conversão de float para inteiro
preco = int(preco)  # Convertendo o valor de 'preco' de float para inteiro
print(preco)  # Exibe o valor convertido de 'preco'
# >>> 10

# Conversão de inteiro para float com divisão
preco = 10  # Definindo 'preco' novamente como um inteiro
print(preco)  # Exibe o valor de 'preco'
# >>> 10

print(preco / 2)  # Divisão normal, resultando em float
# >>> 5.0

# Divisão com duas barras "//" preserva o número inteiro
print(preco // 2)  # A divisão inteira descarta o valor decimal
# >>> 5

# Número para string
preco = 10.50  # Definindo 'preco' como um float
idade = 28  # Definindo 'idade' como um inteiro

print(str(preco))  # Convertendo 'preco' para string
# >>> '10.5'

print(str(idade))  # Convertendo 'idade' para string
# >>> '28'

# Usando o método format() para inserir variáveis em uma string
texto = 'idade {} preço {}'.format(idade, preco)  # Inserindo as variáveis 'idade' e 'preco' na string
print(texto)  # Exibe o texto formatado
# >>> idade 28 preço 10.5

# String para número
preco = '10.50'  # Definindo 'preco' como uma string
idade = '28'  # Definindo 'idade' como uma string

print(float(preco))  # Convertendo a string 'preco' para float
# >>> 10.5

print(int(idade))  # Convertendo a string 'idade' para inteiro
# >>> 28
