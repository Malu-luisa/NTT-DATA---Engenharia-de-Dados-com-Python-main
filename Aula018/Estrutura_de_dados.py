# Criando listas de diferentes maneiras
frutas = ['laranja', 'maça', 'uva']  # Lista simples com strings
frutas = []  # Lista vazia
letras = list('python')  # Construtor list a partir de uma string
numeros = list(range(100))  # Lista de números de 0 a 99
carros = ['Ferrari', 'F8', 4200000, 2020, 2900, 'São Paulo', True]  # Lista com diferentes tipos de objetos

# Acessando elementos pelo índice
frutas = ['maça', 'laranja', 'uva', 'pera']
print(frutas[0])  # Saída: maça
print(frutas[3])  # Saída: pera
print(frutas[2])  # Saída: uva
print(frutas[1])  # Saída: laranja

# Acessando elementos a partir do fim da lista com índice negativo
frutas = ['maça', 'laranja', 'uva', 'pera']
print(frutas[-1])  # Saída: pera
print(frutas[-3])  # Saída: laranja

# Lista de listas (matriz bidimensional)
matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

print(matriz[0])  # Saída: [1, 'a', 2]
print(matriz[0][0])  # Saída: 1
print(matriz[0][-1])  # Saída: 2
print(matriz[-1][-1])  # Saída: 'c'

# Fatiamento de listas (slice)
lista = ['p', 'y', 't', 'h', 'o', 'n']

# Acessando elementos a partir de um índice até o final
print(lista[2:])  # Saída: ['t', 'h', 'o', 'n']

# Acessando elementos do início até o índice 2 (não inclui o índice 2)
print(lista[:2])  # Saída: ['p', 'y']

# Acessando elementos entre índices 1 e 3 (não inclui o índice 3)
print(lista[1:3])  # Saída: ['y', 't']

# Acessando elementos entre índices 0 e 3 com passo de 2
print(lista[0:3:2])  # Saída: ['p', 't']

# Acessando a lista completa
print(lista[::])  # Saída: ['p', 'y', 't', 'h', 'o', 'n']

# Invertendo a lista
print(lista[::-1])  # Saída: ['n', 'o', 'h', 't', 'y', 'p']


# Percorrendo uma lista com for
carros = ['gol', 'celta', 'palio']
for carro in carros:
    print(carro)  # Saída: gol, celta, palio (em linhas separadas)


# Usando enumerate para acessar o índice e o valor ao mesmo tempo
carros = ['gol', 'celta', 'palio']
for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')  # Saída: 0: gol, 1: celta, 2: palio


# Criando uma lista com números pares (modo tradicional)
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)  # Saída: [30, 2, 34]


# Criando uma lista com números pares (usando list comprehension)
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)  # Saída: [30, 2, 34]


# Criando uma lista com os quadrados dos números (modo tradicional)
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2)

print(quadrados)  # Saída: [1, 900, 441, 4, 81, 4225, 1156]


# Criando uma lista com os quadrados dos números (usando list comprehension)
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrados = [numero ** 2 for numero in numeros]

print(quadrados)  # Saída: [1, 900, 441, 4, 81, 4225, 1156]
